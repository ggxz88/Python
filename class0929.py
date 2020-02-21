'''
print("1.easy game")
print("2.hard game")
print("3.exit")

num1 = int(input("선택 : "))

if num1 == 1: #false면 종속문장 실행 안 함
    print("easy game start")
if num1 == 2:
    print("hard game start")
if num1 == 3:
    print("game exit")
'''

'''
#날짜를 입력받아 요일을 구하시오
#(단. 1일은 무조건 월요일이다. 7일은 일요일. 8일은 다시 월요일)
#(어떤 값을 입력 받던 요일이 정확히 출력 되게 만드시오)

date = int(input("날짜 : "))
day = date % 7

if day == 1:
    print("%d일은 월요일 입니다." % date)
if day == 2:
    print("%d일은 화요일 입니다." % date)
if day == 3:
    print("%d일은 수요일 입니다." % date)
if day == 4:
    print("%d일은 목요일 입니다." % date)
if day == 5:
    print("%d일은 금요일 입니다." % date)
if day == 6:
    print("%d일은 토요일 입니다." % date)
#if day == 7: #바보
#   print("%d일은 일요일 입니다." % date)
if day == 0:
    print("%d일은 일요일 입니다." % date)
'''

#입력한 데이터가 3의 배수인 경우 출력하시오
'''
data = int(input("데이터를 입력하시오: "))

if (data % 3 == 0) and (data != 0) :
    print("%d" % data)
if data % 3 != 0 :
    print("3의 배수가 아닙니다")
if data == 0 :
    print("0입니다.")
'''
#절대값을 구하는 프로그램을 작성하시오
'''
num1 = int(input("숫자를 입력하시오 : "))
#나
if num1 < 0 :
    print("절대값 : %d" % (num1 * (-1))) #num *= -1
if num1 >= 0 :
    print("절대값 : %d" % num1)

#선생님
#if num1 < 0 : num *= -1
#print("절대값 : %d" % num1)
'''
#수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
'''
num2 = int(input("숫자를 입력하시오: "))

if (num2 % 2 == 0) and (num2 != 0) :
    print("짝수입니다.")
if num2 % 2 == 1:
    print("홀수입니다.")
if num2 == 0 :
    print("0입니다.")
'''
#두 수를 입력 받아 큰 수를 출력하시오
'''
num3 = int(input("첫 번째 수를 입력하시오: "))
num4 = int(input("두 번째 수를 입력하시오: "))

if num3 == num4 :
    print("두 수는 같습니다.")
if num3 > num4 :
    print("큰 수 : %d" % num3)
if num3 < num4 :
    print("큰 수 : %d" % num4)

#선생님
#if num3 > num4 : num4 = num3
#  print("%d가 큰 수 입니다" % num4)
'''
#세 수를 입력 받아 큰 수를 출력하시오
'''
num5 = int(input("첫 번째 수를 입력하시오: "))
num6 = int(input("두 번째 수를 입력하시오: "))
num7 = int(input("세 번째 수를 입력하시오: "))
#나
#if (num5 > num6) and (num5 > num7):
#    print("큰 수 : %d" % num5)
#if (num6 > num5) and (num6 > num7):
#    print("큰 수 : %d" % num6)
#if (num7 > num5) and (num7 > num6):
#    print("큰 수 : %d" % num7)
#if (num7 == num5) and (num7 == num6):
#    print("세 숫자가 같습니다" % num7)

#선생님
if (num5 >= num6) and (num5 >= num7):
    print("큰 수 : %d" % num5)
if (num6 > num5) and (num6 >= num7):
    print("큰 수 : %d" % num6)
if (num7 > num5) and (num7 > num6):
    print("큰 수 : %d" % num7)

#if num1<num2: num1=num2
#if num1<num3: num1=num3
#print("가장 큰 수는 %d입니다." % num1)
'''
#두 수를 입력 받아 큰 수가 짝수이면 출력하시오
'''
num8 = int(input("첫 번째 수를 입력하시오: "))
num9 = int(input("두 번째 수를 입력하시오: "))

if (num8 > num9) and (num8 % 2 == 0):
    print("큰 수 : %d" % num8)
if (num8 > num9) and (num8 % 2 == 1):
    print("큰 수가 홀수입니다.")
if (num9 > num8) and (num9 % 2 == 0):
    print("큰 수 : %d" % num9)
if (num9 > num8) and (num9 % 2 == 1):
    print("큰 수가 홀수입니다.")   
if (num8 == num9) :
    print("두 수는 같습니다.")
'''
#두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오
'''
num10 = int(input("첫 번째 수를 입력하시오: "))
num11 = int(input("두 번째 수를 입력하시오: "))

sum = num10 + num11

if(sum % 2 == 0) and (sum % 3 == 0):
    print("%d" % sum)
if(sum % 2 != 0) and (sum % 3 == 0):
    print("두 수의 합이 짝수가 아닙니다.")
if(sum % 2 == 0) and (sum % 3 != 0):
    print("두 수의 합이 3의 배수가 아닙니다.")
if(sum % 2 != 0) and (sum % 3 != 0):
    print("두 수의 합이 짝수와 3의 배수가 모두 아닙니다.")
'''

