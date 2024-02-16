### Clone repo
git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp

### Rename dev.env to save credentials from being pushed to repo
cp dev.env .env

### Build Container
docker compose build

### optional update
docker pull mageai/mageai:latest

### Start Container
docker compose up

### Start Mage in Browser
localhost 6789

### Configuring Postgres