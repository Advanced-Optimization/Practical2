::::: collapse  Inverse Kinematics

The goal of the inverse kinematics process is to find the inverse of the previously described relationship, i.e., to compute the motor command positions $\textcolor{red}{\bm{u}_{a}} = \bm{f}^{-1}(\textcolor{darkgreen}{\bm{y}_{e}})$. This means determining the motor inputs that result in the desired end-effector position.
There are several challenges in solving this inverse problem:

- **Non-uniqueness of the inverse**: The robot's structure is deformable, and as a result, the inverse relationship $\bm{f}^{-1}$ is not unique. Different motor positions $\bm{u}_{a}$ can lead to the same end-effector position $\bm{y}_{e}$, depending on the deformation of the robot's legs.
- **Internal forces and lack of analytical model**: The robot's kinematic model is based on internal forces within the deformable structure, and there is no general analytical model for $\bm{f}(\bm{u}_{a})$. This makes it difficult to derive a closed-form expression for the inverse function, particularly because $\bm{f}(\bm{u}_{a})$ is highly nonlinear.
- **Nonlinearity of the system**: As mentioned, $\bm{f}(\bm{u}_{a})$ is a nonlinear function. Therefore, solving for the inverse kinematics requires setting up a nonlinear optimization process that provides motor positions $\bm{u}_{a}$ to minimize the distance to the desired end-effector position $\bm{y}_{e}$.

To handle these challenges, we typically employ SQP optimization techniques. In particular, we can employ the following optimization scheme: 

![](assets/labs/Practical2/latex/algorithm3.svg){width=85%, .center}


Problem (20) in Algorithm 3 is a standard QP.  Instead of solving (20) directly, we write the problem in slightly simpler form, eliminating $d\bm{q}$ and adding additional constraints: 

$$
\begin{aligned}
\underset{\bm{\lambda}_{a}}{\min} \, & \frac{1}{2} \bm{\lambda}_{a}^\top \bm{W}_{ea}^T \bm{W}_{ea} \bm{\lambda}_{a}
+ \bm{\lambda}_{a}^\top \bm{W}_{ea}^T\left(\bm{\delta}_{e}
(\bm{q}^{i-1}) + \bm{H}_{e} d\bm{q}^{\mathrm{free}}  - \textcolor{darkgreen}{\bm{y}_{e}}\right)\\
\text{s.t. } & \textcolor{red}{\bm{u}_{\min}} <=
\bm{\delta}_{a}^{\mathrm{free}} + \bm{W}_{aa}\bm{\lambda}_{a}
<= \textcolor{red}{\bm{u}_{\mathrm{max}}} \text{ (optional)}
\end{aligned}
$$

which, up to the added inequality constraints, gives the same solution as (20). 

The derivation of the above problem is given in _Appendix_ below. Intuitively, this QP eliminates the variable $d\bm{q}$ by substitution, meaning that we can solve a much smaller problem. 

The elements of this QP are: 
- $d\bm{q}^{\mathrm{free}}=\bm{A}^{-1}\bm{b}$
- $\bm{\delta}_{a}^{\mathrm{free}}=\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}d\bm{q}^{\mathrm{free}}$
- $\bm{W}_{ea}=\bm{H}_{e}\bm{A}^{-1}\bm{H}_{a}^T$
- $\bm{W}_{aa}=\bm{H}_{a}\bm{A}^{-1}\bm{H}_{a}^T$

The inequality constraints implement input bounds, which is a very common requirement.  Note that you can also add additional constraints, for example constraints to block one particular actuator.  Once a solution is found, we can obtain $\bm{u}_a$ through: 

$$
\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}d\bm{q}^{\mathrm{free}} + \bm{W}_{aa}\bm{\lambda}_{a}
= \textcolor{red}{\bm{u}_{a}}.
$$

In the case where the number of end-effectors is smaller than the number 
of actuators, there can be several solutions, but we can add a regularization term to minimize the 
deformation energy [[Coevoet17]](https://inria.hal.science/hal-01649355/document) and achieve a unique solution.

In the next exercise, we will implement the above algorithm using Python. 

::: exercise 

**Exercise 5**

Solve the inverse kinematics problem using an off-the-shelve QP solver.
Open the file `myQP_lab_inversekinematics.py` by clicking the *open* button below, and fill in the missing lines, step by step; solving first Exercise 3.1, then Exercise 3.2, and finally Exercise 3.3. The matrices $\bm{W}$ and vectors $d\bm{q}^{\mathrm{free}}$, $\bm{\delta}(\bm{q}^{i-1})$ are provided by the simulator *SOFA*. 

#open-button("assets/labs/Practical2/myQP_lab_inversekinematics.py")

At each step, try your implementation by clicking the *SOFA* button below; for this exercise, we won't connect the robot yet. Each time
you change the file `myQP_lab_inversekinematics.py`, you will need to close and relaunch the simulation for the changes to be taking into account.

#runsofa-button("assets/labs/Practical2/run_simulation.py" "--legsName" "blueleg" "--legsModel" "beam" "--legsPositionOnMotor" "counterclockwisedown" "clockwisedown" "counterclockwisedown" "clockwisedown" "--centerPartName" "bluepart")

Comment on the following questions: 

a) Comment on the behavior you observe after each subtask (i., ii., and iii.), answering in particular any questions asked in the code comments. 

b) What would happen if you were using a different scheme than SQP here, for example an augmented Lagrangian method? Would that be an appropriate method, in your opinion? 

c) Bonus question 1: Implement your own solver instead of using an off-the-shelve solver. 

d) Bonus question 2: Solve the original QP, given in Algorithm 3, instead of the simplified form. Do you observe any performance differences? 

::::

:::::
