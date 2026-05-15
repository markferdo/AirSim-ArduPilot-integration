from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil, mavwp
import time, math

def goto_position_target_local_ned(north, east, down):
    """
    Send SET_POSITION_TARGET_LOCAL_NED command to request the vehicle fly to a specified
    location in the North, East, Down frame.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        north, east, down,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    # send command to vehicle
    vehicle.send_mavlink(msg)

def get_location_metres(original_location, dNorth, dEast):
    """
    Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the 
    specified `original_location`. The returned LocationGlobal has the same `alt` value
    as `original_location`.

    The function is useful when you want to move the vehicle around specifying locations relative to 
    the current vehicle position.

    The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.

    For more information see:
    http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
    """
    earth_radius = 6378137.0 #Radius of "spherical" earth
    #Coordinate offsets in radians
    dLat = dNorth/earth_radius
    dLon = dEast/(earth_radius*math.cos(math.pi*original_location.lat/180))

    #New position in decimal degrees
    newlat = original_location.lat + (dLat * 180/math.pi)
    newlon = original_location.lon + (dLon * 180/math.pi)
    if type(original_location) is LocationGlobal:
        targetlocation=LocationGlobal(newlat, newlon,original_location.alt)
    elif type(original_location) is LocationGlobalRelative:
        targetlocation=LocationGlobalRelative(newlat, newlon,original_location.alt)
    else:
        raise Exception("Invalid Location object passed")
        
    return targetlocation;

print("Connecting to vehicle...")
vehicle = connect("127.0.0.1:14550", wait_ready=True)

print("Connected")
#disarm the vehicle
vehicle.armed = False


#groundspeed 
vehicle.groundspeed = 5

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True

while not vehicle.mode.name=='GUIDED' and not vehicle.armed:
    print(" Getting ready to take off ...")
    time.sleep(1)

print("Vehicle is armed")
print("Taking off!")
aTargetAltitude = 15
vehicle.simple_takeoff(aTargetAltitude)
time.sleep(10)

print("North 40m, East 50m")
#goto_position_target_local_ned(0,50,-10)
# ** note: This only work for the first time. If you try to do run this script again it wont move to the right since its already at the target position. So it will takeoff and land.
#time.sleep(10)

current_location = vehicle.location.global_relative_frame
target_location = get_location_metres(current_location, 40, 50)
vehicle.simple_goto(target_location)
time.sleep(15)

print("North -40m, East -50m")
current_location = vehicle.location.global_relative_frame
target_location = get_location_metres(current_location, -40, -50)
vehicle.simple_goto(target_location)
time.sleep(15);
print("Returned to original position")

print("Landing...")
vehicle.mode = VehicleMode("LAND")

