# Face Detection System using CVZone and Arduino IDE

This project implements a **Human Face Detection System** using **CVZone** (Python) and **Arduino IDE**. It uses a laptop webcam to detect human faces and communicates with an Arduino Uno board to control two LEDs:

- **Blue LED**: Indicates a human face is detected.
- **Red LED**: Indicates no human face is detected.

---

## Features
1. Detect human faces in real-time using **CVZone** and a webcam.
2. Send detection signals to the Arduino Uno via serial communication.
3. Control two LEDs connected to the Arduino Uno:
   - **Blue LED** turns ON when a face is detected.
   - **Red LED** turns ON when no face is detected.

---

## System Overview
1. **Software Used**:
   - **PyCharm**: For Python programming and face detection using CVZone.
   - **Arduino IDE**: For programming the Arduino Uno board.

2. **Hardware Used**:
   - **Laptop Webcam**: To capture live video feed.
   - **Arduino Uno**: To process face detection signals from Python.
   - **Two LEDs** (Red and Blue): To indicate the detection status.

3. **Process Flow**:
   - The laptop webcam captures video.
   - CVZone detects whether a face is present.
   - A signal is sent to the Arduino Uno via serial communication.
   - Based on the signal:
     - The **Blue LED** lights up when a face is detected.
     - The **Red LED** lights up when no face is detected.

---

## Project Files
1. `main.py`:
   - Python script for face detection using CVZone.
   - Communicates with the Arduino Uno via serial port.

2. `Get_LED.ino`:
   - Arduino code to control the LEDs based on the signal received from Python.

---

## Setup Instructions

### 1. Hardware Setup
- Connect the **Blue LED** and **Red LED** to the Arduino Uno board:
  - **Blue LED**: Connect to pin `9` with a 220Ω resistor.
  - **Red LED**: Connect to pin `10` with a 220Ω resistor.
  - GND pin: Connect both LEDs to the ground of the Arduino Uno.

### 2. Software Setup

#### Python (PyCharm)
1. Install Python 3.x on your system.
2. Install required libraries:
   ```bash
   pip install cvzone
   pip install opencv-python
   pip install pyserial
   
3. Open main.py in PyCharm.
4. Update the serial port in the Python code (e.g., COM3 or /dev/ttyUSB0 depending on your system).

### Arduino IDE
1. Install the Arduino IDE.
2. Open Get_LED.ino in Arduino IDE.
3. Select the correct board (Arduino Uno) and port.
4. Upload the code to the Arduino board.

## How to Run
1. Connect the Arduino Uno board to your laptop via USB
2. Open and run main.py in PyCharm.
3. The webcam will start detecting faces.
4. Observe the LEDs:
   - **Blue LED ON**: Face detected.
   - **Red LED ON**: No face detected.

## Future Enhancements
- Add support for multiple face detection.
- Integrate a buzzer for additional feedback.
- Use IoT to send face detection status to a mobile app.

  
   



