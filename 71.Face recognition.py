#Face_recognition

import face_recognition
image = face_recognition.load_image_file("C:\Users\Deadly pursuit\Downloads\SHAREit\iPhone 7 Plus\Documents\Selfies.jpg")
face_locations = face_recognition.face_locations(image)