from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    def parse(cls, path: str):  # -> list():
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(',')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
    
        return quotes
    
