# Basic General Purpose AMR

This repository provides a comprehensive guide for simulating a **4-wheeled robot** in Webots, equipped with GPS, IMU, LiDAR, and a 2-DOF camera. The robot is capable of detecting objects using computer vision, avoiding obstacles, and navigating autonomously.

## Live Interaction

Experience live interaction with the robot through the following link:

[CLOUD INTERACTION_WEBOTS](https://webots.cloud/ScKiz83?upload=webots)


## Demo Videos

Explore the capabilities of the robot through the demo videos below:

| Camera Test | Object Detection | LiDAR in Action |
|-------------|------------------|-----------------|
| [![YouTube Video](https://img.youtube.com/vi/rqTKV85uOz4/0.jpg)](https://youtu.be/rqTKV85uOz4) | [![YouTube Video](https://img.youtube.com/vi/wl0mYWiO184/0.jpg)](https://youtu.be/wl0mYWiO184) | [![YouTube Video](https://img.youtube.com/vi/9qBLSOo2feE/0.jpg)](https://youtu.be/9qBLSOo2feE) |

![GPBot](https://github.com/Mummanajagadeesh/gpbot-w/blob/b1c7eff5d086191858d81d4e660062cbd1c35c6b/gpbot.png?raw=true)

## Robot Overview

This robot features:
- **4-Wheeled Mobility**: The robot is designed for efficient navigation in various environments.
- **Sensors**:
  - **GPS**: For global positioning and navigation.
  - **IMU (Inertial Measurement Unit)**: For monitoring orientation and movement.
  - **LiDAR**: For mapping the environment and detecting obstacles.
  - **2-DOF Camera**: Equipped with linear and rotary actuators for versatile camera movement and object detection capabilities.
  
The robot operates autonomously without relying on complex algorithms, utilizing basic control mechanisms.

## Controls

The controls for the robot are displayed below:

### Movement Controls

| Key    | Action             |
|--------|--------------------|
| ↑      | Move forward        |
| ↓      | Move backward       |
| ←      | Turn left           |
| →      | Turn right          |

### Camera Controls

| Key    | Action                         |
|--------|--------------------------------|
| W      | Move the link upward           |
| S      | Move the link downward         |
| A      | Rotate the link holding camera in ACW |
| D      | Rotate the link holding camera in CW |

### Combined Controls

#### Movement
```plaintext
      ┌───┐┌───┐┌───┐
      │ ← ││ ↑ ││ → │
      │ ← │└───┘│ → │
      │ ← │┌───┐│ → │
      │ ← ││ ↓ ││ → │
      └───┘└───┘└───┘
```

#### Camera
```plaintext
      ┌───┐
      │ W │ 
      └───┘
    ┌───┐┌───┐┌───┐
    │ A ││ S ││ D │
    └───┘└───┘└───┘
```

## Implementation Details

The robot is constructed entirely from scratch, integrating various sensors to enhance its functionality. The design allows it to detect objects and navigate autonomously without the implementation of complex algorithms.

- **Camera Functionality**: The 2-DOF camera enables the robot to capture images and analyze the environment for object detection.
- **Object Detection**: Utilizing computer vision techniques, the robot can identify and respond to obstacles in its path.

## Installation and Usage

### Requirements
- **Webots**: Ensure you have Webots installed to run the simulation. You can download it from [here](https://cyberbotics.com/).

### Steps to Run
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Mummanajagadeesh/gpbot-w.git
   cd webots-self-guide
   ```
2. Open Webots and load the relevant world file associated with the robot.
3. Start the simulation to observe the robot's functionalities in action.

## Future Enhancements
- **Algorithm Integration**: Explore the integration of path planning and control algorithms to enhance navigation capabilities.
- **Advanced Object Recognition**: Implement machine learning techniques for more sophisticated object detection and recognition.
- **Multi-Robot Coordination**: Develop strategies for coordinating multiple robots in a shared environment.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
