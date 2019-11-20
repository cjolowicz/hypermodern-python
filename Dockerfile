FROM python:3.8.0-alpine3.10 as base
FROM base as builder

WORKDIR /app
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VERSION=1.0.0b9
RUN wget -qO- https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN /root/.poetry/bin/poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./
RUN /root/.poetry/bin/poetry build && /venv/bin/pip install dist/*.whl

FROM base as final

COPY --from=builder /venv /venv
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/venv/bin/hypermodern-python"]
