# Workflow Step 6: Creating pipeline

from textSummarizer.config.config import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        
        # initialize the configuration manager class
        config = ConfigurationManager() 

        # get the data validation config from the class
        data_validation_config = config.get_data_validation_config()
        
        # call the data ingestion components
        data_validation = DataValidation(config=data_validation_config)

        # call the the methods validate_all_files_exist()
        data_validation.validate_all_files_exist()
