# Python 자료형

### Index

---

[1. 숫자형](#1-숫자형)  
[2. 문자열](#2-문자열)

---

## 1. 숫자형

- 숫자 형태로 이루진 자료형

| 항목   | 예                 |
| ------ | ------------------ |
| 정수   | 12, -5, 0          |
| 실수   | 12.5, -5.5, 3.4e10 |
| 8진수  | 0o34, 0o25         |
| 16진수 | 0x2A, 0x2FF        |

8진수 작성 : 0o로 시작  
16진수 작성 : 0x로 시작

### 연산

- 사칙 연산 : +, -, \*, /
- ** : x의 y제곱 ex) 2 ** 3 = 2의 3제곱 = 8
- % : 나머지 반환
- // : 몫 반환

## 2. 문자열

### 2-1 문자열 기본

- 문자 단어 등으로 구성된 문자들의 집합
- 따옴표 혹은 큰따옴표로 둘러 싸여 있음

아래는 모두 문자열이다.

```python
"python"

'python'

""python""

'''python'''
```

<br></br>

#### 문자열 안에 따옴표 혹은 큰 따옴표 포함 시키기

1. 포함하려는 따옴표 외에 다른 따옴표 쌍으로 문자열을 둘러싼다.
2. \뒤에 포함하려는 따옴표를 적는다.
   <br></brr>

ex)

```python
"Tom's book is here"    //작은 따옴표를 포함시키기 위해 큰 따옴표로 문자열을 감싸준다.

' "Life is too short, You need python" ' //큰 따옴표를 포함시키기 위해 작은 따옴표로 문자열을 감사준다.

"\"Life is too short, You need python\"" //백슬래쉬 뒤에 잇는 따옴표는 문자 그 자체를 의미한다.
```

<br></br>

#### 여러줄인 문자열 만들기

1. \n 사용하기
   <details>
   <summary>이스케이프 코드</summary>  <!-- to-do 이스케이프 코드 설명 작성 -->
   <br markdown = "1">
    
   | 코드 | 설명 |
   | ---- | ---- |
   |  \n    |      |
   |  \t | |

   </br>
   </details>

2. 연속된 따옴표 쌍으로 감싸기 ('''), (""")

ex)

```python
"Life is too short,\nYou need python"

'''Life is too short,
You need python'''
```

### 2-2 문자열 연산

- 더하기

```python
head = "My name is"
tail = " Dellyu"
full_hello = head + tail
print(full_hello)

#결과
'''
My name is Dellyu
'''

```

- 곱하기

```python
h = "hello"
prtin(h*2)
#결과
'''
hellohello
'''
```

- 길이 구하기

```python
a = 'hello'
len(a)

>> 5
```

### 2-3 문자열 인덱싱

- 문자열의 특정 번째 문자에 접근할 수 있게하는 문법

1. 기본 형태

```python
변수[자리수]
```

ex)

```python
a = "hello world"
a[0]
>> h

#숫자를 0번부터 세기 때문에 0번째(가장 앞에 있는 문자 0이 인덱싱
```

- **파이썬은 숫자를 0부터 셈**

### 2-4 문자열 슬라이싱

## 3. 리스트

## 4. 튜플

## 5. 딕셔너리

## 6. 집합

### 7. 불
