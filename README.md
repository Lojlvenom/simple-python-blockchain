# Simple blockchain API
Simple blockchain example API with python

## Installation

Create a virtual env with python3

```bash
python3 -m venv env
```

Activate your env and install requirements

```bash
source env/bin/activate

(env) pip install -r requirements.txt
```

## Usage

Run uvicorn server 

```bash
uvicorn main:app --reload
```

Acces fastapi docs on [localhost](http://localhost:8000/docs)
