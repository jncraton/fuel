import runpy
from functools import wraps


class Runner:
    def __init__(self, inputs):
        self.inputs = inputs
        self.output = ""

    def run(self):
        runpy.run_path(
            "fuel.py", {"print": self._print, "input": self._input}, "__main__"
        )
        return self.output

    @wraps(print)
    def _print(self, *values):
        self.output += ",".join(map(str, values)) + "\n"

    @wraps(input)
    def _input(self, prompt):
        testentry = str(self.inputs.pop(0))

        self.output += prompt + testentry + "\n"
        return testentry


tests = [
    {"inputs": (0, 10, 2), "expects": ("10", "5")},
    {"inputs": (0, 1, 2), "expects": ("1", "0.5")},
    {"inputs": (1000, 1300, 8), "expects": ("300", "37.5")},
    {"inputs": (12345, 12567, 6), "expects": ("222", "37.0")},
    {"inputs": (12000, 12050, 5), "expects": ("50", "10")},
]


def run_test(test):
    log = Runner(list(test["inputs"])).run()

    for expect in test["expects"]:
        if expect not in log:
            print(f"Expected output {expect} was not found in this test run:")
            print(log)
            return False
    else:
        return True


results = [run_test(t) for t in tests]

print(f"Passed {sum(results)} out of {len(results)} tests.")