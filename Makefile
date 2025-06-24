run:
	python app/main.py

test:
	pytest tests/

lint:
	flake8 app/ tests/

build:
	docker build -t fastapi-helloworld:latest .

docker-run:
	docker run -p 8000:8000 fastapi-helloworld:latest

.PHONY: run test lint build docker-run

