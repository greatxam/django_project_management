# Created by Maximillian M. Estrada on 09-April-2020
# Dockerfile to build Django Project Management

# Use an official Python 3 runtime as our base image
FROM debian:buster

MAINTAINER Maximillian M. Estrada "maximillian_estrada@yahoo.com"

RUN apt-get update && \
	apt-get upgrade -y;

RUN apt-get install -y \
    build-essential \
    python3.7 \
    python3-pip \
    apache2 \
    libapache2-mod-wsgi-py3

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install any needed packages specified in our `requirements.txt`
RUN pip3 install -r requirements.txt

# Set the working directory to `/var/www/project_management`
WORKDIR /var/www/project_management

# Copy the application directory contents into the container at `/var/www/project_management`
COPY ./project_management /var/www/project_management

# Override Apache HTTPD default website configuration
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf

# Set the Hostname
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Apache HTTPD file permissions
RUN chown -R www-data:www-data /var/www
RUN chmod -R 755 /var/www

# Docker entrypoint script
COPY ./docker-entrypoint.sh /
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
