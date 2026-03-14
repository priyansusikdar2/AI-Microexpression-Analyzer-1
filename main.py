import argparse
import pathlib
from typing import Dict, Tuple

import cv2
import numpy as np

import data_logger
from dashboard import Dashboard
from face_mesh_module import iter_landmarks_from_camera, LandmarkFrame
from feature_engineering import FeatureExtractor
from stress_model import StressEstimator, StressScore

COLORS = {
    "calm": (0, 200, 0),
    "mild": (0, 200, 255),
    "high": (0, 0, 230),
}

WHITE = (255, 255, 255)
GRAY = (60, 60, 60)

WINDOW = "AI Micro-Expression Analyzer"
PANEL_W = 320


def draw_landmarks(image, landmarks):
    h, w = image.shape[:2]
    for lm in landmarks:
        x, y = int(lm[0] * w), int(lm[1] * h)
        cv2.circle(image, (x, y), 1, (200, 220, 200), -1)


def render_frame(frame, features, stress):
    image = frame.image.copy()
    draw_landmarks(image, frame.landmarks)

    color = COLORS.get(stress.level, WHITE)

    cv2.rectangle(
        image,
        (0, 0),
        (image.shape[1] - 1, image.shape[0] - 1),
        color,
        3,
    )

    panel = np.zeros((image.shape[0], PANEL_W, 3), dtype=np.uint8)

    y = 40
    for k, v in features.items():
        cv2.putText(
            panel,
            f"{k}: {v:.3f}",
            (10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            WHITE,
            1,
        )
        y += 30

    cv2.putText(
        panel,
        f"Stress: {stress.label} ({stress.score:.2f})",
        (10, y + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2,
    )

    return np.hstack([image, panel])


def run(camera_index, log_path, display, verbose):

    extractor = FeatureExtractor()
    estimator = StressEstimator()

    fields = [
        "eyebrow_raise",
        "lip_tension",
        "head_nod_intensity",
        "symmetry_delta",
        "blink_rate",
        "stress_score",
    ]

    dashboard = Dashboard(verbose)

    with data_logger.DataLogger(log_path, fieldnames=fields) as logger:

        for frame in iter_landmarks_from_camera(camera_index):

            features = extractor.extract(frame)

            stress = estimator.predict(features)

            metrics = {**features, "stress_score": stress.score}

            dashboard.render(features, stress)

            logger.log(metrics)

            if display and frame.image is not None:
                canvas = render_frame(frame, features, stress)
                cv2.imshow(WINDOW, canvas)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    cv2.destroyAllWindows()


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--camera-index", type=int, default=0)

    parser.add_argument(
        "--log-path",
        type=pathlib.Path,
        default=pathlib.Path("logs/session.csv"),
    )

    parser.add_argument("--no-display", action="store_true")

    parser.add_argument("--verbose", action="store_true")

    return parser.parse_args()


def main():
    args = parse_args()

    run(
        camera_index=args.camera_index,
        log_path=args.log_path,
        display=not args.no_display,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()