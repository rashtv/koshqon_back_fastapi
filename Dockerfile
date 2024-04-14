FROM python:3.11-slim

WORKDIR /kq_back

RUN pip install --upgrade pip
COPY requirements.txt /kq_back
RUN pip install --no-cache-dir -r requirements.txt

COPY . /kq_back

EXPOSE $FASTAPI_PORT

CMD ["python3", "src/app/main.py"]
