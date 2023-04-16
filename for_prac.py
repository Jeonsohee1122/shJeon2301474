# for 문 사용법/ (int i=0; i<10; i++)
for i in range(0, 10):
    print(i)

list_t = ['1', '2', '3']
for value in list_t:
    print(value)

# list() 선언
name_list = list()

# for 문을 사용하여 입력받기/ input()
for i in range(0, 3):
    name = input("이름을 입력하세요: ")
# list에 입력받은 name 값 추가(append)
    name_list.append(name)

# 오름차순: sort(), 내림차순: sort(reverse=True)
name_list.sort(reverse=True)
print(name_list)




