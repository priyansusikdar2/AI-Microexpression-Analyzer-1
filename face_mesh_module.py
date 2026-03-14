import cv2
import mediapipe as mp
import numpy as np
import time

from dataclasses import dataclass


@dataclass
class LandmarkFrame:
    timestamp: float
    landmarks: np.ndarray
    image: np.ndarray


mp_face_mesh = mp.solutions.face_mesh


def iter_landmarks_from_camera(camera_index=0):

    cap = cv2.VideoCapture(camera_index)

    with mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        refine_landmarks=True,
    ) as face_mesh:

        while True:

            success, frame = cap.read()

            if not success:
                break

            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            result = face_mesh.process(image_rgb)

            if result.multi_face_landmarks:

                face = result.multi_face_landmarks[0]

                coords = []

                for lm in face.landmark:
                    coords.append([lm.x, lm.y, lm.z])

                coords = np.array(coords)

                yield LandmarkFrame(time.time(), coords, frame)