FROM python:3.8
ENV PYTHONUNBUFFERED 1
ADD /tancho /tancho/
ADD requirements.txt /tancho/
WORKDIR /tancho
RUN pip install -r requirements.txt