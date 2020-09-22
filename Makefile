run:
	uvicorn flowlytics.server:api


run.dev:
	uvicorn flowlytics.server:api --reload


test:
	rm -f ./test.db
	pytest tests/