# input() 기본
# name = input("이름이 뭐예요?")
# print("반가워요,", name)
# print(type(name))

# 형변환
# age = int(input("나이: "))
# print(age + 1)

# print(int("5") + int("3"))

# 문장 조합
# name = "김재현"
# age = 27
# print(f"안녕하세요, {name}님! {age}살 이군요!")
# print(f"내년엔 {age + 1}살이네요")

# 연습 문제
# city = input("사는 곳: ")
# food = input("좋아하는 음식: ")
# print(f"{city}에 사는 사람이 {food}를 좋아한다.")

# 미니 실습 (오늘의 보스)
# **목표:** 이름, 나이, 키를 입력받아 출력하는 프로그램 완성

name = input("name: ")
age = int(input("age: "))
height = float(input("height: "))

print("===== 내 정보 카드 =====")
print(f"이름 : {name}")
print(f"나이 : {age}살 (내년엔 {age + 1}살)")
print(f"키   : {height}cm")
print("========================")