from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_executor import Executor
import spacy
import random
import os
import requests
from bs4 import BeautifulSoup

# Initialize Flask app
app = Flask(__name__)

# Configuration for SQLite and Redis
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///startups.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

# Initialize extensions
db = SQLAlchemy(app)
cache = Cache(app)
executor = Executor(app)

# Load spaCy model for NLP analysis
nlp = spacy.load('en_core_web_sm')

# Model to store startup information
class Startup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    uvp = db.Column(db.Text, nullable=False)
    target_audience = db.Column(db.Text, nullable=False)
    insights = db.Column(db.Text, nullable=True)
    linkedin_profiles = db.Column(db.Text, nullable=True)
    outreach_results = db.Column(db.Text, nullable=True)
    ab_test_results = db.Column(db.Text, nullable=True)
    feedback = db.Column(db.Text, nullable=True)
    refinement_suggestions = db.Column(db.Text, nullable=True)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/submit_startup', methods=['POST'])
def submit_startup():
    """Endpoint to capture startup information."""
    company_name = request.form['company_name']
    industry = request.form['industry']
    uvp = request.form['uvp']
    target_audience = request.form['target_audience']

    # NLP analysis of UVP
    insights = analyze_uvp(uvp)
    
    # Simulated LinkedIn scraping and outreach
    linkedin_profiles = scrape_linkedin_profiles(industry, target_audience)
    outreach_results, ab_test_results = perform_outreach(linkedin_profiles)
    
    # Save startup data in database
    new_startup = Startup(
        company_name=company_name,
        industry=industry,
        uvp=uvp,
        target_audience=target_audience,
        insights=insights,
        linkedin_profiles=linkedin_profiles,
        outreach_results=outreach_results,
        ab_test_results=ab_test_results,
        refinement_suggestions=generate_refinement_suggestions(ab_test_results)
    )
    db.session.add(new_startup)
    db.session.commit()

    return jsonify({"message": "Startup information submitted successfully."}), 200

def analyze_uvp(uvp):
    """Analyze the unique value proposition using NLP to extract insights."""
    doc = nlp(uvp)
    keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'VERB', 'PROPN']]
    return ', '.join(set(keywords))

def scrape_linkedin_profiles(industry, target_audience):
    """Simulate LinkedIn profile scraping based on the industry and target audience."""
    profiles = []
    for i in range(5):  # Simulate scraping 5 profiles
        profiles.append(f"Profile {i+1} - Industry: {industry}, Target Audience: {target_audience}")
    return '; '.join(profiles)

def perform_outreach(profiles):
    """Simulate outreach and A/B testing."""
    outreach_results = []
    ab_test_results = {"Version A": 0, "Version B": 0}
    
    for profile in profiles.split('; '):
        # Simulate sending different versions of outreach messages
        version = random.choice(["A", "B"])
        response = random.choice(["Interested", "Not Interested"])
        
        # Track A/B test results
        ab_test_results[f"Version {version}"] += 1 if response == "Interested" else 0
        outreach_results.append(f"{profile}: Sent Version {version}, Response: {response}")
    
    return '; '.join(outreach_results), ab_test_results

@app.route('/fetch_trend_data', methods=['GET'])
@cache.cached(timeout=50, query_string=True)
def fetch_trend_data():
    """Simulated fetching of Google Trends or other market data."""
    keyword = request.args.get('keyword')
    
    # Simulate generating trend data
    trend_data = [
        {"date": f"2023-09-{i+1:02d}", "value": random.randint(50, 100)} for i in range(30)
    ]
    return jsonify(trend_data), 200

@app.route('/analytics_data', methods=['GET'])
def analytics_data():
    """Return A/B testing results and refinement suggestions."""
    startups = Startup.query.all()
    
    # Aggregate A/B test results
    aggregated_ab_test = {"Version A": 0, "Version B": 0}
    for startup in startups:
        ab_test = json.loads(startup.ab_test_results)
        aggregated_ab_test["Version A"] += ab_test["Version A"]
        aggregated_ab_test["Version B"] += ab_test["Version B"]

    # Generate overall refinement suggestions
    refinement_suggestions = "Focus on Version A as it performs better in most cases."
    
    return jsonify({
        "ab_test_results": aggregated_ab_test,
        "refinement_suggestions": refinement_suggestions
    }), 200

def generate_refinement_suggestions(ab_test_results):
    """Generate refinement suggestions based on A/B test results."""
    if ab_test_results["Version A"] > ab_test_results["Version B"]:
        return "Version A is performing better. Consider refining Version B."
    else:
        return "Version B is performing better. Consider refining Version A."

if __name__ == '__main__':
    app.run(debug=True)
