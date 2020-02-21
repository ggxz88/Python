'''
ls = [10, 20, 30]
ls.append(1000)

for i in range(len(ls)):
    print("ls[{}] : {}".format(i,ls[i]))
print("리스트의 총 개수 : ", len(ls))

print("ls : ",ls)

ls =[] #초기화
print("ls초기화 후 :",ls)
'''

'''
ls = []
for i in range(0, 4):
    ls.append(0)
Sum = 0

for i in range(0, len(ls)):
    ls[i] = int(input(str(i+1) + "번째 숫자 : "))
    Sum += ls[i]

for i in range(0, len(ls)):
    print("입력받은 값 ls[{}] : {}".format(i, ls[i]))

print("합계 : %d" % Sum)
'''

'''
num = int(input('몇 개의 공간을 만들겠습니까? : '))
ls = []
Sum = 0
for i in range(num):
    ls.append(int(input(str(i+1) + "번째 숫자 : ")))
    Sum += ls[i]

for i in range(0, len(ls)):
    print("입력받은 값 ls[{}] : {}".format(i, ls[i]))
print("합계 :", Sum)
'''

'''
List = [30, 20, 10]
print("현재 리스트 :", List)

List.append(40)
print("append(40) 후 리스트 :", List)

print("pop()으로 추출한 값 :", List.pop()) 
print("pop() 후 리스트 :", List)

List.sort()#무조건 오름차순
print("sort()후 리스트 :", List)

List.reverse() #내림차순으로 만들어 주는게 아닌 그냥 인덱스를 역순
print("reverse()후 리스트 :", List)

del(List[2])#추출하지 않고 바로 삭제
print("del() 후 리스트 :", List)
'''

'''
List = [30, 20, 10]
print("현재 리스트 :", List)

print("10 값의 위치 :", List.index(10))

List.insert(2, 200) # 삽입되고 원래 값 이후로 뒤로 하나씩 밀려남
print("insert(2, 200) 후 리스트 :", List)

List.remove(200)
print("remove(200) 후 리스트 :", List)

List.extend([555, 666, 555])
print("extend([555, 666, 555]) 후의 리스트 :", List)

print("555값의 개수 :", List.count(555))
'''


#v
#리스트 2개를 만들어서 홀수 번째의 값, 짝수 번째의 값을 따로 넣고 짝수번째와
#홀수번째의 차를 또다른 리스트에 넣고 출력하시오 append써도 됨
#결과: [5, 13, -22, 1, -13]
'''#나
odd_ls = []
even_ls = []

for i in range(0, len(ls)-1):
    if i % 2 == 0 or i == 0:
        ls[i] = even_ls[i]
   
    else:
        ls[i] = odd_ls[i]
'''
'''
ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]

odd = [0,0,0,0,0]
even = [0,0,0,0,0]
result = [0,0,0,0,0]
j = 0
l = 0

for i in range(1, 10, 2): #홀수 #v
    odd[j] = ls[i] #v
    j+=1
for k in range(0, 10, 2): #짝수 #v
    even[l] = ls[k] #v
    result[l] = even[l] - odd[l]  
    l += 1

print(even)
print(odd)
print(result)
'''
     
#v
#ls의 값중 인덱스 홀수 번째와 짝수번째의 합과 차를 구하시오
#(짝수번째[0, 2, 4, 6, 8] -[1, 3, 5, 7, 9]홀수번째)
'''
ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]

odd = 0
even = 0


minus =  even - odd
for i in range(0, 10, 2): 
    odd += ls[i] #v
    
for k in range(1, 10, 2): 
    even += ls[k] #v
    
print(even)
print(odd)
print(even - odd)
'''

#v
#ls에 저장된 값을 invertLs에 거꾸로 저장하시오
'''
ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]

invertLS = []
for i in range(len(ls)-1):
    invertLS[i] = ls[i]
    

print(invertLS)
'''

'''
invertLs = [0,0,0,0,0,0,0,0,0,0]

k= 10 #v

for i in range (0, 10, 1):
    k -= 1 #v
    invertLs[i] = ls[k] #v
    
print(invertLs)
'''


