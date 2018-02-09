import logging.config
from definition import CONFIG_PATH

logging.config.fileConfig(CONFIG_PATH)

# create logger
logger = logging.getLogger('SearchFiles')

# Set default logger's level
logger.setLevel(logging.INFO)
