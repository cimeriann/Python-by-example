# Practice programs
# Program1
# Ask the user to enter their first name and then display the length of their first name. 
# Then ask for their surname and display the length of their surname. Join their first 
# name and surname together with a space between and display the result. Finally, 
# display the length of their full name (including the space). 
# firstname = input('>Enter first name: ')
# print('Your first name is ' + str(len(firstname)) + ' characters long')
# surname = input('>Enter sutname: ')
# print('Your surname is ' + str(len(surname)) + ' characters long')
# Fullname = ''
# Fullname += firstname + ' ' + surname
# print(Fullname)
# print('Your full name is ' + str(len(Fullname)) + ' characters long')

# Program2
# Ask the user to type in their favourite school subject. 
# Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
# favsubject = input('>Enter you favorite subject: ')
# for i in favsubject:    
#     print(i, end='-')

# Program3
# Show the user a line of text from your favourite poem and ask for a starting and ending point. 
# Display the characters between those two points.
# favline = 'The end is nigh'
# print(favline)
# start = int(input('Please enter a starting point(should be an interger value): '))
# end = int(input('Now enter your endpoint(should also be an integer value): '))
# print(favline[start:end])

# Program4
# Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep 
# repeating this until they type in a message all in uppercase.
# while True:
#     word = input('Enter a word in uppercase: ')
#     if word.isupper():
#         break
#     else:
#         continue

# Program5
# Ask the user to type in their postcode. Display the first two letters in uppercase. 
# code = input('Enter your postcode: ').upper()
# print(code[0:2])

# Program6
# Ask the user to type in their name and then tell them how many vowels are in their name.
# vowels = ('a', 'e', 'i', 'o', 'u')
# name = input('Enter your name: ').lower()
# num_of_vowels = 0
# for i in name:
#     if i in vowels:
#         num_of_vowels += 1
# print('You have ' + str(num_of_vowels) + ' vowels in your name.')

# Program7
# Ask the user to enter a new password. Ask them to enter it again. If the two passwords 
# match, display “Thank you”. If the letters are correct but in the wrong case, display the 
# message “They must be in the same case”, otherwise display the message “Incorrect”. 
# password = input('Enter your password: ')
# verifypw = input('Verify your password ')

# if password == verifypw:
#     print('Thank you!!')
   
# elif (password.isupper() and verifypw.islower()) or (password.islower() and verifypw.isupper()):
#     if password.lower() == verifypw:
#         print('They must be in the same case')
        
#     elif password.upper() == verifypw:
#         print('They must be in the same case')

# else:
#     print('Incorrect')
# Program8
# Ask the user to type in a word and then display it backwards on separate lines. For 
# instance, if they type in “Hello” it should display as shown below: 
# Enter text:
# o
# l
# l
# e
# H
# text = input('Enter text: ')
# index = -1
# try:
    
#     for letter in text:
#         print(text[index], end='')
#         index = index-1
# except IndexError:
#     print('Your word has been reversed')

# Program9
# Ask the user for a list of five integers. Store them in an array. 
# Sort the list and display it in reverse order.
# from array import *
# nums = int(input('How many numbers would you like to add? '))
# list = []
# for i in range(nums):
#     bro = int(input('enter a number: '))
#     list.append(bro)
# myarray = array ('i', list)
# myarray = sorted(myarray)
# myarray.reverse()
# print(myarray)

# Program10
# Create an array which will store a list of integers. Generate five random numbers and store them in the array.
# Display the array (showing each item on a separate line).
# import random
# string = [1,2,3,4,5]
# list = []
# for i in range(len(string)):
#     num = random.randint(1, 1000)
#     list.append(num)
# newarray = array ('i', list)
# for i in newarray:
#     print(i)

# Program11
# Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array, 
# otherwise display the message “Outside the range”. Once five numbers have been 
# successfully added, display the message “Thank you” and display the array with each item shown on a separate line. 
# list = []

# nums = 1
# while nums != 6:
#     num = int(input('Enter a number betwee 10 and 20 '))
#     if num > 20 or num<10:
#         print('Outside the range')
#     else:    
#         list.append(num)
#         nums += 1
# print('Thank you!')
# newarray = array ('i', list)
# for i in newarray:
#     print(i)

