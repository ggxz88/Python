'''
i = 1
while True:
    print(i,"종속문장", end=" ") #멈출려면 ctrl + c
    i+=1
'''

'''
i = 1
flag = True #flag : switch용도(통상적)
while flag:
    print(i, "종속 문장", end = "")
    if i == 10:
        flag = False
    i+=1
'''
'''
i=0
while True:
    if i == 3:
        break
        print("3출력") #break로 인해 실행 x
    print(i, "출력")
    i+=1

print("다음문장")
'''

'''
i = 0
while i<5:
    i+=1
    if i == 3:
        continue
        print("3출력") #continue로 인해 실행x
    print(i,"출력")
print("다음 문장")
'''
'''
num,result,i = 0, 0, 1
while True:
    num = int(input("1~10사이의 숫자 입력: "))
    if num<1 or num>10:
        print("잘못 입력 다시")
        continue
    break
else:
    print("next...")
while i<=num:
    result+=i; i+=1
else:
    print("1~", num,"까지의 합 : ",result)
'''#bug있음
'''#1
num,result,i = 0, 0, 1
while True:
    num = int(input("1~10사이의 숫자 입력: "))
    if num<1 or num>10:
        print("잘못 입력 다시")
        continue
    break
print("next...")
while i<=num:
    result+=i; i+=1
else:
    print("1~", num,"까지의 합 : ",result)
'''
'''#2
num,result,i = 0, 0, 1
while True:
    num = int(input("1~10사이의 숫자 입력: "))
    if num<1 or num>10:
        print("잘못 입력 다시")
        continue
    print("next...")
    break
while i<=num:
    result+=i; i+=1
else:
    print("1~", num,"까지의 합 : ",result)

'''
'''#3
num,result,i = 0, 0, 1
flag = True
while flag:
    num = int(input("1~10사이의 숫자 입력: "))
    if num<1 or num>10:
        print("잘못 입력 다시")
        continue
    else: flag=False
else:
    print("next...")
while i<=num:
    result+=i; i+=1
else:
    print("1~", num,"까지의 합 : ",result)
'''

'''
for i in range(0, 3, 1):
    for k in range(0, 5, 1):
        if k == 3:
            break
        print("(i: %d\tk:%d)" % (i, k))
'''
#while로
'''
i, k = -1, -1

while i < 2:
    i+=1
    while k < 2:
        k+=1
        if k == 3:break
        
    print("(i: %d\tk:%d)" % (i, k))
'''#나
#v
'''
i = 0

while i<3:
    k=0
    while k<5:
        if k == 3:
            break
        print("(i: %d\tk:%d)" % (i, k))
        k+=1
    i+=1
'''

#쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다 쥐한마리가 하루 20g씩의 쌀을 먹고
#10일(10, 20, 30)마다 쥐의 수가 2배씩 증가한다. 며칠만에 창고의 쌀이 모두 쥐의 먹이가
#될까. 그리고 쥐는 총 몇마리 인가?(쌀 한 통 = 1kg)(쌀을 먹은 후 2배 증가하는 조건)
'''
rice = 100 * 1000 
rat = 2
meal = 20
day = 1

while rice > 0:
    day += 1
    rice -= rat*meal
    if day % 10 == 0:
        rat *= 2
    if rice == 0:
        break
    
print("창고의 쌀이 없어지지 까지의 걸린 시간: %d" % day)
print("쥐의 마리수: %d" % rat)
'''
'''
# 나 #v(다시)
charge = 0

while True:
    money = int(input("요금을 투입 하세요 : "))
    charge +=money
    if charge < 200:
            continue
    
    while True:
        print("================ 커피 자판기 ================")
        print("1. 커피(200) 2. 코코아(250) 3. 반환  4. 종료")
        choice = int(input("메뉴를 선택하세요:"))
    
        if choice == 1:
            if charge < 200:
                print("요금이 모자랍니다.")
                break
            print("커피를 선택하셨습니다.")
            charge -= 200
            continue
        elif choice == 2:
            if charge < 250:
                print("요금이 모자랍니다.")
                break
            print("코코아를 선택하셨습니다.")
            charge -=250
            continue
        elif choice == 3 :
            print("반환되는 요금 : %d" % charge)
            break
        elif choice == 4:
            print("반환되는 요금 : %d" % charge)
            print("자판기 종료")
            break
        else:
            print("메뉴를 다시 선택해주세요:")
 
    break  
'''    

