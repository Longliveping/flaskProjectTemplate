from datetime import datetime
from . import db

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(512), unique=True)
    word_count = db.Column(db.Integer)
    sentence_count = db.Column(db.Integer)
    noshow = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(),onupdate=datetime.now())

    def __init__(self, **kwargs):
        super(Article, self).__init__(**kwargs)

    def __repr__(self):
        return f'<Article:{self.id}-{self.article}>'
