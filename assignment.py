 # 1. Create 3 variables to store street, city and country, now create address variable 
# to store entire address. Use two ways of creating this variable, 
# one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
'''
street='konark'
city='puri'
country='india'
address=street+'\n'+city+'\n'+country
print(address)
'''

#2. Create a variable to store the string "Earth revolves around the sun" Print "revolves" using slice operator
#Print "sun" using negative index

'''
st='earth resolves around the  sun'
print(st[6:14])
print(st[-3:])
'''

#After appearing in exam 10 times you got this result,
#result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]
#Using for loop figure out how many times you got Pass

'''
result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"] 
count = 0
for i in result:
  if i == "Pass":
    count += 1
print(f'You passed {count} times') 
'''

# Create two variables to store how many fruits and vegetables you eat in a day.
#Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

#que3

'''
indian=['biriyani','pulaw','rice']
chines=['manchow','egg roles','fried rice']
italian=['pizza','pasta','risotto']
user=input('enter ur dish here :')
if user in indian:
    print('indian')
elif user in chines:
    print('chines')
elif user in italian:
    print('italian')
else:
    print('item is not available')
'''
'''
exp=[2400,3500,4500,5500]
total=0
print(len(exp))
print(range(len(exp)))
for i in range(len(exp)):
    print('month',i+1,':',exp[i])
    total+=exp[i]
print(total)
'''   



# que3// After flipping a coin 10 times you got this result,
#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#Using for loop figure out how many times you got heads

#answer
'''
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in result:
    if i=='heads':
        count=count+1
print(count)
'''

#2.Print square of all numbers between 1 to 10 except even numbers
'''
for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)

'''


#3.Your monthly expense list (from Jan to May) looks like this,
#expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
#If expense is not found then it should print that as well.

'''
month_list = ["January","February","March","April","May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
exp=int(input("Enter your expense:"))
for i in range(5):
 if exp==expense_list[i]:
  print('this is  the month of',month_list[i])
  break
else:
  print(' does not matches the list')
'''

#4.Lets say you are running a 5 km race. Write a program that,
#i.Upon completing each 1 km asks you "are you tired?"
#ii.If you reply "yes" then it should break and print "you didn't finish the race"
#iii.If you reply "no" then it should continue and ask "are you tired" on every km
#iv.If you finish all 5 km then it should print congratulations message
'''
for i in range(1,6):
    if i%1==0:
        n=input('are you tired :')
        if n=='yes':
            print('you did not finish the race')
            break
    if i==5:
        print('congratulation u complete the race')
  '''      

lst=[11,22,33,44,55]
del lst[::4]
print(lst)

 

