import click

from floyd.client.auth import AuthClient
from floyd.config import AuthConfigManager
from floyd.model.credentials import Credentials
from floyd.log import logger as floyd_logger


@click.command()
@click.option('--username', required=True, help='Floyd username')
@click.option('--password', prompt=True, required=True, hide_input=True, help='Floyd password')
def login(username, password):
    credentials = Credentials(username, password)
    access_token = AuthClient().login(credentials)
    AuthConfigManager.set_access_token(access_token)
    floyd_logger.info("Login Successful")


@click.command()
def logout():
    AuthConfigManager.purge_access_token()
    if AuthClient().logout():
        floyd_logger.info("Logout Successful")