#v
#ls의 값을 오름차순으로 sortLs에 저장 후 출력
#ls의 값을 내림차순으로 reverseLs에 저장 후 출력

'''
ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]

sortls = ls[:] #deepcopy #v
reversels = ls[:]        #v

for i in range(0,len(ls)-1, 1):
    for j in range (i+1, len(ls), 1):
        if sortls[i] > sortls [j]:
            sortls[i], sortls[j] = sortls[j], sortls[i]
    
for i in range(0,len(ls)-1, 1):
    for j in range (i+1, len(ls), 1):
        if reversels[i] < reversels [j]:
            reversels[i], reversels[j] = reversels[j], reversels[i]
            
print(sortls)
print(reversels)
'''



#v
'''
aa = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

print('[0][0]',aa[0][0])
print('[0][1]',aa[0][1])
print('[0][2]',aa[0][2])
print('[0][3]',aa[0][3])
print('[1][0]',aa[1][0])
print('[1][1]',aa[1][1])
'''
'''#나
i = 0
k=0
while i <= 2:
    while  k <= 3:
      print(aa[i][k], end = "\t")
      k+=1
    i+=1
'''
'''
for i in aa:
    for k in i:
        print(k, end = "\t")
    print()
'''
'''
for i in range(len(aa)):
    for k in range(len(aa[i])):
        print(aa[i][k],end = "\t")
    print()
'''
#얕은 복사
'''
aa = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

#a = aa[0]
a = aa #얕은 복사 
a[1] = 200000000

print('[0]',aa[0])
print(a)
print(aa)
'''

'''
#깊은 복사
import copy

aa = [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

#a = aa[0][:]
#a = copy.deepcopy(aa[0])
a = aa[:][:]
#a = copy.deepcopy(aa)
#a[1] = 200000000
a[1] = [0,0,0,0]

#print('[0]',aa[0])
print(a)
print(aa)  

'''

#v
#반복문을 이용하여 아래와 같이 출력하시오

'''
ls_1 = [0,0,0,0,0,0,0,0,0,0,0,0]; ls_2 = [0,0,0,0]; value = 1

for i in range (0, 3, 1):
    for k in range (0, 4, 1):
        ls_2[k] = value
        value += 1
    ls_1[i] = ls_2[k]
        
print(ls_2)
print(ls_1)
'''

'''
ls_1 = []
ls_2 = []
value = 1
for i in range(0, 3):
    for k in range(0, 4):
        ls_1.append(value) #append 사용
        value += 1
    ls_2.append(ls_1)
    ls_1 = [] #초기화 해야함

print(ls_2)

for i in ls_2:
    for j in i:
        print(j,end = "\t")
    print()
'''

'''
be = ['2019','12','31']
print(be)

af = list(map(int, be)) #map : 똑같은 작업을 진행할 때 유용, 집합 자료형에 이용
#list : list로 만들어줌

print(af)

'''
#//List 다시해보기

'''
tp = (10, 20, 30)
#tp = 10, 20, 30 #생략 가능

print("tp :",tp)
print("tp type :",type(tp))
print("tp len : ",len(tp))
'''

'''
tp1 = 10, 20, 30

print("tp1 : ",tp1)
print("tp1 type :",type(tp1))

print("tp1[0] type :",type(tp1[0]))

#tp1[0] = 100 #에러
'''

'''
tpType = "문자열",100,1.111

print("tpType : ", tpType)
print("type :", type(tpType))
print("tpType[0] type :", type(tpType[0]))
print("tpType[1] type :", type(tpType[1]))
print("tpType[2] type :", type(tpType[2]))
'''

'''
tplnt = (10)
#print(tplnt[0]) : 인덱스가 아니라 불가능
print("tplnt : ",type(tplnt)); #<class 'int'>

tpT1 = (10,)
print("tpT1 : ",type(tpT1)); #<class 'tuple'>

tpT2 = 10,
#tpT2 = 20
print(tpT2[0])
print("tpT2 : ",type(tpT2)); #<class 'tuple'>
'''

