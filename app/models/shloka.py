from app import db
from datetime import datetime

class Shloka(db.Model):
    __tablename__ = 'shlokas'
    
    id = db.Column(db.Integer, primary_key=True)
    verse = db.Column(db.String(500), nullable=False)
    devanagari = db.Column(db.String(500), nullable=False)
    translation = db.Column(db.Text, nullable=False)
    meaning = db.Column(db.Text, nullable=False)
    context = db.Column(db.Text)
    source = db.Column(db.String(100))
    chapter = db.Column(db.String(100))
    verse_number = db.Column(db.String(20))
    audio_path = db.Column(db.String(200))
    difficulty = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Shloka {self.id}: {self.verse[:50]}...>'

    def to_dict(self):
        return {
            'id': self.id,
            'verse': self.verse,
            'devanagari': self.devanagari,
            'translation': self.translation,
            'meaning': self.meaning,
            'context': self.context,
            'source': self.source,
            'chapter': self.chapter,
            'verse_number': self.verse_number,
            'audio_path': self.audio_path,
            'difficulty': self.difficulty
        }