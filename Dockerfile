FROM python:3.11.7-alpine
LABEL authors="dmytro.kulyk@cognitran.com"
RUN pip install --no-cache-dir boto3
COPY main.py /main.py
ENTRYPOINT ["python","/main.py"]