#! /usr/bin/env python3
import argparse
import subprocess
import signal

def run_simulation(args):
    processes = []
    # Start Gazebo
    processes.append(subprocess.Popen("/entrypoint.sh ros2 launch gazebo_ros gazebo.launch.py gui:={} world:=worlds/empty_sky.world".format("{}".format(args.gui).lower()), shell=True))

    def shutdown(signum, frame):
        print('Exiting...')
        for p in processes:
            p.kill()
        exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.pause()

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_args():
    parser = argparse.ArgumentParser(description='Gazebo simulation')

    parser.add_argument(
        '--gui',
        type=str2bool,
        nargs='?',
        const=True,
        default=True)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    run_simulation(args)

if __name__ == '__main__':
    main()
