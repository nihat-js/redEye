
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Temporary storage (replace with database in production)
submissions = []
hosts = set()

@app.route('/')
def index():
    return render_template('index.html',
                         total_hosts=len(hosts),
                         total_submissions=len(submissions),
                         active_sessions=0,
                         recent_activities=[])

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.json
    data['timestamp'] = datetime.now().isoformat()
    submissions.append(data)
    if 'host' in data:
        hosts.add(data['host'])
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
