from app.models.shloka import Shloka
from app import db
import random

class LearningService:
    @staticmethod
    def get_random_shloka():
        """Get a random shloka for learning"""
        count = Shloka.query.count()
        if count == 0:
            return None
        random_index = random.randint(0, count - 1)
        return Shloka.query.offset(random_index).first()

    @staticmethod
    def get_quiz_questions(shloka_id, num_questions=4):
        """Generate quiz questions for a shloka"""
        shloka = Shloka.query.get_or_404(shloka_id)
        all_shlokas = Shloka.query.filter(Shloka.id != shloka_id).all()
        
        questions = [
            {
                'type': 'meaning',
                'question': f"What is the meaning of: '{shloka.verse[:50]}...'?",
                'correct_answer': shloka.meaning,
                'options': [s.meaning for s in random.sample(all_shlokas, num_questions-1)] + [shloka.meaning]
            },
            {
                'type': 'source',
                'question': f"Where is this shloka from: '{shloka.verse[:50]}...'?",
                'correct_answer': shloka.source,
                'options': [s.source for s in random.sample(all_shlokas, num_questions-1)] + [shloka.source]
            }
        ]
        
        # Shuffle options for each question
        for q in questions:
            random.shuffle(q['options'])
            
        return questions

    @staticmethod
    def evaluate_pronunciation(audio_path, reference_text):
        """Evaluate pronunciation against reference text"""
        # TODO: Implement actual pronunciation evaluation
        return {
            'score': random.randint(70, 95),
            'feedback': 'Good effort! Pay attention to vowel lengths.',
            'matches': [
                {'text': 'First phrase', 'correct': True},
                {'text': 'Second phrase', 'correct': False}
            ]
        }