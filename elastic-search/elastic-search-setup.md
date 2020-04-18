# ElasticSearch Installation 


#### Installation of docker on centos
- `sudo yum check-update`
- `sudo yum install -y yum-utils device-mapper-persistent-data lvm2`
- `sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`
- `sudo yum install docker`

#### Manage docker service:
- Start docker : `sudo systemctl start docker`
- Enable docker : `sudo systemctl enable docker`
- Check status : `sudo systemctl status docker0`

#### Install elastic search using docker
- Pull image: `docker pull docker.elastic.co/elasticsearch/elasticsearch:7.6.1`
- Start: `docker run -p 9200:9200 -p 9300:9300 -e    "discovery.type=single-node" -d docker.elastic.co/elasticsearch/elasticsearch:7.6.1`
