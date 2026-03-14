import numpy as np


class FeatureExtractor:

    def extract(self, frame):

        lm = frame.landmarks

        # Eyebrow raise (distance between eyebrow and eye)
        eyebrow_raise = abs(lm[65][1] - lm[159][1])

        # Lip tension
        lip_tension = abs(lm[13][0] - lm[14][0])

        # Face symmetry
        symmetry_delta = abs(lm[33][0] - lm[263][0])

        # Blink rate approximation
        blink_rate = abs(lm[145][1] - lm[159][1])

        # Head nod movement
        head_nod = abs(lm[1][1] - lm[152][1])

        return {
            "eyebrow_raise": float(eyebrow_raise),
            "lip_tension": float(lip_tension),
            "head_nod_intensity": float(head_nod),
            "symmetry_delta": float(symmetry_delta),
            "blink_rate": float(blink_rate),
        }