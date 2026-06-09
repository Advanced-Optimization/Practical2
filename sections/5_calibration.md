:::: collapse Understanding Camera Calibration

We will start by making sure our camera calibration is accurate. The stereo camera on the Emio robot allows us to compare what the robot is actually doing in the real world, with what our simulation thinks it's doing.    

Interestingly, the standard way to solve the calibration problem is via an optimization problem! The variables can be, for example, the camera's extrinsic parameters (its location) and intrinsic parameters (its focal length, baseline, central points, etc.). 

For Emio, we assume that the camera's intrinsics are calibrated already. The calibration task is to find the extrinsic parameters, i.e., the stereo camera's position and orientation (a.k.a. pose) with respect to a fixed frame. A common way to represent orientations is by using the rotation matrix $R\in\mathrm{SO}(d)$, which is an orthogonal matrix that satisfies $R^\top R=I$ and $\mathrm{det}(R)=1$. 
The extrinsics allow us to get the coordinates of known points (in fixed frame, such as the calibration dots), in the coordinates of the camera frame, as follows: 
$p_i = R p_i^f + t$, where $t\in\mathbb{R}^3$ is the camera's translation, and $p_i, p_i^f \in\mathbb{R}^3$ are the coordinates of the calibration dots in the camera's frame and the fixed frame, respectively. We assume we have $n$ such measurements.

We will practice our ability to formulate tasks as optimization problems using the following exercise. 

<!--
- intrinsics: the stereo camera's internal parameters such as its focal lengths $f_x,f_y$, baseline $b$ (distance between the two cameras), and possibly other parameters such as center coordinates $c_x, c_y$, distortion parameters, and the relative rotations of the two cameras. Ignoring distortion and assuming the two cameras are perfectly aligned, we can calculate the pixel values using the following equation $[u_i, v_i] = 1 / p_{i,z} K(\theta) p_i$, where $u_i$ and $v_i$ are the horizontal and vertical coordinates and $K$ is the intrinsic camera matrix, which is a function of the unknown parameters $\theta=[f_x, f_y, c_x, c_y, b]$. 

Camera calibration consists of finding the parameters $\theta$ and $R, t$, so that we can accurately predict the pixel locations of any points in space. 
-->


::: exercise
**Exercise 1:**

Assuming you are given a dataset $\{(p_i, p_i^f)\}_{i=1}^n$ of points in camera frame and their corresponding points in fixed frame. Can you formulate the optimization problem to find the unknown parameters based on this dataset? Write down the optimization problem and discuss the following points: 
- Is the optimization problem convex? 
- Is the optimization problem constrained or unconstrained? 
- What kind of solver would you choose to solve it?  

:::

Since we want to focus on the actual topic of this practical -- inverse kinematics -- we will not spend much more time on the implementation of the calibration problem. Instead, we use the instructions that the creators of Emio have provided to run camera calibration. 

::::
