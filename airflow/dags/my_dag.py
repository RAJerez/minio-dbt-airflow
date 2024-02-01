from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

def _choose_best_model():
    pass

def _training_model():
    return randint(1, 10)

with DAG("my_dag", start_date = datetime(2025, 1, 1),
         schedule_interval = "@daily",
         catchup = False) as dag:
    
    training_model_A = PythonOperator(
        task_id = "training_model_A",
        python_callable = _training_model
    )
    
    training_model_B = PythonOperator(
        task_id = "training_model_B",
        python_callable = _training_model
    )
    
    training_model_C = PythonOperator(
        task_id = "training_model_C",
        python_callable = _training_model
    )
    
    choose_best_model = BranchPythonOperator(
        task_id = "choose_best_model",
        python_callable = _choose_best_model
    )
    
    