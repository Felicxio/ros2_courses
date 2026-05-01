# 🐢 Turtlesim Catch Them All (ROS 2)

## 🎥 Demo

[catch_them_all.webm](https://github.com/user-attachments/assets/ff7da2ef-d1f8-451c-80fa-379d87463b98)



---

## 👨‍💻 Author

**João Victor Assunção Pereira**
📧 [jvictor3651@gmail.com](mailto:jvictor3651@gmail.com)
🔗 https://www.linkedin.com/in/jo%C3%A3o-victor-assun%C3%A7%C3%A3o-pereira-88a461211/

---

## 📌 Overview

This project is a complete ROS 2 application built using the **Turtlesim** simulator, where a main turtle autonomously hunts and “catches” other turtles spawned dynamically in the environment.

The system demonstrates core ROS 2 concepts such as:

* Distributed node architecture
* Topic-based communication
* Service-based interaction
* Custom message and service definitions
* Real-time control loops

---

## 🎯 Objective

Develop an autonomous agent capable of:

* Tracking multiple targets
* Selecting a target dynamically
* Navigating toward it using control logic
* Removing targets from the environment upon capture

---

## 🏗️ System Architecture

The system is composed of two main nodes:

### 🔹 `turtle_spawner`

Responsible for managing the simulation environment.

**Responsibilities:**

* Spawn turtles at random positions
* Maintain a list of alive turtles
* Provide a service to remove turtles

**Publishes:**

* `/alive_turtles` (`TurtleArray`)

**Services:**

* `catch_turtle` (custom service)

---

### 🔹 `turtle_controller`

Responsible for controlling the main turtle (`turtle1`).

**Responsibilities:**

* Subscribe to turtle positions
* Select a target (closest or first)
* Navigate toward the target
* Request removal when target is reached

**Subscribes to:**

* `/turtle1/pose`
* `/alive_turtles`

**Publishes:**

* `/turtle1/cmd_vel`

**Calls:**

* `catch_turtle` service

---

## 🔄 System Flow

1. The spawner node creates turtles randomly in the environment
2. Alive turtles are published via `/alive_turtles`
3. The controller selects a target:

   * Closest turtle (default)
   * Or first in the list
4. The controller computes:

   * Distance to target
   * Orientation error
5. The turtle moves using proportional control
6. When close enough:

   * A service request is sent to remove the turtle
7. The spawner removes the turtle and updates the list

---

## 📡 ROS Graph

The communication between nodes is illustrated below:

![ROS Graph](./rosgraph.png)

---

## ⚙️ Control Strategy

The controller uses a **proportional control approach**:

* Linear velocity proportional to distance
* Angular velocity proportional to orientation error

Angle normalization is applied to ensure efficient rotation and avoid unnecessary spins.

---

## 🧩 Custom Interfaces

The project includes custom ROS 2 interfaces:

### Messages

* `Turtle.msg`
* `TurtleArray.msg`

### Services

* `CatchTurtle.srv`

These abstractions allow clean communication between nodes and better scalability.

---

## ⚙️ Configuration

Parameters are defined via YAML:

```yaml
/turtle_controller:
  ros__parameters:
    catch_closest_turtle: True

/turtle_spawner:
  ros__parameters:
    turtle_name_prefix: "my_turtle"
    spawn_frequency: 2.0
```

---

## 🚀 Launch

To run the full system:

```bash
ros2 launch my_robot_bringup turtlesim_catch_them_all.launch.xml
```

---

## 🧠 Key Concepts Demonstrated

* ROS 2 Node Design
* Publisher / Subscriber
* Service Client / Server
* Asynchronous programming
* Real-time control loop
* System modularization

---

## 🔧 Possible Improvements

* Add velocity saturation to avoid oscillations
* Introduce PID control instead of proportional-only
* Limit number of spawned turtles
* Add visualization of target tracking
* Implement smarter path planning

---

## 📚 Learning Outcome

This project consolidates the transition from isolated ROS concepts to a **complete distributed robotic system**, emphasizing design, modularity, and real-time interaction.
