FROM python:3.10-slim
COPY backend /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["flask", "run"]