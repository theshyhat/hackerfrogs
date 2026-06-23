# URL
https://hackropole.fr/en/challenges/misc/fcsc2024-misc-welcome-docker/
# Concept
* setting up a Docker compose container to host the challenge infrastructure
# Method of solve
* this challenge is all about testing out the system for challenges on Hackropole
* what we need to do is download the `docker-compose.yml`
```
curl https://hackropole.fr/challenges/fcsc2024-misc-welcome-docker/docker-compose.public.yml -o docker-compose.yml
```
* then run `docker compose` from the same directory
```
docker compose up
```
* to access the Docker container we've started up, run this command, which gets you the flag:
```
nc localhost 4000
```
