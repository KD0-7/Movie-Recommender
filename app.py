from flask import Flask, request, jsonify
from flask_cors import CORS
import recommender  

app = Flask(__name__)
CORS(app)  

@app.route('/api/recommend', methods=['GET'])
def get_recommendations():
    
    movie_name = request.args.get('movie')
    
    if not movie_name:
        return jsonify({"error": "No movie provided"}), 400

    
    try:
        results = recommender.recommend(movie_name)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)