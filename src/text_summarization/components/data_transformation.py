import os
from text_summarization.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from text_summarization.entity import DataTransformationConfig

class DataTransformation:
    """
    DataTransformation class is used to transform the data into the required format for the model training.
    """
    def __init__(self, config: DataTransformationConfig):
        """Constructor

        Args:
            config (DataTransformationConfig): data transformation configuration
        """
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        """Extract features from the examples for the model training in appropriate format.
        """
        logger.info("Tokenizing the input and target text")
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        """
        Convert the data into the required format for model training.
        """
        logger.info("Converting the data into the required format for model training.")
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        dataset_samsum_pt.save_to_disk(self.config.transformed_path)
        logger.info("Data conversion completed.")