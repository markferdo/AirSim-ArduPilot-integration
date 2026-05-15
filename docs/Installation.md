## Issues

### Airsim Installation issues

#### For those who using ubuntu 24

Warning: Try to use required version. Otherwise it going to be pain in the ass

Things to do

- Fix the GCC version
- 


Airsim is not designed for that version. So I had to edit ./setup.sh and ./build.sh according to that.

./setup.sh


~~~
Reading package lists... Done

Building dependency tree... Done

Reading state information... Done

E: Unable to locate package vulkan-utils

~~~

Find the line that says: vulkan-utils.

Change it to: vulkan-tools.


./build.sh

Find sudo apt-get-install -y clang-8 .............. line and change it to this.

sudo apt-get install -y clang-18 clang++-18 libc++-18-dev libc++abi-18-dev

Then I got this error

~~~





52 warnings generated.
70 warnings generated.
70 warnings generated.
49 warnings generated.
52 warnings generated.
49 warnings generated.
[ 82%] Linking CXX static library ../output/lib/libAirLib.a
[ 82%] Built target AirLib
make: *** [Makefile:136: all] Error 2
 ~/AirSim  main !2

~~~

Go to here AirSim/cmake/cmake-modules and edit this file CommonSetup.cmake

Find this line 

~~~

set(CXX_EXP_LIB "-L${LLVM_LIBRARY_DIRS} -lc++fs -ferror-limit=10")

~~~

Then remove -lc++fs . Thats it

~~~
[1350/1825] Compile Module.CurveEditorTools.cpp

[1351/1825] Compile ExampleDeviceProfileSelectorModule.cpp

11 warnings generated.

[1352/1825] Link (lld) libUE4Editor-AirSim.so

ld.lld: error: undefined symbol: __isoc23_strtol

>>> referenced by server.cc

>>>               server.cc.o:(clmdep_asio::detail::socket_ops::inet_pton(int, char const*, void*, unsigned long*, std::__1::error_code&)) in archive /home/mark/AirSim/Unreal/Environments/Blocks/Plugins/AirSim/Source/AirLib/deps/rpclib/lib/librpc.a

clang++: error: linker command failed with exit code 1 (use -v to see invocation)

[1353/1825] Compile Module.GammaUI.cpp

[1354/1825] Compile Module.SoundFields.cpp

[1355/1825] Compile Module.ChaosClothEditor.cpp

[1356/1825] Compile Module.CurveEditorTools.gen.cpp

[1357/1825] Compile Module.NullDrv.cpp

[1358/1825] Compile Module.CameraShakePreview
~~~

Above error: This is the glibc version mismatch. Since I'm using higher version than required, it looked for older standard.

solution: 

~~~
cd ~/AirSim
./clean.sh
./setup.sh //rebuild it
./build.sh

~~~

another error

~~~
[1819/1825] Link (lld) libUE4Editor-TextureFormatUncompressed.so
[1820/1825] Link (lld) libUE4Editor-Advertising.so
[1821/1825] Link (lld) libUE4Editor-PythonScriptPluginPreload.so
[1822/1825] Copy AgentInterface.dll
[1823/1825] Link (lld) libUE4Editor-TraceInsights.so
 ~/AirSim/Unr/E/Blocks  main !3 ?2                                  6 err  1h 3m 1s  19:13:53
~~~

~~~

3 warnings generated.
11 warnings generated.
[4/6] Link (lld) libUE4Editor-AirSim.so
ld.lld: error: undefined symbol: __isoc23_strtol
>>> referenced by server.cc
>>>               server.cc.o:(clmdep_asio::detail::socket_ops::inet_pton(int, char const*, void*, unsigned long*, std::__1::error_code&)) in archive /home/mark/AirSim/Unreal/Environments/Blocks/Plugins/AirSim/Source/AirLib/deps/rpclib/lib/librpc.a
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
 ~/AirSim/Unr/E/Blocks  main !3 ?2

~~~


I ran into a lot of errors and spent 3-4 days trying to get it right with AI. I followed so many different instructions, but Gemini is definitely better for this than ChatGPT.

## Running the project

~/UnrealEngine/Engine/Binaries/Linux/UE4Editor Blocks.uproject


from the airsim/..../blocks folder
> ~/UnrealEngine/Engine/Build/BatchFiles/Linux/Build.sh BlocksEditor Linux Development -Project="/home/mark/AirSim/Unreal/Environments/Blocks/Blocks.uproject"

## Running the ardupilot


1. first load the unreal engine
2. click the play 
3. error window will popup. forcequit or wait. dont do anything
4. navigate to /home/mark/ardupilot/ArduCopter and type this sim_vehicle.py -v ArduCopter -f airsim-copter --console --map and enter.
5. Now unreal drone should be fine

## Intalling airsim (pip install thing)

if you get this

41d69080176539b76b10/airsim/utils.py", line 1, in <module>
          import numpy as np #pip install numpy
          ^^^^^^^^^^^^^^^^^^
      ModuleNotFoundError: No module named 'numpy'               [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.                                                       │ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.


~~~
pip install --upgrade pip setuptools wheel
pip install numpy
pip install backports.ssl_match_hostname
pip install msgpack-rpc-python
pip install --no-build-isolation airsim
~~~
