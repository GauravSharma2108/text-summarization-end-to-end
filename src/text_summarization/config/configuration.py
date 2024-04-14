from text_summarization.constants import *
from text_summarization.utils.common import read_yaml, create_directories
from text_summarization.entity import DataIngestionConfig, DataValidationConfig

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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """Get the data validation configuration

        Returns:
            DataValidationConfig: data validation configuration
        """
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            required_files=config.required_files,
        )
        return data_validation_config