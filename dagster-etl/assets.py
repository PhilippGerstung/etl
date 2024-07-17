from dagster import asset
from loguru import logger


@asset
def update_data_with_git() -> None:
    logger.info("Updating data with git")
    pass


@asset(deps=[update_data_with_git])
def load_stations() -> None:
    logger.info("Loading stations")


@asset(deps=[update_data_with_git])
def load_prices() -> None:
    logger.info("Loading prices")
