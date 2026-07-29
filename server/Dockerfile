FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Install dependencies first — this layer caches until pyproject.toml/uv.lock change.
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY src ./src
COPY alembic ./alembic

EXPOSE 8000

CMD ["/app/.venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
