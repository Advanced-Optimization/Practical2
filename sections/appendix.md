::::: collapse  Derivation of QP

We derive the simplified QP used for inverse kinematics. We start by deriving the simplified equations for kinematics. 

We will decompose the movement at each time step by separating the contributions from the force $\bm{b}$, which is 
related to internal forces, external forces, and gravity (whose values we can compute), and the forces $\bm{H}_{a}^T$ 
related to actuation (whose values are unknown and depend on the force required to satisfy the constraints).

$$
\bm{A}d\bm{q} = \bm{b} + \bm{H}_{a}^T \bm{\lambda}_{a} 
\Leftrightarrow
\left \{
\begin{array}{l}
d\bm{q} = d\bm{q}^{\mathrm{free}}  + d\bm{q}^{\lambda} \\ 
\mathrm{with}: \\
\bm{A}d\bm{q}^{\mathrm{free}} =  \bm{b} \leftrightarrow d\bm{q}^{\mathrm{free}} =  \bm{A}^{-1}\bm{b} \\
\bm{A}d\bm{q}^{\lambda} = \bm{H}_{a}^T 
\bm{\lambda}_{a} 
\leftrightarrow d\bm{q}^{\lambda}  = \bm{A}^{-1}\bm{H}_{a}^T 
\bm{\lambda}_{a}
\end{array}
\right .
$$

Thus, we can rewrite the kinematic constraint, 
$\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}d\bm{q} = \textcolor{red}{\bm{u}_{a}}$, 
as directly depending on the actuation force:

$$
\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}\left(d\bm{q}^{\mathrm{free}} + d\bm{q}^{\lambda}\right) = \textcolor{red}{\bm{u}_{a}} \Longleftrightarrow
$$

$$
\underbrace{
\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}d\bm{q}^{\mathrm{free}}}_{\bm{\delta}_{a}^{\mathrm{free}}} + 
\underbrace{\bm{H}_{a}\bm{A}^{-1}\bm{H}_{a}^T}_{\bm{W}_{aa}} \bm{\lambda}_{a} = \textcolor{red}{\bm{u}_{a}}
$$

This equation expresses the coupling of the actuation motion by the various torques via the compliance matrix $\bm{W}_{aa}$, 
which represents the projection of the inverse matrix in the space of motor constraints.

The same way, we can rewrite 

$$
\textcolor{darkgreen}{\bm{y}_{e}} = \bm{\delta}_{e}(\bm{q}^{i-1}) + \bm{H}_{e} d\bm{q} 
$$

$$
\textcolor{darkgreen}{\bm{y}_{e}} =
\underbrace{
\bm{\delta}_{e}(\bm{q}^{i-1}) + \bm{H}_{e} d\bm{q}^{\mathrm{free}}}_{\bm{\delta}_{a}^{\mathrm{free}}} +
\underbrace{\bm{H}_{e}\bm{A}^{-1}\bm{H}_{a}^T}_{\bm{W}_{ea}} \bm{\lambda}_{a}
$$

Combining equations above, we obtain a reduced formula of the linearized kinematics:

$$
\textcolor{darkgreen}{\bm{y}_{e}} = \bm{\delta}_{e}^{\mathrm{free}} + \bm{W}_{ea}\bm{W}_{aa}^{-1} ( \textcolor{red}{\bm{u}_{a}} - \bm{\delta}_{a}^{\mathrm{free}})
$$

$\bm{J}_{SR} = \bm{W}_{ea}\bm{W}_{aa}^{-1}$ being the Jacobian of the soft robot. 






We can eliminate the equality constraints by introducing a convenient parameterization into free and forced motion of $\bm{q}$ as follows: 
$$
\left \{
\begin{array}{l}
\bm{A}d\bm{q}^{\mathrm{free}}  =  \bm{b} \\
\bm{A}d\bm{q}^{\lambda} = \bm{H}_{a}^T 
\bm{\lambda}_{a} 
\end{array}
\right .
$$

$$
\underset{\bm{\lambda}_{a}}{\min}
\frac{1}{2}\|\bm{\delta}_{{e}}(\bm{q}^{i-1}) + 
\bm{H}_{{e}} d\bm{q}^{\mathrm{free}} 
+ \bm{W}_{{ea}} \bm{\lambda}_{a}  
- \textcolor{darkgreen}{\bm{y}_{{e}}}\|^2 \\
$$

The advantage is that the optimization algorithm corresponds to convex optimization (i.e. Quadratic Programming) 
on small matrices $\bm{W}_{{ea}}$. If we develop the equation above, we obtain:

$$
\underset{\bm{\lambda}_{a}}{min} (
\frac{1}{2} \bm{\lambda}^\top_{a} \bm{W}_{{ea}}^T \bm{W}_{{ea}} \bm{\lambda}_{a}
+ \bm{W}_{{ea}}^T(\bm{\delta}_{{e}}(\bm{q}^{i-1}) + 
\bm{H}_{{e}} d\bm{q}^{\mathrm{free}}   
- \textcolor{darkgreen}{\bm{y}_{{e}}})\bm{\lambda}_{a}
)
$$

Remember that the relation between the motor's torque and displacement 
is given by $\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}d\bm{q}^{\mathrm{free}} + \bm{W}_{{aa}}\bm{\lambda}_{a} = \textcolor{red}{\bm{u}_{a}}$. Thus, to limit the course of the actuators we can add the following constraint to the QP:

$$
\textcolor{red}{\bm{u}_{\min}} <=
\bm{\delta}_{a}(\bm{q}^{i-1}) + \bm{H}_{a}d\bm{q}^{\mathrm{free}} + \bm{W}_{{aa}}\bm{\lambda}_{a}
<= \textcolor{red}{\bm{u}_{max}}
$$

::::: 
