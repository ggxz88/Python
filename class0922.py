#출력함수 제일 중요!!!!
'''
print(123 + 123) 
print(542 - 242)
print(2 * 123)
print(120 / 3) # 숫자
print("120 / 3") #문자열
'''

'''
print("덧셈 결과 : " , 123 + 123) # 숫자는 ,로 구분함. ,는 한칸을 띄움
print("뺄셈 결과 : " , 542 - 242)
print("곱셈 결과 : " , 2 * 123)
print("나눗셈 결과 :", 120 / 3)
'''

'''
print("12 + 54 =", 12 + 54,"입니다")
print("268 - 42 =", 268 - 42,"입니다")
print("2 * 23 =", 2 * 23, "입니다")
print("120 / 3 =", 120 / 3, "입니다")
'''

'''
print(0x36)
print(97)
print(0o53)
print(0b11010100) #전부 10진수 출력(default 10진수임)
'''

'''
print("2진수 : ",bin(0b01111011)) #bin 2진수로 변환해주는 함수
print("8진수 : ",oct(0b01111011)) #oct 8진수로 변환해주는 함수
print("16진수 : ",hex(0b01111011)) #hex 16진수로 변환해주는 함수
print("10진수 : ",0b01111011)
'''

'''
print("%d" % 123) # % : 호출, %는 반드시 한 번만
#print("%d %d" % 123) # 호출되어질 대상 한 개뿐
#print(" %d " % (123, 321)) # 호출 되어질 대상이 두 개나 있음, 대상이 충분치가 않음
print(" %d " % 123, 321) # 정상적으로 출력됨
print("%d %d " % (123, 321))
print("%d + %d = %d" % (123, 321, 123 + 321))
'''

'''
print("%d" % 123)
print("%                d" % 123) #서식 제어문은 떨어져있어도 형식에 맞게 츨력
print("234 \    t") # \는 떨어져 있으면 형식에 맞게 출력 안 됨
'''

'''
print("10진 정수 : %d" % 123)
print("10진 정수 : %d" % 0o173)
print("10진 정수 : %d" % 0x7b)

print("8진 정수 : %o" % 123)
print("8진 정수 : %o" % 0o173)
print("8진 정수 : %o" % 0x7b)

print("16진 정수 : %x" % 123)
print("16진 정수 : %x" % 0o173)
print("16진 정수 : %x" % 0x7b)
'''

'''
print("정수 표현 : %d" % 123)
print("정수 표현 : %d" % 123.623) # 소수자리를 버림
print("정수 표현 : %d %d" % (123, 456))

print("\n실수 표현 : %f" % 456) #f : 소수점 6자리만 f. lf차이 없음
print("실수 표현 : %f" % 456.456) 
print("실수 표현 : %f %f" % (123.123, 456.456))
'''

'''
print("문자 표현 : %c %c" % ("한","글")) # 받침있는 글자도 단일 문자로 인식
print("문자 표현 : %c %c" % ('표','현'))
print("문자 표현 : %c %s" % ('표','현')) # 정상적으로 가능

print("\n문자열 표현 : %s" % "안녕")
print("문자열 표현 : %s\t%s" % ("문자열", '표현방식'))
#print("문자열 표현 : %s\t%c" % ("문자열", '표현방식')) #불가능
print("문자열 표현 : %s\t%c%c%c%c" % ("문자열", '표현방식')) # 글자수 대로 %c를 넣으면 가능

print("%c" % 65) #아스키코드 값으로 출력, 65에 해당하는 아스키코드 값 출력
#print("%d" % 'A') 에러 반대로는 안됨 C에서는 가능 "A"도 마찬가지
'''

'''
#★★★★★
print("기본 값 : %d" % 123)

print("설정 값 : %5d" % 123)
# 숫자 : 몇 칸을 확보할지, %5d일 때 만약 5칸을 넘어가면 무시가 됨
# \t와의 차이점 : 무조건 8칸, 여유가 있을 때까지 계속 확보

print("설정 값 : %05d" % 123) # 빈공간을 0으로 채움, 음수는 안됨 ex)%-05d (x)

print("설정 값 : %5d%5d" % (123, 123)) #

print("설정 값 : %8s%8s" % ('대한', '민국'))
# 서식제어문은 한글은 한 글자로 받아들임 그래서 6칸이 남아있음 씽크가 맞지 않음 -> 한글은 서식 제어문으로 정리가 힘들다.
# \t는 2글자를 4글자로 판단해서 괜찮음

#print("설정 값 : %5d%5d" % 123, 123) #숫자에 괄호 없으면 에러

print("설정 값 : %-5d%-5d" % (123, 123)) 
'''

'''
#★★★
print("기본 값 : %f" % 123.45678)  

print("설정 값 : %10.3f" % 123.45678)
# 앞의 정수부분은 소수점을 포함한 전체 칸 확보하는 수
#소수점 뒤의 수는 소수점을 뒤의 수만큼만 확보(반올림)

print("설정 값 : %2.1f" % 123.45678) #앞의 수가 정수부분 보다 작으면 무시됨
#.1은 그대로 반영(반올림)

print("설정 값 : %.2f" % 123.45678) #앞의 수 없으면 무시, .2는 그대로 반영(반올림)
'''

'''
print("기본 값 : %s" % "python test")
print("설정 값 : %20s" % "python test")
'''

