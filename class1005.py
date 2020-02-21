##반복 제어문

#끝값 - 초기값 -> 실행 횟수

'''
for i in range(1, 11, 1): #11보다 작을 때 까지 반복, 반복 횟수만 결정
    print(i) 

print('다음 문장')
'''

'''
for i in range(0, 3, 1): #범위는 정수만 가능
    print("i : ",i,"for문 이해하기^^")

print('다음 문장들 실행')
'''

'''
for i in range(1, 11, 1):
    if i % 2 == 0:
        print("i = ", i, "값 확인")\

print('다음 문장')
'''    

'''
for i in range(0, 11, 2):
    print("i = ", i, "값 확인")
'''

'''
for i in range(10, -1, -1):
    print(i, ": 10 ~ 0 까지 출력")
'''

'''
sum = 0 #초기화

for i in range(1, 11, 1):
    sum += i

print("1부터 10까지의 합 : %d" % sum) #다시
'''

'''
for i in range(1, 11, 1):
    print(i, end = " ")
'''
'''
for i in range(1, 31, 1): # 5가 아래로 내려감
    if i % 5 == 0: print("\n")
    print(i, end = "\t")
'''

'''
for i in range(1, 31, 1):
    print(i, end = "\t")
    if i % 5 == 0: print("\n")
'''
'''
for i in range(1, 31, 1):
    print("%d\t"%i, end="")
    if i % 5 == 0: print("\n")
'''

'''
i, Sum = 0, 0
start, en, grow = 0, 0, 0

start = int(input("시작값 입력 : "))
en = int(input("끝값 입력 : "))
grow = int(input("증가값 입력 : "))

for i in range (start, en+1, grow):
    Sum = Sum + i

print("%d에서 %d까지 %d씩 증가한 값의 합 : %d" % (start, en, grow, Sum))
'''

'''
for i in range(0, 10): #증감값 생략, 증감값 기본: +1
    print(i)

for i in range(10): #초기값, 증감값 생략, 초기값 기본 :0
    print(i)

#for i in range(10, 2):
#   print(i)

for i in range(0, 10, 2):
    print(i)
'''

#시작 값, 끝 값, 증가값(1)입력 받아 시작과 끝값 사이의 7의 배수를 출력하시오
'''
fir = int(input("시작 값 : "))
las = int(input("끝 값 : "))
grow = int(input("증감 값 : ")) # v
for i in range(fir, las+1, grow): #las만 아님 꼭 +1
    if i % 7 == 0:
        print(i)
'''

#1 ~ 100 사이의 값 중 3의 배수이며, 5의 배수에 해당하는 합을 구하시오
'''
Sum = 0
for i in range(1, 101, 1): #for i in range(101)도 괜찮음
    if i % 3 == 0 and i % 5 == 0:
        Sum += i
print("합 : %d" % Sum)
'''

#두 수를 입력 받아 입력받은 두 수의 범위 안의 합을 구하시오

'''
num1 = int(input("첫 번째 수를 입력하시오 : "))
num2 = int(input("두 번째 수를 입력하시오 : "))
Sum = 0
if num1<num2 : # v
    for i in range(num1, num2+1, 1):
        Sum += i
if num1 > num2: # v
    for i in range(num2, num1+1, 1):
        Sum += i
print("입력한 두 수의 범위 안의 합 : %d" % Sum)
'''

#첫날에 10원을 예금하고 다음날에는 전날의 2배를 예금하는 방식으로 한 달(30일)동안
#저축한 금액 중 마지막 저금액을 구하시오
'''
money = 10

for i in range(1, 30, 1): #31아님
    money *= 2
    #money = money * 2

print("마지막 저축되어지는 금액 : %d" % money)
'''

'''
money = 10

for i in range(2, 31, 1): # v
    money *= 2

print("마지막 저축되어지는 금액 : %d" % money)
'''

'''
save = 10
money = 10

for i in range(2, 31, 1): 
    money *= 2
    save += money
print("총 저축액 : %d" % save)
'''

'''
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: #index의 길이만큼 반복(횟수)
#for i in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: #반복은 되지만 증감은 되지 않음 
    print("i : ",i)
'''
'''
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in ls:
    print("i: ", i)
for i in ls:
    print(i, end = " ")
'''

'''
ls = [10, "test", 123.123]
print("list : ", ls)
print()
for i in ls:
    print("i에", i, "대입한 후 print() 실행")
    print( type(i) )
'''

