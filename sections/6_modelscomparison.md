:::::: collapse Experimental Evaluation

In this section observe the behavior of our algorithm using the *white legs* setup of Emio, in simulation and on the real robot.
We will compare the performance for different models and finally discuss the difference between this approach and the learned approach
from the first practical. 

::::: exercise

**Exercise 6 (optional)**

:::: select exo3model
::: option beam
::: option cosserat
::: option tetra
::::

Run the simulation using the button below, choosing different models from the dropdown menu above. 
Ensure that the robot behaves as expected. 

#runsofa-button("assets/labs/Practical2/lab_inversekinematics.py" "--legsName" "whiteleg" "--legsModel" "exo3model" "--legsPositionOnMotor" "counterclockwisedown" "clockwisedown" "counterclockwisedown" "clockwisedown" "--centerPartName" "bluepart")

Finally, we are ready to run the algorithm on the real robot! Follow the instructions below to setup the robots with the *white legs*.

::: collapse  Set up Emio 

Take four *white legs* and put them on each motor as shown on the image.
The orientations are the same as in exercise 1 and 2. 
Next, attach again the <span style="color:blue">*blue connector*</span> at the tip of each leg, and place
one <span style="color:green">*green marker*</span> on the top of the connector.

![](assets/data/images/lab2-exercice3-emio.png){width=75% .center}
:::

Connect the simulation to the real robot and look at the error, i.e. the difference between the two green and red spheres (you can also use the *Plotting* tab).

- What differences do you observe between the models? 
- Compare this model-based approach with the learned approach that we used in the last practical. Identify some advantages and disadvantages for each. 

::::: 

::::::
