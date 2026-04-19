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
        #user = checkStudentLogin()
        return render_template('homepage.html')
        """if not user:
            return render_template('homepage.html')
        else:
            return render_template('homepage.html')"""
    
    """@app.route('/login', methods=['GET', 'POST'])
    def login():
        logger.info("Student has accessed login page")
        if request.method == 'POST':
            try:
                # get the email and password from the login form
                password = request.form['PWord']
                email = request.form['Email']

                # query for the existence of a user with that email
                user = query.get_User(schema.User, Email=email)

                # create a default error message for security sake
                error = f"failed login attempt for: {email}"

                if not user:
                    logger.warning(f"Login attempt with non-existent email: {email}")
                    return render_template('login.html', error=error)
                
                if bcrypt.checkpw(password.encode('utf-8'), user.PWord.encode('utf-8')):
                    logger.info(f"Successful login: {email}")
                    loggedinuser = str(user.UserID)
                    userCache[loggedinuser] = user
                    response = redirect(url_for('my_feed'))
                    response.set_cookie('userloggedin', loggedinuser)
                    return response
                
                else:
                    logger.warning(f"Login attempted with incorrect password")
                    return render_template('login.html', error=error)
                
            except Exception as e:
                logger.error(f"An error occurred during login: {e}")
                return render_template('login.html')
        elif request.method == 'GET':
            return render_template('login.html')"""
    return app
    
if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True, host='0.0.0.0') # host='0.0.0.0' allows external connections (req'd for docker)