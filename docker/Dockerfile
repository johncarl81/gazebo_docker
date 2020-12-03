FROM osrf/ros:melodic-desktop-full

ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

ENV DEBIAN_FRONTEND noninteractive
ENV WORKSPACE=/workspace

RUN apt-get -qq update && \
    apt-get -qq upgrade && \
    apt-get -qq install apt-utils build-essential vim python-catkin-tools

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install simulation
COPY ./gazebo $WORKSPACE

RUN source /opt/ros/melodic/setup.bash && \
    cd $WORKSPACE && \
    catkin_make && \
    catkin_make install

EXPOSE 11345

# Setup Entrypoint
COPY ./docker/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]
