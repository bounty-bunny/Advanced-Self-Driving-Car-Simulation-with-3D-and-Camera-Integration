# camera_simulation.py
import cv2
import numpy as np

def simulate_camera():
    cap = cv2.VideoCapture(0)  # Use 0 for webcam or a video file path

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Display frame
        cv2.imshow('Camera', gray_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    simulate_camera()
