FROM python:3-alpine

RUN python -m pip install --upgrade pip

RUN pip3 install flask jsonpatch kubernetes

COPY app.py /var/run/app.py
COPY app.py /var/run/quantity.py

WORKDIR /var/run

EXPOSE 8001/tcp

CMD ["python","app.py"]