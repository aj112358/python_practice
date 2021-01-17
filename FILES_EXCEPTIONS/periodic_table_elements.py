# Exercise 161: What's the Element?

def get_data():
    file = open("elements.txt", mode="r")
    lines = list(map(lambda x: x.strip().split(","), file.readlines()))

    num_to_symbol_name = {}
    for info in lines:
        num_to_symbol_name[int(info[0])] = tuple(info[1:])

    symbol_name_to_num = {}
    for key in num_to_symbol_name:
        symbol_name_to_num[num_to_symbol_name[key]] = key

    file.close()
    return num_to_symbol_name, symbol_name_to_num


# The main function.
def main():
    num_keys, symbol_keys = get_data()
    user_input = input("What do you want to know about?  ").capitalize()

    while user_input != "":
        try:
            x = int(user_input)
            print(num_keys[x])
        except ValueError:
            for key in symbol_keys:
                if key[0] == user_input or key[1] == user_input:
                    print(symbol_keys[key])
                    break
            else:
                print("No such element on periodic table.")
        except KeyError:
            print("No element with that atomic number.")
        user_input = input("\nWhat do you want to know about?  ").capitalize()


main()
