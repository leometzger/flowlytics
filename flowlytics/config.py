import logging
import os


APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/api")
DEBUG = os.getenv("ENVIRONEMENT") == "DEV"

HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log") if not DEBUG else None,
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)