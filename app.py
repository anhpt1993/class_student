from class_student import Student

# Thêm mới sinh viên
the_anh = Student(ID=20110998, name="Phạm Thế Anh", DOB="17/05/1993", place="Vũng Tàu", major="Welding Engineer", GPA=3.33)
le_nga = Student(ID=20120001, name="Lê Thị Nga", DOB="10/12/1994", place="Vũng Tàu", major="Economic", GPA=3.1)

list_student = (the_anh, le_nga)

# Xem danh mục sinh viên
for i in list_student:
    print(i.__dict__)
    print("---------------------------------------------")

# Cập nhật thông tin sinh viên

the_anh.update_field("ID", 20116996)
print(the_anh)

# xoá thông tin sinh viên
# del the_anh
# try:
#     print(the_anh)
# except NameError:
#     print("Name is not in student list")

# tìm kiếm thông tin theo tên
for i in list_student:
    if i.find_name("Nga"):
        print(i)