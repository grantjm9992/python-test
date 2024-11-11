build:
	docker-compose build --no-cache

run:
	docker-compose up -d

mongo-indexes:
	 docker exec -it mongodb mongosh --eval "use intelistyle_db" \
		--eval "db.garments.createIndex({'brand': 1})" \
		--eval "db.garments.createIndex({'gender': 1})" \
		--eval "db.garments.createIndex({'product_title': 1})" \
		--eval "db.garments.createIndex({'product_categories': 1})" \
		--eval "db.garments.createIndex({'price': 1})"

setup: build run

setup-test:
	docker exec -it mongodb mongosh --eval "use test_intelistyle_db"
	docker exec -it mongodb bash -c "mongoimport --host mongo --db test_intelistyle_db --collection garments --file /docker-entrypoint-initdb.d/garments.jl"

run-test:
	docker exec -it fastapi_app bash -c "pytest tests/infrastructure/api/v1/garments/search_garments.py"