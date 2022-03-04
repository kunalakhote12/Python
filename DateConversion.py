def date():
  months = [' ','January' , 'February','March','April','May','June','July','August','September','October','November','December']
  print(months[mon],day,yr)
day = int(input("enter day: "))
mon = int(input("enter month: "))
yr = int(input("Enter year: "))

print("The date entered is: ",mon,"/",day,"/",yr)

date()
