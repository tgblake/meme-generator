from typing import List
import pandas
import csv

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str):  # -> list():
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        df = pandas.read_csv(path, header=0)
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
    
        return quotes
    
