# building the smart thermostat alert system 
device_status = "active"
temperature = 38 

if device_status == "active":
    if temperature > 35:
        print("High Temperature Alert")
    else:
        print("Temperature is Normal")
else:
    print(f"Device is Offline")
