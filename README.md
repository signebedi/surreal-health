# surreal-health
SurrealDB health data modeling


#### Run Surreal

I just start with the docker image, which is simple:

```bash
docker run --rm --pull always -p 8977:8000 surrealdb/surrealdb:latest start --log trace --auth --user root --pass root 
```