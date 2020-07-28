"""
All of the calculations pertaining to a monoprotic titration

Common Parameters:
    ph : List of pHs from 0 to 14 with 0.001 per step.
    h  : List of Hydronium concentrations per pH
    oh : List of Hydroxide concentrations per pH

    ka : Acid dissociation constant
    kb : Base dissociation constant

    ca : Acid concentration
    cb : Base concentration

    va : Acid volume
    vb : Base volume
"""

from titration_module import *


def mp_alpha_values(h, ka=1.0, kb=1.0):
    """Monoprotic Alpha Value Calculations"""
    # Convert K_b to K_bh
    kbh = kw / kb

    # Acid alpha values
    AHA = h / (h + ka)
    AA = ka / (h + ka)

    # Base alpha values
    ABH = h / (h + kbh)
    AB = kbh / (h + kbh)

    return AHA, AA, ABH, AB


def sbsa(cb, vb, ca):
    """Strong Base, Strong Acid Titrant"""
    ca = float(ca)
    vb = float(vb)
    cb = float(cb)

    # pH, [H+], [OH-]
    ph, h, oh = start_phs()

    phi = (1 + ((h - oh) / cb)) / (1 - ((h - oh) / ca))
    vol = phi * vb * cb / ca
    return vol, ph


def sasb(ca, va, cb):
    """Strong Acid, Strong Base Titrant"""

    ca = float(ca)
    va = float(va)
    cb = float(cb)

    # pH, [H+], [OH-]
    ph, h, oh = start_phs()

    phi = (1 - ((h - oh) / ca)) / (1 + ((h - oh) / cb))
    vol = phi * va * ca / cb
    return vol, ph


def wasb(ka, ca, cb, va):
    """Weak Acid, Strong Base Titrant"""

    ka = float(ka)
    ca = float(ca)
    cb = float(cb)
    va = float(va)

    # pH, [H+], [OH-]
    ph, h, oh = start_phs()

    # Alpha Values
    alphaHA, alphaA, ABH, AB = mp_alpha_values(h, ka)

    # Phi and titrant
    phi = (alphaA - ((h - oh) / ca)) / (1 + ((h - oh) / cb))
    vol = phi * ca * va / cb

    return vol, ph


def wbsa(ka, ca, cb, vb):
    """Weak Base, Strong Acid Titrant"""

    ka = float(ka)
    ca = float(ca)
    cb = float(cb)
    vb = float(vb)

    # pH, [H+], [OH-]
    ph, h, oh = start_phs()

    # Alpha Values
    alphaHA, alphaA, alphaBH, alphaB = mp_alpha_values(h, kb=ka)

    # Phi and titrant
    phi = (alphaBH + ((h - oh) / cb)) / (1 - ((h - oh) / ca))
    vol = phi * cb * vb / ca

    return vol, ph
