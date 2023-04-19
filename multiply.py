

#for문을 활용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

#컴프리헨션을 활용한 구구단
gugudan = [f"{i} x {j} = {i*j}" for i in range(2, 10) for j in range(1, 10)]

print(gugudan)


#사용자로부터 정수값을 입력받아 그 값의 구구단을 출력
num = int(input("정수를 입력하세요"))
for i in range(1,10):
    print(f"{num} * {i} = {num*i}")

#구구단의 짝수 단만 출력하는 예제
for dan in range(2, 10, 2):    # 2부터 9까지 짝수 단만 반복(iterate)
    print(f"{dan} 단")
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} x {i} = {result}")
    print()

#구구단의 홀수 단만 출력하는 예제
for dan in range(1, 10, 2):    # 1부터 9까지 홀수 단만 반복(iterate)
    print(f"{dan} 단")
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} x {i} = {result}")
    print()
