from db.server import get_session       # import get_session function from server.py
from sqlalchemy import or_, text
from datetime import datetime

def get_Student (table, **filters) -> str:
    session = get_session()
    try:
        student = session.query(table).filter_by(**filters).first()
        return student
    finally:
        session.close()

def get_Student_Info(studentid: int) -> list:
    session = get_session()
    try:
        query = text(
            """
            SELECT S."StudentID" AS studentid, S."FName" AS fname, S."LName" AS lname,
                S."Email" AS email, S."Gender" AS gender, S."DOB" AS dob, S."GPA" AS gpa,
                S."Level" AS level 
            FROM "student" S
            WHERE S."StudentID" = student_id
            """)

        info = session.execute(query, {"student_id": studentid}).mappings().all()
        return [dict(row) for row in info]
    
    except Exception as e:
        session.rollback()
        print(f"Error getting studentinfo: {e}")
        return []
    finally:
        session.close()

def get_Student_Degree(studentid: int) -> list:
    session = get_session()
    try:
        query = text(
            """
            SELECT D."DegreeName" as degreename
            FROM "student" S 
            JOIN "studentdegree" SD ON S."StudentID" = SD."StudentID"
            JOIN "degree" D ON SD."DegreeID" = D."DegreeID"
            WHERE S."StudentID" = student_id
            """)
        
        degree = session.execute(query, {"student_id":studentid}).mappings().all()
        return[dict(row) for row in degree]
    
    except Exception as e:
        session.rollback()
        print(f"Error getting studentdegree: {e}")
        return[]
    finally:
        session.close()

def get_Student_Courses(studentid: int) -> list:
    session = get_session()
    try:
        query = text(
            """
            SELECT C."CourseName" AS coursename, C."CreditHours" As credithours
            FROM  "student" S
            JOIN "studentcourse" SC ON S."StudentID" = SC."StudentID"
            JOIN "course" C ON SC."CourseID" = C."CourseID"
            WHERE S."StudentID" = student_id
            """)
        
        courses = session.execute(query, {"student_id":studentid}).mappings().all()
        return[dict(row) for row in courses]

    except Exception as e:
        session.rollback()
        print(f"Error getting studentcourse: {e}")
        return[]
    finally:
        session.close()

def get_Student_Minor(studentid: int) -> list:
    session = get_session()
    try:
        query = text(
            """
            SELECT M."MinorName" AS minorname
            FROM "student" S
            JOIN "studentminor" SM ON S."StudentID" = SM."StudentID"
            JOIN "minor" M ON SM."MinorID" = M."MinorID"
            WHERE S."StudentID" = student_id
            """)
        
        minor = session.execute(query, {"student_id":studentid}).mappings().all()
        return[dict(row) for row in minor]

    except Exception as e:
        session.rollback()
        print(f"Error getting studentminor: {e}")
        return[]
    finally:
        session.close()

def get_Student_Advisor(studentid: int) -> list:
    session = get_session()
    try:
        query = text(
            """
            SELECT A."FName" AS fname, A."LName" AS lname, A."Email" AS email
            FROM "student" S
            JOIN "studentadvisor" SA ON S."StudentID" = SA."StudentID"
            JOIN "advisor" A ON SA."AdvisorID" = A."AdvisorID"
            WHERE S."StudentID" = student_id
            """)
        advisor = session.execute(query, {"student_id":studentid}).mappings().all()
        return [dict(row) for row in advisor]
    
    except Exception as e:
        session.rollback()
        print(f"Error getting studentAdvisor: {e}")
        return[]
    finally:
        session.close()

def get_Course_Professor(courseid: int) -> list:
    session = get_session()
    try:
        query = text(
            """
            SELECT P."AdvisorName" AS professorname
            FROM "course" C
            JOIN "advisorcourse" AC ON C."CourseID" = AC."CourseID"
            JOIN "advisor" P ON AC."AdvisorID" = P."AdvisorID"
            WHERE C."CourseID" = course_id
            """
        )
        professor = session.execute(query, {"course_id":courseid}).mappings().all()
        return[dict(row) for row in professor]
    
    except Exception as e:
        session.rollback()
        print(f"Error getting courseprofessor: {e}")
        return[]
    finally:
        session.close()
