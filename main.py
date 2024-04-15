from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from text_summarization.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline
from text_summarization.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline
from text_summarization.pipeline.stage_04_model_trainer_pipeline import ModelTrainerPipeline
from text_summarization.pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationPipeline

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

STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\n====================\n\n")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\n====================\n\n")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>> Stage {STAGE_NAME} started <<<<<")
    model_evaluator_pipeline = ModelEvaluationPipeline()
    model_evaluator_pipeline.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<<\n\n====================\n\n")
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e