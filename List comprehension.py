# a= [1,2,3,4]
# result = []
#
# for num in a:
#     result.append(num*3)
#
# print(result)

# a= [1,2,3,4]
# result = [num*3 for num in a if num % 2==1] # %2 == 0은 짝수, %2 ==1은 홀수를 나타냄
# print(result)

# 컴프리헨션을 활용한 구구단
# gugudan= [f"{i}*{j}={i*j} \n" for i in range(2,10) for j in range(1,10)]
# print(gugudan)

# for문을 활용한 구구단
# for i in range(2,10):
#
#     for j in range(1,10):
#         print(f"{i}*{j}={i*j}")




#여러 명의 국어, 수학 성적을 입력받고 학생의 이름순으로 나열하기
# 빈 리스트 생성
score_list = []

# 학생 수와 각 학생의 이름, 국어, 수학 성적을 입력받아 리스트에 추가
num_students = int(input("학생 수: "))
for i in range(num_students):
    name = input(f"{i+1}번째 학생 이름: ")
    korean_score = int(input(f"{name}의 국어 성적: "))
    math_score = int(input(f"{name}의 수학 성적: "))
    score_list.append((name, korean_score, math_score))

# 학생 이름순으로 정렬
score_list.sort()

# 결과 출력
print("학생 성적 ")
for score in score_list:
    print(f"{score[0]}: 국어 {score[1]}, 수학 {score[2]}")




#컴프리헨션을 사용한 방법
# 학생 수와 각 학생의 이름, 국어, 수학 성적을 입력받아 리스트에 추가
score_list = [(input(f"{i+1}번째 학생 이름: "), int(input("국어 성적: ")), int(input("수학 성적: "))) for i in range(int(input("학생 수: ")))]

# 학생 이름순으로 정렬하고 결과 출력
for name, korean_score, math_score in sorted(score_list):
    print(f"{name}: 국어 {korean_score}, 수학 {math_score}")

