FROM ubuntu:22.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install python3-pip bluez -y

# 필요한 Python 라이브러리 설치
RUN pip3 install requests

# 앱 코드를 컨테이너 내 /app 디렉토리로 복사
COPY . /app

# 작업 디렉토리 설정
WORKDIR /app

# 앱 실행
CMD ["sh", "run.sh"]