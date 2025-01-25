import os
from datetime import date

Database_name = 'US_VISA'

Collection_name= 'visa_data'

Mongdb_url_key= 'mongodb_url'

pipeline_name: str = 'usvisa'
artifact_dir: str = 'artifact'

train_file_name: str = 'train.csv'
test_file_name: str = 'test.csv'

file_name: str = 'usvisa.csv'
model_file_name= 'model.pkl'

target_column = 'case_status'
current_year = date.today().year
preprocessing_object_file_name= 'preprocessing.pkl'
schema_file_path = os.path.join('config', 'schema.yaml')
'''

Data Ingestion related constant start with Data_ingestion Var Name
'''

data_ingestion_collecion_name: str ='visa_data'
data_ingestion_dir_name: str = 'data_ingestion'
data_ingestion_feature_store_dir: str = 'feature_store'
data_ingestion_ingested_dir: str = 'ingested'
data_ingestion_train_test_split_ratio: float = 0.2

'''
Data Validation related constant start with Data_validation Var Name
'''

data_validation_dir_name: str = 'data_validation'
data_validation_drift_report_dir: str = 'drift_report'
data_validation_drift_report_file_name: str = 'report.yaml'
