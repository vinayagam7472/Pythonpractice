## frequency of each character of given string
# name="vinayagam"
# modify=list(name)
# i=0
# while i<len(name):
#     count=0
#     word=name[i]
#     j=1
#     while j <len(name):
#         if word==modify[j]:
#             count=count+1
            
#         j+=1
#     print(word,count)
#     i+=1



##find smallest number
# number=1234567
# smallest=9
# while number >0:
#     digit=number%10
#     if digit<smallest:
#         smallest=digit
#     number=number//10
# print(smallest)



##pattern 1
# i=1
# while i <=5:
#     print(" "*(6-i)+i*"* ")
#     i+=1


##pattern 2
# for i in range(5,0,-1):
#     print(i*"*")



## remove space
# name="how are you"
# for letter in name:
#     if letter!=" ":
#         print(letter,end="")



# #search word
# name="vinayagam"
# key="v"
# for i in range(len(name)):
#     if name[i]==key:
#         print(i,name[i])



##remove space
# name = 'how are you'
# for letter in name:
#     if letter!=' ':
#         print(letter,end='')


##prime number
# def prime1(num):   
#     div=2
#     count=0
#     while div<num:
#         if num %div==0:
#             count+=1
#         div+=1
#     if count==0:
#         return("prime")
#     else:
#         return("not")
# print(prime1(45))



##Add given number
# num=12345
# add=0
# while num>0:
#     rem=num%10
#     add+=rem
#     num=num//10
# print(add)


##num convert to str and to num
# num=12345
# for i in str(num):
#     print(1+int(i))


#Find the factorial of a number.
num=4
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)


#Reverse a number.
num=12345
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)


##count the num
# num=14500023450
# count=0
# while num>0:
#     rem=num%10
#     count+=1
#     num=num//10
# print(count)


##list
# grocery_list = ['soap', 12, True, 'rice', 'veggies',4.5]
# print(grocery_list)
# for grocery_item in grocery_list:
#     if type(grocery_item) == str:
#         print(type(grocery_item))


##list
# l1 = ['Sai', 'Abhishek', 'Sanju', 'Shreyas']
# l2 = [65, 85, 105, 56]
# # player_score_list = [l1, l2]
# for i in range(len(l1)):
#     if l2[i]>100:
#         print(l1[i],l2[i])  


