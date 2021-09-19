FROM python:3.8-slim
COPY app/src /src/
WORKDIR /src
RUN apt-get update && apt-get install -y curl
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["main.py"]