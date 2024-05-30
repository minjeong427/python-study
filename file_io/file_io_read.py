'''
* 파일 읽기 기능 (read)
- 파일로부터 데이터를 읽어들일 때는 분량에 따라 적당한 메서드를 선택해서 사용합니다.
1. read(): 파일 전체를 통째로 읽어서 리턴.
2. readline(): 파일 데이터를 한 줄씩 읽어서 리턴.
3. readlines(): 파일 전체를 읽어서 한 줄씩 분리한 후에 리스트에 담아서 리턴.
'''
file_path =  r'C:\MyWorkspace\python-study\test.txt'

'''
try:
    f = open(file_path, 'r')
    text = f.read()
    print(text)
except:
    print('파일 로드 실패!')
finally:
    f.close()
'''

# readline() 메서드는 자동으로 \n을 기준으로 하여
# 데이터를 줄 단위로 읽어들이기 때문에 메모리 부담을 줄일 수 있습니다.

'''
try:
    f = open(file_path, 'r')
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)
except:
    print('파일 로드 실패!')
finally:
    f.close()
'''

# readlines()는 파일 데이터를 한 줄씩 읽어서
# 리스트에 담아서 리턴하기 때문에 읽은 데이터를
# 리스트 문법을 사용하여 처리할 수 있습니다.
try:
    f = open(file_path, 'r')
    text = f.readlines()
    print(text)
    print(type(text))
    text.reverse()
    for t in text:
        print(t)
except:
    print('파일 로드 실패!')
finally:
    f.close()

