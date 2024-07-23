import cv2
from flask import Flask, jsonify
# Initialize Flask application
app = Flask(__name__)

# Load the pre-trained fire detection cascade model
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

# Function to detect fire and return the status
def detect_fire():
    # Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return False, "Camera not opened"

    # Read a single frame
    ret, frame = cap.read()
    
    if not ret:
        cap.release()  # Release the camera if the frame capture fails
        return False, "Failed to grab frame"

    # Detect fires in the frame
    fire_detected = len(fire_cascade.detectMultiScale(frame, 1.2, 5)) > 0
    
    # Release the camera
    cap.release()

    return fire_detected, None

@app.route('/check_fire', methods=['GET'])
def check_fire():
    # Check for fire detection
    fire_detected, error = detect_fire()
    
    if error:
        return jsonify({"error": error}), 500  # Return with error status code
    
    if fire_detected:
        return jsonify({"status": "Fire detected"})
    else:
        return jsonify({"status": "No fire detected"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)