# hometap-equity

hometap take home app

Working locally

In order to load the third party data you should create a .rnv file in the root of the folder, following the structure of the .env.local file and adding there the URLs and the API_KEYS.

Then create a virtual environment in your project directory like this:

```bash
python3 -m venv .venv
```

Now activate your virtual environment by running:

```bash
source .venv/bin/activate
```

Deactivate the virtual environment running:

```bash
deactivate
```

Installing dependencies:

```bash
.venv/bin/pip install "fastapi[standard]"
.venv/bin/pip install -r requirements.txt
```

Running the application:

Production mode:

```bash
fastapi run src/main.py
```

Development mode:

```bash
fastapi dev src/main.py
```

Running docker

```bash
docker build -t hometap-equity-api .
```

```bash
docker run -d -p 8000:8000 hometap-equity-api
```