'''
num = int(input("수 입력 : "))

if num == 1:
    print("1입력")
else:
    print("1이 아닌 값 입력")
'''

'''
arr = [1, 2, 3, 4, 5]
na = int(input("찾을 숫자 입력 : "))

if na in arr: #in :멤버 연산자 in(존재하면 참)/not in(존재하지 않으면 참)
    print("arr : ", arr, "찾는 숫자가 존재 합니다. : ", na)
else:
    print("arr : ", arr, "안에는 찾고자 하는 숫자가 없습니다: " , na)
print('결과 : ',na in arr)
'''

'''
st = "Hello Python Fun" #공백 인식
na = input("찾고자 하는 문자열 입력 : ")

if na in st:
    print("st : ", st, "찾는 문자열 : ", na, "존재한다")
else:
    print("st 안에는 ", na, "존재 하지 않습니다") 
'''

'''
old_id = input("저장할 ID 입력 : ")
print("인증 프로그램입니다")
print("ID와 PW를 입력하세요")
new_id = input("ID 입력 : ")
if old_id == new_id :
    print("인증 통과 했습니다")
else:
    print("인증 실패")
'''

'''
num = int(input("수 입력 : "))

if num % 3 == 0:
    if num % 2 == 0:
        print("num은 3의 배수이면서 짝수 입니다")

#if문 하나로 변경
#if num % 3 == 0 and num % 2 ==0 :
#    print("num은 3의 배수이면서 짝수 입니다")   

print("다음문장 실행")
'''

'''
num = int(input("수 입력 : "))

if num > 0:
    if num % 2 == 0:
        print("num은 양의 짝수 입니다")
    else:
        print("num은 양의 홀수 입니다")
else:
    print("num은 음수 입니다")
print("다음 문장 실행")
'''

#사용자로부터 Gbyte의 값을 입력받아 byte, Kbyte, Mbyte로 각각 출력 되게 만드시오.
#(1.byte 2.Kbyte 3.Mbyte 선택)
'''
Gb = int(input("Gbyte를 입력하시오 : "))
ch = int(input("1.byte 2.Kbyte 3.Mbyte 선택 : "))

if ch == 1:
    print("byte : %d" % (Gb*1024*1024*1024))
#   print("byte : %d" % Gb*1024**3)
if ch == 2:
    print("Kbyte : %d" % (Gb*1024*1024))
#   print("Kbyte : %d" % Gb*1024**2)
if ch == 3:
    print("Mbyte : %d" % (Gb*1024))
#   print("Mbyte : %d" % Gb*1024)
if ch > 3 or ch < 1:
    print("선택이 잘못되었습니다.")
'''
#인증 프로그램을 만드시오
#1. 아이디가 틀리면 등록되지않은 아이디 입니다 출력
#2. 비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
#3.아이디와 비밀번호가 일치하다면 인증 통과 출력
'''
Id = input("저장할 아이디를 입력하시오 : ")
pwd = input("저장할 비밀번호를 입력하시오 : ")

s_id = input("아이디를 입력하시오 :")

if s_id == Id:
    s_pwd = input("비밀번호를 입력하시오 :")
    if s_pwd == pwd:
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("등록되지않은 아이디 입니다.") #나
'''
'''
Id = input("저장할 아이디를 입력하시오 : ")
pwd = input("저장할 비밀번호를 입력하시오 : ")

s_id = input("아이디를 입력하시오 :")
s_pwd = input("비밀번호를 입력하시오 :")

if s_id == Id:
    if s_pwd == pwd:
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("등록되지않은 아이디 입니다.")
'''

