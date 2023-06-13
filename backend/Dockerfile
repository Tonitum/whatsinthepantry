FROM python:3.10.12

ENV PYTHONPATH=/run/

COPY database.py /run/backend/
COPY recipe.py /run/backend/
COPY server.py /run/backend/

RUN python3 -m pip install flask
RUN mkdir /run/backend/db
WORKDIR /run/backend

EXPOSE 5000
CMD ["python3", "/run/backend/server.py"]
