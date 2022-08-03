 class Train:
    def _init_(self,tname,tno):
        self.tname=tname;
        self.tno=tno;
    def display(self):
        print("\nTrain Name: {}\nTrain Number: {}".format(self.tname,self.tno))
 class Booking(Train):

    def _init_(self,tname,tno,name,age,no_of_seats,gender):
        super()._init_(tname,tno)
        self.name=name
        self.age=age
        self.no_of_seats=no_of_seats
        self.gender=gender

    def display_details(self):
        self.display()
        print("Name: {}\nGender: {}\nAge: {}\nNo Of Seats: {}\nYour Booking Was Successfull".format(self.name,self.gender,self.age,self.no_of_seats))


obj=Booking(input("Enter Train Name: "),int(input("Enter Train Number: ")),input("Enetr Your Name: "),input("Enter Your Age: "),int(input("Enter Number Of Seats To Be Booked: ")),input("Enter Gender: "))
obj.display_details()