"""
**읽기 과제**
1. 각 `if` 분기가 어떤 경우를 처리하는지 주석으로 달기
2. `1, 2, 10` 이 왜 삼각형이 안 되는지 수식으로 확인
"""
def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a: # 어느 두 변의 길이의 합이 나머지 한 변의 길이보다 작거나 같을 때
        return "삼각형 아님"
    elif a == b == c: # 세 변의 길이가 모두 같을 때
        return "정삼각형"
    elif a == b or b == c or a == c: # 어느 두 변의 길이가 같을 때
        return "이등변삼각형"
    else:  
        return "일반삼각형"

print(classify_triangle(3, 3, 3))
print(classify_triangle(3, 4, 5))
print(classify_triangle(1, 2, 10))