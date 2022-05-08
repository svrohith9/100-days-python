import sqlite3
from contextlib import closing


def connect_db(path):
    DB_FILE = path
    return sqlite3.connect(DB_FILE)


def get_students(path):
    students = []
    with open(path, newline="") as file:
        for line in file:
            data = line.strip()
            if len(data.split(",")) == 3:
                data += ",null,null"
            students.append(data.split(","))
    return students


def insert_students(conn, students):
    capacity = len(students)
    result = ""
    with closing(conn.cursor()) as c:
        for student in students:
            query = '''INSERT INTO allmajors (stuID, major, gpa, GRE, GradAssistant) VALUES (?, ?, ?, ?, ?)'''
            c.execute(query, (student[0], student[1],
                      student[2], student[3], student[4]))
            conn.commit()
            if(student[3] == 'null' and student[3] == 'null'):
                result = student[0] + "," + student[1] + ","+student[2]
            else:
                result = student[0] + "," + student[1] + "," + \
                    student[2]+"," + student[3] + "," + student[4]
            print(result)
    print(capacity, " students in students.txt are inserted in allmajors table of students.sqlite")


def main():
    # extracts data as a list of students
    students = get_students("students.txt")
    print(len(students), " students are found in students.txt")

    conn = connect_db("students.sqlite")
    insert_students(conn, students)


if __name__ == "__main__":
    main()
