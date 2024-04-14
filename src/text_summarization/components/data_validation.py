import os
from text_summarization.logging import logger
from text_summarization.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self)-> bool:
        try:
            logger.info("Validating all files exist")
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.required_files:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            if validation_status:
                logger.info("Validation true")
            else:
                logger.info("Validation false")
            return validation_status
        except Exception as e:
            logger.error(f"Validation failed: {e}")
            raise e