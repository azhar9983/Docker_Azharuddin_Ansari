from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS to allow the Node.js frontend to securely send data to this backend
CORS(app)

@app.route('/')
def index():
    return "Flask backend is running!"

@app.route('/api/submit', methods=['POST'])
def handle_submit():
    # Extract data sent via JSON from the frontend
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400
        
    username = data.get('username')
    email = data.get('email')
    
    # Process your data here (simulating processing)
    processed_message = f"Hello {username}! Your email ({email}) was successfully processed by the Flask backend."
    
    # Send a JSON response back to the client
    return jsonify({
        "status": "success",
        "message": processed_message,
        "received_data": {
            "username": username,
            "email": email
        }
    }), 200

if __name__ == '__main__':
    # Runs the Flask server on port 5000
    app.run(port=5000, debug=True)
