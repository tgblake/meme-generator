from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
#from .DocxImporter import DocxImporter
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor

class Ingestor(IngestorInterface):
    ingestors = [PDFIngestor, CSVIngestor, TXTIngestor]  #DocxIngestor
    
    ##@classmethod
    #def can_ingest(cls, path: str) -> bool:
    #    ext = path.split('.')[-1]
    #    return ext in cls.allowed_extensions
    
    #@abstractmethod
    @classmethod
    def parse(cls, path: str) -> list():
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
