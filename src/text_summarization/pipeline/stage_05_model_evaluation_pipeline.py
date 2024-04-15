from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self, config):
        self.config = config

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate_model()