from flask import Flask, request, jsonify
import face_recognition.api as fr
import json
import numpy as np
import os

app = Flask(__name__)

DB_FILE = "encodings_db.json"

def load_known_encodings():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Load known encodings
    known_db = load_known_encodings()
    known_encodings = [np.array(person["encoding"]) for person in known_db]
    known_names = [person["name"] for person in known_db]

    # Process incoming image
    image_file = request.files['image']
    image = fr.load_image_file(image_file)
    locations = fr.face_locations(image, model="cnn")
    encodings = fr.face_encodings(image, locations)

    results = []

    for encoding in encodings:
        matches = fr.compare_faces(known_encodings, encoding, tolerance=0.5)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        results.append({
            "name": name,
            "matched": name != "Unknown"
        })

    return jsonify({
        "num_faces": len(encodings),
        "attendance": results
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