'''
tt1 = (10, 20, 30, 40)
tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3]
print(sum(tt1))
print("튜플 합 : %d" % tt2)

print("tt1[1:3] :", tt1[1:3])
print("tt1[1:] :", tt1[1:])
print("tt1[:3] :", tt1[:3])
'''

'''
a =1,2,3
b =4,5,6
c = a+b

print("a :",a)
print("b :",b)
print("c :",c)
'''


#★★★★★

'''
pack = 1,2,"패킹"
print("packing\npack :",pack)

a,b,c = pack #unpacking 할때는 구성요소의 개수를 확인해야함(len()사용)
print("unpacking\na:",a,"b:",b,"c:",c)
#unpacking한 후 tuple 수정후 packing or list로 변환 후에 수정한 다음 다시tuple로 강제 형변환
'''

'''
tp = 100,200,"함수",100,"개수"

print("tp안의 200의 위치 :", tp.index(200),"번째 인덱스")
print("tp안의 100의 개수 :", tp.count(100),"개")

#튜플은 초기화도 불가능
'''

'''
tp = "회사정보", "제품명","가격정보","출시일"

ls = ["삼성전자","갤럭시","100원","미정"]

print("(튜플)\t   (리스트)")
for i in range (0,4,1):
    print("%s\t: %s"%(tp[i],ls[i]))
    print("%5s\t: %s"%(tp[i],ls[i]))

for i  in range(len(ls)):
    print("{}\t:{:<5}".format(tp[i].ls[i]))
for i  in range(len(ls)):
    print("{}\t:{0:<5}".format(tp[i].ls[i]))
for i  in range(len(ls)):
    print("{}\t:{:=^10}".format(tp[i].ls[i]))
'''
#//튜플


#딕셔너리 : 리스트와 비슷, 리스트 처럼 첨자를 이용해서 요소에 접근
#첨자는 키(key)
#탐색 속도가 빠르고 사용하기도 편리
#키값은 중복을 허용하지 않음 ,중복되면 마지막 값만 남음 value는 중복 가능
#컴퓨터가 빨리 처리할수 있는 순서대로 출력됐었음

'''
student = {'학번':1234, '이름':'홍길동', '학과':'it학과'}
print(student)

mobile = {"품명":"갤럭시","가격":100,"크기":10}
print(mobile)
'''

'''
impo = {}
impo['파이썬'] = 'www.python.org'
impo['네이버'] = 'www.naver.com'
impo['구글'] = 'www.google.com'

print("파이썬 : ",impo['파이썬'])
print("네이버 : ",impo['네이버'])
print("구글 : ",impo['구글'])
print(impo) #키값
'''

'''
impo = {}#빈딕셔너리 생성

name = input('키값 입력 :')
val = input('값 입력 :')
impo[name] = val

print(name,": ",impo[name])
print(impo)

'''

'''
dic = {}

for i in range(0,5,1):
    key = input("이름(key) 입력 : ")
    value = input("값(value) 입력 : ")
    dic[key] = value

print(dic)
'''

'''
num = {1:"일", 2:"이", 3:"삼", 4:"사"}

print('keys() 키:' , num.keys())
print()
print('values() 값:' , num.values())
'''
'''
num = {1:"일", 2:"이", 3:"삼", 4:"사"}

print("num.keys() : ",num.keys())
print("list(num) : ",list(num))
print('list(num.keys()) : ', list(num.keys()))
print()
print("num.values() : ",num.values())
print("list(num.values()) :",list(num.values()))
'''

menu = {}; bl = True; num = 0
while bl:
    print("1.메뉴 등록"); print("메뉴별 가격 보기"); print("3. 가격 수정"); print("4.종료")
    num = int(input(">>>"))
    if num == 1:
        name == input("메뉴 입력 : "); menu[name] = input("가격 입력 :")
    elif num == 2:
        for i in menu.keys():
            print(i,":",menu[i])
    elif num == 3:
        name == input("수정할 목록 입력 : "); menu[name] = input("수정 가격 :")
    elif num == 3:
        name == print("종료"
        bl = False










