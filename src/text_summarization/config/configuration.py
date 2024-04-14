from text_summarization.constants import *
from text_summarization.utils.common import read_yaml, create_directories
from text_summarization.entity import DataIngestionConfig

class ConfigurationManager:
    """
    Configuration Manager class to read the configuration and parameters files for each module
    """
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH
    ):
        """Constructor
        
        Args:
            config_filepath (_type_, optional): path to the configuration file. Defaults to CONFIG_FILE_PATH.
            params_filepath (_type_, optional): path to the parameters file. Defaults to PARAMS_FILE_PATH.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        """Get the data ingestion configuration

        Returns:
            DataIngestionConfig: data ingestion configuration
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = config.source_url,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )