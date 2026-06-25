####2.
##start=1
##while start<=5:
##    print (start,end=" ")
##    start=start+1



####3.
##start=1
##while start<=10:
##    if start%2 !=0:
##        print (start)
##    start=start+1


####4.
##start=3
##while start<=15:
##    if start%3==0:
##        print (start)
##    start+=1


####4.1
##start=15
##while start>=1:
##    if start%3==0:
##        print(start)
##    start=start-1


####4.2
##start=10
##while start>=2:
##    if start%2==0:
##        print(start)
##    start=start-1


# ##4.3
# start=10
# while start>=1:
#    if start%2 !=0:
#        print(start)
#    start=start-1


####5.
##start=1
##while start<=50:
##    if start%3==0 and start%5==0:
##        print("divisible by both",start)
##    elif start%3==0:
##        print("divisible by 3",start)
##    elif start%5==0:
##        print("divisible by 5",start)
##    start+=1


####6.
##start=1
##while start<=20:
##
##
##

###11.
##no=9837
##add=0
##while no>0:
##    rem=no%10
##    print(rem,end=' ')
##    no=no//10
##    add=add+1
##    
##print(add)
    


##### Task1: 34 23 12
##### Task2: 34 12
##### Task3: Addition of Task1
##### Task4: Addition of Task2
##no=123456
##count=0
##while no >0:
##    rem=no%100
##    print(rem)
##    count=count+rem
##    no=no//100
##print(count)



### Task5: given number 123456 --> 456 123
##no=123456
##first=no//1000
##second=no%1000
##print(second,first)


####reverse
##def reversed(no):
##    reverse = 0        # --> 31
##    while no > 0:
##        reverse = (reverse * 10) + no%10
##        no=no//10
##    print(reverse)
##
##reversed(21)




##def find_prime(no):
##    div = 2
##    divisors_count = 0
##
##    while div <= no//2:
##        if no % div == 0:
##            divisors_count += 1
##        div += 1
##
##    return divisors_count == 0
##
##def reverse_num(no):
##    reverse = 0        # --> 31
##    while no > 0:
##        reverse = (reverse * 10) + no%10
##        no=no//10
##    return reverse
##
##
##no = 11
##while no<=60:
##    result = find_prime(no)
##    if result:
##        reversed_no = reverse_num(no)
##        result = find_prime(reversed_no)
##    if result == True:
##        print(no,'EMIRP NUMBER')
##    else:
##        print(no,'NOT EMIRP')
##    no+=1





##no1 = 10000
##no2 = 120
##small = no1 if no1<no2 else no2
##div = 2
##gcd = 0 
##while div <= small:
##    if no1 % div == 0 and no2 % div == 0:
##        gcd = div
##
##    div+=1
##
##print(gcd)




####prime program
##no=15
##div=2
##divisor=0
##while div<=no//2:
##    if no%div==0:
##        divisor=divisor+1
##    div=div+1
##if divisor==0:
##    print("prime")
##else:
##    print("not prime")



##
##def sum_of_factors(no):
##    total = 0
##    div = 1
##
##    while div < no:
##        if no % div == 0:
##            total += div
##        div += 1
##
##    return total
##
##
##first = int(input("Enter first number: "))
##second = int(input("Enter second number: "))
##
##a = sum_of_factors(first)
##b = sum_of_factors(second)
##
##if a == second and b == first:
##    print("Amicable Numbers")
##else:
##    print("Not Amicable Numbers")



####armstrong
##def find_power(base, power):
##    result = 1
##    while power > 0:
##        result = result * base
##        power-=1
##    
##    return result
##
##def count_of_digits(no):
##    count = 0
##    while no > 0:
##        no = no // 10
##        count+=1
##    return count
##
##no = 153
##digits_count = count_of_digits(no)
##print('Count of Digits:', digits_count)
##
##armstrong = 0
##while no > 0:
##    rem = no % 10
##
##    result = find_power(rem, digits_count)
##    print(rem, ' -->',result)
##    armstrong = armstrong + result
##    no = no // 10
##
##
##print('Armstrong value is', armstrong)
##
##if no == armstrong: 
##    print("Given Number is Armstrong")
##else:
##    print("Not Armstrong")



##no = 111
##
##def find_power(base, power):
##    result = 1
##    while power > 0:
##        result = result * base
##        power-=1
##    
##    return result
##
##decimal = 0
##power = 0
##while no>0:
##    rem = no%10     #1 * findpower(2,0) 0   1
##    decimal = decimal + (rem * find_power(2,power))
##    no = no // 10
##    power += 1
##
##print(decimal)

##
##for i in range(0,5):
##    print(i,end=" ")



name="vinayag"
print(name[:])
print(name[3:])
print(name[:4])
print(name[3::2])
print(name[:4:2])
print(name[::2])
print(name[::-1])
print(name[-1::-1])
print(name[-1::-2])














