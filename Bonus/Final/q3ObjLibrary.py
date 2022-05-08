class Student:
    def __init__(self, sid: str, major: str, gpa: float):
        self.sid = sid
        self.major = major
        self.gpa = gpa

    @property
    def stu_id(self):
        return self.sid

    @property
    def GPA(self):
        return self.gpa

    @GPA.setter
    def GPA(self, value):
        if value >= 0 and value <= 4:
            self.gpa = value


class GraduateStudent(Student):
    def __init__(self, sid: str, major: str, gpa: float, gre: int, ga: float):
        super().__init__(sid, major, gpa)
        self.ga = ga
        self.gre = gre

    @property
    def GRE(self):
        return self.gre

    @GRE.setter
    def GRE(self, value):
        if value >= 260 and value <= 340:
            self.gre = value

    @property
    def GA(self):
        if self.ga in ['y', 'Y']:
            return True
        else:
            return False

    @GA.setter
    def GA(self, value):
        if value in ['y', 'Y']:
            self.ga = 'y'
        else:
            self.ga = 'n'


if __name__ == "__main__":
    # -------------------- Testing Student
    a = Student('U111', 'EE', 2.81)
    print(a.stu_id, a.major, a.GPA)
    # a.stu_id = 'U333'  # ERROR, must remove or comment out
    a.major = 'CS'  # new major
    a.GPA = 6.05  # new GPA, won't be accepted
    print(a.stu_id, a.major, a.GPA)
    a.GPA = 3.05  # new GPA
    print(a.stu_id, a.major, a.GPA)

    # -------------------- Testing GraduateStudent
    b = GraduateStudent('U222', 'BIO', 3.33, 315, 'N')
    print(b.stu_id, b.major, b.GPA, b.GRE, b.GA)
    b.major = 'MUSIC'  # new major
    b.GPA = -1  # new GPA, won't be accepted
    b.GRE = 500  # new GRE, won't be accepted
    b.GA = 'yes'  # new GA but accepted as 'n'
    print(b.stu_id, b.major, b.GPA, b.GRE, b.GA)
    b.GPA = 2.9  # new GPA
    b.GRE = 260  # new GRE
    b.GA = 'xx'  # new GA but accepted as 'n'
    print(b.stu_id, b.major, b.GPA, b.GRE, b.GA)
    b.GA = 'y'  # new GA
    print(b.stu_id, b.major, b.GPA, b.GRE, b.GA)
