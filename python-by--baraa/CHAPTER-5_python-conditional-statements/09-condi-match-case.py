# This if elif problem is solve by match case

country = "USA"

if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("GE")
else:
    print("Unknown Country")


# Easy to Read and Write and Organized
# can be used only for matching value

match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("EG")
    case _:
        print("Unknown Country")