#List : 다양한 자료형을 담을 수 있음 c의 배열은 같은 자료형만!
#양수(좌에서 우)(: 0부터 시작)와 음수(우에서 좌)(: -1부터 시작) 둘다 사용가능
'''
ls = [500, 200, 300, 400]; Sum = 0

print("ls : ", ls)
print("ls[0] :", ls[0])
print("ls[1] :", ls[1])
print("ls[2] :", ls[2])
print("ls[3] :", ls[3])

print("ls : ", ls)
print("ls[0] :", ls[-4])
print("ls[1] :", ls[-3])
print("ls[2] :", ls[-2])
print("ls[3] :", ls[-1])
'''
'''
ls = [500, 200, 300, 400]; Sum = 0
Sum = sum(ls) #계산이 가능한 속성만 가능
print(Sum)

print("ls : ", ls)
print("ls[0] :", ls[0])
print("ls[1] :", ls[1])
print("ls[2] :", ls[2])
print("ls[3] :", ls[3])
'''

'''
ls =[0, 0, 0, 0]; Sum = 0

ls[0] = int(input("첫 번째 숫자 입력 : "))
ls[1] = int(input("두 번째 숫자 입력 : "))
ls[2] = int(input("세 번째 숫자 입력 : "))
ls[3] = int(input("네 번째 숫자 입력 : "))

Sum = ls[0] + ls[1] + ls[2] + ls[3]

print("ls[0] :", ls[0])
print("ls[1] :", ls[1])
print("ls[2] :", ls[2])
print("ls[3] :", ls[3])

print("리스트의 합 : %d" %Sum)
'''

'''
ls = [0, 0, 0, 0]; Sum = 0

print("len(ls) : ",len(ls))
for i in range(len(ls)):
    ls[i] = int(input(str(i)+"째 숫자 입력 : ")) #강제형변환 :str(i)
    Sum += ls[i]

for i in range(len(ls)):
    print("ls[%d] :" % i, ls[i])
print("리스트의 합 :", Sum)

'''

'''
#slicing(:) : 원본은 안바뀜, 잘라서 가져와서 쓰는 것
ls = [10, 20, 30 ,40]

print("ls : ",ls)

print("\nls[1:3] => ls[1] ~ [2] :", ls[1:3])
print("ls[0:3] => ls[0] ~ [2] :",ls[0:3])
print("ls[2:] => ls[2] ~ [끝까지] :",ls[2:])
print("ls[2:] => ls[2] ~ [끝까지] :",ls[2:4])
print("ls[:2] => ls[0] ~ ls[1] :", ls[:2])
'''
'''
#★★★★★
#얕은 복사 : 주소값만 전달(동기화를 해야할 때만, 함부로 쓰면 안됨

ls = [10, 20, 30, 40]
arr = ls 
print("ls : {}, id : {}".format(ls,id(ls)))
print("arr : {}, id : {}".format(arr,id(arr)))
'''
'''
ls = [10, 20, 30, 40]
arr = ls

arr[2] = 20000

print("ls : {}, id : {}".format(ls,id(ls)))
print("arr : {}, id : {}".format(arr,id(arr)))
'''

'''
#★★★★★
#깊은 복사 : 새로운 개체를 만듦 

ls = [10, 20, 30, 40]
arr = ls[:] #처음부터 끝까지

arr[2] = 20000

print("ls : {}, id : {}".format(ls,id(ls)))
print("arr : {}, id : {}".format(arr,id(arr)))
'''
'''
import copy #import:가져오다 #copy파일을 전부다
ls = [10, 20, 30, 40]
#arr = ls[:]
arr = copy.deepcopy(ls)
arr[2] = 'deepcopy'

print("ls : {}, ls id : {}".format(ls,id(ls)))
print("arr : {}. arr id :{}".format(arr,id(arr)))
'''
'''
from copy import deepcopy
ls = [10, 20, 30, 40]
#arr = ls[:]
arr = deepcopy(ls)
arr[2] = 'deepcopy'

print("ls : {}, ls id : {}".format(ls,id(ls)))
print("arr : {}. arr id :{}".format(arr,id(arr)))
'''

'''
ls = [10, 20, 30]
arr = [40, 50, 60]

print("ls : ", ls)
print("arr : ", arr)

Str = ls + arr
print("ls + arr => Str:", Str)

string = ls * 3
print("ls * 3 => string:", string)
'''
'''
#반복문
ls = [10, 20, 30]
arr = [40, 50, 60]
sum_ = [0, 0, 0]

for i in range(len(ls)):
    sum_[i] = ls[i]+arr[i]
print(sum_)
print()
for j in range (len(ls)):
    ls[j]*=3
print(ls)
'''
#선택정렬
# v
#오름차순
ls = [4, 8, 2, 7, 6]

for i in range (len(ls)-1):
    for j in range (i+1, 5):
        if ls[i] > ls[j]:
            ls[i],ls[j] = ls[j],ls[i]
print(ls)

#내림차순
ls = [4, 8, 2, 7, 6]

for i in range (len(ls)-1):
    for j in range (i+1, 5):
        if ls[i] < ls[j]:
            ls[i],ls[j] = ls[j],ls[i]
print(ls)























