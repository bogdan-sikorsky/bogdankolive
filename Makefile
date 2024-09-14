# Default to .env and docker-compose.yml
# Use prod env command: make up ENV=prod
ifeq ($(ENV), prod)
	ENV_FILE = .env.prod
	COMPOSE_FILE = docker-compose.prod.yml
else
	ENV_FILE = .env
	COMPOSE_FILE = docker-compose.yml
endif


### Compose shortcuts
up:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) up -d

up_debug:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) up

down:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) down

build:
	docker-compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) build

logs:
	docker-compose logs -f

check:
	docker-compose ps && docker ps


### Project shortcuts
streamlit:
	docker-compose run -d --rm -p 8501:8501 web_app streamlit run app/01_Home.py

streamlit_debug:
	docker-compose run --rm -p 8501:8501 web_app streamlit run app/01_Home.py

### Clean up
# Removes everything unused
clean:
	- docker ps -aq
	- docker system prune -f
	- docker container prune -f
	- docker image prune -f
	- docker network prune -f
	- docker volume prune -f
	- docker system prune -a --volumes -f
	- docker ps -aq

# Should stop (regarding compose file) and delete everything
erase: down
	- docker ps -aq
	- docker stop $(docker ps -aq)
	- docker rm $(docker ps -aq)
	- docker rmi $(docker images -q)
	- docker volume prune -f
	- docker network prune -f
	- docker image prune -f
	- docker system prune -f
	- docker system prune -a --volumes -f
	- docker ps -aq
