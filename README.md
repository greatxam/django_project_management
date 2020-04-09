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

# Starting up the Server
**Running the app**
```
$ docker-compose up
```

**Getting the docker container ID**
```
$ docker ps
```

Example:
```
CONTAINER ID        IMAGE                            
280daaa3a347        django_project_management_core   
```

**Creating super user**
```
$ docker exec -ti <container_id> python3 manage.py createsuperuser
```

Example: Use the container ID
```
$ docker exec -ti 280daaa3a347 python3 manage.py createsuperuser
```

# Web App Navigation
```
http://localhost:8080/
```
