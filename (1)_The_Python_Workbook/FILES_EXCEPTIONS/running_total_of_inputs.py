# Exercise 156: Sum a Collection of Numbers

def running_total():

    total = float(0)
    while True:

        try:
            num = input("\nNumber: ")
            if num == "":
                print("Program ended. Final total:", total)

                break
            total += float(num)
            print("Current Sum:", total)
        except ValueError:
            print("Not a number!")


running_total()
