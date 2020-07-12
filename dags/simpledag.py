from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

# Parâmetros
args = {
    'owner':'janilson',
    'start_date': days_ago(1)
}

# Criação do dag
dag = DAG(dag_id="my_simple_dag", default_args=args, schedule_interval=None)

# Função python para ser executada pelas tarefas
def run_this_func(**context):
    print('hi')

with dag:
    # Tarefa teste 1
    run_this_task = PythonOperator(
        task_id = 'run_this',
        python_callable = run_this_func,
        provide_context = True,
    )

    # Tarefa teste 2
    run_this_task2 = PythonOperator(
        task_id = 'run_this2',
        python_callable = run_this_func,
        provide_context = True,
    )

    # Definindo a ordem das tarefas
    run_this_task >> run_this_task2