# Titration Generator

Allows the user to plot any polyprotic or polyfunctional titration curve.

Use:

```python
from titration_class import Titration
``` 

to import the Titration class used.

## Class Arguments

There are 6 positional arguments:

* analyte_is_acidic
    * Whether the analyte is acting as an acid.

* volume_analyte
    * The volume of the analyte.

* concentration_analyte
    * The concentration of the analyte.

* concentration_titrant
    * The concentration of the titrant.

* pkt_values
    * A list of the pK values for the titrant. If it is acidic, use pKa, else use the pKb values.

* pka_values
    * A list of the pK values for the analyte. If it is acidic, use pKa, else use the pKb values.

There are 4 optional key-word arguments:

* strong_analyte
    * Whether the analyte is strong. Default = True

* strong_titrant
    * Whether the titrant is strong. Default = True

* precision
    * The step size of the pH being calculated. Default = 0.01

* kw
    * The dissociation constant of water. Default = 1.023 * (10 ** -14)

## Class Methods

* plot_titration_curve
    * Plots and shows the titration curve for a reasonable range of volumes.
    * Takes in a title string as a required positional argument.

* plot_alpha_curve
    * Plots and shows the bjerrum plot for each species in solution for the entire pH range.
    * Takes in a title string as a required positional argument.

* write_titration_data
    * Writes the pH and volume of titrant to a csv file.
    * Takes in a title string as a required positional argument.

* write_alpha_data
    * Writes the pH and species predominances at the pH to a csv file.
    * Takes in a title string as a required positional argument.

## TODO:

* <del>"Show Plot" method</del> *Done*
* <del>"Save Data CSV" method</del> *Done*
* <del>Make a N-Functional analyte option</del> *Done*
* <del>Make a M-Functional titrant option</del> *Done*
* <del>Support for showing Bjerrum Plots </del> *Done*
* <del>EQ point finder (either mathematically or with 2nd deriv.)</del> (
  See [OpenTitration](https://github.com/dalevens/OpenTitration), by Dale Evans.)
* More Plot options
    * Probably just pass through matplotlib figure **kwargs
* A GUI.

Equations
from [Quantitative Chemical Analysis 9th Ed.](https://www.amazon.com/Quantitative-Chemical-Analysis-Daniel-Harris/dp/146413538X)
by Daniel C. Harris. (Ch. 11.10)

The equations utilized from the textbook above leverage the following type of relationship (in this case for a diprotic
acid being reacted with a strong base):

![equation](https://latex.codecogs.com/svg.latex?\phi%20%20\equiv%20%20%20\frac{C_b%20V_b}{C_a%20V_a}%20=%20%20\frac{\alpha_{HA^{-}}+2\alpha_{A^{2-}}%20+%20\frac{[H^{+}]%20-%20[OH^{-}]}{C_{a}}}{1%20+%20\frac{[H^{+}]%20-%20[OH^{-}]}%20{C_{b}}})

Where phi is defined as the "Fraction of the way to the equivalence point." Since the values for alpha are calculatable,
phi is calculable as well. Solving the left most equality for the volume of base lets us find the amount if base
added to reach the pH used in the alpha values and concentration of ions. So the pH is the input, and the Volume of
titrant is the output. 

