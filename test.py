from subprocess import run, PIPE

# Name of Python interpreter
# This can be replaced with a full path to Python 3
python_bin = "python3"

tests = [
    {"inputs": (0, 10, 2), "expects": ("10", "5")},
    {"inputs": (0, 1, 2), "expects": ("1", "0.5")},
    {"inputs": (1000, 1300, 8), "expects": ("300", "37.5")},
    {"inputs": (12345, 12567, 6), "expects": ("222", "37.0")},
    {"inputs": (12000, 12050, 5), "expects": ("50", "10")},
]

def run_test(test):
    stdin = '\n'.join(map(str, test["inputs"])).encode()
    
    stdout = run([python_bin, "gas.py"], input=stdin, stdout=PIPE).stdout
    
    for expect in test["expects"]:
        if expect.encode() not in stdout:
            print(f"Expected output {expect} was not found for input {test['inputs']}")
            print(f"Got: {stdout.decode()}")
            return False
    else:
        return True
        
results = [run_test(t) for t in tests]
 
print(f"Passed {sum(results)} out of {len(results)} tests.")