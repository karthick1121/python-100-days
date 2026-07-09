print("====ATM SYSTEM====")
name=(input("Enter your name:"))
account_number=int(input("Enter your account number:"))
account_balance=int(input("Enter your account balance:"))
withdrawal_amount=int(input("Enter withdrawal amount:"))      
print("\n ACCOUNT DETAILS")
print("Name:",name)
print("Account number:",account_number) 
print("Account balance:",account_balance)    
print("Withdrawal amount:",withdrawal_amount)
print("\n RESULT")
if withdrawal_amount<=account_balance:
      print("withdrawal successful")
      reamining_balance=acccount_balance-withdrawal_amount
      print("remaining balance:",remaining_balance)
else:
      print("insufficient balance")  
print("\n thank you for using our atm:")          
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      