##count=1
##while count<=5:
##    print(1, end= '#')
##    count=count+1



##total = 0 
##no = 1
##while no<=10:
##    total = total + no
##    no = no + 1
##print(total)

##flowers = 1
##temples_covered = 7
##while temples_covered>0:
##    temples_covered = temples_covered - 1
##    flowers = flowers * 2   #2
##
##print(flowers)


##
##beat =512
##num=10
##total=0
##while 10>0:
##    beat=beat%2
##    total=total+1
##print(total)




##stations = 30
##i = 1
##while i <= stations:
##    if i % 3 == 0:
##        print("train 1",i)
##    if i % 5 == 0:
##        print("train 2",i)
##    if i % 3 == 0 and i % 5 == 0:
##        print("Meeting at station:", i)
##    i += 1




##station_no = 1
##
##first = 0
##last = 0
##count = 0
##
##print("All Stations:")
##
##while station_no <= 300:
##    if station_no % 3 == 0 and station_no % 8 == 0:
##        
##        # print all stations
##        print(station_no)
##
##
##        # first station
##        if first == 0:
##            first = station_no
##        
##        # last station
##        last = station_no
##        
##        # count
##        count += 1
##
##    station_no += 1
##
##
##print("\nFirst Station:", first)
##print("Last Station:", last)
##print("Total Stations:", count)
##
##
##
##
##
##station_no = 24
##
##count = 0
##
##while station_no <= 300:
##
##    print(station_no)
##
##    last_station = station_no
##    count = count + 1
##
##    station_no = station_no + 24
##
##
##print("\nFirst Station :", 24)
##print("All Stations Count :", count)
##print("Last Station Number :", last_station)




##def find_prime(no):
##    if no>1:
##        div = 2
##        divisors_count = 0
##        while div <= no//2:
##            if no % div == 0: 
##                print('Divisor: ', div)
##                divisors_count+=1
##            div+=1
##
##        if divisors_count == 0:
##            return True
##        else:
##            return False
##
##result = find_prime(2)
##print(result)
##result = find_prime(13)
##print(result)
##result = find_prime(12)
##print(result)


##--------task--------
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


#Sum of Digits
no = 6739
sum_of_digits = 0 
while no>0:   
    sum_of_digits = sum_of_digits + no%10   #4321
    no = no // 10   

print(sum_of_digits)

