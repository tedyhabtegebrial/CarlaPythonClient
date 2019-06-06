# CARLA driving simulator

Version 8.4.0

Important Note:
Under carla/sensors.py comment out the screen space to unreal engine conversion of camera poses.
This leads to a wrong rotation matrix with -1 determinant.

# Command to run Carla Engine on Server
```
./CarlaUE4.sh /Game/Maps/Town01 -carla-server -world-port=2000  -benchmark -fps=4
```

# Command to run Carla dataset recording script
```
python client_example.py -a -i
```


