# Mac VScode 에서 파이썬 개발 환경 설정

## 1. python 설치

python 웹사이트 : https://www.python.org/

## 2. VScode python Extension 설치

## 3. 파이썬 작업 폴더 생성

파이썬 프로젝트를 작업할 폴더를 생성한다.

## 4. 파이썬 가상환경 환경 설정

- 프로젝트 간의 독립성을 위해 프로젝트 파일 마다 가상환경을 설정 해 주는 것이 좋음

### 4-1 파이썬 가상환경 이란

- 독립적인 파이썬 실행 환경, 가상환경마다 다르게 파이썬 개발환경을 설정해 줄 수 있음
  - 장점 : 프로젝트가 여러개 일때 프로젝트간의 패키지 호환 문제를 줄일 수 있음

### 4-2 가상환경 설치

1. 터미널을 통해 프로젝트 파일로 이동한 후 아래 명령어 작성

```
python3 -m venv folder_name

//foler_name 에 원하는 이름
```

2. 터미널로 생성한 폴더로 이동

```
cd folder_name
```

3. bin 폴더로 이동한 후 아래 명령어를 통해 가상환경 실행

```
source ./activate
```

4. 필요한 패키지를 pip install 을 통해 설치해준다.

### 5. VScode interpreter 설정

VScode 들어가 `cmd` + `shift` + `p`로 인터프리터를 방금 생성한 가상 환경으로 설정해준다.
