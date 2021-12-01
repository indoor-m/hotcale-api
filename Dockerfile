FROM python:3.8

WORKDIR /usr/src/api
ADD requirements.txt ./
# requirements install
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# listen 8000 port...
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
