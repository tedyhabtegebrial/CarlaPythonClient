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
python client_example_left_and_right_cams.py -a -i -p 2000 -t 1


```


# Light Field

```

# Run carla simulator server
DISPLAY= ./CarlaUE4.sh /Game/Maps/Town01 -carla-server -world-port=2000  -benchmark -fps=4
# Run the client

python2.7 main_carla_lf.py -a -i -p 2000 --town_id=1 --data-path /data/teddy/Datasets/carla_temp
```