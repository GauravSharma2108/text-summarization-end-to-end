from text_summarization.constants import *
from text_summarization.utils.common import read_yaml, create_directories
from text_summarization.entity import ModelTrainerConfig
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import torch
from text_summarization.logging import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Initializing model components")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=int(self.config.num_train_epochs),
            warmup_steps=int(self.config.warmup_steps),
            per_device_train_batch_size=int(self.config.per_device_train_batch_size),
            per_device_eval_batch_size=int(self.config.per_device_train_batch_size),
            weight_decay=float(self.config.weight_decay),
            logging_steps=int(self.config.logging_steps),
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=int(self.config.eval_steps),
            save_steps=int(eval(self.config.save_steps)),
            gradient_accumulation_steps=int(self.config.gradient_accumulation_steps)
        )

        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["test"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        
        logger.info("Training starting")
        trainer.train()

        logger.info("Training finished, saving components")
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))