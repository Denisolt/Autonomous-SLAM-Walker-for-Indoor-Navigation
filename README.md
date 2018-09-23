# An Autonomous Simultaneous Localization and Mapping Walker for Indoor Navigation

This project is part of the larger Parkinson's Disease research at NYIT. It extends to projects in fields of robotics, virtual reality and gait tracking. The repository provides instructions and the source code for research paper: "Autonomous Simultaneous Localization and Mapping Walker for Indoor Navigation".



## Abstract:
Walkers have been used to help the elderly and individuals with movement disorders as an assistive and reha- bilitation tool. This study presents a smart walker, a system which guides the users to navigate in an indoor environment. The Walker can be controlled by voice commands to create location markers and navigate the user while avoiding obstacles. We evaluated three localization implementations, namely, Adaptive Monte Carlo Localization (AMCL), Gmapping and Hector Slam for this system and compared their navigation accuracy with an ideal path. We collected the data on the paths of AMCL, Gmapping and Hector Slam and applied statistical tests on the data. The results show that AMCL achieves the lowest mean absolute error while navigating to its goal with an error of 2.15% over the path distance, as compared to Gmapping and Hector in this implementation.

## Requirements:

Hardware (left) and software (right) diagrams are attached above.

For complete set of instructions and requirements please refer to Documentation

Clone this repository into the src folder of your catkin workspace using:

`
cd ~/catkin_ws/src
git clone https://github.com/NYIT-PD/MoonWalker.git
`


## Documentation:
https://github.com/NYIT-PD/MoonWalker/wiki

