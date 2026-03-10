:::::: collapse Static Analysis

Our approach is grounded in structural mechanics, which enables to account for both the geometric and material properties of the robot. To achieve a good level of generality, all models are derived from mechanical energy principles. 
We assume that whatever the configuration, the robot exhibits elastic behavior, meaning the energy considered is potential energy. 
Additionally, we assume that the robot moves slowly enough that kinetic energy can be neglected for the time being. 

We suppose that the vector $\mathbf{q}$ represents the parameters of the motion. Depending on the model that we will use, it will consist of the motion of the nodes in FEM, or of strains for Cosserat models. The potential energy of the deformation of the structure will be denoted by $\mathcal{W}(\mathbf{q})$. 
The internal forces $\mathbf{F}(\mathbf{q}) = \frac{\partial \mathcal{W}(\mathbf{q})}{\partial \mathbf{q} }$ are obtained by the derivative of this deformation potential energy.

The configuration of the robot, given by $\mathbf{q}$, is obtained by solving for the minimum-energy configuration of the robot. This configuration corresponds to the static equilibrium between these internal forces  $\mathbf{F}(\mathbf{q})$, gravity, and eventual external loads $\mathbf{F}_{ext}$, which we ignore here. 

$$
\mathbf{F}(\mathbf{q}) + \mathbf{M}\mathbf{g} + \mathbf{F}_{ext} = \mathbf{0}
$$

![](assets/labs/Practical2/latex/algorithm1.svg){width=85%, .center}

::: exercise 
**Exercise 2**
Show that the above algorithm can be obtained by applying a Newton scheme to the minimization of potential energy.
::: 

To model the various legs and their deformations, different models of internal forces exist:

- an FEM beam model, computed in global coordinates
- a Cosserat rod model, computed in local coordinates (strain space)
- a volume FEM with corotational linear tetrahedral elements

If you want to learn more about the physics behind each model, you can take a look at the last section of this practical (_Beam Models_). To continue our development, all we need to know is that we have a way to compute $F(q)$ and $A := \frac{\partial F(q)}{\partial q}$.

## Hands-on

Now you will play with the simulation and compare the deformations with the ones of the real device. 
You will see which parameters influence the beam and Cosserat models the most.


::::: exercise
::: collapse  Set up Emio 
Take the <span style="color:blue">*blue leg*</span> and put it on the *motor n°0* (clockwise down as shown on the image). 
Next, attach the <span style="color:grey">*grey cube*</span> at the tip of the leg, then place
two <span style="color:green">*green markers*</span> on the leg: one in the middle of the leg and the second at the tip,
just above the cube.

![](assets/data/images/lab1-exercice1-leg.png){.center width=50%}

:::


**Exercise 3:**

Once setup, choose a model between *beam* and *cosserat* in the drop-down menu below:

:::: select modelsexo1
::: option beam 
::: option cosserat 
::: option tetra
::::

Launch the simulation, make sure that the markers you put on the leg match the 
markers in the simulation, then change the motor's position. Observe the deformation differences 
between the simulation and the real leg. Adjust the parameters until the simulation accurately 
mirrors the deformation of the real device.

Answer the following questions: 
1. Which parameters influences the most the deformation of the leg in this configuration?  
2. Which parameters did you choose to change and why?

#runsofa-button("assets/labs/lab_models/lab_models.py", "blueleg", "modelsexo1")

:::::

::::::
