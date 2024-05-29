'''
* 리스트의 내부 요소 다루기
- 리스트는 시퀀스 자료형이기 때문에 인덱스를 통한 요소들의 관리가 가능합니다.
- 리스트를 다룰 때는 문자열과 비슷한 방식을 사용합니다.
'''
foods = ['짜장면', '탕수육', '삼겹살', '족발', '피자']

print(foods[2])
print(foods[1][2])
print(foods[0][:2])


# 리스트 슬라이싱 -> 리스트 데이터[begin:end:step]
nums = [0,1,2,3,4,5,6,7,8,9]

print(nums[2:5:1])
print(nums[:4])
print(nums[1:7:2])
print(nums[::5])


# 리스트는 인덱싱을 사용하여 변수처럼 내부의 값을 변경하는 것이 자유롭습니다.
print('-' * 40)
print(nums)

nums[2] = 34
print(nums)

nums[7] = 88
print(nums)

nums[3] = nums[6]
print(nums)


'''
- 문자열은 상수 형태로 저장되는 고정형 리스트입니다.
- 따라서 인덱싱이나, 슬라이싱을 통해 값의 복사본을 활용하는 것은 가능하지만, 
  영역에 직접 접근해서 내부의 값을 편집할 수는 없습니다.
- 문자열은 변경이 불가능한 자료형입니다. (immutable)
'''
s = 'python'
# s[2] = 'x' (x)


# unpackaging: 리스트 내부의 요소를 각각의 변수에 저장
'''
f1 = foods[0]
f2 = foods[1]
f3 = foods[2]
f4 = foods[3]
f5 = foods[4]
'''
# 좌항의 변수의 개수와 우항의 리스트의 요소의 개수가 일치한다면
# 자동으로 변수에 리스트 내부 요소의 값들이 차례대로 할당됩니다.
# javascript의 디스트럭쳐링(구조 분해 할당)과 유사
f1, f2, f3, f4, f5 = foods
print(f1, f2, f3, f4, f5)


# 빈 리스트 만들기
list1 = []

list2 = list()
print(list2)
