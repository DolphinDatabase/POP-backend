FROM python:3.11-bullseye

COPY ./source /pop-backend
COPY requirements.txt /pop-backend/requirements.txt

WORKDIR /pop-backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5050

CMD ["python", "main.py"]
