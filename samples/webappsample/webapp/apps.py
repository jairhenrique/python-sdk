import configcatclient
from django.apps import AppConfig


class WebappConfig(AppConfig):
    name = 'webapp'
    configcat_client = configcatclient.create_client('PKDVCLf-Hq-h-kCzMp-L7Q/psuH7BGHoUmdONrzzUOY7A')