'''
st = "Hello Python"
for i in st:
    print("i : ", i)

for i in st:
    print(i, end = "")
'''


#st = "It is a fun Python class" 다음 문자열 중에서 'a'의 개수와 's'의 개수
#그리고 총 개수(공백 포함)도 구하시오

#결과
#총개수 : 24
#a 개수 : 2
#s 개수 : 3

'''
st = "It is a fun Python class"
Sum = 0
A = 0
S = 0

for i in st:
    Sum += 1
    if i == 'a':
        A += 1
    if i == 's':
    #elif i == 's': # 좀 더 효율적
        S += 1
print("총개수 : %d" % Sum)
print("a 개수 : %d" % A)
print("s 개수 : %d" % S)
'''

'''
# v
print("{0} + {1} = {2}".format(10, 2, 10+2)) #format:형식 지정
print("{2} + {1} = {0}".format(10, 2, 10+2))
print("{} + {} = {}".format(10, 2, 10+2))

print("{:,}".format(1000000))#1000 단위마다 , 찍어붐

print("{:<10},왼쪽정렬,{:0<10}".format('첫번째','두번째'))
print("{:>10},오른쪽정렬,{:9>10}".format('첫번째', '두번째'))
print("{:^10},가운데정렬,{:5^10}".format('첫번째', '두번째'))
#홀수이면 처음바이트를 제외하고 가운데 정렬
'''

'''
for i in range(0, 3, 1):
    for k in range(0, 5, 1):
        print("이중 for문(i : %d\tk: %d)" % (i, k ))
'''

#위의 내용을 바탕으로 구구단 만들기

'''
print("---------------------------- 구 구 단 -------------------------")
#print("{:-^63}".format(' 구 구 단'))
print("  2단\t  3단\t  4단\t  5단\t  6단\t  7단\t  8단\t  9단")
#for i in range(2, 10):
#    print("{:^6}".format('%d단'%i),end="\t")
#print()
print("---------------------------------------------------------------")
#print("-"*63)
for i in range(1, 10, 1):
    for k in range(2, 10, 1):
        print("%d*%d=%d" %(k, i, i*k), end = "\t")#print("%d*%d=%d\t" %(k, i, i*k), end = "")  
        if k == 9:
            print("")#print("\n")
    #print() #if문 대신        
#print("{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}{:^7}".format('2단','3단','4단','5단','6단','7단','8단','9단'))
'''

# v
#아래와 같이 출력 되게 만드시오
#상위포문 %d일때 하위 포문 : 0 0 0 0 0
'''
#나
for i in range(0, 5, 1):
    print("상위포문 %d일때 하위 포문 : " % i)
    for k in range(0, 5, 1):
        print("%d %d %d %d %d " % (i*k, i*k, i*k, i*k,i*k),end = '')
        print()
'''
'''
for i in range(0, 5, 1):
    print("상위포문 %d일때 하위 포문 : " % i, end = '')
    for k in range(0, 5, 1):
        print(i*k, end="  ")
    print()
'''
#v
#2중 for 문을 이용하여 아래와 같이 출력하시오
'''   
for i in range(1, 22, 5):
    for k in range(0, 5, 1):
        print(i+k, end = "\t")
    print()        
'''
'''
#나
sum = 0
for i in range(1, 6, 1):
    for k in range(0, 5, 1):
        sum += 1
        print(sum, end = "\t")
    print()  
'''

'''
i = 0 #초기값
while i < 5: #끝값
    print(i, "종속 문장")
    i+=1 #증감값

print("다음 문장")

#for문으로 변경
for i in range(0, 5, 1):
    print(i, "종속 문장")

print("다음 문장")

'''
'''
i = 1
odd, even = 0, 0

while i<=10:
    if i % 2 == 0:
        even +=i
    else:
        odd+=i
    i+=1
print("1-10 짝수의 합: ", even)
print("1-10 홀수의 합: ", odd)
'''
'''
#for문으로 변경
odd, even = 0, 0

for i in range(1, 11, 1):#끝값 10 아님!!!
    if i % 2 == 0:
        even +=i
    else:
        odd+=i
print("1-10 짝수의 합: ", even)
print("1-10 홀수의 합: ", odd)

'''

i = 0
while i< 5:
    print(i, "종속 문장")
    i+=1
else:
    print("조건식이 거짓일 경우 : ", i)
print("다음 문장")





















