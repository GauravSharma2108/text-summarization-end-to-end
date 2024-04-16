# Text Summarization API Using HuggingFace, FAST API and Deployment to AWS with CI/CD Pipeline

>***A short video demonstrating the working of the API***<br>
https://www.youtube.com/watch?v=QG-pj9tV81M

## A brief workflow of the project
1. Setup logging
1. Getting the dataset and model from HuggingFace
2. Build modules and pipelines (mentioned below in pipelines section) right from data gathering to model training and inferencing
3. Use FAST API and Uvicorn to create training and inferencing endpoints.
5. Deployment of the dockerized app to ECR and ECS on AWS
6. Build CI/CD pipeline using GitHub Actions
5. Postman for inferencing


## Pipelines
1. Data Ingestion
2. Data Transformation
3. Data Validation
4. Model Training
5. Model Evaluation
6. Inferencing


### References
**Model**: Hugging Face [Google Pegasus](https://huggingface.co/google/pegasus-cnn_dailymail)<br>
Citations:Jingqing Zhang, Yao Zhao, Mohammad Saleh, & Peter J. Liu. (2019). PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization.<br>
 
**Dataset**: Hugging Face [Samsum dataset](https://huggingface.co/datasets/samsum)<br>
License: CC BY-NC-ND 4.0<br>
Citations: Gliwa, B., Mochol, I., Biesek, M., & Wawer, A. (2019). SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization. In Proceedings of the 2nd Workshop on New Frontiers in Summarization (pp. 70–79). Association for Computational Linguistics.<br>