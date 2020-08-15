"""
Testing an N-functional Analyte, M-functional Titrant calculator
If successful, this can consolidate all three calculation modules to one, and by massively simplifying the replot logic.
"""

from confirmed_functioning import *
from titration_module import *
import matplotlib.pyplot as plt


def get_vol(alpha_analyte, conc_analyte, volume_analyte, alpha_titrant, conc_titrant, h, oh, acid_titrant):
    """
    Take in a whole bunch of information, returns a list of volumes for the given data, with a length equal to the
    [H+] and [OH-] lists.

    :param alpha_analyte: Alpha Analyte
    :param conc_analyte: Concentration Analyte
    :param volume_analyte: Volume Analyte
    :param alpha_titrant: Alpha Titrant
    :param conc_titrant: Concentration Titrant
    :param h: Concentration Hydronium. Must be the same length of oh.
    :param oh: Concentration Hydroxide. Must be the same length of h.
    :param acid_titrant: Whether or not the titrant is an acid.

    :return vol: An array of volumes for the given [H+] and [OH-]
    :return phi: An array of phi (fraction of the way to the equivilence point) values
    """

    # Alpha values scaled by their index
    scaled_alphas_analyte = scale_alphas(alpha_analyte)
    scaled_alphas_titrant = scale_alphas(alpha_titrant)

    # Sume the scaled alpha values. Axis=1 forces the summation to occur for each individual [H+] value.
    summed_scaled_alphas_analyte = np.sum(scaled_alphas_analyte, axis=1)
    summed_scaled_alphas_titrant = np.sum(scaled_alphas_titrant, axis=1)

    beta = h - oh  # No technical definition

    # Conditional addition or subtraction based on the titrant.
    if acid_titrant:
        numerator = summed_scaled_alphas_analyte + (beta / conc_analyte)
        denominator = summed_scaled_alphas_titrant - (beta / conc_titrant)
        print("Acid Titrant")
    else:
        numerator = summed_scaled_alphas_analyte - (beta / conc_analyte)
        denominator = summed_scaled_alphas_titrant + (beta / conc_titrant)
        print("Base Titrant")

    # Solve for the volume
    phi = numerator / denominator

    volume = phi * volume_analyte * conc_analyte / conc_titrant

    return volume, phi


# Driver code
pka = [5, 12]
k = pka_to_ka(pka)
ph, h, oh = start_phs()

ct = 0.1  # M
ca = 0.1  # M
va = 100  # mL

aa = alpha_values(k, h, base=True, strong=False)  # Triprotic Analyte Base
at = alpha_values([1], h, base=False, strong=True)  # Monoprotic Titrant Acid

v, phi = get_vol(aa, ca, va, at, ct, h, oh, acid_titrant=True)

good_val_index = np.where((phi >= 0) & (phi <= len(pka)+1))

v = v[good_val_index]
ph = ph[good_val_index]
phi = phi[good_val_index]

print("v", v)
print("phi", phi)

plt.plot(v, ph)
plt.show()
