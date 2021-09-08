class QuoteModel:
    """Encapsulate quote bodies and authors
    """
    
    def __init__(self, body, author):
        """Accept quote body and author.
        """
        self.body = body
        self.author = author
        
    def __repr__(self):
        return f'<{self.body}, {self.author}>'
