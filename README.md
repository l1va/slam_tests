# slam_tests
Testing different slam libraries. 

<u>Do not forget to add your bags inside slam_bags pkg.</u>

1. <b>rtabmap_test</b>. Tried to make slam by mono camera and odometry, 
but rtabmap can not work with mono camera. Only stereo or RGB-D.

2. <b>orb_slam2_test</b>. Goes good but i have bag with fast rotations and 
it started work only when i run bag with "-r 0.1" that means 10 times slower.