# Program12
# Create an array which contains five numbers (two of which should be repeated). 
# Display the whole array to the user. Ask the user to enter one of the numbers from the array and 
# then display a message saying how many times that number appears in the list.
# myarray = array('i', [1,1,3,4,5])
# print(myarray)
# num = int(input('Enter a number from the array above: '))
# if num in myarray:
#     numofoccurences = myarray.count(num)
#     print(f'{num} appears {numofoccurences} times')

# Program13
# Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers).
# Join these two arrays together into one large array. Sort this large array and display it so that each number appears on a separate line.
# list = []
# for i in range(5):
#     num = random.randint(1,50)
#     list.append(num)
# myarray = array('i', list)
# userlist = []
# for i in range(3):
#     usernum = int(input('Provide a number: '))
#     userlist.append(usernum)
# userarray = array('i', userlist)
# myarray.extend(userarray)
# myarray = sorted(myarray)
# for  i in myarray:
#     print(i)

# Program14 
# Ask the user to enter five numbers. Sort them into order and present them to the user. 
# Ask them to select one of the numbers. Remove it from the original array and save it in a new array.
# listofnums = []
# for i in range(5):
#     num = int(input('Enter a number: '))
#     listofnums.append(num)
# listofnums = sorted(listofnums)
# print(listofnums)
# numtoremove = int(input('which number would you like to remove? '))
# listofnums.remove(numtoremove)
# newlist = []
# newlist.append(numtoremove)
# newarray = array('i', newlist)
# print(newarray)

# Program15
# Display an array of five numbers. Ask the user to select one of the numbers. 
# Once they have selected a number, display the position of that item in the array. 
# If they enter something that is not in the array, ask them to try again until they select a relevant item.
# mylist = []
# for i in range(5):
#     num = random.randint(10, 150)
#     mylist.append(num)
# myarray = array('i', mylist)
# print(myarray)
# selection = int(input('choose a number from array: '))
# while True:
#     if selection in myarray:
#         print(myarray.index(selection))
#         break
#     else:
#         continue 

# Program16
# Create an array of five numbers between 10 and 100 which each have two decimal places.
# Ask the user to enter a whole number between 2 and 5. If they enter something outside of that range,
# display a suitable error message and ask them to try again until they enter a valid amount. 
# Divide each of the numbers in the array by the number the user entered and display the answers shown to two decimal places. 
# mylist = [11.45, 64.27, 34.32, 89.23, 57.82]
# myarray = array('f', mylist)
# userinput = int(input('Enter a number between 2 and 5: '))
# while True:    
#     if userinput>5 or userinput<2:
#         print('You have gone of the requested range')
#         continue
#     else:
#         for i in myarray:
#             i = i /userinput
#             print(round(i,2))
#         break

# Program17
# Create the following using a simple 2D list using the standard Python indexing: 
# list = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]

# Program18
# Using the 2D list from program17, ask the user to select a row and a column and display that value.
# coord1 = int(input('select a row(number between 0 and 2) '))
# coord2 = int(input('select a column(number between 0 and 3) '))
# print(list[coord2][coord1])

# Prpogram19
# Using the 2D list from program17, ask the user which row they would like displayed and display 
# just that row. Ask them to enter a new value and add it to the end of the row and display the row
# row = int(input('Which row would you like to be displayed? (0-3) '))
# print(list[row])
# newval = input('Enter a new value to be added to your selected row. ')
# list[row].append(newval)
# print(list[row])

# Program20
# Change your previous program to ask the user which row they want displayed. Display that 
# row. Ask which column in that row they want displayed and display the value that is held 
# there. Ask the user if they want to change the value. If they do, ask for a new value and change 
# the data. Finally, display the whole row again.
# row = int(input('Which row would you like to be displayed? (0-3) '))
# print(list[row])
# col = int(input('Which column would you like to access. (0-2) '))
# print(list[row][col])
# response = input('Would you like to change this value').lower()
# while True:
#     if response.startswith('y'):
#         newval = int(input('Which value would you like to replace it with? '))
#         list[row][col] = newval
#         break
#     else:
#         print('you\'re to type in yes or no ')
#         continue
# print(list[row])

# Program21
# Create the following using a 2D dictionary showing the sales each person has made in the different 
# geographical regions.
# mydict = {'John':{'N':3056,'S':8463,'E':8441,'W':2694}, 'Tom':{'N':4832,'S':6786,'E':4737,'W':3612},
#          'Anne':{'N':5239,'S':4802,'E':5820,'W':1859}, 'Fiona':{'N':3904,'S':3645,'E':8821,'W':2451}}

