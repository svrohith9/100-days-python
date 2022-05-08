import sqlite3
from contextlib import closing


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
            display_summary(summary)


def display_summary(summary):
    if len(summary) > 0:
        for student in summary:
            if(student[3] == 'null' and student[3] == 'null'):
                result = str(student[0]) + " " + \
                    str(student[1]) + " "+str(student[2])
            else:
                result = str(student[0]) + " " + str(student[1]) + " " + \
                    str(student[2])+" " + str(student[3]) + \
                    " " + str(student[4])
            print(result)
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
