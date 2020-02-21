
'''
#원본 1012에
menu = {}; bl = True; num = 0
while bl:
    print("1.메뉴 등록"); print("2.메뉴별 가격 보기"); print("3.가격 수정");
    print("4.종료")
    num = int(input(">>>"))
    if num == 1: #메뉴등록도 되고 수정도 됨
        name = input("메뉴 입력 : ");
        if menu.get(name) == None:
            menu[name] = input("가격 입력 :")
        else: print("이미 등록된 메뉴입니다")
    elif num == 2:
        for i in menu.keys():
            print(i,":",menu[i])
    elif num == 3: #메뉴등록도 되고 수정도 됨
        name = input("수정할 목록 입력 : ");
        if menu.get(name) != None:
            menu[name] = input("수정 가격 :")
        else: print("등록되지 않은 메뉴 입니다.")
    elif num == 4:
        name = print("종료")
        bl = False
    else:
        print("숫자를 다시 입력해주세요")
'''

'''
num = {1:"일",2:"이",3:"삼",4:"사",5:"오"}

print(num)
print("num.get(3) :",num.get(3))
print("num.get(9) :",num.get(9))
print("num.get(0) :",num.get(0,'없음'))
# 키값이 존재하지않을때 실수 정수 글자 다 반환가능 '없음'이 반환

su = int(input("찾고자하는 키 입력 : "))
if num.get(su) == None:
    print("값이 없습니다.")
else:
    print(num.get(su))
'''
#교안 보면서 하기
'''
num = {1:"일",2:"이",3:"삼",4:"사",5:"오"}

print("변경전 값 :", num)
print()
print("num.setdefault(9) :",num.setdefault(9, "구~우"))
#어떠한 자료형 전부 가능
#있는 값은 그대로 유지 , 없는 값 추가
print()
print("변경전 후 :",num)
print()
print("num.get(9)번째 value :",num.get(9))
'''
#//dictionary

#set(집합)
#여러값들의 모임
#저장속도는 빠르지만 검색은 반복하여 찾아야함(나올때까지 찾아야함)

'''
names = {'허준','신사임당','권율','홍길동','허준'} #중복되는 요소 허용x

print(type(names))
print(len(names))
print(names)
'''

'''
s = {}
#s=set({}) #set로 초기화
#set(s) #강제 형변환(1회성)
print(type(s)) #<class 'dict'> 기본 자료형 dict

print(set('programming'))
print(set([12,15,17,11,15]))

dic = {'a':1, 'b':2, 'c':3}
print(set(dic)) #강제형변환
#values이용
'''


'''
for x in {'가','나','다','라'}:#컴퓨터가 빨리 출력하는 순서(거의 무작위)
    print(x)
'''


'''
asia = {'korea','china','japan'}
print(asia)

asia.add('thailand')
print(asia)
asia.add('china')
print(asia)
asia.remove('japan')

print(asia)
'''

'''
two = {2,4,6,8,10,12}
three = {3,6,9,12,15}
print('교집합', two & three)
print('합집합', two | three)
print('차집합', two - three)
print('배타적 차집합', two^three)
'''

'''
animal = {'호랑이','사자','강아지','치타','햄스터','고양이'}
pet = {'강아지','고양이','햄스터'}

print(pet <= animal)
print(pet <= pet)

print(pet < animal)
print(pet < pet)
'''

#//set

#문자열

'''
Str = 'Python is Easy. 그리고 programming 할만하다 ^^'
print("Str :",Str)
print()
print('Str.upper() :',Str.upper()) #소문자를 대문자로 변경
print()
print('Str.lower() :',Str.lower()) #대문자를 소문자로 변경
print()
print('Str.swapcase() :',Str.swapcase()) #대소문자 상호 변경    
print()
print('Str.title() :',Str.title()) #각 단어의 첫번째 문자 대문자로 변경
#2,3번째가 만약 대문자라면 소문자로 변경,
#특수문자가 첫번째 있으면 그거 건너뛰고 그 다음 문자 대문자로
'''

