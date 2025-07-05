FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# 暴露端口
EXPOSE 8001

# 启动命令
CMD ["uv", "run", "uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8001"]
