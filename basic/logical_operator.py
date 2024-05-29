'''
* 논리 연산자 (&, |, and, or, not)
# &, and 연산자는 좌항과 우항의 논리값이 모두 True일 경우에만
전체 결과를 True로 도출합니다.
'''
a = 6

if a > 1 and a < 10:
    print('a는 1보다 크고 10보다는 작습니다.')
else:
    print('a는 1~10 사이의 숫자가 아닌 것 같아요.')

# 파이썬은 위의 식을 연결해서도 작성할 수 있습니다.
if 1 < a < 10:
    print('ok!')


'''
|, or 연산자는 좌항과 우항의 논리값이 한 쪽만 True여도
전체 결과를 True로 도출.

* 단축 평가 연산 (short circuit operate: and, or)
- 좌항에서 전체 결과가 판명났을 경우
우항 연산을 진행하지 않는 연산자 입니다.
'''
c = 0

if c == 0 or 10 / c == 5:
    print('통과')


# not 연산자는 논리값을 반전시킵니다. (!)
d = False
if not d:
    print('반전됨!')

'''
- C언어에서는 정수 0을 False로 해석하고, 0이 아닌
모든 정수를 True로 해석합니다. (논리형 타입이 없어서)
파이썬에서도 C의 논리해석을 그대로 적용시킬 수 있습니다.
'''
apple = 3
if not apple:
    print('사과가 하나도 없습니다.')
else:
    print('사과가', apple, '개 있습니다.')