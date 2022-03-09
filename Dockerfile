FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src .

CMD [ "python" ,"main.py" ]