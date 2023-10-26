FROM python:3.11-alpine

# RUN pip install --no-cache-dir --upgrade pip

WORKDIR /pop-backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /pop-backend/

CMD ["python", "main.py"]

EXPOSE 5050