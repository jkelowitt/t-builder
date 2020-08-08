"""
Testing an N-functional Analyte, M-functional Titrant calculator
If successful, this can consolidate all three calculation modules to one, and by massively simplifying the replot logic.
"""

from confirmed_functioning import *
from titration_module import *
import matplotlib.pyplot as plt


def get_vol(aa, ca, va, at, ct, h, oh, acid_t=True):
    """
    Take in a whole bunch of information, returns a list of volumes for the given data, with a length equal to the
    [H+] and [OH-] lists.

    :param aa: Alpha Analyte
    :param ca: Concentration Analyte
    :param va: Volume Analyte
    :param at: Alpha Titrant
    :param ct: Concentration Titrant
    :param h: Concentration Hydronium. Must be the same length of oh.
    :param oh: Concentration Hydroxide. Must be the same length of h.
    :param acid_t: Whether or not the acid is the titrant.

    :return vol: An array of the volumes for the given [H+] and [OH-]
    """

    # Scale the alpha values by their indicies.
    anum = scale_alphas(aa)
    atir = scale_alphas(at)

    # Sum the scaled alphas
    sanum = np.sum(anum)
    satir = np.sum(atir)

    # Generate the non-alpha dependent portions of the numerators and denominators
    beta = h - oh
    nbeta = beta / ca  # Numerator Beta
    dbeta = beta / ct  # Denominator Beta

    # Add or subtract the alpha and beta dependent parts of the numerator or denominator conditionally.
    # If the titrant is an acid, the top needs to be added together and the bottom subtracted. Else the opposite.
    num = cond_add_sub(sanum, nbeta, acid_t)
    den = cond_add_sub(satir, dbeta, not acid_t)

    # Phi is equal to the percent of the way to the equivalence point
    phi = num / den

    # Solve for volume
    vol = phi * ca * va / ct

    return vol, phi


k = np.array([1e-5, 1e-7, 1e-9])
ph, h, oh = start_phs()

ct = 0.1  # M
ca = 0.1  # M
va = 100  # mL

aa = alpha_values(k, h, base=True, strong=False)  # Triprotic Weak Base Analyte
at = alpha_values([1], h, base=False, strong=True)  # Monoprotic Strong Acid Titrant

v, phi = get_vol(aa, ca, va, at, ct, h, oh, acid_t=True)

print("v", v)

plt.plot(v, ph)
plt.show()
