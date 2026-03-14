from dataclasses import dataclass


@dataclass
class StressScore:
    score: float
    level: str
    label: str


class StressEstimator:

    def predict(self, features):

        # Strongly weighted stress score
        score = (
            features["eyebrow_raise"] * 20
            + features["lip_tension"] * 18
            + features["blink_rate"] * 15
            + features["symmetry_delta"] * 12
            + features["head_nod_intensity"] * 10
        )

        # Limit maximum score
        score = min(score, 10)

        # Stress classification ranges
        if score < 3:
            level = "calm"
            label = "Calm"

        elif score < 6:
            level = "mild"
            label = "Mild Stress"

        else:
            level = "high"
            label = "High Stress"

        return StressScore(score, level, label)