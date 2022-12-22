FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install python-multipart
RUN pip install -r requirements.txt
CMD ["python", "ml_api.py"]