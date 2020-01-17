# sweet-handy-api

[![Build Status](https://travis-ci.org/innsmthdwlr/sweet-handy-api.svg?branch=master)](https://travis-ci.org/innsmthdwlr/sweet-handy-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Diabetes self-management. Check out the project's [documentation](http://innsmthdwlr.github.io/sweet-handy-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```


# Continuous Deployment

Deployment automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Enable this by:

Creating the production sever:

```
heroku create sweethandy-prod --remote prod && \
    heroku addons:create newrelic:wayne --app sweethandy-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app sweethandy-prod && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="sweethandy-prod" \
        --app sweethandy-prod
```

Creating the qa sever:

```
heroku create sweethandy-qa --remote prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app sweethandy-qa && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="sweethandy-qa" \
        --app sweethandy-qa
```

Securely add your heroku credentials to travis so it can automatically deploy your changes.

```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -m "ci(travis): added heroku credentials" && \
git push origin master && \
git checkout -b qa && \
git push -u origin qa
```

Create Heroku container
```
heroku login
heroku container:login
heroku container:release --app sweethandy-qa web
```
