https://tomas123.herokuapp.com/dogapp/


**How to deploy the apliccation on Heroku** 

- Init a git repository:
 ```$ git init```

- Add all the files and commit them:
```
$ git add .

$ git commit -m "Message"
```

- Login with heroku:

```$ heroku login```

- Create an aplication:

```$ heroku create```

- Deploy the code:

```$ git push heroku master```

- Scale the web:

```$ heroku ps:scale web=1```

- On settings.py you have to add your host on ALLOWED_HOSTS, example:
Settings.py:

```ALLOWED_HOSTS = ['tomas123.herokuapp.com']```
