import os
import yaml
from text_summarization.logging import logger
from pathlib import Path
from typing import Any, Dict, List


def read_yaml(path_to_yaml: str) -> Dict:
    """reads and returns yaml file

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        Dict: yaml file content
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return content

    except Exception as e:
        logger.error(f"Error reading yaml file: {path_to_yaml}, {e}")
        raise e

def create_directories(path_to_directories: List, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): prints the message. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

def get_size(path: str) -> str:
    """get size in KB

    Args:
        path (str): path of file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"