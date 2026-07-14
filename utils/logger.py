"""
==========================================================
AgriNova AI v2.0
Central Logging Utility
==========================================================
"""

import logging

from pathlib import Path

from logging.handlers import RotatingFileHandler

from utils.constants import (
    LOG_FORMAT,
    LOG_LEVEL
)


# ==========================================================
# Log Directory
# ==========================================================

LOG_DIRECTORY = Path("logs")

LOG_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)

LOG_FILE = LOG_DIRECTORY / "agrinova.log"


# ==========================================================
# Logger Factory
# ==========================================================

def get_logger(name: str) -> logging.Logger:
    """
    Return configured logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(

        getattr(
            logging,
            LOG_LEVEL.upper(),
            logging.INFO
        )

    )

    formatter = logging.Formatter(

        LOG_FORMAT

    )

    # ------------------------------------------------------
    # Console Handler
    # ------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    # ------------------------------------------------------
    # File Handler
    # ------------------------------------------------------

    file_handler = RotatingFileHandler(

        LOG_FILE,

        maxBytes=5 * 1024 * 1024,

        backupCount=5,

        encoding="utf-8"

    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(console_handler)

    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


# ==========================================================
# Default Logger
# ==========================================================

app_logger = get_logger("AgriNova")


# ==========================================================
# Helper Functions
# ==========================================================

def log_info(message: str):

    app_logger.info(message)


def log_warning(message: str):

    app_logger.warning(message)


def log_error(message: str):

    app_logger.error(message)


def log_debug(message: str):

    app_logger.debug(message)


def log_exception(message: str):

    app_logger.exception(message)