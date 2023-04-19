# for문과 그 안에 if문 사용. n개의 정수 입력받고 list요소로 집어넣은 후 index를 사용해 홀수&짝수번 정수의 합
# 10개의 정수값을 받아들인다
numbers = []
for i in range(10):
    num = int(input("정수를 입력하세요: "))
    numbers.append(num)

# 홀수번 정수의 합을 구한다
total = 0
for i in range(len(numbers)):
    if i % 2 == 1:  # 홀수번째 요소인 경우
        total += numbers[i]

print("홀수번 정수의 합:", total)
