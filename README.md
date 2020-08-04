# Titration Generator
Allows the user to plot any monoprotic, diprotic, or triprotic titration curve.

Run **main.py** to start the program.

There are 5 parts to the program:
  * The plot is where the titration curve is shown once all of the required data is input. 
  * The Titrant Section is where you select either a strong acid or a strong base as a titrant.
  * The Analyte Section is where you select whether the analyte is Monoprotic, Diprotic, or Triprotic.
  * Once the Titrant and Analyte have been selected, the Assign Parameters button will function. Clicking on the Assign Parameters button will open a menu with boxes to enter the required data to plot the requested titration curve. Clicking Ok will save the data.
  * Clicking Force Plot after the data has been entered will put a plot into the plot section. 
  * Clicking Save Plot allows the user to specify a name under which the plot will be saved. The png will be saved to the program's directory.
  * Clicking Save CSV allows the user to specify a name under which a csv with the following information will be saved (in the program's directory):
    * Analyte Parameters
    * Titrant Parameters
    * pH
    * [H+]
    * [OH-]
    * Volume of Titrant
    * Alpha Values
    
  * Quit will exit the program.

TODO:
  * <del>"Save Plot" Button</del> *Done but broken*
  * <del>"Save Data CSV" Button</del> *Done*
  * Auto closing and plotting of the graph when "Ok" is pressed
  * Dynamic Chart Title
  * Plot options
  * Fix Spacing on the Titrant and Analyte Sections
  * Make an executable
  * Make a N-Functional analyte option
  * Support for showing Bjerrum Plots
  * EQ point finder (either mathematically or with 2nd deriv.)
  * Group Boxes for data entry
  * Close all windows on main gui's close

  
Gui built using [Guietta](https://github.com/alfiopuglisi/guietta) by [alfiopuglisi](https://github.com/alfiopuglisi).
Equations from [Quantitative Chemical Analysis 9th Ed. by Daniel C. Harris](https://www.amazon.com/Quantitative-Chemical-Analysis-Daniel-Harris/dp/146413538X). (Ch. 11.10)

The equations utilized from the textbook above leverage the following type of relationship (in this case for a diprotic acid being reacted with a strong base):

![equation](https://latex.codecogs.com/svg.latex?\phi%20%20\equiv%20%20%20\frac{C_b%20V_b}{C_a%20V_a}%20=%20%20\frac{\alpha_{HA^{-}}+2\alpha_{A^{2-}}%20+%20\frac{[H^{+}]%20-%20[OH^{-}]}{C_{a}}}{1%20+%20\frac{[H^{+}]%20-%20[OH^{-}]}%20{C_{b}}})

Where phi is defined as the "Fraction of the way to the equivalence point." Since the values for alpha are calculatable, phi is calculate able as well. Solving the left most equality for the volume of base lets us find the amount if base added to reach the pH used in the alpha values and concentration of ions. So the pH is the input, and the Volume of titrant is the output. 

This equation is entirely scalable, and combined with the scalablility of the alpha value equations, it is theoretically possible to calculate the plot of an n-functional analyte with an m-functional titrant.