# Program22
# Using program21, ask the user for a name and a region. Display the relevant data. 
# Ask the user for the name and region of data they want to change and allow them to make 
# the alteration to the sales figure. Display the sales for all regions for the name they choose.
# name = input('Enter a name from the dictionary: ').title()
# region = input('Enter a region (N,W,S,E)  ').upper()
# print(mydict[name][region])
# name2 = input('Enter the name from the dictionary you\'d like to make changes on: ').title()
# region2 = input('Enter a corresponding region (N,W,S,E):  ').upper()
# newvalue = int(input('what\'s the new value? '))
# mydict[name2][region2] = newvalue
# print(f'These are the values of the regional sales of {name2}')
# print(mydict[name2])

# Program23
# Ask the user to enter the name, age and shoe size for four people. 
# Ask for the name of one of the people in the list and display their age and shoe size.
# data = {}
# for num in range(1,5):
#         print(f'Collecting data for user{num}')
#         name = input('Enter the name: ')
#         age = input('Enter age')
#         shoesize = (input('Enter a shoe size: '))
#         data[name] = {'age': age, 'shoesize': shoesize}    
# newname = input('Whose details would you like to view? ')
# print(data)
# print(data[name])

# Program24
# Adapt program 102 to display the names and ages of 
# all the people in the list but do not show their shoe size.
# data = {}
# for num in range(1,5):
#         print(f'Collecting data for user{num}')
#         name = input('Enter the name: ')
#         age = input('Enter age')
#         shoesize = (input('Enter a shoe size: '))
#         data[name] = {'age': age, 'shoesize': shoesize}    
# print(data)
# for k in data:
#     print(k + ', age:'+ data[k]['age'] )

# Program25
# After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want to remove from 
# the list. Delete this row from the data and display the other rows on separate lines. 
# data = {}
# for num in range(1,5):
#         print(f'Collecting data for user{num}')
#         name = input('Enter the name: ')
#         age = input('Enter age')
#         shoesize = (input('Enter a shoe size: '))
#         data[name] = {'age': age, 'shoesize': shoesize}    

# print('whose data would you like to delete? ')
# deleted = input()
# del data[deleted]
# for k in data:
#     print(k + ', age: '+ data[k]['age'] + ', shoesize: ' + data[k]['shoesize'])

# Program26
# Write a new file called “Numbers.txt”. Add five numbers to the document which are stored 
# on the same line and only separated by a comma. Once you have run the program, look in the location where 
# your program is stored and you should see that the file has been created. The easiest way to 
# view the contents of the new text file on a Windows system is to read it using Notepad.
# numbers = open('Numbers.txt', 'w')
# numbers.write('1, 2, 3, 4, 5')
# numbers.close()

# Program27
# Create a new file called “Names.txt”. Add five names to the 
# document, which are stored on separate lines. Once you have 
# run the program, look in the location where your program is 
# stored and check that the file has been created properly.
# Names = open('Names.txt', 'w')
# Names.write('Holy God\n')
# Names.write('Jesus' + '\n')
# Names.write('Adonai\n')
# Names.write('Yaweh\n')
# Names.write('Father\n')
# Names.close()

# # Program28
# # Open the Names.txt file and display the data in Python. 
# Names = open('Names.txt','r')
# print(Names.read())

# Program29
# Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file. 
# userinput = input('Enter a name: ')
# Names = open('Names.txt', 'a')
# Names.write(userinput + '\n')
# Names = open('Names.txt', 'r')
# print(Names.read())
# Names.close()

# Program30
# Display the following menu to the user: 
# 1) Create a new  file
# 2) Display the file
# 3) Add a new item to the file
# Make a selection 1, 2 or 3
# Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a 
# suitable error message. If they select 1, ask the user to enter a school subject and save it to a new file called 
# “Subject.txt”. It should overwrite any existing file with a new file. 
# If they select 2, display the contents of the “Subject.txt” file. 
# If they select 3, ask the user to enter a new subject and save it to the file and then display 
# the entire contents of the file. Run the program several times to test the options.

