from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngestionConfig class is used to store the configuration for the data ingestion process.
    """
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    """
    DataValidationConfig class is used to store the configuration for the data validation process.
    """
    root_dir: Path
    status_file: Path
    required_files: list

@dataclass(frozen=True)
class DataTransformationConfig:
    """
    DataTransformationConfig class is used to store the configuration for the data transformation process.
    """
    root_dir: Path
    data_path: Path
    transformed_path: Path
    tokenizer_name: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path