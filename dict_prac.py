# dict() = {key: value}

# 3명의 학생, (국어, 수학)
# 국어는 오름차순, 수학은 내림차순으로 정렬

score_list = dict() # 딕셔너리 선언

korea_list = list() # 점수 리스트 선언
math_list = list()

for i in range(0, 3):
    korea = input("국어 성적을 입력하세요: ")
    math = input("수학 성적을 입력하세요: ")
    korea_list.append(korea) # 점수를 받아서 각각 리스트에 append
    math_list.append(math)

korea_list.sort() # 오름차순 정렬
math_list.sort(reverse=True) # 내림차순 정렬

score_list['국어'] = korea_list  # 딕셔너리 key에 값 추가
score_list['수학'] = math_list

print(score_list['국어'])
print(score_list.get('수학'))



# 한 명인데 국어랑 수학
# korea_s = input("국어점수: ")
# math_s = input("수학점수: ")
#
# score = dict()
#
# score['국어'] = korea_s
# score['수학'] = math_s
#
# print(score)
