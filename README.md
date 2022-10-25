# Car_price_prediction
Python project for car price prediction with the ability to run through Airflow


This project is a continuation of the Classification model for determining the price category of used cars, depending on the vehicle characteristics offered for sale in the United States.
And it includes a code designed as Pipeline for integration, as well as the ability to launch on schedule in Airflow.

!!!Guide for deploying and launching this project in Airflow via Docker loccaly on Windows 10:
1. Start Docker Desktop and remove all containers.
2. Create a folder "C:\Users\user\airflow".
3. Start Git Bash, run the following commands:
	3.1. "cd /c/Users/user/airflow"
	3.2. "mkdir airflow-docker"
	3.3. "cd airflow-docker"
	3.4. "curl -O https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"
	3.5. Do not close Git Bash.
4. Open the "C:\Users\user\airflow\airflow-docker\docker-compose.yaml" file and make the following changes:
	4.1. Replace the line "AIRFLOW_CORE_LOAD_EXAMPLES: 'true'" to "AIRFLOW_CORE_LOAD_EXAMPLES: 'false'".
	4.2. In the volumes section, add the line "- C:\Users\user\Car_price_prediction:/Car_price_prediction".
	4.3. Change the line "_PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-}" to "_PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-pandas scikit-learn}".
	4.4. Save and close this file
5. With Git Bash open, run the following commands:
	5.1. "mkdir dags logs plugins"
	5.2. "echo -e 'AIRFLOW_UID=50000' > .env"
	5.3. "docker-compose up airflow-init"
	5.4. "docker-compose-up"
6. Docker Desktop should have running containers.
7. Go to "http://localhost:8080/" (via browser address bar) and the Airflow interface will open.
8. Enter username: "airflow" and password: "airflow".
10. Copy "Car_price_prediction" repository to "C:\Users\user".
11. Copy the file "C:\Users\user\Car_price_prediction\dags\hw_dag.py" to "C:\Users\user\airflow\airflow-docker\dags".
12. Open Docker Desktop. Stop all containers. Then start all containers.
15. Refresh the page with the Airflow interface, the "car_price_prediction" DAG should appear.
16. After some time, when the code of your DAG is executed, the "pkl-file" of the model should appear in the "C:\Users\user\Car_price_prediction\data\models", 
then "csv-file" with predictions should appear in the "C:\Users\user\Car_price_prediction\data\predictions".
