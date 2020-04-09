# Django Project Management
***Django Project Management*** system let businesses manage the project 
initialization, planning, executing and tracking the progress of a project 
the team is working on. It make easier to oversight the project and 
identify bottleneck along the way.

# Requirements
* [Debian 10.0](https://www.debian.org/releases/buster/)
* [Python 3.7](https://www.python.org/downloads/)
* [Django Framework 3.0](https://pypi.org/project/Django/#files/)
* [Apache HTTP Server 2.4](https://httpd.apache.org/download.cgi)
* [Django Rest Framework 3.11](https://www.django-rest-framework.org/)
* [PostgreSQL 12.1](https://www.postgresql.org/download/)

# Starting up the Server with Django runserver
**Running the app**
```
cd project_management
python3 manage.py runserver 0.0.0.0:80
```

**Creating super user**
```
python3 manage.py createsuperuser
```

# Starting up the Server with Docker Settings
**Running the app**
```
docker-compose up
```

**Getting the docker container ID**
```
docker ps

# Example:
CONTAINER ID        IMAGE                            
280daaa3a347        django_project_management_core   
```

**Creating super user**
```
docker exec -ti <container_id> python3 manage.py createsuperuser --settings=project_management.settings_docker

# Example: Use the container ID
docker exec -ti 280daaa3a347 python3 manage.py createsuperuser --settings=project_management.settings_docker
```

# Running the test
**Default Settings**
```
cd project_management
python3 manage.py test
```

**Docker Settings**
```
docker exec -ti <container_id> python3 manage.py test --settings=project_management.settings_docker
```

# Web App Navigation
* [Admin Site](http://localhost/admin)
* [Web API Agile API](http://localhost/api/agile/)

**Agile Value List API endpoint**
```
curl http://localhost/api/agile/values/
```

**Create Agile Value API endpoint**
* name - required
* description - optional
```
{
    "name": "Value Name",
}
```
```
curl -X POST -H 'Content-Type: application/json' -d '{"name": "Value Name"}' http://localhost/api/agile/values/
```

**Agile Principle List API endpont**
```
curl http://localhost/api/agile/principles/
```

**Create Agile Principle API endpoint**
* name - required
* description - optional
* order - optional
```
{
    "name": "New Principle Name",
}
```
```
curl -X POST -H 'Content-Type: application/json' -d '{"name": "New Principle Name"}' http://localhost/api/agile/principles/
```
