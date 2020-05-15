class Student:
    name = None 
    roll_no = None
    addres = None 
    contact = None 
    city = None 
    standard = None

    def add(self):
        self.name = input("enter student name: ")
           
    def show(self):
        print(self.name)


st = Student()
st.add()
st.show()


