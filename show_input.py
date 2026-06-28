ones=["zero","one","two","three","four","five","six","seven","eight","nine",
      "ten","eleven","twelve","thriteen","forteen","fifteen","sixteen",
      "seventeen","eighteen","nineteen"]
tens=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


num =int( input("enter the value"))
while num>0:
    if num<20:
        print(ones[num],end=" ")
        break
    elif num<100:
        res=num//10
        print(tens[res-1],end=" ")
        num=num%10
    else:
        if num<1000:
            res=num//100
            print(ones[res],"hundred",end=" ")
            num=num%100
