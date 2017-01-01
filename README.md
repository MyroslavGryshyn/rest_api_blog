# Simple blog made with DjangoRestFramework

Run server
- git clone https://github.com/MyroslavGryshyn/rest_api_blog.git
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver 8088

All the documentation you can find then on http://127.0.0.1:8088/docs/

# Usage
- Create user via 'curl -X POST http://127.0.0.1:8088/auth/register/ --data "email=djose2345r@gmail.com&password=new"'
- Login via 'curl -X POST http://127.0.0.1:8088/auth/login/ --data "email=djose2345r@gmail.com&password=new"'

With token you will get from login you can create/get posts. For example: 'curl -X POST http://127.0.0.1:8088/blog/posts/ --data "title='Djosser post'&body='My body'" -H 'Authorization: Token 123456...'


# Tests
- python manage.py test

# Additional information:

/blog/posts/

You can use search parameter:
http://127.0.0.1:8088/blog/posts/?search=body

/blog/posts/all/

You can use search parameter:
http://127.0.0.1:8088/blog/posts/all/?search=body

You can use pagination:
You can use search parameter:
http://127.0.0.1:8088/blog/posts/?page=1
