from text_summarization.constants import *
from text_summarization.utils.common import read_yaml, create_directories
from text_summarization.entity import (
    DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
)

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

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Get the data transformation configuration

        Returns:
            DataTransformationConfig: data transformation configuration
        """
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            transformed_path=config.transformed_path,
            tokenizer_name = config.tokenizer_name
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """Get the model trainer configuration

        Returns:
            ModelTrainerConfig: model trainer configuration
        """
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )
        return model_evaluation_config