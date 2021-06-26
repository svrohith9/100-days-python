# Steps to deploy py apps in Heroku

1. `pip install gunicorn`

2. At the top level of the project generate requirements.txt for fetching dependencies.

   `pip freeze > requirements.txt`

3. create a **Procfile** file with config to run the py app.

   `web: gunicorn server:app`

[svrohith9-portfolio-card](https://github.com/svrohith9/svrohith9.github.io/tree/py-portfolio) deployed using _heroku_.
