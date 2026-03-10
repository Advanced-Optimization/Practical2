# Practical 2: solve inverse kinematics 

::: highlight
##### Overview 

In the last practical, we learned the inverse kinematics of Emio using a model-free (deep-learned) approach. This week, we will use a more model-based approach, using our newly acquired skills in constrained optimization.  

You model the robot, simulate its forward kinematics and solve its inverse kinematics using a QP to control it. You will then learn how to do camera calibration to evaluate your algorithm on the real robot and quantify its results.  

You will gain hands-on experience with solving real-world, nonlinear robotics problems. This will naturally teach you how to handle constraints, explore another numerical optimization toolbox, and get to know the complexities of soft robots in a practical context.

:::

#include(assets/labs/Practical2/sections/5_calibration.md)

#include(assets/labs/modules/camera_calibration.md)

#include(assets/labs/Practical2/sections/1_staticanalysis.md)

#include(assets/labs/Practical2/sections/2_forwardkinematics.md) 

#include(assets/labs/Practical2/sections/4_inversekinematics.md)

#include(assets/labs/Practical2/sections/6_modelscomparison.md)

## Appendix

#include(assets/labs/Practical2/sections/3_beammodels.md)

#include(assets/labs/Practical2/sections/appendix.md)
