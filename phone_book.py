import sys

def initial_phonebook():
   rows, cols = int(input("please enter initial number of contacts: ")), 5

    
phone_book = []  
print(phone_book)
for i in range(rows):
   print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
   print("NOTE: * indicates mandatory fields")
   print("....................................")
   temp = []
   for j in range(cols):
      if j == 0:
         temp.append (str(input("Enter name*: ")))
         if temp[j] == '' or temp[j] == '':
            sys.exit(
               "Name is a mandatory field. process exiting duo to blank field...")
            if j == 1:
               temp.append(int(input("Enter number*: ")))
            if j == 2:
               temp.append(str(input("Enter e-mail address: ")))
            if temp[j] == '' or temp[j] == '':
               temp[j] = None
            if j == 3:
               temp.append(str(input("Enter date of birth(dd/mm/yy)": )))
            if temp[j] == '' or temp[j] == '':
               temp[j] = None
            if j == 4:
               temp.append(str(input("Enter category(Family/Friends/work/others): ")))
               if temp[j] == '' or temp[4] == ' ':
                  temp[j] = None
            phone_book.append(temp)

print(phone_book)
return(phone_book)

def menu():
   print("***************************************")
   print("\t\t\tSMARTPHONE DIRECTORY", flush=false)
   print("***************************************")
   print("\itYou can now perform the followingg operations on thhis phonebook\n")
   print("add a new contact")
   print("remove an esisting contact")
   print("delete all contact ")
   print("search for a contact ")
   print("display all contacts")
   print("exit phonebook")
   phone_book.append
   def add_contact(pb):
      dip =[]
      for i in range(len(pb[0]))
      if i == 0:
         dip.append(str(input("Enter name: ")))
      if i == 1:
         dip.append(str(input("Enter nunber: ")))
         if i == 2:
         dip.append(str(input("Enter e-mail address: ")))
         if i == 3:
         dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
         if i == 4:
         dip.append(str(input("Enter cetagory (Family/Friends/Work/Others): ")))
      pb.append(dip)
      return pb
   def remove_existing(pb):
      query = str(
         input("please wnter the name of the contact you wish to remove:"))
      temp = 0
      for i in range(len(pb)):
         if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("this query has now been removed")
            return pb
         if temp == 0:
            print("sorry, you have entered an invalid query.\nPlease recheck and try again later.")
            return pb.clear()
         def search_existing(pb):
            choice = int(input("Enter search criteria\n\n\n 1. Name\n2. Number\n3. Email-id\n4. DOB\n5.")
         cetegory(Family/Friends/Work/Others)\ \nPlease enter:)
            temp = []
            check = -1:
            query = str(
               input("please enter the name of the contact you wish to search: "))
            for i in range(len(pb)):
               if query == pb[i][0]:
                  check = i
                  temp.append(pb[i])
               elif choice == 2:
                  query = int(
                     input("please enter the number of the contact you wish to search:"))
                  for i in range(len(pb)):
                     if query == pb[i][1]:
                        check = i
                        temp.append(pb[i])
                     elif choice == 3:
                        query = str(input("please enter the e-mail I\ of the contact you wish to search: ")
                                    for i in range(len(pb)):
                                    if query == pb[i][2]:
                                    check = i
                                    temp.append(pb[i])
                                    elif  choice == 4:
                                    query = str(input("please enter the DOB (in dd/mm/yyyy format ONLY)\ of the contact you wish to search: "))
                                    for i in range(len(pb)):
                                    if query == pb[i][3]:
                                    check = i
                                    temp.append(pb[i])
                                    elif choice == 5:
                                    query = str(
                                       input("please enter the category of the contact you wish to search: "))
                                       for i in range(len(pb)):
                                       if query == pb[i][4]:
                                       check = i
                                       temp.append(pb[i])
                                       else:
                                       print("Invalide search criteria")
                                       return -1
                                       if check == -1:
                                       return -1
                                       else:
                                       display_all(temp)
                                       return check
                                    def display_all(pb):
                                    if not pb:
                                    print("list is empty: []")
                                    else:
                                    for i in range(len(pb)):
                                    print(pb[i])
                                 def thanks():
                                 print("**************************")
                                 
