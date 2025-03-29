from flask import render_template, request, jsonify
from app.models.shloka import Shloka
from app import db
from app.learning import bp

@bp.route('/')
def learn_home():
    return render_template('learning/index.html')

@bp.route('/<int:shloka_id>')
def view_shloka(shloka_id):
    shloka = Shloka.query.get_or_404(shloka_id)
    return render_template('learning/view.html', shloka=shloka)

@bp.route('/practice/<int:shloka_id>')
def practice_shloka(shloka_id):
    shloka = Shloka.query.get_or_404(shloka_id)
    return render_template('learning/practice.html', shloka=shloka)

@bp.route('/quiz/<int:shloka_id>')
def quiz_shloka(shloka_id):
    shloka = Shloka.query.get_or_404(shloka_id)
    return render_template('learning/quiz.html', shloka=shloka)

@bp.route('/api/shlokas')
def get_shlokas():
    shlokas = Shloka.query.all()
    return jsonify([shloka.to_dict() for shloka in shlokas])