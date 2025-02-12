from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/info')
def get_info():
    return jsonify({
        "email": "olukotunflourish@gmail.com",
        "timestamp": datetime.utcnow().isoformat(),
        "github_url": "https://github.com/f-olukotun/hng-internship"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
