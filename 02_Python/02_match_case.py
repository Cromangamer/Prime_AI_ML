color = str(input("Enter your favorite color: "))

match color:
    case "red":
        print("Your favorite color is red.")
    case "blue":
        print("Your favorite color is blue.")
    case "green":
        print("Your favorite color is green.")
    case _: # this is the default case, it will be executed if none of the above cases match
        print("Your favorite color is not red, blue, or green.")
    