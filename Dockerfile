FROM python:3.12-slim

# # 2. Only install system tools the APP actually needs to run
# # (Removed git, vim, net-tools, etc.)
# RUN apt-get update && apt-get install -y \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # 3. Set the working directory
# WORKDIR /app

# # 4. Copy requirements first (better for caching)
# COPY requirements.txt .

# # 5. Install libraries (without the "root" warning issues)
# RUN pip install --no-cache-dir -r requirements.txt

# # 6. Copy ONLY the source code (don't copy .devcontainer or tests)
# COPY src/ ./src/

# # 7. Set the same path logic you used in dev
# ENV PYTHONPATH=/app/src

# # 8. The command that starts the app automatically
# CMD ["python", "-m", "src.project.main"]