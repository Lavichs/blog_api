FROM python:3.12-slim

WORKDIR ./app

RUN apt update
RUN apt install bat -y
RUN apt install zsh -y

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD ["python", "app.py"]
