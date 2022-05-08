import sqlite3
from contextlib import closing

from q3ObjLibrary import GraduateStudent, Student


def connect_db(path):
    DB_FILE = path
    return sqlite3.connect(DB_FILE)


def query(conn, major):
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM allmajors WHERE major = ?'''
        c.execute(query, (major,))
        summary = c.fetchall()
        if len(summary) < 1:
            print("Sorry, no students of ", major, " exists in the database")
            print()
        else:
            display(summary)


def display(summary):
    graduate_student_obj = None
    student_obj = None
    if len(summary) > 0:
        for student in summary:
            if(student[3] == 'null' and student[3] == 'null'):
                student_obj = Student(student[0], student[1], student[2])
            else:
                graduate_student_obj = GraduateStudent(
                    student[0], student[1], student[2], student[3], student[4])
            if graduate_student_obj != None:
                if graduate_student_obj.GA:
                    ga_or_not = "(GA)"
                else:
                    ga_or_not = "(not GA)"
                print(graduate_student_obj.stu_id, graduate_student_obj.major,
                      graduate_student_obj.GPA, graduate_student_obj.GRE, ga_or_not)
                graduate_student_obj = None
            else:
                print(student_obj.stu_id, student_obj.major, student_obj.GPA)
                student_obj = None
    print()


def main():
    conn = connect_db("students.sqlite")
    major = input(
        "Enter student major to view their details or 'q' to quit: ")
    while major not in ['q', 'Q']:
        query(conn, major)
        major = input(
            "Enter student major to view their details or 'q' to quit: ")


if __name__ == "__main__":
    main()
