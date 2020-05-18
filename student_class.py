class Student:
    def __init__(self,name,address,contact,rollno,standard):
        self.name = name
        self.address = address
        self.contact = contact
        self.rollno = rollno
        self.standard = standard

    def add(self):
        self.name = input("enter student name: ")
        self.address = input("enter student address: ")
        self.contact = input("enter student contact details: ")
        self.rollno = input("enter student rollno: ")
        self.standard = input("enter student's standard: ")

           
    def show(self):
        print(self.name)
        print(self.address)
        print(self.contact)
        print(self.rollno)
        print(self.standard)

    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
        return " Not Found!! "
ls = []
st = Student(" ", " ", " "," "," ")
st.add()
st.show()



