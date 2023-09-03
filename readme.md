Fuel Economy Calculator
=======================

![A gas station](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Bp_station_zanesville_ohio.jpg/640px-Bp_station_zanesville_ohio.jpg)

A fuel economy calculator. This tool can be used to quickly calculate your fuel economy when filling up your tank.

Assignment
----------

Create program which does the following, in this order

1. Request the mileage at the last fill-up from the user
2. Request the current mileage from the user
3. Display the miles travelled to the user
4. Request amount of gas added to the tank on this fill-up
5. Display the miles per gallon for this fill-up to the user

Here's an example run of a correct program:

    Enter mileage from last fill-up: 1000
    Enter current mileage: 1300
    Miles traveled: 
    300
    How many gallons did you just put in the tank? 8
    You gas mileage for this fill-up was: 
    37.5

Here is a screen recording of a correct run:

![Demo of program running](demo.gif)

The text of your program need not be identical to the above, but the calculated values should be correct.

Testing
-------

I will be grading your program in part by passing a number of inputs to it and checking the output in an automated fashion. If you'd like to confirm that your program is working correctly, you may run these tests yourself by running `test.py`.

A successful run of test.py will produce output like the following:

```
Passed 5 out of 5 tests.
```

If tests are not passing, you will see something more like this:

```
Expected output 5 was not found for input (0, 10, 2)
Got: Enter mileage from last fill-up: Enter current mileage: Miles traveled: 
10
How many gallons did you just put in the tank? Your gas mileage for this fill-up was: 
0.2
```

The included `test.py` program assumes that Python 3 is in your path and is available as `python3`. If that assumption is not valid on your system, you may need to add Python to your path or modify the Python location in `test.py`.