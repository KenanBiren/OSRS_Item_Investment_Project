# How to

## Run this project via command line 
Start with a local or virtual machine capable of running Docker.
### 1. Make a directory titled "OSRS_Item_Investment_Project" and navigate to it, or copy this repo and navigate to the project folder
### 2. Delete previous Docker images and containers (optional, highly recommended) 

Backend
```
docker image rm kenanbiren/osrs_item_investment_project:extract -f
docker image rm kenanbiren/osrs_item_investment_project:transform -f
docker container prune -f   
```
Frontend
```
docker image rm kenanbiren/osrs_item_investment_project:app -f
docker container prune -f
```
### 3. Pull and run "production" Docker images from my Docker Hub 

Backend
```
docker pull kenanbiren/osrs_item_investment_project:extract
docker run -v "$PWD":/OSRS_Item_Investment_Project kenanbiren/osrs_item_investment_project:extract
```
Frontend
```
docker pull kenanbiren/osrs_item_investment_project:app
docker run -ti --platform=linux/amd64 --env=DISPLAY -v "$PWD":/OSRS_Item_Investment_Project kenanbiren/osrs_item_investment_project:app
```
Project will automatically stay up-to-date with my version releases.

## Make your own changes to this project
### 1. Create your own Docker Hub repository
### 2. Create your own Github project repository as a copy of this one
### 3. Edit Github workflows to send Docker images to your Docker Hub
Now when you push code to the "test" branch on your Github, your "test" Docker images will be automatically sent to your Docker Hub via Github workflow actions.
You can then run the "test" Docker images in a test environment for verification before pushing the code to the production version ("main" branch) of the project.
### 4. Set up Apache Airflow to trigger Docker containers if you wish to have email notification upon task failure (optional) 
Airflow supporting files such as .config or example DAGs are not included in this project's repository. This project only utilizes basic 
Airflow operators (SSHOperator, SFTPOperator, PythonOperator) and DAG structure (no parallel processing or custom operators). Default settings and configurations
are used for things such as the executor type (SequentialExecutor) and backend database (SQLite). Here is a link to Airflow's [Quick-Start Guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html)









