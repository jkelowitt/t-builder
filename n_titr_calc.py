"""
Testing an N-functional Analyte, M-functional Titrant calculator
If successful, this can consolidate all three calculation modules to one, and by massively simplifying the replot logic.
"""
import numpy as np  # Keep for other matrix manipulations
from confirmed_functioning import *


def cond_add_sub(a, b, cond):
    if cond:
        return a + b
    else:
        return a - b


def scale_alphas(arr):
    for i, item in enumerate(arr):
        item[i] *= i
    return arr


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

    anum = scale_alphas(aa)
    atir = scale_alphas(at)

    sanum = np.sum(anum)
    satir = np.sum(atir)

    beta = h - oh
    nbeta = beta / ca  # Numerator Beta
    dbeta = beta / ct  # Denominator Beta

    num = cond_add_sub(sanum, nbeta, acid_t)
    den = cond_add_sub(satir, dbeta, not acid_t)

    phi = num / den
    vol = phi * ca * va / ct

    return vol


k = np.array([1e-5, 1e-12])
h = np.array([0.04375221051582521, 0.043651583224016584])
oh = np.array([2.3381675758530645e-13, 2.3435576087814323e-13])

ct = 0.1  # M
ca = 0.1  # M
va = 100  # mL

aa = alpha_values(k, h, base=True, strong=False)  # Triprotic Weak Base Analyte
at = alpha_values([1], h, base=False, strong=True)  # Monoprotic Strong Acid Titrant

print(aa)
print(at)

v = get_vol(aa, ca, va, at, ct, h, oh, acid_t=True)
print("v", v)