# while True:
#     print('''
#     1) Create a new  file
#     2) Display the file
#     3) Add a new item to the file
# ''')
#     response = int(input('Make a selection 1, 2 or 3: '))
#     if response == 1:
#         newfile = open('Subject.txt', 'w')
#         subj = input('Which subject would you like to add? ')
#         newfile.write(subj+'\n')
#         newfile.close()
#     elif response == 2:
#         file = open('Subject.txt', 'r')
#         print(file.read())
#     elif response == 3:
#         file = open('Subject.txt', 'a')
#         res = input('Which new subject would you like to add to the file? ')
#         file.write(res + '\n')
#         file.close()
#         file = open('Subject.txt', 'r')
#         print(file.read())
#     else:
#         print('Please enter a valid integer')
#     
#     Note: This is just my own modification to the question.
#     ask = input('Would you like to do something else? (y or n) ').lower()
#     if ask.startswith('y'):
#         continue
#     else:
#         break

# Program31
# Create a .csv file that will store the following data. Call it “Books.csv”. 
#       Book                                    Author                      Year Released 
# 0     To Kill A Mockingbird                   Harper Lee                  1960 
# 1     A Brief History of Time                 Stephen Hawking             1988 
# 2     The Great Gatsby                        F. Scott Fitzgerald         1922 
# 3     The Man Who Mistook His Wife for a Hat  Oliver Sacks                1985 
# 4     Pride and Prejudice                     Jane Austen                 1813
import csv
# newcsvfile = open('Books.csv','w')
# newcsvfile.close()
# for i in range(5):
#     print('adding a new book.')
#     newcsvfile = open('Books.csv', 'a')
#     bookname = input('Book\'s name: ')
#     author = input('Author of the book: ')
#     year = input('when was the book released? ')
#     newcsvfile.write(bookname +', '+author +', '+ year + '\n')
#     newcsvfile.close()

# Program32
# Using the Books.csv file from program 111, ask the user to enter another 
# record and add it to the end of the file. Display each row of the .csv file on a separate line. 
# file = open('Books.csv', 'a')
# print('Add a new record')
# bookname = input('Book\'s name: ')
# author = input('Author of the book: ')
# year = input('when was the book released? ')
# file.write(bookname +', '+author +', '+ year + '\n')
# file.close()
# file = open('Books.csv', 'r')
# for row in file:
#     print(row)
# file.close()


# Progam33
# Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add 
# that many. After all the data has been added, ask for an author and display all the books in the list by that author. 
# If there are no books by that author in the list, display a suitable message.
# rec = int(input('How many records do you want to add? '))
# for i in range(rec):
#     newcsvfile = open('Books.csv', 'a')
#     bookname = input('Book\'s name: ')
#     author = input('Author of the book: ')
#     year = input('when was the book released? ')
#     newcsvfile.write(bookname +', '+author +', '+ year + '\n')
#newcsvfile.close()
# file = open('Books.csv', 'r')
# reply = input('whose book would you like to view? ').title()
# # reader = csv.reader(file)
# for row in file:
#     if reply in row:
#         print(row)
# if reply not in row:
#     print('no results for that author.')

# Program34
# Using the Books.csv file, ask the user to enter a starting year and an end 
# year. Display all books released between those two years. 
# start = int(input('Which year would you like to start you search? '))
# end = int(input('Which year would you like to end you search? '))
# file = list(csv.reader(open('Books.csv')))
# fmp = []
# for row in file:
    # fmp.append(row)
# for i in range(len(file)):
#     if int(file[i][2]) >= start and int(file[i][2]) <= end:
#         print(file[i])
# This block of code works just fine too.
# for i in range(len(fmp)):
#     if int(fmp[i][2]) >= start and int(fmp[i][2]) <= end:
#         print(fmp[i])


# Program35
# Using the Books.csv file, display the data in the file along with the row number of each.
# file = open('Books.csv')
# fmp = list(file)
# rownum = 0
# for i in fmp:
#     print('Row number: ' + str(rownum+1))
#     print(i)
#     rownum += 1
# This block works just fine too
# rownum = 0
# for i in file:
#     print('Row number: ' + str(rownum+1))
#     print(i)
#     rownum += 1

# Program36
# Import the data from the Books.csv file into a list. Display the list to the user. Ask them to select which row from the list 
# they want to delete and remove it from the list. Ask the user which data they want to change and allow them to change it. 
# Write the data back to the original .csv file, overwriting the existing data with the amended data. 
# file = open('Books.csv')
# fmp = list(file)
# rownum = 0
# for i in fmp:
#     print('Row number: ' + str(rownum+1))
#     print(i)
#     rownum += 1

