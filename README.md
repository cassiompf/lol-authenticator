# lol-authenticator v1.0.0

### Content index
--- 

* [Project Setup](#project-setup)
* [Dependencies](#dependencies)

## Project Setup
------------------------

### Dependencies

 - Python v3.9.6
     - If you don't have Python installed on your machine, we recommend using [PyEnv](https://github.com/pyenv/pyenv) to install it.

**************************

**Download repository**

Access the location of your projects via terminal and download from the repository.
```bash
$ git clone git@github.com:cassiompf/lol-authenticator.git
```

**Installation of dependencies**

The `pipenv` tool will install all the libraries that were defined in the project's Pipfile.
```bash
$ pip install pipenv
$ pipenv install
```

**Configuration**

First you need to open the file from the `src/main.py` location.
You will find two lines like:

```
user_nickname = 'your-nickname'
user_password = 'your-password'
```

Replace 'your-nickname' with your nickname and 'your-password' with your account password to login correctly.

**NOTE:** Remember to run the code where the Riot Client is open.

**Start project**
```bash
$ pipenv run python ./src/main.py
```

---
**Demo**

![lol-authenticator-compressed](https://user-images.githubusercontent.com/20346767/145660282-faba26fe-6062-476c-9f2f-031e8ed9c83d.gif)
