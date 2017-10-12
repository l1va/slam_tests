# slam_tests
Testing different slam libraries. 

<u>Do not forget to add your bags inside slam_bags pkg.</u>

1. <b>rtabmap_test</b>. 
Tried to make slam by mono camera and odometry, 
but rtabmap can not work with mono camera. Only stereo or RGB-D.
[Rtabmap install](https://github.com/introlab/rtabmap/wiki/Installation)

2. <b>orb_slam2_test</b>. 
Goes good but i have bag with fast rotations and 
it did not work fully even when i run bag with "-r 0.7" that means ~1.4 times slower. 
It was default settings of camera. Be careful with path to vocabulary in launch!
[ORB_SLAM2 install](https://github.com/l1va/ORB_SLAM2)
