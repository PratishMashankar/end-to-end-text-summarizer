# Workflow Step 6: Creating pipeline

from textSummarizer.config.config import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        
        # initialize the configuration manager class
        config = ConfigurationManager() 

        # get the data validation config from the class
        data_transformation_config = config.get_data_transformation_config()
        
        # call the data ingestion components
        data_transformation = DataTransformation(config=data_transformation_config)

        # call the the methods validate_all_files_exist()
        data_transformation.convert()