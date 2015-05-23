Python Web-App with Docker
==========================

Flask web-app served by nginx+Gunicorn with a Postgresql database,
all running in Docker containers using docker-compose.

Fedora 21 Docker Setup
----------------------

```shell
sudo yum install docker
sudo pip install docker-compose

sudo systemctl enable docker
sudo systemctl start docker

sudo groupadd docker
sudo chown root:docker /var/run/docker.sock
sudo usermod -a -G docker $USERNAME
```

Running
-------

```shell
# Build docker images:
make build

# Create database and set up test-data
# by running psql in another container:
make dbsetup

# Run nginx container + python app container + postgresql
make run

# Test it out:
curl http://localhost:8080
```
