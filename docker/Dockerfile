FROM ros:humble-ros-base

ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

ENV DEBIAN_FRONTEND noninteractive
ENV WORKSPACE=/workspace

RUN apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get -qq install apt-utils build-essential vim

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install Dependencies
RUN apt-get -qq install ros-humble-desktop python3-dev python3-opencv python3-wxgtk4.0 python3-pip python3-matplotlib python3-pygame python3-lxml python3-yaml gazebo libgazebo-dev ros-humble-gazebo-ros-pkgs python-is-python3

# Clear apt cache to save on space
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p $WORKSPACE/gazebo

COPY ./gazebo $WORKSPACE/gazebo

RUN apt-get -qq install git

RUN git clone https://github.com/osrf/gazebo_models $WORKSPACE/models

RUN source /opt/ros/humble/setup.bash && \
    cd $WORKSPACE/gazebo && \
    colcon build

# Setup Entrypoint
COPY ./docker/entrypoint.sh /
COPY ./docker/entrypoint.py /

ENTRYPOINT ["/entrypoint.py"]
