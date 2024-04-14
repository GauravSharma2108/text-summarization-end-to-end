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