#### Repl.it - remote db in local virtual environment

---

Setup virtual environment on local machine

```bash
# install venv
python3 -m venv venv

# activate venv
source venv/bin/activate

# install Flask
pip3 install Flask
```

Install Repl.it

https://replit-py.readthedocs.io/en/latest/

```bash
# install replit
pip3 install replit
```

Remote db

```bash
# get the db url from remote replit shell
echo $REPLIT_DB_URL
```

Local machine...

```bash
#set the environment variable in bash venv on local machine
export REPLIT_DB_URL="<REPLIT_DB_URL>"
```
