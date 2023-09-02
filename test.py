from subprocess import run, PIPE

tests = [
    {"inputs": (0, 10, 2), "expects": ("10", "5")},
    {"inputs": (0, 1, 2), "expects": ("1", "0.5")},
    {"inputs": (1000, 1300, 8), "expects": ("300", "37.5")},
    {"inputs": (12345, 12567, 6), "expects": ("222", "37.0")},
    {"inputs": (12345, 12567, 6), "expects": ("222", "37.0")},
]

# Generate additional tests
for i in range(10 - len(tests)):
    start = randint(0, 100000)
    end = randint(100000, 105000)
    gallons = randint(1, 50)
    miles = end - start
    tests.append({
        "inputs": (start, end, gallons),
        "expects": (str(miles), str(miles / gallons)),
    })

print(tests)

passed = 0
failed = 0

for test in tests:
    stdin = '\n'.join(map(str, test["inputs"])).encode()
    
    stdout = run(["python3", "gas.py"], input=stdin, stdout=PIPE).stdout
    
    for expect in test["expects"]:
        if expect.encode() in stdout:
            passed += 1
        else:
            failed += 1
            print(f"Expected output {expect} was not found for input {test['inputs']}")
            print(f"Got: {stdout.decode()}")
 
print(f"Passed {passed} out of {passed+failed} tests.")