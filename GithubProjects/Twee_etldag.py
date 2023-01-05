from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from ETLdatextraction import etl_twitterdataextraction

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2023,1,5),
    'email':['example@ex.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

dag = DAG(
    'Twee_etldag',
    default_args=default_args,
    description='Data extraction from twitter api'

)

exe_etl=PythonOperator(
    task_id='monitor_twee_etl',
    python_callable='etl_twitterdataextraction',
    dag=dag,
)

exe_etl