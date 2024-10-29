import sys

number = int(sys.argv[1])  # 명령줄 인수로 입력된 숫자를 받아서 정수로 변환

for i in range(1, number + 1):  # 1부터 number까지 반복
    if number % i == 0:  # number를 i로 나눈 나머지가 0이면 i는 약수
        print(i, end=" ")  # 약수를 출력, 각 약수는 공백으로 구분
print()  # 줄바꿈

