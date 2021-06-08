<p align="center">
  <a href="" rel="noopener">
    <img width=200px height=200px src="https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png" alt="Epic-Events">
  </a>
</p>

<h3 align="center">Create a secured RESTful API using Django REST</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/Emericdefay/OCR_P12.svg)](https://github.com/Emericdefay/OCR_P12/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Emericdefay/OCR_P12.svg)](https://github.com/Emericdefay/OCR_P12/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> RESTful API for Epic Events
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [About <a name="about"></a>](#about-)
- [🏁 Getting Started <a name="getting_started"></a>](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
  - [Linter](#linter)
- [Tests <a name = "tests"></a>](#tests-)
- [🎈 Usage <a name = "usage"></a>](#-usage-)
- [⛏️ Built Using <a name = "built_using"></a>](#️-built-using-)
- [Recommandations <a name = "recommandations"></a>](#recommandations-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)

---

## About <a name="about"></a>

<p>
This project provide a RESTful API localy.<br>
Allow developper to create the front-end.
</p>

## 🏁 Getting Started <a name="getting_started"></a>

Those instructions will bring you the API at the url : `http://127.0.0.1:8000/`.<br>

### Prerequisites

<p>Before started to setup the RESTful API, you need to get : </p>
<ul>
  <li>Python <strong>>= 3.6</strong></li>
  <li>Postman</li>
  <li>Git</li>
  <li>PostgreSQL</li>
</ul>
<p>It will provide you tools to extract, run and detail the API.</p>

### Installing

- Create a folder
- Clone the project `git clone` inside the folder
- Go to the folder OCR_P12 `cd OCR_P12`
- Create environment named env `python -m venv env`
- Start the environment `env\Scripts\activate.bat`
- Install requirements `pip install -r requirements.txt`
- Run server `python CRM/manage.py runserver`

### Linter

If you want to check the PEP8 from the code :

- From OCR_P12 go to CRM `cd CRM`
- run `flake8`

## Tests <a name = "tests"></a>

For potential future updates, tests have been made.<br>
To launch tests :
- Go to CRM/CRM_epic_event/settings.py
- Switch from postgreSQL DATABASE to sqlite3
- Instead of running server `python CRM/manage.py test`

Don't forget to Switch back to postgreSQL when finish testing.


## 🎈 Usage <a name = "usage"></a>

<p>Once you ran the server, you can check those endpoints and get documentation on them from the <a href="https://documenter.getpostman.com/view/15717033/TzXwFyk3">Postman API Collection</a>.</p>

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming language
- [Django](https://www.djangoproject.com/) - Website Framework
- [Django REST Framework](https://www.django-rest-framework.org/) - REST Framework for Django (DRF)
- [Django REST Framework simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) - JWT Authentification backend for DRF
- [PostgreSQL](https://www.postgresql.org/) - Database

## Recommandations <a name = "recommandations"></a>

- [Postman](https://www.postman.com/) - API Development

## ✍️ Authors <a name = "authors"></a>

- [@Emericdefay](https://github.com/Emericdefay) - Work
- [@OpenClassRoom](https://openclassrooms.com/) - Project
