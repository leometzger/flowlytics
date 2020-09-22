run:
	uvicorn flowlytics.server:api


run.dev:
	uvicorn flowlytics.server:api --reload


test:
	pytest tests/