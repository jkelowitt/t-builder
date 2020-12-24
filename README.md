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
    * Writes the pH and species predominance at the pH to a csv file.
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

## Math

Variables with the subscript 't' refer to the titrant. Variables with the subscript 'a' refer to the analyte.

Equations are a generalized form of the equations found
in [Quantitative Chemical Analysis 9th Ed.](https://www.amazon.com/Quantitative-Chemical-Analysis-Daniel-Harris/dp/146413538X)
by Daniel C. Harris. (Ch. 11.10)

The alpha value for a species tells the relative predominance of the species at a given pH. The values range between 0
and 1. The larger the alpha value for the species, the higher concentration the species is in at that pH. The alpha
value for a given species at a certain concentration of hydronium can be given by the equation:

![alpha_equation](https://latex.codecogs.com/png.latex?\dpi{150}&space;\bg_white&space;\fn_cm&space;\alpha_s&space;=&space;\frac{\Omega_s}{\sum_{n,m=\gamma,0}&space;^{0,&space;\gamma}([H^&plus;]^{n}&space;*&space;\prod^{m}&space;_{i=0}(K_i))})

where Omega_s is equal to the component of the sum in the denominator with the index equal to the absolute value of the
charge on the species (assuming the un-reacted species is neutral). The un-reacted species, the species with no charge,
s = 0, and thus Omega_s would equal the first component of the summation in the denominator. These values can be
directly ported into a bjerrum plot or predominance zone diagram.

With the alpha values now calculated, another relationship can be utilized. The equation:

![phi_definition](https://latex.codecogs.com/png.latex?\dpi{200}&space;\bg_white&space;\phi&space;\equiv\frac{C_tV_t}{C_aV_a}=&space;\frac{(\sum_{n=0}^{\gamma}n\alpha_{an})\pm\frac{[H^&plus;]-[OH^-]}{C_a}}{(\sum_{m=0}^{\theta}n\alpha_{tm})\mp\frac{[H^&plus;]-[OH^-]}{C_t}})

where phi is defined as the "Fraction of the way to the equivalence point", and gamma and theta are the functionality of
the analyte and titrant, respectively, can be used to determine the volume of titrant required to reach a certain pH.
Since all the values in the definition of phi are known, they can be solved to find phi. Using phi and known values for
the volume of analyte, and the concentration of both analyte and titrant, the volume of titrant can be calculated
through rearanging the previous equation to find:

![phi_usage](https://latex.codecogs.com/png.latex?\dpi{200}&space;\bg_white&space;V_t&space;=&space;\frac{\phi&space;C_a&space;V_a}&space;{C_t})

This equation is then solved thousands of times to produce a plot of volumes to pH values. The axes are flipped, and a
titration curve is born.

## Observations

1) On average, the class takes about 0.1s to initialize on my computer and the precision set to 0.01.
2) The initialization time is majorly dependent on the precision and to a lesser degree the number of pK values.
3) I'd like to do some more research into what would be useful to have with a titration simulator. It will probably end
   up copying a lot of what [OpenTitration](https://github.com/dalevens/OpenTitration) has already done.
4) I dread making a gui more than anything else. I dread making a *web app* even more, even though that is probably
   where this program will be heading. This is the last of the items on my list for now. I'll find excuses to not work
   on them for now though.