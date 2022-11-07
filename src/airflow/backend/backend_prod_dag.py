from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.providers.sftp.operators.sftp import SFTPOperator
from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.providers.sftp.hooks.sftp import SFTPHook
import time
import datetime

sshHook = SSHHook(ssh_conn_id="prod_ec2")
sftpHook = SFTPHook(ssh_hook=sshHook)




with DAG(
    'BackendDag',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': True,
        'email': ['EMAIL@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': True,
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
    start_date=datetime.datetime(2022, 11, 4),
    catchup=False
) as dag:



    t1 = SSHOperator(
     task_id="run_extract",
     command='cd ~/OSRS_Item_Investment_Project/;docker image rm kenanbiren/osrs_item_investment_project:extract -f;docker container prune -f;docker pull kenanbiren/osrs_item_investment_project:extract;docker run -v "$PWD":/OSRS_Item_Investment_Project kenanbiren/osrs_item_investment_project:extract',
     ssh_hook=sshHook,
     dag=dag)


    t2 = SSHOperator(
     task_id="run_transform",
     command='cd ~/OSRS_Item_Investment_Project/;docker image rm kenanbiren/osrs_item_investment_project:transform -f;docker container prune -f;docker pull kenanbiren/osrs_item_investment_project:transform;docker run -v "$PWD":/OSRS_Item_Investment_Project kenanbiren/osrs_item_investment_project:transform',
     ssh_hook=sshHook,
     dag=dag)


     t3 = SFTPOperator(
     task_id="file_transfer_to_app_server",
     sftp_hook=sftpHook,
     local_filepath="/Users/kenanbiren/OSRS_Item_Investment_Project/test/OSRS_Item_Investment_Project/data",
     remote_filepath="~/OSRS_Item_Investment_Project/data",
     operation="get",
     dag=dag)


     

     
    t1 >> t2 >> t3