#syntax=docker/dockerfile:1.4.0
ARG ROS2_VERSION=humble
FROM ghcr.io/aica-technology/ros2-ws:${ROS2_VERSION} as base

# install dependencies
RUN sudo apt-get update && sudo apt-get install -y \
  python3-tk \
  && sudo ldconfig \
  && sudo rm -rf /var/lib/apt/lists/*

RUN pip install aica-api
