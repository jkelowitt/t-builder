"""
All of the calculations pertaining to a triprotic titration

Common Parameters:
    ph  : List of pHs from 0 to 14 with 0.001 per step.
    h   : List of Hydronium concentrations per pH
    oh  : List of Hydroxide concentrations per pH

    ka1 : 1st Acid dissociation constant
    ka2 : 2nd Acid dissociation constant
    ka3 : 3rd Acid dissociation constant

    kb1 : 1st Base dissociation constant
    kb2 : 2nd Base dissociation constant
    kb3 : 3rd Base dissociation constant

    ca  : Acid concentration
    cb  : Base concentration

    va  : Acid volume
    vb  : Base volume
"""

from titration_module import *


def tp_alpha_values(h, ka1=1.0, ka2=1.0, ka3=1.0, weak_base=False):
    """Triprotic Alpha Value Calculations"""
    if weak_base:
        k1 = kw / ka3
        k2 = kw / ka2
        k3 = kw / ka1
    else:
        k1 = ka1
        k2 = ka2
        k3 = ka3

    denom = h ** 3 + (h ** 2 * k1) + (h * k1 * k2) + (k1 * k2 * k3)

    ah3a = h ** 3 / denom
    ah2a = (h ** 2 * k1) / denom
    aha2 = (h * k1 * k2) / denom
    aa3 = (k1 * k2 * k3) / denom

    abh3 = ah3a
    abh2 = ah2a
    abh = aha2
    ab = aa3

    return ah3a, ah2a, aha2, aa3, abh3, abh2, abh, ab


def tp_wasb(ka1, ka2, ka3, ca, cb, va):
    """Triprotic acid calculation"""
    ka1 = float(ka1)
    ka2 = float(ka2)
    ka3 = float(ka3)
    ca = float(ca)
    cb = float(cb)
    va = float(va)

    ph, h, oh = start_phs()

    ah3a, ah2a, aha2, aa3, abh3, abh2, abh, ab = tp_alpha_values(h, ka1, ka2, ka3, weak_base=True)

    alpha = {
        "alphaH3A" : ah3a,
        "alphaH2A-": ah2a,
        "alphaHA2-": aha2,
        "alphaA3-" : aa3,
        "alphaBH3+": abh3,
        "alphaBH2+": abh2,
        "alphaBH+" : abh,
        "alphaB"   : ab
        }

    phi = (ah2a + (2 * aha2) + (3 * aa3) - ((h - oh) / cb)) / (1 + ((h - oh) / ca))
    vol = phi * ca * va / cb

    return vol, ph, h, oh, alpha


def tp_wbsa(ka1, ka2, ka3, ca, cb, vb):
    """Trifunctional base calculation"""
    ka1 = float(ka1)
    ka2 = float(ka2)
    ka3 = float(ka3)
    ca = float(ca)
    cb = float(cb)
    vb = float(vb)

    ph, h, oh = start_phs()

    ah3a, ah2a, aha2, aa3, abh3, abh2, abh, ab = tp_alpha_values(h, ka1, ka2, ka3, weak_base=False)

    alpha = {
        "alphaH3A" : ah3a,
        "alphaH2A-": ah2a,
        "alphaHA2-": aha2,
        "alphaA3-" : aa3,
        "alphaBH3+": abh3,
        "alphaBH2+": abh2,
        "alphaBH+" : abh,
        "alphaB"   : ab
        }

    phi = (abh + (2 * abh2) + (3 * abh3) + ((h - oh) / cb)) / (1 - ((h - oh) / ca))
    vol = phi * cb * vb / ca

    return vol, ph, h, oh, alpha
