FROM python:3.9-slim

WORKDIR /app

RUN pip install fastapi
RUN pip install uvicorn[standard]

COPY . .

EXPOSE 8000

CMD ["uvicorn", "Main:app", "--host", "0.0.0.0", "--port", "8000"]