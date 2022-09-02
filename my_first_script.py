"""Run a simple flow in Prefect 2.x"""
from prefect import flow
from prefect.logging import get_run_logger

@flow
def my_favorite_number():
    logger = get_run_logger()
    logger.info("Some info about my_favorite_number...")
    return 42
