from main import *

"""PUT BELOW HERE"""

# Strong monoprotic acid titrant, Strong monoprotic basic analyte
ca = 0.5  # M
pka1 = 4

vb = 0.01  # L
cb = 0.5  # M

basic_analyte = False
strong_analyte = False

pkas = [pka1]


"""PUT ABOVE HERE"""

ph, h, oh = start_phs()

print(ph)

alphas = alpha_values(pkas, basic_analyte, strong_analyte)