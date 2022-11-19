FROM python:3.11
ENV FLASK_APP=app
COPY requirements.txt /opt
RUN pip install -r /opt/requirements.txt
COPY app /opt/app
WORKDIR /opt
CMD flask run --host 0.0.0.0 -p $PORT