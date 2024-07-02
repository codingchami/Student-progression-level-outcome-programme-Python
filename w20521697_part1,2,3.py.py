#I declare that my work contains no example of misconduct,such as plagirism,or collusion.
#Any code taken from other sources is referenced with my code solution.

#reference:- https://www.w3schools.com/python/default.asp
#https://www.webucator.com/article/python-color-constants-module/
#https://anh.cs.luc.edu/handsonPythonTutorial/graphics.html

#Student ID: w20521697
#IIT student ID: 20231564
#Date:12/10/2023

#open for the outcomefile to write
outcomefile_1 = open("Progression Outcome Data.txt","w")
outcomefile_1.close()

#varibales
PASS=0
DEFER=0
FAIL=0
progress=0
exclude=0
Trailer=0
retriever=0
total=0
outcomelist=[]

import graphics

#user input for selecting the user want version
print()
user=input('''To gain entry to the 'student version' please enter '1'\nTo gain entry to the 'staff version' please enter '2'\nFor the 'quit' program please enter '3'\n
  Please Enter Here: ''')

#This function use for check the range and user input is correct or not
def Stu_Validation(credit_value_student):
  while True:
   try:  
     credit_level=int(input("Please enter your credit at "+credit_value_student+"level:" ))
     if credit_level/20 not in range(0,7) :
       print("OUT OF RANGE!.")
       continue
       
   except ValueError:
        print("INTEGER REQUITRED!.. ")
        continue
   break
  return credit_level

#function for check the range and integer in staffversion
def Stu_Validation_Staff(credit_value_staff):
  while True:
   try:  
     credit_level=int(input("please enter the student credit at "+credit_value_staff+"level:" ))
     if credit_level/20 not in range(0,7) :
       print("OUT OF RANGE!.")
       continue
       
   except ValueError:
        print("INTEGER REQUITRED!.. ")
        continue
   break
  return credit_level


#progerssion outcome in student version for students
def Stu_Progression():     
 while True:
   Pass=Stu_Validation ("PASS ")
   Defer=Stu_Validation("DEFER ")
   Fail=Stu_Validation ("FAIL ")

     
   if Pass+Defer+Fail != 120:    #check weather total is correct or not
      print("TOTAL INCORECT")
      continue
   break
#check what is the progression outcome
 if Pass==120:
     credit_progress="\nProgress"
    
          
 elif Pass==100:
     credit_progress="\nProgress(module trailer)"
  
        
 elif Fail==80 or Fail==100 or Fail==120:                 
     credit_progress="\nExclude"
     
        
 else:
   credit_progress="\nDo not progress-module retriever"

        
 print(credit_progress)      
 print()

#progerssion outcome in staff version
def Stu_Progression_Staff():
  global progress,Trailer,exclude,retriever
  while True:
    Pass=Stu_Validation_Staff ("PASS  ")
    Defer=Stu_Validation_Staff("DEFER ")
    Fail=Stu_Validation_Staff ("FAIL ")

    if Pass+Defer+Fail != 120:
       print("TOTAL INCORECT")
       continue
    break
  
#check what is the progression outcome
  if Pass==120:
     credit_progress="\nProgress"
     creditprogress="progress"
     progress+=1
          
  elif Pass==100:
     credit_progress="\nProgress(module trailer)"
     creditprogress="Progress(module trailer)"
     Trailer+=1 
        
  elif Fail==80 or Fail==100 or Fail==120:
     credit_progress="\nExclude"
     creditprogress = "Exclude"
     exclude+=1 
        
  else:
    credit_progress="\nDo not progress-module retriever"
    creditprogress = "Do not progress-module retriever"
    retriever+=1
  print(credit_progress)

  #part2-List(extension)
  #append is use for the collect all data in a list
  outcomelist.append([creditprogress,Pass,Defer,Fail])

  
  #part3-Text File(extension)
  outcomefile = open("Progression Outcome Data.txt","a")
  outcomefile.write(f"{creditprogress}-{Pass},{Defer},{Fail}\n")
  outcomefile.close()

from graphics import*
def staffsystem():
    option=input("\nWould you like to enter another set of data set enter  \'y\' " "to continue or \'q\'" "to quit \nPlease enter: ")
    print()

