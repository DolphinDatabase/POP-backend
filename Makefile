run:
	python source/main.py

install_postgis:
	docker run -p 5432:5432 --name dolphin-postgis -e POSTGRES_PASSWORD=admin -d postgis/postgis
	
run_postgis:
	docker exec -ti dolphin-postgis psql -U postgres

psql:
	docker exec -ti dolphin-postgis psql -U postgres

docker:

	docker logout

	docker build -t dolphindatabase/visiona-back:latest .

	docker login

	docker push dolphindatabase/visiona-back:latest

	docker run -p 5050:5050 dolphindatabase/visiona-back:latest
