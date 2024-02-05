from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://poonamchourey01:Poonam123@cluster0.b8fggs8.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Create overlay settings
@app.route('/overlay/create', methods=['POST'])
def create_overlay():
    data = request.get_json()
    # Validate and insert data into the MongoDB
    overlay_id = mongo.db.overlays.insert_one(data).inserted_id
    return jsonify({'message': 'Overlay created successfully', 'overlay_id': str(overlay_id)})

# Read overlay settings
@app.route('/overlay/<overlay_id>', methods=['GET'])
def get_overlay(overlay_id):
    overlay = mongo.db.overlays.find_one_or_404({'_id': overlay_id})
    return jsonify(overlay)

# Update overlay settings
@app.route('/overlay/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    data = request.get_json()
    mongo.db.overlays.update_one({'_id': overlay_id}, {'$set': data})
    return jsonify({'message': 'Overlay updated successfully'})

# Delete overlay settings
@app.route('/overlay/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    mongo.db.overlays.delete_one({'_id': overlay_id})
    return jsonify({'message': 'Overlay deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
