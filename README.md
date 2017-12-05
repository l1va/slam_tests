# slam_tests
Testing different slam libraries. 

<i>Note! Do not forget to add your bags inside slam_bags pkg.</i>

1. <b>rtabmap_test</b>. 
Tried to make slam by mono camera and odometry, 
but rtabmap can not work with mono camera. Only stereo or RGB-D.
[Rtabmap install](https://github.com/introlab/rtabmap/wiki/Installation)

> How to run demo:
> - run "roslaunch rtabmap_test rtabmap.launch" in terminal.

2. <b>orb_slam2_test</b>. 
Goes good but i have bag with fast rotations and 
it did not work fully even when i run bag with "-r 0.7" that means ~1.4 times slower. 
It was default settings of camera. Be careful with path to vocabulary in launch!
[ORB_SLAM2 install](https://github.com/l1va/ORB_SLAM2)

> How to run demo:
> - run "<i>roslaunch orb_slam2_test orb_slam.launch</i>" in terminal, and after it 
will start run "<i>roslaunch orb_slam_test bag.launch</i>" to launch bag file. 
> - When you stop ORB the 
KeyFrameTrajectrory.txt file will be saved in the ~/.ros directory (by default). 
[The file format](https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats): 
"<i>timestamp tx ty tz qx qy qz qw</i>". It means timestamp, 3 floats - position, 
4 floats - orientation.
> - if you need visualize just xyz points, run 
"<i>python <project_path>/orb_slam2_test/visualization/show_trajectory.py</i>". You can 
put your KeyFrameTrajectory.txt in visualization directory and update 
show_trajectory.py for your needs.