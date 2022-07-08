import pendulum
from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': pendulum.datetime(2022, 1, 1, tz="Asia/Singapore"),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


with DAG(dag_id='batchwith2tags',
        default_args=default_args,
        schedule_interval='*/5 * * * *',
        dagrun_timeout=timedelta(seconds=120),
        catchup=False,
        tags=['JP','Learning','Batch']
        ) as dag:
# Step 1
   t1 = BashOperator(
      task_id='task_1',
      bash_command="echo 'Task 1 - Jean-Paul is the GREATEST!'")

   t2 = BashOperator(
      task_id='task_2',
      bash_command="echo 'Task 2 - Jean-Paul is the GREATEST!'")

t1 >> t2

