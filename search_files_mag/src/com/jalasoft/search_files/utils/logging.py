import logging.config

from definition import CONFIG_PATH

logging.config.fileConfig(CONFIG_PATH)

logger = logging.getLogger('searhFiles')

