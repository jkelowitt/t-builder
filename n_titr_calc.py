"""
Testing an N-functional Analyte, M-functional Titrant calculator
If successful, this can consolidate all three calculation modules to one, and by massively simplifying the replot logic.
"""

from confirmed_functioning import *
from titration_module import *
import matplotlib.pyplot as plt


def get_vol(alpha_analyte, conc_analyte, volume_analyte, alpha_titrant, conc_titrant, h, oh):
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

    numerator = summed_scaled_alphas_analyte - (beta / conc_analyte)
    denominator = summed_scaled_alphas_titrant + (beta / conc_titrant)

    phi = numerator / denominator

    volume = phi * volume_analyte * conc_analyte / conc_titrant

    return volume, phi

pka = [5, 7, 9]
k = pka_to_ka(pka)
ph, h, oh = start_phs()

ct = 0.1  # M
ca = 0.1  # M
va = 100  # mL

aa = alpha_values(k, h, base=False, strong=False)  # Triprotic Analyte Acid
at = alpha_values([1], h, base=True, strong=True)  # Monoprotic Titrant Base

v, phi = get_vol(aa, ca, va, at, ct, h, oh)

good_val_index = np.where((phi >= 0) & (phi <= 4))

v = v[good_val_index]
ph = ph[good_val_index]

print("v", v)
print("phi", phi)

plt.plot(v, ph)
plt.show()
