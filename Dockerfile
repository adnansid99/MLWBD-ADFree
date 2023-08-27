FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN sudo apt update && \
    sudo apt install software-properties-common -y && \
    sudo add-apt-repository ppa:deadsnakes/ppa -y && \
    sudo apt update && sudo apt install python3.11 -y

COPY . .

RUN pip install --force-reinstall -r requirements.txt

CMD ["python", "main.py"]