# getrid = int(input('which row would you like to delete? '))
# del fmp[getrid-1]
# print(f'row {getrid} has been deleted.')
# newnum = 0
# for i in fmp:
#     print('Row number: ' + str(newnum+1))
#     print(i)
#     newnum += 1
# print('which row would you like to change? ')
# ans = int(input())
# name = input('Name of book: ')
# author = input('name of author: ')
# year = input('when was the book published?: ')
# fmp[ans-1] = name+', '+author+', '+year
# file = open('Books.csv', 'w')
# for i in fmp:
#     file.write(i+'\n')
# file.close()

# Program38
# Create a simple maths quiz that will ask the user for their name and then generate two 
# random questions. Store their name, the questions they were asked, their answers and 
# their final score in a .csv file. Whenever the program is run it should add to the .csv file 
# and not overwrite anything.
# import csv
# import random

# def mathsquiz():
    
#     questionbank = ['What is 10 divided by 2?', 'What is six multiplied by six?','Divide 169 by 13',
#                 'how many sevens are there in 49?', 'what\'s the result of 16 divided by 2?', 'What is the square root of 144?']
#     answerbank = ['5', '36', '13','7', '8', '12']
#     score = 0
#     name = input('What is your name? ')
#     q1 = questionbank[random.randint(0, (len(questionbank)-1))]
#     print(q1)
#     answer1 = input('Enter your answer to question1 (integers only): ')
#     for i in range(len(answerbank)):
#         if answer1 == answerbank[i]:
#             print('correct!')
#             score += 1
       
#     q2 = questionbank[random.randint(0, (len(questionbank)-1))]
#     print(q2)
#     answer2 = input('Enter your answer to question2 (integers only): ') 
#     for i in range(len(answerbank)):
#         if answer2 == answerbank[i]:
#             print('correct!')
#             score += 1
        
#     file = open('Data.csv','w')
#     file.close()
#     file = open('data.csv', 'a')
#     newdata = name + ', ' + q1 + ' answer: ' + answer1 +', '+ q2 + ' answer: ' + answer2 + ' total score: ' + str(score) 
#     file.write(newdata + '\n')
#     file.close()
#     return 'Your final score is ' + str(score)

# mathsquiz()

# Program39 
# Define a subprogram that will ask the user to enter a number and save it as the variable 
# “num”. Define another subprogram that will use “num” and count from 1 to that number.
# def asknum():
    # num = int(input('Enter a number: '))
# def gen_nums(num):
    # for i in range(1, (num+1)):
        # print(i)

# Program40
# Define a subprogram that will ask the user to pick a low and a high number, and then generate a random number between those two 
# values and store it in a variable called “comp_num”. Define another subprogram that will give the instruction “I am thinking of a number…” 
# and then ask the user to guess the number they are thinking of. Define a third subprogram that will check to see if the comp_num is the same 
# as the user’s guess. If it is, it should display the message “Correct, you win”, otherwise it shouldkeep looping, telling the 
# user if they are too low or too high and asking them to guess again until they guess correctly.
# import random
# def pick_num():
#     low = int(input('Pick a low number: '))
#     high = int(input('Pick a high number: '))
#     comp_num = random.randint(low, high)
#     return comp_num
# def guess_num():
#     print('I am thinking of a number. ')
#     user_guess = int(input('Input your guess. '))
#     return user_guess
# def compare(): 
#     figure = pick_num() 
#     while True:
#         usernum = guess_num()
#         if figure == usernum:
#             print('Correct, you win!')
#             break
#         elif figure < usernum:
#             print('You guessed too high. ')
#             continue
#         elif figure > usernum:
#             print('You guessed too low, try again. ')
#             continue
# compare()

# Program41
# Display the following menu to the user: 
    # 1) Addition
    # 2) Subtraction
    # Enter 1 or 2:
