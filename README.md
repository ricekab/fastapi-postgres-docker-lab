# flask-postgres-docker-lab

## About

This repository is for testing a development workflow using docker compose for Python web applications
including backing services.

The Python section of this lab uses Python 3.8+ .

## Requirements

* Docker compose

## Todo list

* [ ] TODO: Fix having to rebuild container each time /python changes (annoying for development)
* [ ] Add message queue into the mix?
* [ ] Allow safe configuration of database connection URI (via file?)
* [ ] ...

## Usage

1. Start containers

```
docker compose build
docker compose up
```

2. First time setup

When the containers are new, the database will start empty (no tables nor entries). The following will
create the tables and two entries:

```
docker-compose run --rm app python -m myapp.cli db create
docker-compose run --rm app python -m myapp.cli airport create --icao EBAW --name "Antwerp International Airport"
docker-compose run --rm app python -m myapp.cli airport create --icao EBBR --name "Brussels Airport"
```

Alternatively, you could do this from a temporary shell:

```
docker-compose run --rm app bash
/python# python -m myapp.cli db create
/python# python -m myapp.cli airport create --icao EBAW --name "Antwerp International Airport"
/python# python -m myapp.cli airport create --icao EBBR --name "Brussels Airport"
```

3. Access FastAPI

The FastAPI endpoint should be accessible using http://127.0.0.1:5000

The two airports we added should be visible at http://127.0.0.1:5000/airport

Similarly, the single airport endpoints should work: http://127.0.0.1:5000/airport/EBAW

Swagger docs are accessible at http://127.0.0.1:5000/docs

4. (Optional) View database contents using adminer

You can use adminer to view the database contents as well at http://127.0.0.1:8080/ with these options:

* Server: `db` 
* Username: `fastapidbo` 
* Password: `fastapidevelopment` 
* Databse: `appdb` 

## Contributing

If this repository is useful to you but you encounter an issue. Feel free to open a GitHub issue for this [here](https://github.com/ricekab/fastapi-postgres-docker-lab/issues).

## License

MIT license.

## Project status

This is a development / lab project. None of this is tested nor intended for production workloads, although it may
be a suitable baseline to work from.