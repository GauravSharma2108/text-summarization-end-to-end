import os
import urllib.request as request
import zipfile
from text_summarization.logging import logger
from text_summarization.utils.common import get_size
from text_summarization.entity import DataIngestionConfig

class DataIngestion:
    """
    This class is responsible for downloading and extracting the data from the source URL
    """
    def __init__(self, config: DataIngestionConfig):
        """Initializes the DataIngestion class

        Args:
            config (DataIngestionConfig): DataIngestionConfig object
        """
        self.config = config
    
    def download_file(self):
        """
        Downloads the file from the source URL if it doesn't exist
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with info:\n{headers}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}\nSize: {get_size(self.config.local_data_file)}")
    
    def extract_zip_file(self):
        """
        Extracts the zip file to the specified directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)