# create a class to hold methods we want to test

class CodeMethods:

    # Define a method that returns True if 1 number is divisible by another number
    def divisible(self, numer, denom):
        return numer % denom == 0

    #define a method that returns if the numbers given are positive
    def positive(self, *args):
        #loop round the args given
        for arg in args:
            if arg < 0:
                return f"{False}, one of these numbers is negative"
        return True