'''
st = 'Have a nice day'#문자열의 끝에는 \0 생략되어 있음
print("st :",st)
print()
print("st안에 'a'문자 개수 :",st.count('a')) #대소문자 구분
print("st안에 ''문자 개수 :",st.count('')) #\0포함 16 
print("st안에 'day'문자열 개수 :",st.count('day'))
print("st안에 'dak'문자열 개수 :",st.count('dak'))
'''

#v
#a의 총개수와 첨자의 위치를 출력하시오
#결과 : [1,5,13,17,21,29,33,37,45]
'''
st = "Have a nice day Have a nice day Have a nice day"

a_cnt = 0
i = 0


while st != '\0':
    st.count('a')

    #st.find('a');
    
    if st == '\0':
        print(st.count('a'))
'''#나

'''

st = "Have a nice day Have a nice day Have a nice day"

cnt = 0
ls = []

while True:
    cnt = st.find('a',cnt) #a이면 cnt

    if cnt != -1:
        ls.append(cnt)
        cnt+=1
    else:
        break
print("a의 개수 :", st.count('a'))
print("a의 개수 :", len(ls))
print("a의 인덱스 위치 :",ls)
'''

'''
st = '2015/04/02'

print('st\t\t:',st)
print('replace()\t:',st.replace('/','.'))#/를 .으로
print('replace([0:4])\t:',st.replace(st[0:4],'2017'))#슬라이싱을 이용, 2015를 2017로
print('replace([0:4])\t:',st.replace(st[0:],'2017')) #치환되는 값만 남음
print('replace([0:4])\t:',st.replace(st[1:4],'2017'))#22017/04/02
'''

'''
print("""Sdfadfa
sdfajdklf
asdfjasdf""")
    
st = """ 
dfdf
dfdf
dfdfd
"""
print(st)

print(st1)

'''

'''
#join() : 합치는 것이 아님
Str = '123'
print('"%".join(123)\t: ','%'.join(Str)) #사이마다 넣어줌
print('123.join("%a")\t: ',Str.join('%a'))

li = [ '', '123','456']
print('"공백".join([123,456])\t:'," ".join(li))
li =['','안녕하세요','만나서 반갑습니다','행복한 하루 되세요^^']
print('"엔터".join(li)\t:',"\n\n".join(li))
'''

#//문자열

#함수

'''
def cal(su1,op,su2): #매개변수(지역변수) : 함수 안에서만 사용
    result = 0

    result = su1 + su2
    print(su1,'+',su2,'=',result)

su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
cal(su1,op,su2) #매개변수와 달라도 됨
'''

'''
def cal(su1,op,su2):
    result=0
    result = su1+su2
    print('cal 실행')
    return result #데이터를 호출한 함수로 되돌려줌, 종료도 됨

su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
result=cal(su1,op,su2)
print(su1,'+',su2,'=',result)
print("다음 문장 실행")

'''

'''
def showAvrg(a,b,c):
    print("{}와 {}의 평균".format(a,b))
    print("값은 {}입니다".format(round(c,1)))
#중간에 있어도 됨 선언한 함수가 더 위에 있다면
def avrg(j,k):
    total = j+k;
    f=total/2
    return f;
i=2;j=3;
f=avrg(i,j)
showAvrg(i,j,f)
print("다음 문장 실행")
'''

'''
def func1():
    a=100
    print("func1의 a : %d" % a)

def func2():
    a=200
    print("func1의 a : %d" % a)

func1()
func2()
'''
'''
def func1():
    print("func1의 a : %d" % a)
def func2():
    print("func1의 a : %d" % a)

a = 200 #전역변수

func1()
func2()
'''
'''
def func1():
    a =123
    print("func1의 a : %d" % a)
def func2():
    print("func1의 a : %d" % a)

a = 200#전역변수

func1()
func2()
'''

'''
def sum_func(x1,x2,x3 = 100):
    result = 0
    result = x1 + x2 + x3
    return result
def display():
    Sum = 0
    a,b,c = 10, 20, 30
    Sum = sum_func(a, b)#a하나만 하게되면 에러 매칭이 안된것
    print("매개변수 2개 함수호출 :", Sum)
    Sum = sum_func(a, b, c)
    print("매개변수 3개 함수호출 :", Sum)
display()
'''

#//함수





























