class Student:
    def __init__(self, ID = "", name = "", DOB = "", place = "", major = "", GPA = 0.00):
        self.ID = ID
        self.name = name
        self.DOB = DOB
        self.place = place
        self.major = major
        self.GPA = GPA

    def __str__(self):
        return f"""
        +) {"Name":15} : {self.name}
        +) {"ID":15} : {self.ID}
        +) {"DOB":15} : {self.DOB}
        +) {"Place":15} : {self.place}
        +) {"Major":15} : {self.major}
        +) {"GPA":15} : {self.GPA:.2f}
        """

    def update_field(self, key, value):
        return self.__setattr__(key, value)

    def __del__(self):
        return "DONE!!!"

    def find_name(self, name):
        if name in self.name:
            return True
        else:
            return False
