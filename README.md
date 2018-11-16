# docker-django-react

I am investigating some different setups with docker-compose to run a Django server & api with React.js frontend. Right now, I am following some different tutorials around the web on branches to learn as much as I can about the different options for settings this up.

A lot of people are making decoupled Django and React containers, running React as a Single Page Application using `create-react-app` and fetching data from the Django API RESTfully. My first impression is that isn't a great pattern if you need to build a robust frontend a lot of features, but would work great for a small site like a company or personal website.

Ideally I will eventually set up an Django REST API container (or maybe do a SOA with multiple containers), and a Django frontend container routing to Views that use React templates. Then each view can be a different React app.

The repo is a little messy right now, but at the end I will clean it up and share it around and maybe write a blog post.

----------

[docker-compose-django-react](https://github.com/18F/docker-compose-django-react) -- I looked into this one first. This one made me realize I did not want to do a decoupled set up with a SPA, but I took some inspiration for my docker-compose.yml file.

[Django/Rest w/ React](https://www.valentinog.com/blog/tutorial-api-django-rest-react/#Django_REST_with_React_setting_up_the_controll_ehm_the_views) -- Currently in progress on this one on the `react-template` branch. I think is close to what I'm wanting so far. More notes to come.

[React + Redux + Webpack 3 + Django](https://blog.cloudboost.io/react-redux-webpack-3-django-nov-2017-53a09d09cf75?gi=e2e794d38ae2) -- my friend recommended this one, going to look into it next.

----------

# Tips

Attach to running container in bash prompt:
```
docker-compose run <container> /bin/bash
```

To initialize a Django project & apps:
```
> (in container bash)
> django-admin startproject <project_name>
> cd project
> django-admin startapp <app_name>
```

NOTE: Make sure to add `<app_name>` to `INSTALLED_APPS` in `settings.py`.

Create and run database migrations:
```
> python manage.py makemigrations <app_name> (leads)
> python manage.py migrate
```

Load fixtures (database seeding):
```
> python manage.py loaddata leads
```

Check Django code coverage:
```
> coverage run --source='.' manage.py test
> coverage report
```
