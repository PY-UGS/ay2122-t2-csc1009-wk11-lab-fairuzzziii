class Calculator:  # constructor
    def __init__(self, input1, input2):
        self.input1 = 0
        self.input2 = 0

    def adder(self):  # add values together
        return self.input1 + self.input2

    def subtractor(self):  # subtract values
        return self.input1 - self.input2

    def multiplier(self):  # multiply values
        return self.input1 * self.input2

    def divider(self):  # divide values
        return self.input1 / self.input2

    def clear(self):  # clear values
        self.input1 = 0
        self.input2 = 0

#  ask for input and store inside x and y
x = float(input("Enter 1st value: "))
y = float(input("Enter 2nd value: "))
c1 = Calculator(x, y)

print("Add: ", c1.adder())
print("Subtract: ", c1.subtractor())
print("Multiply: ", c1.multiplier())
print("Divide: ", c1.divider())

# check if numbers are cleared
print("Numbers before clear function are: " + str(c1.input1) + " and " + str(c1.input2))
c1.clear()
print("Numbers after clear function: " + str(c1.input1) + " and " + str(c1.input2))


