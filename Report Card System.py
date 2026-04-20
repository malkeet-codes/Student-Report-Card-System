#Report Card System

eng=int(input("Enter your marks in English"))
hindi=int(input("Enter your marks in Hindi"))
maths=int(input("Enter your marks in Maths"))
total=eng+hindi+maths
percentage=(eng+hindi+maths)/3
p=int(percentage)
if(percentage>=90):
  if(percentage>=95):
       print("Congractulations Your Percentage is:",p,", You've scored A+")
  else:
       print("Congractulations Your Percentage is:",p,", You've scored A")
elif(percentage>=80):
   if(percentage>=85):
       print("Congractulations Your Percentage is:",p,", You've scored B+")
   else:
       print("Congractulations Your Percentage is:",p,", You've scored B")
else:
   print("Your Percentage is:",p,", You've scored  C")
