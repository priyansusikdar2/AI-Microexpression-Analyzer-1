class Dashboard:

    def __init__(self, verbose=False):
        self.verbose = verbose

    def render(self, features, stress):

        if not self.verbose:
            print(f"Stress: {stress.label} ({stress.score:.2f})")
            return

        print("\n------ Metrics ------")

        for k, v in features.items():
            print(f"{k}: {v:.3f}")

        print(f"Stress Score: {stress.score:.2f}")
        print(f"Stress Level: {stress.label}")