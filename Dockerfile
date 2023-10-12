#syntax=docker/dockerfile:1.4.0
# ARG CL_VERSION=v7.2.0
# ARG NETIF_VERSION=v1.4.1
ARG ROS2_VERSION=humble
# FROM ghcr.io/aica-technology/control-libraries:${CL_VERSION} as cl
# FROM ghcr.io/aica-technology/network-interfaces:${NETIF_VERSION} as netif
FROM ghcr.io/aica-technology/ros2-ws:${ROS2_VERSION} as base

# install dependencies
# COPY --from=cl / /
# COPY --from=netif / /
RUN sudo apt-get update && sudo apt-get install -y \
  libxinerama1 \
  libxcursor-dev \
  python3-tk \
  && sudo ldconfig \
  && sudo rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${HOME} && cd ${HOME} && git clone https://github.com/aica-technology/api.git

# RUN pip install aica-api
