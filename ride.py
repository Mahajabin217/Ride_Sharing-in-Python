from datetime import datetime
from vehicle import Car, Bike

class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"Company Name {self.company_name} With Riders: {len(self.riders)} and Drivers: {len(self.drivers)}"
        
class Ride:
    def __init__(self, start_location, end_location, vehicle) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        self.vehicle = vehicle

    def set_driver(self,driver):
        self.driver = driver 

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f"Ride Details: Started {self.start_location} to {self.end_location}"
    
# Ride_rqst a ki hoy:
# dhaka thke sylhet jabe 
# reqst krbe = rider 
# se jabe = end_loaction

class Ride_request:
    def __init__(self,rider,end_location) -> None:
        self.end_location = end_location


class Ride_matching:
    def __init__(self,drivers):
        self.available_drivers = drivers 

    def find_driver(self,ride_request, vehicle_type):
        if len(self.available_drivers) > 0:
            print("-------- Looking for Drivers -------")
            driver = self.available_drivers[0]

            if vehicle_type == 'car':
                vehicle = Car("Car", "AJf653", 30)
            elif vehicle_type == 'bike':
                vehicle = Bike("Bike", "17643Hh", 50)
            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
            
            driver.accept_ride(ride)
            return ride 

        
        


    

        