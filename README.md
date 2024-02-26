# Simple HTMX WebApp Experiment

## Quickstart


```sh
python3 -m venv .venv
./.venv/bin/python3 -m pip install -U pip pip-tools
mkdir -p requirements src/myproject
touch src/myproject/__init__.py
```

```sh
./.venv/bin/python3 -m pip install --upgrade pip-tools
./.venv/bin/python3 -m piptools compile --generate-hashes requirements/app.in --output-file requirements/app.txt
./.venv/bin/python3 -m pip install --require-hashes --no-deps --only-binary :all: -r requirements/app.txt
```
