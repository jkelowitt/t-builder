# T-Builder

Allows the user to plot any polyprotic or polyfunctional titration curve.

Run the executable to open the GUI.

Enter the data as indicated into the data entry area of the GUI. Click "Save Titration Data" or "Save Bjerrum Data" to
save the data plotted above to a CSV file.

## Features

* Plot Titration curves and Relative Species Plots
* Arbitrarily protic or functional analyte
* Arbitrarily protic or functional titrant
* Calculate Equivalence Points
* Calculate buffer points. Where pH = pKa or pKb
* View Derivatives of plots
* Save Titration or Relative Species plots to CSV

### Citric acid titrated with KOH:
![citric_acid_koh_titration](https://i.imgur.com/gQIjOxH.png)


### Species of Citric acid as pH increases:
![citric_acid_relative_speciation](https://i.imgur.com/Ng8gZpb.png)

## TODO:

* <del>"Show Plot" method</del> ***Done 7/31/2020***
* <del>"Save Data CSV" method</del> ***Done 7/31/2020***
* <del>Make a N-Functional analyte option</del> ***Done 12/23/2020***
* <del>Make a M-Functional titrant option</del> ***Done 12/23/2020***
* <del>Support for showing Bjerrum Plots </del> ***Done 12/23/2020***
* <del>EQ point finder (either with phi or with 2nd deriv.)</del> ***Done 12/28/2020***
* <del>Support for different temperatures </del> ***Done 12/24/2020***
* <del>A GUI</del> ***Done 12/26/2020***
* <del>Make a better name</del> ***Done 12/26/2020***
* <del>More Plot options</del>
    * <del>Probably just pass through matplotlib figure **kwargs</del> ***No longer pursued due to GUI***
* Figure out how to make the titration curve of a mixture of analytes
* Optional activity coefficients.
* Optional Species Names
* Advanced Features
    * <del>Calculate the equivalence points</del> ***Done 12/28/2020***
    * <del>Plot the derivatives</del> ***Done 12/28/2020***
    * Allow for preset compounds
    * Saving and loading compounds
* <del>In GUI support for different temperatures<\del> ***Done 1/2/2021***

## Math

Variables with the subscript 't' refer to the titrant. Variables with the subscript 'a' refer to the analyte.

Equations are a generalized form of the equations found
in [Quantitative Chemical Analysis 9th Ed.](https://www.amazon.com/Quantitative-Chemical-Analysis-Daniel-Harris/dp/146413538X)
by Daniel C. Harris. (Ch. 11.10)

The alpha value for a species tells the relative predominance of the species at a given pH. The values range between 0
and 1. The larger the alpha value for the species, the higher concentration the species is in at that pH. The alpha
value for a given species at a certain concentration of hydronium can be given by the equation:

![alpha_equation](https://latex.codecogs.com/png.latex?\dpi{200}&space;\bg_white&space;\fn_cm&space;\alpha_s&space;=&space;\frac{\Omega_s}{\sum_{n,m=\gamma,0}&space;^{0,&space;\gamma}([H^&plus;]^{n}&space;*&space;\prod^{m}&space;_{i=0}(K_i))})

where Omega_s is equal to the component of the sum in the denominator with the index equal to the absolute value of the
charge on the species (assuming the un-reacted species is neutral). The un-reacted species, the species with no charge,
s = 0, and thus Omega_s would equal the first component of the summation in the denominator. The value of gamma is the
degree of functionality for the analyte. K_i represents the indexed dissociation constant for the analyte (For this
notation, assume K_0 = 1). These values can be directly ported into a bjerrum plot or predominance zone diagram.

With the alpha values now calculated, another relationship can be utilized. The following equation can be obtained:

![phi_definition](https://latex.codecogs.com/png.latex?\dpi{200}&space;\bg_white&space;\phi&space;\equiv\frac{C_tV_t}{C_aV_a}=&space;\frac{(\sum_{n=0}^{\gamma}n\alpha_{an})\pm\frac{[H^&plus;]-[OH^-]}{C_a}}{(\sum_{m=0}^{\theta}m\alpha_{tm})\mp\frac{[H^&plus;]-[OH^-]}{C_t}})

where phi is defined as the "Fraction of the way to the equivalence point", and gamma and theta are the functionality of
the analyte and titrant, respectively, alpha_an represents the indexed alpha values of the analyte, and the similarly,
alpha_tm represents the indexed alpha values of the titrant. The ± in the numerator is positive if the analyte is a
base, and negative if the analyte is an acid. The opposite is true for the denominator, as indicated. C_a and V_a are
the concentration and volume of the analyte. C_t and V_t are the concentration and volume for the titrant.

Phi can be used to determine the volume of titrant required to reach a certain pH. Since all the values in the
definition of phi are known, they can be solved to find phi. Using phi and known values for the volume of analyte, and
the concentration of both analyte and titrant, the volume of titrant can be calculated through re-aranging the previous
equation to find:

![phi_usage](https://latex.codecogs.com/png.latex?\dpi{200}&space;\bg_white&space;V_t&space;=&space;\frac{\phi&space;C_a&space;V_a}&space;{C_t})

This equation is then solved thousands of times to produce a plot of volumes to pH values. The volume of titrant is set
as the x-axis, and the pH the y-axis, and a titration curve is born.

