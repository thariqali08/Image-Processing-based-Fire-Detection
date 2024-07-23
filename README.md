# Image Processing based Fire Detection System

This project consists of two main components: a Flask-based server for fire detection and a Raspberry Pi Pico receiver for handling fire alerts. The system uses OpenCV for real-time fire detection and communicates with the Raspberry Pi Pico to trigger alerts.

## Overview

- **Main Program**: A Flask server that uses OpenCV to detect fire from a camera feed.
- **Receiver Program**: Runs on a Raspberry Pi Pico to check for fire status and activate an LED and buzzer in case of fire detection.

## Components

1. **Main Program (Flask + OpenCV)**
   - **File Name**: `main.py`
   - **Purpose**: Provides a Flask endpoint to check for fire status using OpenCV.

2. **Receiver Program (Raspberry Pi Pico)**
   - **File Name**: `rasp_pi.py`
   - **Purpose**: Runs on the Raspberry Pi Pico to check the Flask server for fire status and control an LED and buzzer.

## Installation

1. **For the Flask Server**:
   - Install the required Python libraries:
     ```bash
     pip install flask opencv-python
     ```
   - Ensure you have the `fire_detection_cascade_model.xml` file in the same directory as `main.py`.

2. **For the Raspberry Pi Pico**:
   - Ensure you have the MicroPython firmware installed on your Raspberry Pi Pico.
   - Connect the Pico to your computer and upload `rasp_pi.py` using a MicroPython IDE (e.g., Thonny).

## Usage

1. Start the Flask server by running:
   ```bash
   python main.py
