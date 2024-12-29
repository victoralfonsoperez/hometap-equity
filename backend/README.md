# hometap-equity
hometap take home app

Working locally

In order to load the third party data you should create a .rnv file in the root of the folder, following the structure of the .env.local file and adding there the URLs and the API_KEYS.

Then create a virtual environment in your project directory like this:
```
python3 -m venv .venv
```
Now activate your virtual environment by running:
```
source .venv/bin/activate
```


Installing dependencies:
```
.venv/bin/pip install "fastapi[standard]"
.venv/bin/pip install -r requirements.txt
```

Running the application:

```
fastapi run src/main.py
```

