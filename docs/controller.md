# Radiomaster TX16S

Install the joystick

~~~
sudo apt install joystick
~~~

- open the mavpoxy terminal
- mode stabilize
- mode load joystick


Run this to open the mavpoxy terminal
~~~
mavproxy.py --master=127.0.0.1:14550 --console --map
~~~

Make sure you are in the correct venv.

~~~
> source /home/mark/venv-ardupilot/bin/activate
> which mavproxy.py
/home/mark/venv-ardupilot/bin/mavproxy.py
> mavproxy.py --master=127.0.0.1:14550 --console --map
Connect 127.0.0.1:14550 source_system=255
Loaded module console
Loaded module map
Log Directory:
Telemetry log: mav.tlog
Waiting for heartbeat from 127.0.0.1:14550
MAV> Detected vehicle 1:1 on link 0
GUIDED> Received 1368 parameters (ftp)
Saved 1368 parameters to mav.parm
~~~

Load the joystick

~~~
GUIDED> module load joystick device=/dev/input/js0
GUIDED> pygame 2.6.1 (SDL 2.28.4, Python 3.12.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
MAVProxy.modules.mavproxy_joystick: Found joystick (OpenTX RM TX16S Joystick)
MAVProxy.modules.mavproxy_joystick: Using /home/mark/venv-ardupilot/lib/python3.12/site-packages/MAVProxy/modules/mavproxy_joystick/joysticks/T16S.yml ("OpenTX RM TX16S Joystick" matches pattern "*TX16*")
Loaded module joystick
~~~

Then configure the joysticks

~~~
STABILIZE> joystick set roll 0
STABILIZE> joystick set pitch 1
STABILIZE> joystick set throttle 2
STABILIZE> joystick set yaw 3
~~~

Then calibrate if needed
~~~
rc calibrate
STABILIZE> Usage: rc <set|channel|all|clear|status|guiin|guiout> <pwmvalue>
hit enter here when you done with calibration
STABILIZE> rc status
~~~

Then configure left right joysticks by moving fully up/down/left/right. and finnaly at the joystick should be in the neutral position then hit enter. Then check the status by running rc status

~~~
1: 1503
2: 1500
3: 1520
4: 1500
5: 1000
6: 1500
7: 1000
8: 0      (no override)
9: 0      (no override)
10: 0      (no override)
11: 0      (no override)
12: 0      (no override)
13: 0      (no override)
14: 0      (no override)
15: 0      (no override)
16: 0      (no override)
17: 0      (no override)
18: 0      (no override)
~~~

Note: 1-4 channel should be 1500 at when the joysticks at neutral position.


If you want to set configuration mannully run this,

~~~
rc <channel> <value>

STABILIZE> rc 5 1000
STABILIZE> rc 7 1000
~~~

To fly the drone follow below steps

~~~
STABILIZE> mode alt_hold  -> changeing the mode
ALT_HOLD> arm throttle -> arming the motors
ALT_HOLD> arm throttle force -> run this if arm throttle doesn't work
~~~

Note: arm throttle force this command disable the safety check. Not recommend for real drone

Now all done. You can control the drone with the controller.

## Controller Configuration

### Just an idea

Can set a switch to issue command, so we can switch between modes

Eample:

button/switch press -> mode guided (Script works in this mode)

button/switch press -> mode alt_hold (controller joysticks work in this mode)



# Links

https://ardupilot.org/mavproxy/docs/getting_started/forwarding.html
https://uavcoach.com/how-to-fly-a-quadcopter-guide/
https://docs.qgroundcontrol.com/Stable_V5.0/en/qgc-user-guide/




SEQURE H743 