'''
#if~elif~else문

num = int(input("수 입력 : "))
if num > 100:
    print("100보다 큰 수 입력")
elif num > 50:
    print("50보다 큰 수 입력")
elif num > 0:
    print("0보다 큰 수 입력")
else:
    print("그 외의 값 입력")
'''
'''
if num > 0:
    print("0보다 큰 수 입력")
elif num > 50:
    print("50보다 큰 수 입력")
elif num > 100:
    print("100보다 큰 수 입력")
else:
    print("그 외의 값 입력")
#음수를 제외한 수들은 0보다 크다고 출력함
'''

#이름, 학번, 3과목의 성적을 입력받아 합계와 평균을 구하고, 평균이 90이상이면 'A',
#80이상 'B', 70이상 'C', 60이상 'D', 60미만이면 'F'를 출력하시오
'''
name = input("이름 :")
sch_id = input("학번 : ")
#result = ""
sub1 = int(input("과목1 성적 (100점 만점): "))
sub2 = int(input("과목2 성적 (100점 만점): "))
sub3 = int(input("과목3 성적 (100점 만점): "))
sum = sub1 + sub2 + sub3
avg =  sum / 3

if avg <= 100 and avg >= 90:
    print("이름:%s 학번:%s 합계:%d 성적:A" % (name, sch_id, sum))
elif avg < 90 and avg >= 80:
    print("이름:%s 학번:%s 합계:%d 성적:B" % (name, sch_id, sum))
elif avg < 80 and avg >= 70:
    print("이름:%s 학번:%s 합계:%d 성적:C" % (name, sch_id, sum))
elif avg < 70 and avg >= 60:
    print("이름:%s 학번:%s 합계:%d 성적:D" % (name, sch_id, sum))
elif avg < 60:
    print("이름:%s 학번:%s 합계:%d 성적:F" % (name, sch_id, sum))
else:
    print("성적을 잘못 입력하였습니다.")
'''
#if avg >= 90: result = 'A'도 가능


#커피의 개당 가격은 2000원이다. 10개 초과하면 초과하는 양에 대해서만 개당 1500원씩
#받는다. 커피의 개수를 입력 받아 금액을 출력하시오.
'''
cof = int(input("커피의 개수를 입력하시오 : "))

if cof > 10:
    print("금액 : %d" % (((cof-10)*1500)+(10*2000)))
else:
    print("금액 : %d" % (cof*2000))
'''

'''
money = 0
cof = int(input("커피의 개수를 입력하시오 : "))

if cof > 10:
    money += 20000+(num-10)*1500
    print("금액 : %d" % money)
else:
    money = num*2000
    print("금액 : %d" % money))
'''

#정수를 입력 받아 아래와 같이 출력하시오.
#3의 배수이면서, 4의 배수 입니다
#3의 배수 입니다
#4의 배수 입니다
#3의 배수도 4의 배수도 아닙니다
#0은 3의 배수도 4의 배수도 아닙니다
'''
num = int(input("정수 입력: "))

if num == 0:
    print("0은 3의 배수도 4의 배수도 아닙니다") #1
elif num < 0:
    print("음수입니다.")
elif num % 3 == 0 and num % 4 == 0 :
    print("3의 배수이면서, 4의 배수 입니다") #3
elif num % 3 == 0:
    print("3의 배수 입니다") #4
elif num % 4 == 0:
    print("4의 배수 입니다") #4
elif num % 3 != 0 and num % 4 != 0:
    print("3의 배수도 4의 배수도 아닙니다.") #2
else:
    print("잘못 입력하였습니다.")
'''

#비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 10분 단위로 추가요금 5000원씩
#부가된다. 비행기 탈 시간을 입력하여 요금 계산기를 만드시오
'''
time = int(input("비행기 탈 시간(분) :"))
fee = 30000 # 연산할 때에 초기값 필수

if time > 30:
    fee = 35000
    add = (time - 31) // 10 #add = (time - 30) // 10#나
    if add >= 1:
        fee += 5000 * add
    print("금액 : %d" % fee)
else:
    print("금액 : %d" % fee) # 나
'''

'''
time = int(input("비행기 탈 시간(분) :"))
fee = 30000 # 연산할 때에 초기값 필수
time -= 30

if time > 0:
    fee +=(5000+((time-1)//10)*5000) #41분부터 추가요금
print("요금 : %d" % fee)
'''
#money = 30000
#money += round((time+4)/10)*5000
