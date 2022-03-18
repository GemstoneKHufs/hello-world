# 두번 풀퀘스트 전송
# 정수 뒤집기 문제
'''-------------------------------------------------------------------------'''
# 입력문
num = int(input())

# 뒤에 있는 0 없애기
while num % 10 == 0:
    num = num // 10
# 문자열 리스트로 저장 후 reverse 함수 써서 뒤집은 뒤 리스트를 다시 정수로 바꿈
arr = [i for i in str(num)]
arr.reverse()
print(int("".join(list(arr))))
"""
# 뒤의 자리부터 리스트에 추가
sum = 0

while num > 0:
    a = num % 10  # a는 10으로 나눈 나머지
    arr.append(a)  # 리스트에 추가
    num = num // 10  # 낮은 자리숫자 제거

# 리스트에 있는 수를 정수로 바꿔줌
bestr = list(map(str, arr))  # 정수리스트를 문자열 리스트로
digit = ''.join(bestr)  # 문자열 함수 join을 써서 리스트 밖으로
print(int(digit))  # 문자열을 정수로
# 배열의 있는 수를 십진법 정수로 계산해서 바꿈
'''sum = 0
for i in range(len(arr)):
    sum += arr[i] * 10**(len(arr)-i-1)

print(sum)
'''
"""
