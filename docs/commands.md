1. first load the unreal engine
2. click the play 
3. error window will popup. forcequit or wait. dont do anything
4. navigate to /home/mark/ardupilot/ArduCopter and type this sim_vehicle.py -v ArduCopter -f airsim-copter --console --map and enter.
5. Now unreal drone should be fine
6. give below commands froms the arduCopter terminal

STABILIZE> mode guided
STABILIZE> mode guided
GUIDED> GUIDED>
GUIDED> arm throttle force
GUIDED> arm throttle force
GUIDED> takeoff 10i
GUIDED> Take Off started

GUIDED> velocity 2 0 0
GUIDED> x:2.000000, y:0.000000, z:0.000000

GUIDED> takeoff 20
GUIDED> Take Off started

GUIDED> reposition 0 0 20
GUIDED> Unknown command 'reposition 0 0 20'

GUIDED> guided 0 0 20
GUIDED> Guided (0.0, 0.0) 20.0 frame 3

GUIDED> guided 0 0 40
GUIDED> Guided (0.0, 0.0) 40.0 frame 3
