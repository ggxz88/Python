'''
A = 10
B = 10
print("type :", type(A<B)); print("type :",(A<B)) #type함수는 데이터의 자료형 출력
num = 100; print("type : %s" % type(num))
flt = 321.321; print("type : %s" % type(flt))
ch = "A "; print("type : %s" % type(ch))
st = "test"; print("type : %s" % type(st))
'''

'''
#변수의 내용도 바뀌고 할당된 주소도 바뀜, 주소에 있는 값을 꺼내서 쓰는 것
num = 100
print("type : %s\tid : %s" % (type(num), id(num)))

num = 321.321
print("type : %s\tid : %s" % (type(num), id(num)))

num = "A"
print("type : %s\tid : %s" % (type(num), id(num)))

num = "test"
print("type : %s\tid : %s" % (type(num), id(num)))
'''

'''
st1 = "Python"
st2 = "Test"
su = 100
flt = 1.11

num = '100'

print(flt + su) # 숫자 + 숫자
print(st1 + st2) # 좌와 우의 자료가 대칭 
#print(su + num) # int + str이라서 오류 
'''

'''
su = 100

print('type(su) : ', type(su)) 
print('type(str(su)) : ', type(str(su))) # 강제 형변환
print('type(float(su)) : ', type(float(su))) # 강제 형변환
#강제 형변환은 1회성!
#모든 자료는 문자열로 강제 형변환 가능
#강제 형변환은 단 한번만 ex) sum = '3.14'를 정수형으로 형변환 불가능
'''

'''
#모름
su = 100
num = '100'
flt = "1.111"
#아래와 같이 출력
#200
#101.111
#100100


print("\t",su + int(num)) #int(num):형변환
print("\t",su + float(flt))
print("\t",str(su) + num)
'''
#//변수

#입력함수
'''
print("숫자 입력")

num1 = input()

print("입력받은 값 : ", num1)
'''

'''
print("이름 입력")
name = input()

print("나이 입력") #type이 str, 숫자 입력했다고 int형이 아님
age = input()

print("%s 님의 나이는 %s 살 입니다." % (name, age))
'''

'''
print("두 수의 합을 구해 줍니다.")
print("두 수 입력")

num1 = input() #입력함수로 받는 변수는 기본타입이 문자열
num2 = input()
num3 = num1 + num2
print("두 수의 합", num1,"+", num2,'=',num3)
'''

'''
#강제 형변환을 일일히 해줘야 함
print("두 수의 합을 구해 줍니다.")
print("두 수 입력")

num1 = input()
num2 = input()
num3 = int(num1) + int(num2)
print("두 수의 합", num1,"+", num2,'=',num3)

print("num1 type : ", type(num1))
print("num2 type : ", type(num2))
print("num3 type : ", type(num3))
'''

'''
num1 = int(input())
num2 = int(input())

result = num1 + num2
print(num1,"+",num2,"=",result)

result = num1 - num2
print(num1,"-",num2,"=",result)

result = num1 * num2
print(num1,"*",num2,"=",result)

result = num1 / num2
print(num1,"/",num2,"=",result)

'''

'''
print("문자열 입력")
name = input()
print("정수 입력")
age = int(input())
print("실수 입력")
flt = float(input())

print("name 값: ",name,"\t type: ",type(name))
print("age 값: ",age,"\t type: ",type(age))
print("float 값: ",flt,"\t type: ",type(flt))
'''

'''
#input안에 문자열 입력 가능 즉, input의 ()안에 print 생략
name = input("이름을 입력하세요 : ")
#
age = int(input("나이를 입력하세요 : "))

addr = input("주소를 입력하세요 : ")

print("이름 : ", name,"\n나이 : ", age, "\n주소 : ", addr)

name = input("이름을 %d번 입력하세요 : " % 10)
#name = input("이름을 입력 하세요 : ", 10) #입력함수에 , 가 들어가면 무조건 error
'''

'''
this_year = int(input("올해의 연도를 4자리로 입력하세요 : "))

birth_year = int(input("당신이 태어난 연도를 4자리로 입력하세요 : "))

age = (this_year - birth_year) + 1

print("당신의 나이는 %d살 입니다." % age)
print("당신의 나이는 %d살 입니다." % ((this_year - birth_year) + 1))
'''

'''
# 600kg제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로 입력 받아
# 현재 엘리베이터에 더 적재할 수 있는 무게를 구하시오.

total = 600 # 입력 안 했음

thing1 = float(input("첫 번째 물건의 무게를 입력하시오: "))

thing2 = float(input("두 번째 물건의 무게를 입력하시오: "))

allow_weight = total - (thing1 + thing2)

print("현재 엘리베이터의 허용 무게는 %.2fkg 입니다." % allow_weight)

'''

'''
#다음과 같은 방법으로 표준 체중을 구할 수 있다
#표준체중 = (현재 키 - 100) * 0.9
#키를 입력하여 표준 체중을 구하시오
#아래와 같이 실행되게 만드시오
#ex> 키를 입력하세요 182
#    표준 체중은 73.8입니다.


height = float(input("키를 입력하세요 : ")) #int여도 상관 없음

standard_weight = (height - 100) * 0.9

print("표준 체중은 %.2f입니다." % standard_weight)

'''

