The test was run on a postgres 15.2 container launched with

```
docker run --rm -p 5432:5432 -e POSTGRES_DB=timeslot -e POSTGRES_PASSWORD=mysecretpassword -d postgres:15.2-bullseye
```
