class calc:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
    def get_input(self):
        while True:
            try:
                self.value1=float(input('Enter the first number:'))
                self.value2=float(input('Enter the second number:'))
                break # Add break to exit the loop after valid input
            except ValueError:
                print("Please enter valid input")
    def add(self):
        return self.value1 + self.value2
    def sub(self):
        return self.value1 - self.value2
    def mul(self):
        return self.value1 * self.value2
    def div(self):
        try:
            return self.value1 / self.value2
        except ZeroDivisionError:
            print("Can't divide by Zero")
            return None # Return None in case of division by zero
        


cal =calc()
while True:
    print('select an option')
    print('1 for Addition')
    print('2 for Subtraction')
    print('3 for Multiplication')
    print('4 for Division')
    print('5 for Exit') # Added exit option


    op=input('Enter your choice:')
    if op in ('1','2','3','4'):
        cal.get_input()
        if op=='1':
            result=cal.add()
            print("Result",result)
        elif op=='2':
            result=cal.sub()
            print("Result",result)
        elif op=='3':
            result=cal.mul()
            print("Result",result)
        elif op=='4':
            result=cal.div() # Corrected typo from reuult to result and mul to div
            if result is not None: # Check if division was successful
                print("Result",result)
    elif op == '5': # Added exit condition
        print("Exiting calculator.")
        break
    else:
        print('Enter a valid option')        