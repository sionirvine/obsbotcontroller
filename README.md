OBSBOT controller with OSC

written in Python, to control OBSBOT app using OBSBOT center app. the app communicates through the app with OSC. make sure to enable OSC feature first in the OBSBOT center app.

# running the app

1. make sure to install all the required dependencies:

```bash
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

2. to run the app, run:

```bash
python main.py
```

the app will run on 0.0.0.0, port 3000.

3. `waitress` is installed as a WSGI server. to run with WSGI server:

```bash
waitress-serve --host 0.0.0.0 --port 3000 main:app
```
