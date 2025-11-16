# train Ticket System Info 
seat_type = input("Enter Seat Type (Sleeper/AC/General/Luxury) ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, Beds Available")
    case "ac":
        print("AC - Air Conditioned")
    case "general":
        print("General - No Reservation Required")
    case "luxury":
        print("Luxury Seats and food")
    case _:
        print("INvalid Typo")
    