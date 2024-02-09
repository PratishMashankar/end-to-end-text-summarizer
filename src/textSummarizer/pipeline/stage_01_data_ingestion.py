# Workflow Step 6: Creating pipeline

from textSummarizer.config.config import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # initialize the configuration manager class
        config = ConfigurationManager() 

        # get the data ingestion config from the class
        data_ingestion_config = config.get_data_ingestion_config()
        
        # call the data ingestion components
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # call the two methods: download_file() and extract_zip_file()
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