# If they enter a 1, it should run a subprogram that will generate two random numbers between 5 and 20, and 
# ask the user to add them together. Work out the correct answer and return both the user’s answer and the 
# correct answer. If they entered 2 as their selection on the menu, it should run a subprogram that will generate one number 
# between 25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. This way they will not have to 
# worry about negative answers. Return both the user’s answer and the correct answer. Create another subprogram that will check if the user’s 
# answer matches the actual answer. If it does, display “Correct”, otherwise display a message that will say “Incorrect, the answer is” and 
# display the real answer. If they do not select a relevant option on the first menu you should display a suitable message.
import random
# def add():
#     num1 = random.randint(5, 20)
#     num2 = random.randint(5, 20)
#     true_result = num1 + num2
#     print(f'Add {num1} and {num2} together')
#     result = int(input('What is your answer? '))
#     # print('True answer: ' + str(true_result))
#     datatup = (result, true_result)
#     return datatup
    
# def subtract():
#     num1 = random.randint(25, 50)
#     num2 = random.randint(1, 25)
#     true_result = num1 - num2
#     print(f'Work out {num1} minus {num2}')
#     result = int(input('What is your answer? '))
#     datatup = (result, true_result)
#     return datatup
#     # print('True answer: ' + str(true_result))
# def checkresult(result,true_result):
#     if result == true_result:
#             print('Correct.')
#     else:
#         print('Incorrect, the answer is: ' + str(true_result))

# def main():
#     while True:
#         print('''
#         1) Addition
#         2) Subtraction
#         Enter 1 or 2:
#         ''')
#         reply = int(input())
        
#         if reply == 1:
#             result,true_result = add()
#             checkresult(result,true_result)
#             break
#         elif reply == 2:
#             result,true_result = subtract()
#             checkresult(result,true_result)
#             break
#         else:
#             print('Please pick a valid option.')
#             continue
# main()

# Program42
# Create a program that will allow the user to easily manage a list of names. You should 
# display a menu that will allow them to add a name to the list, change a name in the 
# list, delete a name from the list or view all the names in the list. There should also be a 
# menu option to allow the user to end the program. If they select an option that is not 
# relevant, then it should display a suitable message. After they have made a selection 
# to either add a name, change a name, delete a name or view all the names, they 
# should see the menu again without having to restart the program. The program 
# should be made as easy to use as possible.

# def edit():
#     names = ['alpha', 'tango', 'bravo', 'yinka','jojo','namikaze','demi']
#     while True:
#         print(''' What would you like to do?
#     1) Add a name to the list
#     2) Change a name in the list
#     3) delete a name from the list
#     4) View the entire list of names
#     5) End the program
#     ''') 
#         response = int(input('Enter 1,2,3,4 or 5 '))
#         if response == 1:
#             newname = input('which new name would you like to the list? ')
#             names.append(newname)
#         elif response == 2:
#             mod = input('Which name would you like to modify? ').lower()
#             if mod in names:
#                 word = input('Enter your new name: ')
#                 index = names.index(mod)
#                 names[index] = word
#                 continue
#             elif mod not in names:
#                 print('The name you entered does not exist in the list of names')
#                 continue
#         elif response == 3:
#             deleted = input('Enter the name you\'d like to delete from the list ').lower()
            
#             if deleted in names:
#                 index = names.index(deleted)
#                 del names[index]
#                 continue
#             else:
#                 print('The name you entered does not exist in the list of names')
#                 continue
#         elif response == 4:
#             print(names)
#             continue
#         elif response ==5:
#             break
# edit()

# Program43
# Create the following menu: 
# 1) Add to file
# 2) View all records
# 3) Quit program
# If the user selects 1, allow them to add to a file called Salaries.csv which will store their name 
# and salary. If they select 2 it should display all records in the Salaries.csv file. If they select 3 it should stop the program. 
# If they select an incorrect option they should see an error message. They should keep returning to the menu until they select option 3.


file = open('Salaries.csv','w')
file.close()
def myprogram():
    while True:
        print(''' What would you like to do?
        1) Add to file
        2) View all records
        3) Quit program
        ''')
        response = int(input('Enter 1, 2 or 3 '))
        if response == 1:
            file = open('Salaries.csv','a')
            name = input('Enter a name: ')
            salary = input('Enter their salary: ')
            newrecord = 'name: ' + file + ', ' + 'salary: ' + salary
            file.write(newrecord + '\n')
            file.close()
            continue
        elif response== 2:
            file = open('Salaries.csv')
            files = list(file)
            for i in files:
                print(i)
            continue
        elif response == 3:
            break
        else:
            print('Please select a valid option from the menu(must be an integer value)')