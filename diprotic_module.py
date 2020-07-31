"""
All of the calculations pertaining to a diprotic titration

Common Parameters:
    ph  : List of pHs from 0 to 14 with 0.001 per step.
    h   : List of Hydronium concentrations per pH
    oh  : List of Hydroxide concentrations per pH

    ka1 : 1st Acid dissociation constant
    ka2 : 2nd Acid dissociation constant

    kb1 : 1st Base dissociation constant
    kb2 : 2nd Base dissociation constant

    ca  : Acid concentration
    cb  : Base concentration

    va  : Acid volume
    vb  : Base volume
"""

from titration_module import *


def dp_alpha_values(h, ka1=1.0, ka2=1.0, weak_base=False):
    if weak_base:
        k1 = kw / ka2
        k2 = kw / ka1
    else:
        k1 = ka1
        k2 = ka2

    denom = (h ** 2) + (h * k1) + (k1 * k2)

    ah2a = (h * h) / denom
    aha = h * k1 / denom
    aa2 = k1 * k2 / denom

    abh22 = ah2a
    abh = aha
    ab = aa2

    return ah2a, aha, aa2, abh22, abh, ab


def dp_wasb(ka1, ka2, ca, cb, va):
    """Diprotic weak acid, strong base titrant"""

    ka1 = float(ka1)
    ka2 = float(ka2)
    ca = float(ca)
    cb = float(cb)
    va = float(va)

    ph, h, oh = start_phs()
    ah2a, aha, aa2, abh22, abh, ab = dp_alpha_values(h, ka1, ka2)

    alpha = {
        "alphaH2A"  : ah2a,
        "alphaHA-"  : aha,
        "alphaA2-"  : aa2,
        "alphaBH22+": abh22,
        "alphaBH+"  : abh,
        "alphaB"    : ab
        }

    phi = ((aha + (2 * aa2)) - ((h - oh) / ca)) / (1 + ((h - oh) / cb))
    vol = phi * ca * va / cb

    return vol, ph, h, oh, alpha


def dp_wbsa(ka1, ka2, ca, cb, vb, weak_base=True):
    """Diprotic weak base, strong acid titrant"""

    ka1 = float(ka1)
    ka2 = float(ka2)
    ca = float(ca)
    cb = float(cb)
    vb = float(vb)

    ph, h, oh = start_phs()
    ah2a, aha, aa2, abh22, abh, ab = dp_alpha_values(h, ka1, ka2, weak_base)

    alpha = {
        "alphaH2A"  : ah2a,
        "alphaHA-"  : aha,
        "alphaA2-"  : aa2,
        "alphaBH22+": abh22,
        "alphaBH+"  : abh,
        "alphaB"    : ab
        }

    phi = (abh + (2 * abh22) + ((h - oh) / cb)) / (1 - ((h - oh) / ca))
    vol = phi * cb * vb / ca

    return vol, ph, h, oh, alpha
