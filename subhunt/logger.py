import logging
import sys

def setup_logger(log_level: int = logging.INFO, log_file: str = "subhunt.log"):
    """
    Configures and returns a logger for the application.

    The logger will output to both the console and a file.

    Args:
        log_level (int): The minimum logging level for the console (e.g., logging.INFO).
        log_file (str): The name of the file to save logs to.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    console_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger