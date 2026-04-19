import os
import bcrypt
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from db.server import init_database
import db.query as query
from db import schema

# load environment variables from .env
load_dotenv()

#create cache for the user
userCache = {}

folderPath = "logs"
os.makedirs(folderPath, exist_ok = True)

# configure logging
logging.basicConfig(
    filename="logs/log.txt", level=logging.INFO, filemode="a", format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

# database connection - values set in .env
# defaults to localhost for local dev
db_host = os.getenv('db_host','localhost')
# defaults to local port where postgres svr running
db_port = os.getenv('db_port','5432')
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@{db_host}:{db_port}/{db_name}"

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # Initialize database
    with app.app_context():
        if not init_database():
            print("Failed to initialize database. Exiting.")
            exit(1)
    
    def checkStudentLogin():
        loggedinstudent = request.cookies.get('studentloggedin')
        return userCache.get(loggedinstudent)
    
    @app.route('/')
    def index():
        student = checkStudentLogin()
        if not student:
            return render_template('homepage.html')
        else:
            return render_template('homepage.html', studentid=student.StudentID)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        logger.info("Student has accessed login page")
        if request.method == 'POST':
            try:
                password = request.form['PWord']
                email = request.form['Email']

                student = query.get_Student(schema.Student, Email=email)

                error = f"failed login attempt for: {email}"

                if not student:
                    logger.warning(f"Login attempt with non-existent email: {email}")
                    return render_template('login.html', error=error)
                
                if bcrypt.checkpw(password.encode('utf-8'), student.PWord.encode('utf-8')):
                    logger.info(f"Successful login: {email}")
                    loggedinstudent = str(student.StudentID)
                    userCache[loggedinstudent] = student
                    response = redirect(url_for('index'))
                    response.set_cookie('studentloggedin', loggedinstudent)
                    return response
                
                else:
                    logger.warning(f"Login attempted with incorrect password")
                    return render_template('login.html', error=error)
                
            except Exception as e:
                logger.error(f"An error occurred during login: {e}")
                return render_template('login.html')
        elif request.method == 'GET':
            return render_template('login.html')
    
    @app.route('/logout', methods=['GET','POST'])
    def logout():
        logger.info("Student has logged out")
        
        try:
            loggedinstudent = request.cookies.get('stuentloggedin')

            if loggedinstudent in userCache:
                del userCache[loggedinstudent]
        
            response = redirect(url_for('index'))
            response.delete_cookie('studentloggedin')

            return response 
        except Exception as e:
            logger.warning(f"Error logging student out: {e}")
            return redirect(url_for('index'))
        
    @app.route('/student')
    def student():
        logger.info("Student has accessed student page")
        
        student = checkStudentLogin()
        if not student:
            logger.warning("No student logged in")
            return redirect(url_for('login'))
        try:
            studentinfo = query.get_Student_Info(student.StudentID)
            studentdegree = query.get_Student_Degree(student.StudentID)
            studentcourses = query.get_Student_Courses(student.StudentID)
            studentminor = query.get_Student_Minor(student.StudentID)
            studentadvisor = query.get_Student_Advisor(student.StudentID)
            
            return render_template('student.html', studentid=student.StudentID, studentinfo = studentinfo, studentdegree = studentdegree,
                                   studentcourses = studentcourses, studentminor = studentminor, studentadvisor = studentadvisor)
        except Exception as e:
            logger.warning(f"Error loading student page: {e}")
            return redirect(url_for('index'))

    return app
    
if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True, host='0.0.0.0') # host='0.0.0.0' allows external connections (req'd for docker)