FROM python:3.13.1-slim

# sets the working directory
WORKDIR /app

# copies the required files to the destination directory
COPY . .

# install the dependencies
# installs the fastapi dep on its own to be able to run it as a command
RUN pip install "fastapi[standard]"
RUN pip install --no-cache-dir -r requirements.txt

# exposes the port (fast api defaults to 8000)

EXPOSE 8000

CMD ["fastapi", "run", "src/main.py"]