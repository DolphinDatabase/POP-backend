run:
	uvicorn main:app --reload

install_postgis:
	docker run -p 5432:5432 --name dolphin-postgis -e POSTGRES_PASSWORD=admin -d postgis/postgis
	
run_postgis:
	docker exec -ti dolphin-postgis psql -U postgres

psql:
	docker exec -ti dolphin-postgis psql -U postgres