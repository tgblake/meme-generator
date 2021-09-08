from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str):  # -> list():
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        #text = docx.Document(path)
        with open(path, 'r') as file:
            for line in file.readlines():
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
    
        return quotes
    
