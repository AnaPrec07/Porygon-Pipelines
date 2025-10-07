"""
core/pipeline.py

This module defines the Pipeline abstract class, which serves as a template for all pipelines in this repository.
It provides a consistent interface for data extraction, transformation, and loading.
"""

from src.core.bigquery_client import BigQueryClient
from abc import ABC, abstractmethod

class Pipeline(ABC):
    """
    Abstract base class for all data pipelines.
    """
    def __init__(self):
        """
        Initialize abstract pipeline class.
        """
        self.bq_client = BigQueryClient()

    @abstractmethod
    def extract(self, table_name: str):
        """
        Abstract method to extract data from a specified table.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def transform(self, table_name: str):
        """
        Abstract method to transform extracted data.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def load(self, table_name: str):
        """
        Abstract method to load transformed data.
        Must be implemented by subclasses.
        """
        pass

    def run(self):
        """
        Run the pipeline.
        """
        self.extract()
        self.transform()
        self.load()