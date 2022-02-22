from datetime import timedelta,datetime
from airflow import DAG 
from airflow.operators.dummy import DummyOperator


default_args = {
    'retries' : 5,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(
    'universidades_c',
    description='university_processes',
    default_args= default_args,
    #defino ejecucion
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2022,2,18)
    ) as dag:
    
    
    #Queries
    #SQL for Universidad Nacional
    #SQL for Universidad de Palermo
    
    #Data processing 
    #pandas as pd 
    
    #Upload data to S3    
    
    universidad_nacional= DummyOperator(task_id='universidad_nacional')
    universidad_de_palermo= DummyOperator(task_id='universidad_de_Palermo')


    universidad_nacional >> universidad_de_palermo
