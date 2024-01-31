FROM python:3.11.7-alpine
LABEL authors="dmytro.kulyk@cognitran.com"
RUN pip install --no-cache-dir boto3
COPY main.py /tmp/main.py
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]