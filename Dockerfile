FROM python:3.10
COPY . /script
WORKDIR /script
RUN pip install -r requirements.txt
CMD ["python", "run.py"]