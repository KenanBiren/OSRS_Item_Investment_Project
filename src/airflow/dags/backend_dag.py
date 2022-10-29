import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
import time


sshHook = SSHHook(ssh_conn_id="ec2ssh")





with DAG(
    'BackendDag',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['xenu4587@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': datetime.timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='Backend DAG',
    schedule_interval=datetime.timedelta(days=1),
    start_date=datetime.datetime(2022, 9, 12),
    catchup=False
) as dag:



    t1 = SSHOperator(
     task_id="first_task",
     command="**COMMAND TO RUN process_backend.py",
     ssh_hook=sshHook,
     dag=dag)
    ## this is where docker commands will go to build the image before running it


    t1
