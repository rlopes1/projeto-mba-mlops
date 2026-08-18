"""DAG de ingestão dos boletins de ocorrência (esqueleto Aula 01)."""

from datetime import datetime

from airflow import DAG

with DAG(
    dag_id="dag_ingestao_bo",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["pcdf", "bo"],
):
    pass
