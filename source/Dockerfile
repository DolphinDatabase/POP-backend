FROM python:3.11-bullseye

COPY ./requirements.txt /pop-backend/requirements.txt

WORKDIR /pop-backend

RUN pip install -r ./requirements.txt

COPY . /pop-backend/

CMD ["python", "main.py"]

EXPOSE 5050