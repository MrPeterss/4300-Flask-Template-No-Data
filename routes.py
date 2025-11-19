import json
from flask import render_template, request
from models import db, Episode, Review

# Search function
def json_search(query):
    # Query episodes with matching title and join with reviews
    results = db.session.query(Episode, Review).join(
        Review, Episode.id == Review.id
    ).filter(
        Episode.title.ilike(f'%{query}%')
    ).all()
    
    # Convert results to JSON format
    matches = []
    for episode, review in results:
        matches.append({
            'title': episode.title,
            'descr': episode.descr,
            'imdb_rating': review.imdb_rating
        })
    
    return json.dumps(matches)

def register_routes(app):
    """Register all routes with the Flask app"""
    
    @app.route("/")
    def home():
        return render_template('base.html', title="sample html")

    @app.route("/episodes")
    def episodes_search():
        text = request.args.get("title")
        return json_search(text)