'''
#비만도 비율은 다음과 같은 방법으로 구할 수 있다
#비만도(%) = (현재체중/표준체중) * 100
#현재 체중을 입력하고 1번에서 구한 표준 체중을 이용하여 비만도를 구성하시오
#ex>키를 입력하시오 181
#현재 체중을 입력하시오 81
#표준체중을 73.8이고 비만도는 109.76입니다


height = float(input("키를 입력하시오 : "))

weight = float(input("현재 체중을 입력하시오 : "))

st_weight = (height - 100) * 0.9

fat = (weight/st_weight) * 100

print("표준 체중은 %.2fkg이고 비만도는 %.2f%%입니다." % (st_weight, fat))
'''

'''
#학생이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오

name = input("학생 이름 : ")

korean = int(input("국어 점수 : "))

english = int(input("영어 점수 : "))

math = int(input("수학 점수 : "))

total = korean + english + math

avg = total / 3

print("==================== 학생 정보 ====================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name, korean, english, math, total, avg))
'''

#//입력


#산술 연산자
'''
num1 = 9; num2 = 2

print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
print(num1, "//", num2, "=", num1 // num2)
print(num1, "%", num2, "=", num1 % num2)
print(num1, "**", num2, "=", num1 ** num2)
'''

#관계 연산자

'''
su1 = 3.1; su2 = 3

#true or false로 표현
print("su1 >= su2 : ",(su1 >= su2))
print("su1 <= su2 : ",(su1 <= su2))
print("su1 == su2 : ",(su1 == su2))
print("su1 != su2 : ",(su1 != su2))

#true : 1 false : 0 숫자로 출력, true나 false도 숫자이기 때문, 0을 제외한 모든 값은 true
print("su1 >= su2 : %d" % (su1 >= su2))
#true : 1.000000 false : 0.000000 숫자로 출력
print("su1 >= su2 : %f" % (su1 >= su2))
#true or false로 표현
print("su1 >= su2 : %s" % (su1 >= su2))

'''

#복합 대입 연산자
'''
su1 = su2 =5

su1 += 1
print("su1 + 1 = ", su1)

su1 -= 1
print("su1 - 1 = ", su1)

su1 *= su2
print("su1 * su2 = ", su1)

su1 //= su2
print("su1 // su2 = ", su1)

su1 %= su2
print("su1 % su2 = ", su1)
'''

'''
su1 = 5
su2 = 3
su1 **= su2
su1 -= 2

print("su1 / 4 = ",su1 / 4)
print("su1 // 4 = ",su1 // 4)
print("su1 % 4 = ",su1 % 4)

'''
#논리 연산자

'''
print(0 or 0,":", False or False)
print(1 or 0,":", True or False)
print(0 or 1,":", False or True)
print(1 or 1,":", True or True)
print("not : ",not(0 or 0), ":",not(False or False))
print("not : ", not(1 or 1), ":", not(True or True))
'''

'''
a = 20
b = 10

print(0 or 0, ":", False or (a+b)) #산술 연산 값 반환
print(1 or 0, ":", True or (a+b)) # 뒷 산술 연산을 안함
print(0 and 0, ":", False and (a+b))# 뒷 산술 연산을 안힘
print(1 and 0, ":", True and (a+b)) #산술 연산 값 반환
'''

#비트 연산자

'''
5|3 : 7
5&3 : 1
5^3 : 6
~5 : -6
~-6 : 5
5<<2 : 20
20 >>2 : 5
20 >> 6 : 0
'''

#//연산자

# 조건제어문 => 흐름 제어
'''
num1 = 10
num2 = 5

if num1 > num2: # 종속문장이 꼭 있어야 함
    print("num1이 num2보다 크다") #들여쓰기를 해야함

if True: 
    print("num1이 num2보다 크다") 

if 1: 
    print("num1이 num2보다 크다") 

if num1 + num2: #0을 제외한 모든 수 참
    print("num1이 num2보다 크다") 
'''

'''
num1 = int(input("수 입력 : "))

if num1 % 2 == 0:
    print("num1 : ", num1, "짝수다")
print("나는 다음 문장")

if num1 % 2 == 0:print("num1 : ", num1, "짝수다") #짧고 간결할 때 가능, 한줄이거나

'''

#종속문장이 2개 일 때
'''
num1 = int(input("수 입력: "))

if num1 % 2 == 0:
    print("num1 : ", num1, "짝수다")
    print("num1 : ", num1, "2의 배수이다")

print("나는 다음 문장")

#if num1 % 2 == 0:print("num1 : ", num1, "짝수다")
#   print("num1 : ", num1, "2의 배수이다") # 불가

if num1 % 2 == 0:print("num1 : ", num1, "짝수다"); print("num1 : ", num1, "2의 배수이다") # 불기

'''






