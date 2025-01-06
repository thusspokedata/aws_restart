# List of dictionaries to store flight data
flight_data = [
    {
        "Aircraft Name": "Flight A123",
        "Latitude": 37.7749,
        "Longitude": -122.4194,
        "Speed": 500,
        "Heading": 90,
        "Altitude": 35000,
        "Status": "In Flight",
    },
    {
        "Aircraft Name": "Flight B456",
        "Latitude": 40.7128,
        "Longitude": -74.0060,
        "Speed": 300,
        "Heading": 180,
        "Altitude": 0,
        "Status": "Landed",
    },
    {
        "Aircraft Name": "Flight C789",
        "Latitude": 51.5074,
        "Longitude": -0.1278,
        "Speed": 450,
        "Heading": 270,
        "Altitude": 28000,
        "Status": "Delayed",
    },
]

# Function to display flight data
def display_flight_data(flights, filter_status=None):
    """
    Displays flight data. If filter_status is provided, only displays flights matching that status.
    """
    for flight in flights:
        if filter_status and flight["Status"] != filter_status:
            continue
        print(f"Aircraft Name: {flight['Aircraft Name']}")
        print(f"  Latitude: {flight['Latitude']}")
        print(f"  Longitude: {flight['Longitude']}")
        print(f"  Speed: {flight['Speed']} knots")
        print(f"  Heading: {flight['Heading']}°")
        print(f"  Altitude: {flight['Altitude']} ft")
        print(f"  Status: {flight['Status']}")
        print("-" * 30)

# Function to add a new aircraft
def add_aircraft(flights):
    name = input("Enter Aircraft Name: ")
    latitude = float(input("Enter Latitude: "))
    longitude = float(input("Enter Longitude: "))
    speed = int(input("Enter Speed (knots): "))
    heading = int(input("Enter Heading (°): "))
    altitude = int(input("Enter Altitude (ft): "))
    status = input("Enter Status (e.g., 'In Flight', 'Landed', 'Delayed'): ")
    flights.append({
        "Aircraft Name": name,
        "Latitude": latitude,
        "Longitude": longitude,
        "Speed": speed,
        "Heading": heading,
        "Altitude": altitude,
        "Status": status,
    })
    print("Aircraft added successfully!")

# Function to update the status of an aircraft
def update_aircraft_status(flights):
    name = input("Enter the Aircraft Name to update: ")
    for flight in flights:
        if flight["Aircraft Name"] == name:
            new_status = input(f"Enter new status for {name} (current: {flight['Status']}): ")
            flight["Status"] = new_status
            print(f"Status of {name} updated to {new_status}.")
            return
    print(f"Aircraft {name} not found.")

# Main program
while True:
    print("\nFlight Data System")
    print("1. Display all flights")
    print("2. Display flights by status")
    print("3. Add a new aircraft")
    print("4. Update aircraft status")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_flight_data(flight_data)
    elif choice == "2":
        status = input("Enter status to filter by (e.g., 'In Flight', 'Landed', 'Delayed'): ")
        display_flight_data(flight_data, filter_status=status)
    elif choice == "3":
        add_aircraft(flight_data)
    elif choice == "4":
        update_aircraft_status(flight_data)
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
