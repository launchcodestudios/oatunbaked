# oatunbaked

SSG using python and jinja

## Setup

CD to repo root

```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## Developing

```
python app.py
```

Files are pre-rendered and saved as flat HTML files when you view the URL, served from `/build/` directory. 

**NOTE** Currently when dev'ing you have to view the page URL in your browser to generate it. This means you can't just make a quick fix and commit. You have to view it (page URL) locally to generate it.

Locally they are served as flat files from /build/ via flask with auto-reloader setup.

## Deploying

Serve files as flat HTML site via AWS amplify or nginx container using `/build/` as web root. 