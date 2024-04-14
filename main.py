from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from text_summarization.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\n====================\n\n")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\n====================\n\n")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e
