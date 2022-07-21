# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /python
# Uvicorn env stuff here?
# ENV PYTHONPATH=???
# RUN apt install <needed?>
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./python .
CMD ["uvicorn", "myapp.app:app", "--host", "0.0.0.0", "--port", "5000"]