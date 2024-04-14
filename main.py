from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e