FROM python:3.11

WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . .


EXPOSE 8000


CMD ["fastapi", "run", "main.py", "--port", "8000"]