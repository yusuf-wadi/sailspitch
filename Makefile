.PHONY: run run-container gcloud-deploy

run:
	@streamlit run app.py --server.port=8080 --server.address=127.0.0.1

run-container:
	@docker build . -t SailsPitch
	@docker run -p 8080:8080 SailsPitch

gcloud-deploy:
	@gcloud app deploy app.yaml
