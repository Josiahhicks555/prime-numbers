#looked up what range was and did 
#also found out % can be used as a value for a string

YourNumber = 0

false = False

if YourNumber > 1:

    for x in range(2, YourNumber):
        if (YourNumber % x) == 0:
            Run = True


if false:
    print(YourNumber, "is not a prime Number try a diffrent number")
else:
    print(YourNumber, "is a prime Number")
