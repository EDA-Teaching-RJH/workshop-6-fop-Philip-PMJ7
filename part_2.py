rover_status = {
    "Battery":100, "Heater":"Off", "Camera":"Standby"
    }

print(rover_status["Battery"])


rover_status["Battery"] = 85
rover_status["Heater"] = "On"  # Change marks
rover_status.update({"Speed": 5})
print(rover_status)

mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": False},
    {"Site": "Dune B", "Radiation": "High", "Water": True}
    ]

for mission in mission_log:
    print("Site ", mission["Site"], " has ", mission["Radiation"], " radiation.")
