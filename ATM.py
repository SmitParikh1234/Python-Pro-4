class Atm(object):

 def __init__(self,atmCardNo , pinNo) :
        self.atmcardnumber=atmCardNo
        self.pinnumber=pinNo


    
 def withDrawl(self):
      print("CashWithdrawl")


 def balance(self):
      print("BalanceEnquiry")

axis = Atm("444555","333333333")
print(axis.atmCardNo)
print(axis.pinNo)


axis.withDrawl()
axis.balance()