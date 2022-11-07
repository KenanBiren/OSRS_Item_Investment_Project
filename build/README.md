# How to

## Run this project via command line 
Start with a local or virtual machine with Docker installed.
#### 1. Make a directory titled "OSRS_Item_Investment_Project" and navigate to it, or copy this repo and navigate to the project folder
#### 2. Delete previous Docker images and containers (highly recommended, not needed first time)

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
#### 3. Pull and run "production" Docker images from my Docker Hub 

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
#### 1. Create your own Docker Hub repository
#### 2. Create your own Github project repository as a copy of this one
#### 3. Edit Github workflows to send Docker images to your Docker Hub
My Docker Hub repository for this project is named "kenanbiren/osrs_item_investment_project". I suggest you name yours "*YOUR NAME*/osrs_item_investment_project", so you can easily find and replace my Docker Hub url with your own in each workflow file and in Docker commands (if you are usinf Airflow don't forget to edit the Docker commands in your DAG)

Now when you push code to the "test" branch on your Github, your "test" Docker images will be automatically sent to your Docker Hub via Github workflow actions.
You can then run the "test" Docker images in a test environment to verify functionality and make more changes before pushing the code to the production environment ("main" branch in Github).
#### 4. Set up Apache Airflow to trigger Docker containers if you wish to have email notification upon task failure (optional) 
Airflow non-DAG files such as .config or example DAGs are not included in this project's repository. This project only utilizes basic 
Airflow operators (SSHOperator, SFTPOperator, PythonOperator) and DAG structure (no parallel processing or custom operators). Default settings and configurations
are used for things such as the executor type (SequentialExecutor) and backend database (SQLite). The default settings in Airflow's [Quick-Start Guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html) are sufficient to run the DAG for this project.

I choose to run the backend of this project on an EC2 virtual machine, so I utilize the Airflow's SSHOperator to run commands from the Airflow DAG.



## Deployment Diagram

<img width="827" alt="Screen Shot 2022-11-06 at 2 39 39 PM" src="https://user-images.githubusercontent.com/116853630/200199148-0c29bb20-9c89-465a-974c-71656ba4512a.png">


