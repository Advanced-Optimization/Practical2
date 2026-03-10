:::: collapse  Forward Kinematics

Using the above beam models, we can also solve the forward kinematics of the more complex robot structure of Emio (4 coupled legs).  

In the previous homework, you already learned how to formulate the forward kinematics of a simple coupled spring-mass system as a constrained optimization problem. You will see now that the same principles carry over seamlessly to Emio. 

In particular, we can write the forward kinematics (technically, the forward statics) of Emio as a minimization problem of potential energy, where we constrain the end-effector location to be the same for all four legs.

$$
\begin{aligned}
\min_{\{\bm{q}_1, \cdots, \bm{q}_4\}} \sum_i & \mathcal{W}(\bm{q}_i) + \mathcal{W}_\mathrm{pot}(\bm{q}_i)\\
\text{s.t.}\,\,
\bm{\delta}_1(\bm{q}_1) &= \bm{\delta}_2(\bm{q}_2) \\
\bm{\delta}_2(\bm{q}_2) &= \bm{\delta}_3(\bm{q}_3) \\
\bm{\delta}_3(\bm{q}_3) &= \bm{\delta}_4(\bm{q}_4) \\
\bm{\delta}_a(\bm{q}) &= \bm{u}_a
\end{aligned}
$$  
where we introduced $\bm{\delta}_i(\bm{q}_i)$ to denote the operation that generates the 3-d position of the end effector attached to arm $i$, and $\bm{u}_a$ is the input that we provide (motor angles), which leads to actual leg angles $\bm{\delta}_a(\bm{q}^{i-1})$. Here is the big difference between rigid and soft robots: Just because we input a certain motor angle, doesn't mean that the leg will be exactly at that angle, because of compliance.

We note that $\frac{\partial \mathcal{W}(\bm{q}_i)}{\partial \bm{q}_i}=\bm{F}_i(\bm{q}_i)$, $\frac{\partial \mathcal{W}_{\mathrm{pot}}(\bm{q}_i)}{\partial \bm{q}_i} = \bm{M}_i \bm{g}$.

::: exercise

**Exercise 4:**

Introducing $\bm{H}_i:=\frac{\partial \bm{\delta}_i(\bm{q}_i)}{\partial \bm{q}_i}$, and  $\bm{A}_i := \frac{\partial \bm{F}_i(\bm{q}_i)}{\partial \bm{q}_i}$, show that the SQP update for the above problem takes the following form. What simplification did we make here compared to what we saw in class? 

$$
\begin{bmatrix}
\bm{A} & -\bm{H}_e^\top & -\bm{H}_a^\top  \\
-\bm{H}_e & 0 & 0 \\
-\bm{H}_a & 0 & 0 
\end{bmatrix}
\begin{bmatrix}
d\bm{q} \\
\lambda_e \\
\lambda_a
\end{bmatrix}
= 
\begin{bmatrix}
\bm{F}(\bm{q}) + \bm{M}\bm{g} \\ 
0 \\
0
\end{bmatrix}, \quad \text{with: } 
\bm{A} = 
\begin{bmatrix}
\bm{A}_1 & & \\
 & \ddots & \\
 & & \bm{A}_4 
 \end{bmatrix}, 
$$
$$
\bm{H}_e^\top = 
\begin{bmatrix}
-\bm{H}_1^\top & -\bm{H}_1^\top & -\bm{H}_1^\top \\
\bm{H}_2^\top & 0 & 0 \\
0 & \bm{H}_3^\top & 0 \\
0 & 0 & \bm{H}_4^\top
\end{bmatrix}, \quad
\bm{q} = \begin{bmatrix}
d\bm{q}_1 \\
\vdots \\
d\bm{q}_4 \\
\end{bmatrix}, \quad
\bm{F}(\bm{q}) + \bm{M}\bm{g} = \begin{bmatrix}
\bm{F}_1(\bm{q}_1) + \bm{M}_1\bm{g} \\ 
\vdots \\
\bm{F}_4(\bm{q}_4) + \bm{M}_4\bm{g} 
\end{bmatrix}
$$ 

::: 

Therefore, the full optimization loop to find the minimum-energy solution, i.e., to compute the end effector position $\bm{y}_e = f(\bm{u}_a)$ is given by:

![](assets/labs/Practical2/latex/algorithm2.svg){width=85%, .center}

:::: 

