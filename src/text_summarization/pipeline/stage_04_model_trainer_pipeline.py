from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.model_trainer import ModelTrainer
from text_summarization.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()