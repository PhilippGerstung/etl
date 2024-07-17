FROM python:3.12-slim
ARG workdir=/app
WORKDIR ${workdir}

RUN pip install poetry
COPY . .
RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
