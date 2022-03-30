class ClockTime:
    #  attributes of the class
    hours = 0
    minutes = 0
    seconds = 0

    def setHours(self, hr):  # set hour
        self.hours = hr

    def setMins(self, mins):  # set minutes
        self.minutes = mins

    def setSeconds(self, sec):  # set seconds
        self.seconds = sec

    def setTime(self, hr, mins, sec):  # set hour, minutes and seconds
        self.hours = hr
        self.minutes = mins
        self.seconds = sec

    def showTime(self):  # show the time in hours:minutes:seconds
        print("The set time is: " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))


newClock = ClockTime()

while True:
    try:
        hr = int(input("Enter hours in 24h format (value 0-23): "))
        if hr >= 0 and hr <= 23:  # make sure user types in the correct 24hr format for hours (0-23)
            break
        print("Incorrect Format!")
    except Exception as e:
        print(e)

while True:
    try:
        mins = int(input("Enter minutes in 24h format (value 0-59): "))
        if mins >= 0 and mins <= 59:  # make sure user types in the correct 24hr format for minutes (0-59)
            break
        print("Incorrect Format!")
    except Exception as e:
        print(e)

while True:
    try:
        sec = int(input("Enter seconds in 24h format (value 0-59): "))
        if sec >= 0 and sec <= 59:  # make sure user types in the correct 24hr format for seconds (0-59)
            break
        print("Incorrect Format!")
    except Exception as e:
        print(e)


newClock.setTime(hr, mins, sec)
newClock.showTime()
