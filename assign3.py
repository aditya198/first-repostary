#Q1)

list1=['Aditya','Abhi','Abhishek','Aditi']
print(list1)

#Q2)

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1+list2)
#Q3)

list1=[1,2,6,5,2,2,3]
print("Occurenct count of 2=",list1.count(2))

#Q4)

list4=[5,8,2,3,1,9]
list4.sort()
print("sorted list is ",list4)

#Q5)

list5=[]
list6=[3,5,6,70]
list7=[7,8,9,50,40]
lis5=list6+list7
list5.sort()
print(list5)

#Q6)

list8=[1,2,3,4,5,6,7,8,9]
even=0;
odd=0;
for i in list8:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total Odd number= ",odd)
print("Total Even number= ",even)



#Q7)

list1=[40,50,60,70,80]
list2=reversed(list1)
print(tuple(list2))
#Q8)

tuple1=[1,4,6,8,10,40,60]
print("Max element=",max(tuple1))
print("Min element=",min(tuple1))

#Q9)

str1="i study pyhon"
str2=str1.upper()
print(str2)

#Q10)

num='1234'
print(num.isnumeric())

#Q11)

txt='Hello World'
txt1=txt.replace('World', 'Aditya')
print(txt1)


