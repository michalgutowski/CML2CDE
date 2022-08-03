# The new Airflow DAG
from dateutil import parser
    
from datetime import datetime, timedelta
    
from datetime import timezone
    
from airflow import DAG
    
from airflow.operators.email import EmailOperator
    
from airflow.operators.python_operator import PythonOperator
    
from cloudera.cdp.airflow.operators.cdw_operator import CDWOperator
    
from cloudera.cdp.airflow.operators.cde_operator import CDEJobRunOperator

default_args = {
    'owner': 'your_username_here',
    'retry_delay': timedelta(seconds=5),
    'depends_on_past': False,
    'start_date': parser.isoparse('2021-05-25T07:33:37.393Z').replace(tzinfo=timezone.utc)
    }

dag = DAG(
    'airflow-pipeline-demo',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    is_paused_upon_creation=False
    )

SparkPi_Step = CDEJobRunOperator(
        task_id='SparkPi',
        dag=dag,
        job_name='SparkPi'
        )
