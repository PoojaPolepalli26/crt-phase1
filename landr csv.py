import csv
class landreg:
    def regis(self,username,password,phoneno,pincode,city):
        self.uname=username
        self.pw=password
        self.phno=phoneno
        self.pin=pincode
        self.city=city
        with open('e-com_proj/user_reg.csv','a',newline='')as file:
            store=csv.writer(file)
            store.writerow([self.uname,self.pw,self.phno,self.pin,self.city])
    def login(self,username,password)
        with open('e-com_proj/user_reg,csv','r',newline='')as file