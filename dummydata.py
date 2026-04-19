import bcrypt
from db.server import get_session

from db.schema.student import Student
from db.schema.advisor import Advisor
from db.schema.course import Course
from db.schema.degree import Degree
from db.schema.minor import Minor


# -----------------------
# PASSWORD HASHING
# -----------------------
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def create_dummy_data():
    session = get_session()

    try:
        # -----------------------
        # ADVISORS
        # -----------------------
        advisors = [
            Advisor(AdvisorID="20160001", FName="Alice", LName="Johnson", Email="alice.johnson@marist.edu"),
            Advisor(AdvisorID="20160002", FName="Robert", LName="Smith", Email="robert.smith@marist.edu"),
            Advisor(AdvisorID="20160003", FName="Linda", LName="Garcia", Email="linda.garcia@marist.edu"),
        ]
        session.add_all(advisors)
        session.flush()

        # -----------------------
        # COURSES
        # -----------------------
        courses = [
            Course(CourseName="Database Systems", CreditHours=3),
            Course(CourseName="Data Structures", CreditHours=4),
            Course(CourseName="Computer Networks", CreditHours=3),
            Course(CourseName="Operating Systems", CreditHours=4),
            Course(CourseName="Software Engineering", CreditHours=3),
            Course(CourseName="Cybersecurity Fundamentals", CreditHours=3),
        ]
        session.add_all(courses)
        session.flush()

        # -----------------------
        # DEGREES
        # -----------------------
        degrees = [
            Degree(DegreeName="Computer Science"),
            Degree(DegreeName="Information Technology"),
            Degree(DegreeName="Software Engineering"),
        ]
        session.add_all(degrees)
        session.flush()

        # -----------------------
        # MINORS
        # -----------------------
        minors = [
            Minor(MinorName="Mathematics"),
            Minor(MinorName="Cybersecurity"),
            Minor(MinorName="Business Analytics"),
        ]
        session.add_all(minors)
        session.flush()

        # -----------------------
        # STUDENTS
        # -----------------------
        students = [
            Student(
                StudentID="22157263",
                FName="Jimmy",
                LName="Johnson",
                Email="jimmy.johnson@marist.edu",
                PWord=hash_password("pass123"),
                Gender="Male",
                DOB="2002-05-10",
                GPA=3.75,
                Level="Senior",
            ),
            Student(
                StudentID="27652681",
                FName="Emma",
                LName="Brown",
                Email="emma.brown@marist.edu",
                PWord=hash_password("pass456"),
                Gender="Female",
                DOB="2003-11-22",
                GPA=3.90,
                Level="Junior",
            ),
            Student(
                StudentID="24679034",
                FName="Michael",
                LName="Davis",
                Email="michael.davis@marist.edu",
                PWord=hash_password("secure1"),
                Gender="Male",
                DOB="2001-08-14",
                GPA=3.40,
                Level="Senior",
            ),
            Student(
                StudentID="31252780",
                FName="Sophia",
                LName="Miller",
                Email="sophia.miller@marist.edu",
                PWord=hash_password("secure2"),
                Gender="Female",
                DOB="2004-02-18",
                GPA=3.85,
                Level="Sophomore",
            ),
        ]
        session.add_all(students)
        session.flush()

        # -----------------------
        # RELATIONSHIPS
        # -----------------------

        # Advisors ↔ Students (many-to-many style)
        students[0].Advisor.append(advisors[0])
        students[1].Advisor.append(advisors[1])
        students[2].Advisor.append(advisors[2])
        students[3].Advisor.append(advisors[0])  # shared advisor

        # Courses per student
        students[0].Course.extend([courses[0], courses[1], courses[2]])
        students[1].Course.extend([courses[1], courses[3]])
        students[2].Course.extend([courses[2], courses[4]])
        students[3].Course.extend([courses[0], courses[5]])

        # Advisors ↔ Courses
        advisors[0].Course.extend([courses[0], courses[4]])
        advisors[1].Course.extend([courses[1], courses[3]])
        advisors[2].Course.extend([courses[2], courses[5]])

        # Degrees
        students[0].Degree.append(degrees[0])
        students[1].Degree.append(degrees[1])
        students[2].Degree.append(degrees[0])
        students[3].Degree.append(degrees[2])

        # Minors
        students[0].Minor.append(minors[0])
        students[1].Minor.append(minors[1])
        students[2].Minor.append(minors[2])
        students[3].Minor.extend([minors[0], minors[1]])

        # -----------------------
        # COMMIT
        # -----------------------
        session.commit()
        print("dummy data inserted successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error inserting dummy data: {e}")

    finally:
        session.close()


if __name__ == "__main__":
    create_dummy_data()