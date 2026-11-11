# omron_grasping_capabilities

This package specializes the generic [grasping_capabilities](../grasping_capabilities) runners for the Omron MoMa LD250 and TM12 arm. It owns the MoMa motion configuration, application launch files, manipulation plans, semantic interfaces, and providers that select the MoMa startup chain.

The generic runner implementations and base interfaces remain in `grasping_capabilities`. MoMa providers select the TM12 configuration and depend on the MoMa robot launch provider before starting the grasping motion server.

## Build

```bash
colcon build --packages-up-to omron_grasping_capabilities --symlink-install
```

## Run

```bash
source install/setup.bash
ros2 launch omron_grasping_capabilities system.launch.py filename:=manipulation_1.xml
```

The system launch starts Fabric, Capabilities2, and prompt tools. Robot and grasping stack startup is provided by the selected MoMa capability providers. Set `start_prompt_tools:=false` to disable prompt tools.# omron_grasping_capabilities
# omron_grasping_capabilities
