"""
bigquery_utils.py

This module contains utility functions for interacting with Google BigQuery.
"""

from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from typing import Optional


class BigQueryClient:
    """
    Client for interacting with Google BigQuery.
    """
    def __init__(self, credentials_path: str = "config/gcp-service-account.json", project: str = "Porygon-Pipelines"):
        """
        Initializes the BigQuery client.
        
        Args:
            credentials_path: Path to service account JSON file.
            project: GCP project ID.
        """
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = bigquery.Client(credentials=credentials, project=project)

    def run_query(self, query: str) -> bigquery.job.QueryJob:
        """
        Executes a SQL query on BigQuery and returns the job result.
        
        Args:
            query: SQL query string.
        Returns:
            bigquery.job.QueryJob: The BigQuery job result object.
        """
        job = self.client.query(query)
        return job.result()