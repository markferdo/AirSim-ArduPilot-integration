# Autonomouss Flying

We have two options to make drones autonomous. 

- Mission planner
- DroneKit API

In mission planner all are fixed and there is no logic. The drone flies to the given position no matter what. But in dronekit we have more control and since we are using Python, we can set logics. For example, if we have a sensor to avoid obstacles, we can set a logic if the sensor reading triggers an obstacle, we can avoid that while it is flying to the given path.
