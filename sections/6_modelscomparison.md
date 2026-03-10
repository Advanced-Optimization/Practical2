:::::: collapse Experimental Evaluation

In this section observe the behavior of our algorithm using the *white legs* setup of Emio, in simulation and on the real robot.

::::: exercise

**Exercise 6**

Run the simulation using the button below and ensure that the robot behaves as expected. 

#runsofa-button("assets/labs/lab_inversekinematics/lab_inversekinematics.py" "--legsName" "whiteleg" "--legsModel" "exo3model" "--legsPositionOnMotor" "counterclockwisedown" "clockwisedown" "counterclockwisedown" "clockwisedown" "--centerPartName" "bluepart")

- Can you bring the robot in an unstable position? Take a screenshot and describe what you are seeing in your report. 
- Can you find a configuration where, for given motor commands, there are two possible robot positions? Take screenshots of these two situations to put in your report.  

::::: 

Finally, we are ready to run the algorithm on the real robot! 

::: collapse  Set up Emio 

Take four *white legs* and put them on each motor as shown on the image.
The orientations are the same as in exercise 1 and 2. 
Next, attach again the <span style="color:blue">*blue connector*</span> at the tip of each leg, and place
one <span style="color:green">*green marker*</span> on the top of the connector.

![](assets/data/images/lab2-exercice3-emio.png){width=75% .center}
:::

::::: exercise

**Exercise 7**

Connect the simulation to the real robot and look at the error, i.e. the difference
between the two green and red spheres (you can also use the *Plotting* tab).
- Comment on the error as you move the robot to different positions. Can you discern any trends? 
- Compare this model-based approach with the learned approach that we used in the last practical. Identify some advantages and disadvantages for each. 

::::: 

::::::