#user inputs 'y' loop the starf version again and again    
    if option.lower()=='y':
      staffversion()
      
    elif option.lower()=='q':
      #Create the Histogram      
      win = GraphWin("Histogram",600,400)
      win.setBackground("Mint Cream")
      x_1 = 40
      y_1 = 300
      bar_width = 100

      #create the header for histogram 
      text = Text(Point(150,30),"Histogram Results")
      text.setTextColor("grey")
      text.setSize(20)
      text.setStyle("bold")
      text.setFace("helvetica")
      text.draw(win)
      
      #create footer sentence
      text2 = Text(Point(100,350),f"{progress+Trailer+exclude+retriever} outcomes in total.")
      text2.setTextColor("grey")
      text2.setSize(15)
      text2.setFace("helvetica")
      text2.draw(win)

      base_line =Line(Point(20,300),Point(500,300))
      base_line.draw(win)

      bar1 = Rectangle(Point(x_1,y_1),Point(x_1+bar_width,y_1-progress*20))
      bar1.setFill("palegreen")
      bar1.draw(win)

      x_2 = x_1+bar_width+10
      y_2 = y_1
      bar2 = Rectangle(Point(x_2,y_2),Point(x_2+bar_width,y_2-Trailer*20))
      bar2.setFill("darkseagreen")
      bar2.draw(win)
      
      x_3 = x_2+bar_width+10
      y_3 = y_2
      bar3 = Rectangle(Point(x_3,y_3),Point(x_3+bar_width,y_3-exclude*20))
      bar3.setFill("yellowgreen")
      bar3.draw(win)


      x_4 = x_3+bar_width+10
      y_4 = y_3
      bar4 = Rectangle(Point(x_4,y_4),Point(x_4+bar_width,y_4-retriever*20))
      bar4.setFill("lightpink")
      bar4.draw(win)

      lable_1 = Text(Point(x_1+50,y_1+15),"Progress")
      lable_2 = Text(Point(x_2+50,y_2+15),"Trailer")
      lable_3 = Text(Point(x_3+50,y_3+15),"Exclude")
      lable_4 = Text(Point(x_4+50,y_4+15),"Retriever")


      lable_1.setStyle("bold")
      lable_1.draw(win)
      lable_2.setStyle("bold")
      lable_2.draw(win)
      lable_3.setStyle("bold")
      lable_3.draw(win)
      lable_4.setStyle("bold")
      lable_4.draw(win)


      toplable_1 = Text(Point(x_1+50,y_1-(progress*20+20)),progress)
      toplable_2 = Text(Point(x_2+50,y_2-(Trailer*20+20)),Trailer)
      toplable_3 = Text(Point(x_3+50,y_3-(exclude*20+20)),exclude)
      toplable_4 = Text(Point(x_4+50,y_4-(retriever*20+20)),retriever)
      toplable_1.draw(win)
      toplable_2.draw(win)
      toplable_3.draw(win)
      toplable_4.draw(win)
      try:                   #this try except use for the except error in when close the histogram window
        win.getMouse()
      except:
        win.close()
      #print outcomelist after the histogram 
      print("\npart 2-List")
      for x in outcomelist:
        print(f"{x[0]}- {x[1]},{x[2]}, {x[3]}")
        
      #print whole data after the list (text file data)
      print("\npart 3-Text file")
      with open("Progression Outcome Data.txt","r") as file:
        a=file.read()
        print(a)
    
   
    else:
      print("Inavalid Option,please try again!")

#loop in  starf version
def staffversion():
     while True:
        Stu_Progression_Staff()
        staffsystem()
        break 

#to gain access to student version
if user=="1":
   text="WELCOME TO THE STUDENT VERSION!\nNow you are in 'student version'."
   print()
   print(text)
   print()

   Stu_Progression()
   
#to gain acsess to staff version   
elif user=="2":

     text="WELCOME TO THE STAFF VERSION!\nNow you are in 'staff version'."
     print()
     print(text)
     print()
     
     staffversion()
     
#to quit the programme  
elif user=="3":
      print("THANK YOU!..")
else:
   print("Wrong input...please enter the correct input again! ")





