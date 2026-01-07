def phoneNumberSearch():

    numDict = {
        "amal": 111111111,
        "mohammed": 222222222,
        "khalid": 333333333,
        "abdullah": 444444444,
        "rawan": 555555555,
        "faisal": 666666666,
        "layla": 777777777
    }

    while True:
        user_inp = input("Enter your number (or type 'q' to exit): ")

        if user_inp.lower() == "q":
            print("Program stopped.")
            break

        if not user_inp.isdigit():
            print("Please enter a valid number.")
            continue

        user_num = int(user_inp)
        found = False

        for key, value in numDict.items():
            if value == user_num:
                print(f"The user of this number is {key}")
                found = True
                break

        if not found:
            print("Sorry, the number is not found")

phoneNumberSearch()