'''
print("========== 출력 결과 ==========")
print("\n")
print("이름 \t: %s" % "홍길동")
print("나이 \t: %d" % 20)
print("Tel \t: %s" % '010-1234-1234') #'', '' 둘 다 상관 x
print("키 \t: %.1f" % 178.5)
print("몸무게 \t: %d" % 75)
print("혈액형 \t: %c" % "O")  #'', '' 둘 다 상관 x

print("Tel   : %s-%d-%d" % ('010', 1234, 1234))
#%d, %f를 하면 010 안됨 010이란 숫자는 없기 때문
print("Tel   : %s%c%d%c%d" % ('010' ,'-', 1234, '-', 1234))
print("Tel   : 0%d-%d-%d" % (10, 1234, 1234))
print("Tel   : %03d-%d-%d" % (10, 1234, 1234))
'''
#//출력함수



###변수(in python 변수와 포인터의 의미 합쳐짐) : 주소값 그대로 그 안의 수는 매일 바뀜
#변수는 마지막에 들어간 데이터만 사용 가능

'''
num = 100 # = : 대입 연산자
# 규칙 : ⓐ우측항을 좌측항으로 대입한다. ⓑ우측항이 우선(모든 연산에 있어서 우측이 먼저)
# 좌측에는 상수 불가
# 대입 : num의 주소가 x100일 때 x100에 100이 들어간 것(in python)

print("정수 형 변수 사용 : %d" % num)

print("정수 형 변수 사용 : ", num)

print("정수 형 변수 사용 : num ") #이 곳에서의 num은 변수가 아님
'''

'''
num = 5

print("변경 전 num : ", num)

num = num + 10 #주소 값도 변경됨

print("변경 후 num : " , num) 
'''

'''
num1 = 5
num2 = 10
#sum = num1 + num2 # sum은 함수, 예약어가 변수처럼 사용됨

#print("두 수의 합 : " ,sum)

_sum = num1 + num2 # sum은 함수, 예약어가 변수처럼 사용됨

print("두 수의 합 : " ,_sum)

print(sum(range(1, 11)))

'''

'''
num1 = 5
num2 = 10
_sum = num1 + num2

print("id num1 : ", id(num1)) #id는 idenfier operator의 약자
# id : 동일 객체 여부 판단, 일련번호(주소) 출력
print(id(5))
print("id num2 : ", id(num2))
print("id _sum : ", id(_sum))
'''

'''
num1 = 10
num2 = 20 # num1 = 10, num2 = 20는 안됨
_sum = num1 + num2

print("num1(%d) + num2(%d) = %d" %(num1, num2, _sum)) # %뒤에 괄호 빼먹지 말기!
print("num1(%d) + num2(%d) = %d" %(num1, num2, num1 + num2)) 
'''

'''
#다음과 같이 나오도록 코딩하시오.(단 변수를 사용하시오)
#파이썬 100점
score = 100

print("파이썬 %d점" % score)

#나는 27살이다.

age = 27

print("나는 %d살 이다." % age)

#파이썬, c언어, Java 3과목의 점수를 입력하고
#합계와 평균을 구하는 프로그램를 작성하시오.(평균 소수점 2자리까지)

python_score = 97
c_score = 87
java_score = 76
_sum = python_score + c_score + java_score
average = _sum/3

print("합계 : %d, 평균 : %.2f" % (_sum, average))
# python_score + c_score + java_score괄호 없이 하면 에러
print("합계 : %d, 평균 : %.2f" % ((python_score + c_score + java_score), (python_score + c_score + java_score)/3))
'''
'''
#당신은 놀이공원을 가기 위해 11개의 지하철 역을 지나왔다.
#출발역에서 도착역까지 37분이 걸렸다면 한 역을 지나가는데 걸리는 시간은?
#(소수점 두자리까지 출력)

all_time = 37
station = 11
s_time = all_time/station


print("한 역을 지나가는데 걸리는 시간 : %.2f분" % (all_time/station))

print("한 역을 지나가는데 걸리는 시간 : %.2f분" % s_time)

'''
'''
flt = 123.567

print("%.2f"% flt)
print(flt)
flt = round(flt, 2)
print(flt)
'''

'''
print("round(flt) : ", round(flt)) #실수를 넣으면 정수처리 반올림

print("round(flt, 1) : ", round(flt, 1)) # 소수점 첫째 자리에서 끊어서 반올림

print("round(flt, 2) : ", round(flt, 2)) # 소수점 둘째 자리에서 끊어서 반올림

#round함수와 %.2f와 다른 점 : %.2f는 원래 데이터 값 안바뀜 round는 원래 값 가공
'''

flt = 123.123

print("%.3f + %.3f = %.3f" % (flt, 321.321, flt+321.321)) # %두번 못씀
print(flt, "+", 321.321, "=", flt + 321.321)

ch1, ch2, ch3 = "파", '2', "썬"

print("%c + %c + %c = %s" %(ch1, ch2, ch3, ch1+ch2+ch3))
print(ch1, "+", ch2, "+", ch3, "=", ch1+ch2+ch3)

str_1 = "python ";str_2 = "test"
str_3 = str_1 + str_2

print("%s + %s = %s" % (str_1, str_2, str_1+str_2))
print(str_1, "+", str_2, "=", str_1+str_2)

#자료형 +(연산자) 자료형 = 합산











