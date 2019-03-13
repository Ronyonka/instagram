# Instagram Clone
This is a clone of the web version of the popular social media app Instagram.

#### Date of Current Version (March 13th,2019)
#### By **Ron Onyonka**

## Description
This is my attempt to clone instagram and its features.


## Behaviour Driven Development
| Behaviour     | Input     | Output  |
| ------------- |:-------------:| -----:|
| User Signs Up| Enter Their Credentials| Redirected to the profile creation page|
| User log in | Username and password | Redirected to the homepage with other users images |
| Search for User| They enter a username in the search bar | They are directed to a page with profiles of the specific users displayed |
| Uploading images | They select add image| they select an image from their device that they would love to add |
| Liking a picture | They select a heart icon at the bottom of the image| one like is added to the image |

## Link to Live Website 
Here is a link to the live website: <https://ronstagram.herokuapp.com/>

### Technologies Used

- HTML
- CSS
- django-Bootstrap4
- Python3.6
- Heroku
- Django

## Setup/Installation Requirements


### Prerequisites
You need the following to work on the project: -
* Python version 3.6 
* Pip 
* venv 
* A text Editor(vscode preferably)
* git

### Clone the repo and check into the project folder

- `git clone https://github.com/Ronyonka/instagram`
- `cd instagram-clone`

### Create and activate the virtual environment

- `$ python3.6 -m venv virtual`
- `$ source virtual/bin/activate`


### Install the dependencies found in the  requirements.txt file

```bash
(virtual)$ pip install -r requirements.txt
```

### Create a .env file and in it input the following:

```bash
SECRET_KEY=''
DEBUG=True #Set To False in Production
DB_NAME='instagram'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to prod in production
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1
```
### Create a database

```bash
(virtual)$ psql
    user=# CREATE DATABASE instagram;
```

### Make migrations


- `(virtual)$ python3.6 manage.py makemigrations photos`
- `(virtual)$ pytohon3.6 manage.py migrate`


### Run `manage.py` in the terminal

```bash
(virtual)$ python3.6 manage.py runserver
```

## Known Bugs
None at the moment.

## License
MIT License

Copyright (c) 2019 Ron Onyonka

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.