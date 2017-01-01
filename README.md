# Simple blog made with DjangoRestFramework

- Run server
1) git clone https://github.com/MyroslavGryshyn/rest_api_blog.git
2) pip install -r requirements.txt
3) python manage.py migrate
4) python manage.py runserver 8088

All the documentation you can find then on http://127.0.0.1:8088/docs/

- Tests
1) python manage.py test

Additional information:

/blog/posts/

You can use search parameter:
http://127.0.0.1:8088/blog/posts/?search=body

/blog/posts/all/

You can use search parameter:
http://127.0.0.1:8088/blog/posts/all/?search=body

You can use pagination:
You can use search parameter:
http://127.0.0.1:8088/blog/posts/?page=1
