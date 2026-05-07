from dronekit import connect, VehicleMode
import time

print("Connecting to vehicle...")
vehicle = connect("127.0.0.1:14550", wait_ready=True)

print("Connected")
#disarm the vehicle
vehicle.armed = False


#set the default groundspeed to be used in movement commands
vehicle.groundspeed = 3.2

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True

while not vehicle.mode.name=='GUIDED' and not vehicle.armed:
    print(" Getting ready to take off ...")
    time.sleep(1)

print("Vehicle is armed")
print("Taking off!")
aTargetAltitude = 10
#vehicle.simple_takeoff(aTargetAltitude)
print("Landing...")
vehicle.mode = VehicleMode("LAND")
print("Landed")