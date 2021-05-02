import titration_class as ts

"""pK values and names taken from http://www.periodensystem-online.de/index.php (tyty)"""

acidic_water = ts.Compound(name="Water", acidic=True, pKas=[14.0])
basic_water = ts.Compound(name="Water", acidic=False, pKas=[14.0])

# Acids
Hydrochloric = ts.Compound(name="HCl", acidic=True, pKas=[-6.5])
Hydroiodic = ts.Compound(name="HI", acidic=True, pKas=[-10])
Nitric = ts.Compound(name="HNO3", acidic=True, pKas=[-1.4])
Hydrobromic = ts.Compound(name="HBr", acidic=True, pKas=[-8.7])
Hydroperchloric = ts.Compound(name="Perchloric Acid", acidic=True, pKas=[-8])
P_Toluenesulfonic = ts.Compound(name="p-Toluenesolfonic Acid", acidic=True, pKas=[-2.8])
Propane1sulfonic = ts.Compound(name="1-propanesulfonic Acid", acidic=True, pKas=[-1.49])
Propane2sulfonic = ts.Compound(name="2-propanesulfonic Acid", acidic=True, pKas=[-1.79])
Amidosulfonic = ts.Compound(name="Amidosulfonic", acidic=True, pKas=[0.99])
Benzenesulfonic = ts.Compound(name="Benzenesulfonic", acidic=True, pKas=[-2.5])
Bromic = ts.Compound(name="Bromic", acidic=True, pKas=[0.0])
Butanesulfonic = ts.Compound(name="Butanesulfonic", acidic=True, pKas=[-1.68])
Chlorous = ts.Compound(name="Chlorous", acidic=True, pKas=[1.97])
Chlorosulfonic = ts.Compound(name="Chlorosulfonic", acidic=True, pKas=[-10.43])
Chloric = ts.Compound(name="Chloric", acidic=True, pKas=[-2.7])
Chromic = ts.Compound(name="Chromic", acidic=True, pKas=[-0.61])
Dibromoacetic = ts.Compound(name="Dibromoacetic", acidic=True, pKas=[1.39])
Dichloroacetic = ts.Compound(name="Dichloroacetic", acidic=True, pKas=[1.29])
Dichromic = ts.Compound(name="Dichromic", acidic=True, pKas=[-4.5])
Difluoroacetic = ts.Compound(name="Difluoroacetic", acidic=True, pKas=[1.24])
Difluorophosphoric = ts.Compound(name="Difluorophosphoric", acidic=True, pKas=[-1.5])
Diiodoacetic = ts.Compound(name="Diiodoacetic", acidic=True, pKas=[1.49])
Dimethylphosphonic = ts.Compound(name="Dimethylphosphonic", acidic=True, pKas=[1.29])
Disulfuric = ts.Compound(name="Disulfuric", acidic=True, pKas=[-12.0])
Dithionic = ts.Compound(name="Dithionic", acidic=True, pKas=[-3.4, 0.35])
Ethanesulfonic = ts.Compound(name="Ethanesulfonic", acidic=True, pKas=[-1.68])
Fluorosulfonic = ts.Compound(name="Fluorosulfonic", acidic=True, pKas=[-14.0])
Heptafluoropropanesulfonic = ts.Compound(name="Heptafluoropropanesulfonic", acidic=True, pKas=[-5.0])
EDTA = ts.Compound(name="EDTA", acidic=True, pKas=[0.0, 1.5, 2.00, 2.69, 6.13, 10.37])  # Pg 268 QCA
Citric = ts.Compound(name="Citric Acid", acidic=True, pKas=[3.13, 4.76, 6.40])
Carbonic = ts.Compound(name="Carbonic Acid", acidic=True, pKas=[6.37, 10.25])
Acetic = ts.Compound(name="Acetic Acid", acidic=True, pKas=[4.75])
Ammonium = ts.Compound(name="Phenol", acidic=True, pKas=[9.2])
Malic = ts.Compound(name="Malic", acidic=True, pKas=[3.46])
Enanthic = ts.Compound(name="Enanthic", acidic=True, pKas=[4.89])
Acrylic = ts.Compound(name="Acrylic", acidic=True, pKas=[4.23])
Adipic = ts.Compound(name="Adipic", acidic=True, pKas=[4.43])
Alanine = ts.Compound(name="Alanine", acidic=True, pKas=[9.87])
Formic = ts.Compound(name="Formic", acidic=True, pKas=[3.75])
Amidophosphonic = ts.Compound(name="Amidophosphonic", acidic=True, pKas=[2.74])
Arsenic = ts.Compound(name="Arsenic", acidic=True, pKas=[2.25])
Azelaic = ts.Compound(name="Azelaic", acidic=True, pKas=[4.53])
Benzoic = ts.Compound(name="Benzoic", acidic=True, pKas=[4.21])
Succinic = ts.Compound(name="Succinic", acidic=True, pKas=[4.16])
Hydrocyanic = ts.Compound(name="Hydrocyanic", acidic=True, pKas=[9.21])
Bromoacetic = ts.Compound(name="Bromoacetic", acidic=True, pKas=[2.87])
Brominous = ts.Compound(name="Brominous", acidic=True, pKas=[2.85])
Butanethiol = ts.Compound(name="Butanethiol", acidic=True, pKas=[10.66])
Butyric = ts.Compound(name="Butyric", acidic=True, pKas=[4.82])
Butylarsonic = ts.Compound(name="Butylarsonic", acidic=True, pKas=[4.23])
Butylphosphinic = ts.Compound(name="Butylphosphinic", acidic=True, pKas=[3.41])
Butylphosphonic = ts.Compound(name="Butylphosphonic", acidic=True, pKas=[2.79])
Capric = ts.Compound(name="Capric", acidic=True, pKas=[4.9])
Caproic = ts.Compound(name="Caproic", acidic=True, pKas=[4.88])
Caprylic = ts.Compound(name="Caprylic", acidic=True, pKas=[4.89])
Chloroacetic = ts.Compound(name="Chloroacetic", acidic=True, pKas=[2.83])
Crotonic = ts.Compound(name="Crotonic", acidic=True, pKas=[4.69])
Cyanic = ts.Compound(name="Cyanic", acidic=True, pKas=[3.46])
Diamidophosphonic = ts.Compound(name="Diamidophosphonic", acidic=True, pKas=[4.83])
Dihydrogenperoxodiphosphate = ts.Compound(name="Dihydrogenperoxodiphosphate", acidic=True, pKas=[5.18])
Disulfane = ts.Compound(name="Disulfane", acidic=True, pKas=[5.0])
Dithioarsenic = ts.Compound(name="Dithioarsenic", acidic=True, pKas=[2.4])
Iron_VI = ts.Compound(name="Iron_VI_", acidic=True, pKas=[3.5])
Ethanethiol = ts.Compound(name="Ethanethiol", acidic=True, pKas=[10.5])
Ethylarsonic = ts.Compound(name="Ethylarsonic", acidic=True, pKas=[3.89])
Ethylhydroperoxide = ts.Compound(name="Ethylhydroperoxide", acidic=True, pKas=[11.8])
Ethylphosphinic = ts.Compound(name="Ethylphosphinic", acidic=True, pKas=[3.29])
Ethylphosphonic = ts.Compound(name="Ethylphosphonic", acidic=True, pKas=[2.43])
Fluoroacetic = ts.Compound(name="Fluoroacetic", acidic=True, pKas=[2.57])
Hydrofluoric = ts.Compound(name="Hydrofluoric", acidic=True, pKas=[3.14])
Glycine = ts.Compound(name="Glycine", acidic=True, pKas=[9.6])
Glycolic = ts.Compound(name="Glycolic", acidic=True, pKas=[3.83])
Hexafluoroantimonic = ts.Compound(name="Hexafluoroantimonic", acidic=True, pKas=[-17.0])
Hexafluoroarsenic = ts.Compound(name="Hexafluoroarsenic", acidic=True, pKas=[-13.0])
Hexafluorophosphoric = ts.Compound(name="Hexafluorophosphoric", acidic=True, pKas=[-10.0])
Hexafluorotitan_IV = ts.Compound(name="Hexafluorotitan_IV_", acidic=True, pKas=[2.14])
Hexafluorosilicic = ts.Compound(name="Hexafluorosilicic", acidic=True, pKas=[-3.0])
Hexasulfane = ts.Compound(name="Hexasulfane", acidic=True, pKas=[3.2])
Hydrazidosulfonic = ts.Compound(name="Hydrazidosulfonic", acidic=True, pKas=[3.85])
Hydrogenperoxodiphosphate = ts.Compound(name="Hydrogenperoxodiphosphate", acidic=True, pKas=[7.67])
Hypobromous = ts.Compound(name="Hypobromous", acidic=True, pKas=[8.68])
Hypochlorous = ts.Compound(name="Hypochlorous", acidic=True, pKas=[7.54])
Hypodiphosphoric = ts.Compound(name="Hypodiphosphoric", acidic=True, pKas=[2.22])
Hypoiodous = ts.Compound(name="Hypoiodous", acidic=True, pKas=[10.64])
Hypophosphorous = ts.Compound(name="Hypophosphorous", acidic=True, pKas=[2.23])
Hypo_nitrous = ts.Compound(name="Hypo-nitrousacid", acidic=True, pKas=[7.21])
Hypothiocyanitic = ts.Compound(name="Hypothiocyanitic", acidic=True, pKas=[5.3])
Imidodiphosphoric = ts.Compound(name="Imidodiphosphoric", acidic=True, pKas=[2.0])
Iodic = ts.Compound(name="Iodic", acidic=True, pKas=[0.804])
Iodoacetic = ts.Compound(name="Iodoacetic", acidic=True, pKas=[3.13])
Isocyanic = ts.Compound(name="Isocyanic", acidic=True, pKas=[3.92])
Isopropylhydroperoxide = ts.Compound(name="Isopropylhydroperoxide", acidic=True, pKas=[12.1])
Isopropyloxonium = ts.Compound(name="Isopropyloxonium", acidic=True, pKas=[-3.2])
Isothiocyanic = ts.Compound(name="Isothiocyanic", acidic=True, pKas=[-1.28])
Suberic = ts.Compound(name="Suberic", acidic=True, pKas=[4.51])
Malonic = ts.Compound(name="Malonic", acidic=True, pKas=[2.83])
Manganese_VI = ts.Compound(name="Manganese_VI_", acidic=True, pKas=[5.0])
Mellitic = ts.Compound(name="Mellitic", acidic=True, pKas=[1.4])
Metaarsenous = ts.Compound(name="Metaarsenous", acidic=True, pKas=[9.28])
Metaboric = ts.Compound(name="Metaboric", acidic=True, pKas=[9.12])
Metagermanic = ts.Compound(name="Metagermanic", acidic=True, pKas=[8.59])
Metasilicic = ts.Compound(name="Metasilicic", acidic=True, pKas=[9.51])
Metaniobic = ts.Compound(name="Metaniobic", acidic=True, pKas=[7.4])
Metaperiodic = ts.Compound(name="Metaperiodic", acidic=True, pKas=[1.64])
Metatantalic = ts.Compound(name="Metatantalic", acidic=True, pKas=[9.6])
Metavanadium_V = ts.Compound(name="Metavanadium_V_", acidic=True, pKas=[3.8])
Methanal = ts.Compound(name="Methanal", acidic=True, pKas=[13.3])
Methaneselenol = ts.Compound(name="Methaneselenol", acidic=True, pKas=[5.2])
Methanesulfonic = ts.Compound(name="Methanesulfonic", acidic=True, pKas=[-1.92])
Methanethiol = ts.Compound(name="Methanethiol", acidic=True, pKas=[10.4])
Methylarsonic = ts.Compound(name="Methylarsonic", acidic=True, pKas=[3.41])
Methylhydroperoxide = ts.Compound(name="Methylhydroperoxide", acidic=True, pKas=[11.5])
Methylphosphinic = ts.Compound(name="Methylphosphinic", acidic=True, pKas=[3.08])
Methylphosphonic = ts.Compound(name="Methylphosphonic", acidic=True, pKas=[2.38])
Methylsulfinic = ts.Compound(name="Methylsulfinic", acidic=True, pKas=[2.28])
Lactic = ts.Compound(name="Lactic", acidic=True, pKas=[3.9])
Molybdic = ts.Compound(name="Molybdic", acidic=True, pKas=[3.7])
Monofluorophosphoric = ts.Compound(name="Monofluorophosphoric", acidic=True, pKas=[0.5])
Nitramine = ts.Compound(name="Nitramine", acidic=True, pKas=[6.6])
Nitromethane = ts.Compound(name="Nitromethane", acidic=True, pKas=[10.2])
Octanesulfonic = ts.Compound(name="Octanesulfonic", acidic=True, pKas=[-1.41])
Ortho_periodic = ts.Compound(name="Ortho-periodicacid", acidic=True, pKas=[3.29])
Orthoantimonic = ts.Compound(name="Orthoantimonic", acidic=True, pKas=[2.55])
Orthoboric = ts.Compound(name="Orthoboric", acidic=True, pKas=[9.25])
Orthogermanic = ts.Compound(name="Orthogermanic", acidic=True, pKas=[8.68])
Orthosilicic = ts.Compound(name="Orthosilicic", acidic=True, pKas=[9.66])
Orthotelluric = ts.Compound(name="Orthotelluric", acidic=True, pKas=[7.7])
Orthovanadic = ts.Compound(name="Orthovanadic", acidic=True, pKas=[2.6])
Oxalic = ts.Compound(name="Oxalic", acidic=True, pKas=[1.23])
Pelargonic = ts.Compound(name="Pelargonic", acidic=True, pKas=[4.95])
Pentacarbonylmanganese = ts.Compound(name="Pentacarbonylmanganese", acidic=True, pKas=[7.1])
Pentafluoroethanesulfonic = ts.Compound(name="Pentafluoroethanesulfonic", acidic=True, pKas=[-5.1])
Pentasulfane = ts.Compound(name="Pentasulfane", acidic=True, pKas=[3.5])
Perchlorylamide = ts.Compound(name="Perchlorylamide", acidic=True, pKas=[8.6])
Perchlorylamine = ts.Compound(name="Perchlorylamine", acidic=True, pKas=[3.7])
Perchromic = ts.Compound(name="Perchromic", acidic=True, pKas=[4.95])
Permanganic = ts.Compound(name="Permanganic", acidic=True, pKas=[-2.25])
Perosmic = ts.Compound(name="Perosmic", acidic=True, pKas=[7.2])
Peroxoformic = ts.Compound(name="Peroxoformic", acidic=True, pKas=[7.1])
Peroxobutyric = ts.Compound(name="Peroxobutyric", acidic=True, pKas=[8.2])
Peroxodiphosphoric = ts.Compound(name="Peroxodiphosphoric", acidic=True, pKas=[-3.0])
Peroxodisulfuric = ts.Compound(name="Peroxodisulfuric", acidic=True, pKas=[-3.5])
Peroxyacetic = ts.Compound(name="Peroxyacetic", acidic=True, pKas=[8.2])
Peroxohypositrous = ts.Compound(name="Peroxohypositrous", acidic=True, pKas=[2.51])
Peroxopropionic = ts.Compound(name="Peroxopropionic", acidic=True, pKas=[8.1])
Peroxonitric = ts.Compound(name="Peroxonitric", acidic=True, pKas=[-5.0])
Peroxo_nitrous = ts.Compound(name="Peroxo-nitrousacid", acidic=True, pKas=[6.8])
Peroxosulphuric = ts.Compound(name="Peroxosulphuric", acidic=True, pKas=[0.8])
Perrhenic = ts.Compound(name="Perrhenic", acidic=True, pKas=[-1.25])
Perruthenic = ts.Compound(name="Perruthenic", acidic=True, pKas=[11.2])
Pertechnetic = ts.Compound(name="Pertechnetic", acidic=True, pKas=[0.3])
Phenol = ts.Compound(name="Phenol", acidic=True, pKas=[9.99])
Phenylphosphonic = ts.Compound(name="Phenylphosphonic", acidic=True, pKas=[1.83])
Phenylsulfinic = ts.Compound(name="Phenylsulfinic", acidic=True, pKas=[1.84])
Phosphorous = ts.Compound(name="Phosphorous", acidic=True, pKas=[1.92])
Phosphoric = ts.Compound(name="Phosphoric", acidic=True, pKas=[2.13])
Pimelic = ts.Compound(name="Pimelic", acidic=True, pKas=[4.47])
Poly = ts.Compound(name="Poly", acidic=True, pKas=[4.09])
Propanethiol = ts.Compound(name="Propanethiol", acidic=True, pKas=[10.65])
Propionic = ts.Compound(name="Propionic", acidic=True, pKas=[4.87])
Propylarsonic = ts.Compound(name="Propylarsonic", acidic=True, pKas=[4.21])
Propylphosphinic = ts.Compound(name="Propylphosphinic", acidic=True, pKas=[3.46])
Propylphosphonic = ts.Compound(name="Propylphosphonic", acidic=True, pKas=[2.49])
Salicylic = ts.Compound(name="Salicylic", acidic=True, pKas=[2.75])
Nitrous = ts.Compound(name="Nitrous", acidic=True, pKas=[3.35])
Sulfuric = ts.Compound(name="Sulfuric", acidic=True, pKas=[-3.0])
Hydrogensulfide = ts.Compound(name="Hydrogensulfide", acidic=True, pKas=[7.06])
Sulphurous = ts.Compound(name="Sulphurous", acidic=True, pKas=[1.92])
Seaborgium_VI = ts.Compound(name="Seaborgium_VI_", acidic=True, pKas=[3.75])
Sebacic = ts.Compound(name="Sebacic", acidic=True, pKas=[4.72])
Selenous = ts.Compound(name="Selenous", acidic=True, pKas=[2.62])
Selenophenol = ts.Compound(name="Selenophenol", acidic=True, pKas=[5.9])
Selenophosphoric = ts.Compound(name="Selenophosphoric", acidic=True, pKas=[0.02])
Selenic = ts.Compound(name="Selenic", acidic=True, pKas=[-3.0])
Hydroselenic = ts.Compound(name="Hydroselenic", acidic=True, pKas=[3.73])
Hydrazoic = ts.Compound(name="Hydrazoic", acidic=True, pKas=[4.76])
Tartronic = ts.Compound(name="Tartronic", acidic=True, pKas=[2.3])
Telluric = ts.Compound(name="Telluric", acidic=True, pKas=[2.64, 2.7])
Tetracarbonyliron = ts.Compound(name="Tetracarbonyliron", acidic=True, pKas=[4.4])
Tetrafluoroboric = ts.Compound(name="Tetrafluoroboric", acidic=True, pKas=[-0.4])
Tetraphosphoric = ts.Compound(name="Tetraphosphoric", acidic=True, pKas=[0.5])
Tetrasulfane = ts.Compound(name="Tetrasulfane", acidic=True, pKas=[3.8])
Tetrathiophosphoric = ts.Compound(name="Tetrathiophosphoric", acidic=True, pKas=[1.5])
Thioarsenic = ts.Compound(name="Thioarsenic", acidic=True, pKas=[3.3])
Thiocyanic = ts.Compound(name="Thiocyanic", acidic=True, pKas=[-1.85])
Thiophenol = ts.Compound(name="Thiophenol", acidic=True, pKas=[6.52])
Thiophosphoric = ts.Compound(name="Thiophosphoric", acidic=True, pKas=[1.79])
Thiosulfuric = ts.Compound(name="Thiosulfuric", acidic=True, pKas=[0.6])
Thioselenic = ts.Compound(name="Thioselenic", acidic=True, pKas=[0.99])
Tribromoacetic = ts.Compound(name="Tribromoacetic", acidic=True, pKas=[0.72])
Trichloroacetic = ts.Compound(name="Trichloroacetic", acidic=True, pKas=[0.65])
Trifluoroacetic = ts.Compound(name="Trifluoroacetic", acidic=True, pKas=[0.23])
Trifluoromethanesulfonic = ts.Compound(name="Trifluoromethanesulfonic", acidic=True, pKas=[-5.21])
Trihydrogenperoxodiphosphate = ts.Compound(name="Trihydrogenperoxodiphosphate", acidic=True, pKas=[0.5])
Triiodoacetic = ts.Compound(name="Triiodoacetic", acidic=True, pKas=[0.9])
Trioxide = ts.Compound(name="Trioxide", acidic=True, pKas=[9.5])
Triphosphoric = ts.Compound(name="Triphosphoric", acidic=True, pKas=[1.0])
Triselenocarbonic = ts.Compound(name="Triselenocarbonic", acidic=True, pKas=[1.16])
Trisulfane = ts.Compound(name="Trisulfane", acidic=True, pKas=[4.2])
Trithiocarbonic = ts.Compound(name="Trithiocarbonic", acidic=True, pKas=[2.68])
Valeric = ts.Compound(name="Valeric", acidic=True, pKas=[4.84])
HydrogenHyperoxide = ts.Compound(name="Hydrogenhyperoxide", acidic=True, pKas=[4.7])
HydrogenOzonide = ts.Compound(name="Hydrogenozonide", acidic=True, pKas=[8.2])
HydrogenPeroxide = ts.Compound(name="Hydrogenperoxide", acidic=True, pKas=[11.62])
Tartaric = ts.Compound(name="Tartaric", acidic=True, pKas=[2.98])
Tungstic = ts.Compound(name="Tungstic", acidic=True, pKas=[3.8])
Xenon_VI = ts.Compound(name="Xenon_VI_", acidic=True, pKas=[10.5])
Xenon_VIII = ts.Compound(name="Xenon_VIII_", acidic=True, pKas=[2.0])

# Bases
CesiumHydroxide = ts.Compound(name="CsOH", acidic=False, pKas=[15.76])
FranciumHydroxide = ts.Compound(name="FrOH", acidic=False, pKas=[15.7])
RubidiumHydroxide = ts.Compound(name="RbOH", acidic=False, pKas=[15.4])
LithiumHydroxide = ts.Compound(name="LiOH", acidic=False, pKas=[14.36])
CalciumHydroxide = ts.Compound(name="calcium_hydroxide", acidic=False, pKas=[12.6, 11.57])
RadiumHydroxide = ts.Compound(name="Radiumhydroxide", acidic=False, pKas=[14.0])
BariumHydroxide = ts.Compound(name="Bariumhydroxide", acidic=False, pKas=[13.85])
SodiumHydroxide = ts.Compound(name="NaOH", acidic=False, pKas=[13.8])
StrontiumHydroxide = ts.Compound(name="Strontiumhydroxide", acidic=False, pKas=[13.7])
PotassiumHydroxide = ts.Compound(name="KOH", acidic=False, pKas=[13.5])
Thallium_I_Hydroxide = ts.Compound(name="Thallium_I_hydroxide", acidic=False, pKas=[13.36])
MagnesiumHydroxide = ts.Compound(name="Magnesiumhydroxide", acidic=False, pKas=[12.2])
Manganese_II_Hydroxide = ts.Compound(name="Manganese_II_hydroxide", acidic=False, pKas=[12.0])
Indium_I_Hydroxide = ts.Compound(name="Indium_I_hydroxide_InOH", acidic=False, pKas=[11.83])
SilverHydroxide = ts.Compound(name="Silverhydroxide", acidic=False, pKas=[11.5])
Neptunyl_V_Hydroxide = ts.Compound(name="Neptunyl_V_hydroxide", acidic=False, pKas=[11.3])
Protactinyl_V_Hydroxide = ts.Compound(name="Protactinyl_V_hydroxide", acidic=False, pKas=[11.19])
ActiniumHydroxide = ts.Compound(name="Actiniumhydroxide", acidic=False, pKas=[11.1])
Americium_III_Hydroxide = ts.Compound(name="Americium_III_hydroxide", acidic=False, pKas=[11.1])
Curium_III_Hydroxide = ts.Compound(name="Curium_III_hydroxide", acidic=False, pKas=[11.1])
Plutonium_III_Hydroxide = ts.Compound(name="Plutonium_III_hydroxide", acidic=False, pKas=[11.1])
Iron_II_Hydroxide = ts.Compound(name="Iron_II_hydroxide", acidic=False, pKas=[11.07])
Triethylamine = ts.Compound(name="Triethylamine", acidic=False, pKas=[11.01])
Dipropylamine = ts.Compound(name="Dipropylamine", acidic=False, pKas=[10.91])
ethylamine = ts.Compound(name="ethylamine", acidic=False, pKas=[10.75])
Dimethylamine = ts.Compound(name="Dimethylamine", acidic=False, pKas=[10.73])
Methylamine = ts.Compound(name="Methylamine", acidic=False, pKas=[10.66])
Tripropylamine = ts.Compound(name="Tripropylamine", acidic=False, pKas=[10.66])
Propylamine = ts.Compound(name="Propylamine", acidic=False, pKas=[10.57])
Hydrogenxenonate_VIII_ = ts.Compound(name="Hydrogenxenonate_VIII_", acidic=False, pKas=[10.5])
Diethylamine = ts.Compound(name="Diethylamine", acidic=False, pKas=[10.49])
CadmiumHydroxide = ts.Compound(name="Cadmiumhydroxide", acidic=False, pKas=[10.4])
Nickel_II_Hydroxide = ts.Compound(name="Nickel_II_hydroxide", acidic=False, pKas=[10.22])
Trimethylamine = ts.Compound(name="Trimethylamine", acidic=False, pKas=[9.81])
LanthanumHydroxide = ts.Compound(name="Lanthanumhydroxide", acidic=False, pKas=[9.8])
Plutonyl_V_Hydroxide = ts.Compound(name="Plutonyl_V_hydroxide", acidic=False, pKas=[9.7])
Cobalt_II_Hydroxide = ts.Compound(name="Cobalt_II_hydroxide", acidic=False, pKas=[9.63])
Lead_II_Hydroxide = ts.Compound(name="Lead_II_hydroxide", acidic=False, pKas=[9.62])
Cerium_III_Hydroxide = ts.Compound(name="Cerium_III_hydroxide", acidic=False, pKas=[9.6])
YttriumHydroxide = ts.Compound(name="Yttriumhydroxide", acidic=False, pKas=[9.6])
Neodymium_III_Hydroxide = ts.Compound(name="Neodymium_III_hydroxide", acidic=False, pKas=[9.5])
Praseodymium_III_Hydroxide = ts.Compound(name="Praseodymium_III_hydroxide", acidic=False, pKas=[9.4])
Promethium_III_Hydroxide = ts.Compound(name="Promethium_III_hydroxide", acidic=False, pKas=[9.4])
Samarium_III_Hydroxide = ts.Compound(name="Samarium_III_hydroxide", acidic=False, pKas=[9.4])
ammonia = ts.Compound(name="ammonia", acidic=False, pKas=[9.25])
Platinum_II_Hydroxide = ts.Compound(name="Platinum_II_hydroxide", acidic=False, pKas=[9.2])
ZincHydroxide = ts.Compound(name="Zinchydroxide", acidic=False, pKas=[8.99])
Europium_III_Hydroxide = ts.Compound(name="Europium_III_hydroxide", acidic=False, pKas=[8.8])
Terbium_III_Hydroxide = ts.Compound(name="Terbium_III_hydroxide", acidic=False, pKas=[8.8])
Trimethylphosphine = ts.Compound(name="Trimethylphosphine", acidic=False, pKas=[8.65])
BerylliumHydroxide = ts.Compound(name="Berylliumhydroxide", acidic=False, pKas=[8.6])
Perchlorylimide = ts.Compound(name="Perchlorylimide", acidic=False, pKas=[8.6])
Dysprosium_III_Hydroxide = ts.Compound(name="Dysprosium_III_hydroxide", acidic=False, pKas=[8.5])
Copper_II_Hydroxide = ts.Compound(name="Copper_II_hydroxide", acidic=False, pKas=[8.5])
Holmium_III_Hydroxide = ts.Compound(name="Holmium_III_hydroxide", acidic=False, pKas=[8.4])
Erbium_III_Hydroxide = ts.Compound(name="Erbium_III_hydroxide", acidic=False, pKas=[8.3])
GadoliniumHydroxide = ts.Compound(name="Gadoliniumhydroxide", acidic=False, pKas=[8.3])
Thulium_III_Hydroxide = ts.Compound(name="Thulium_III_hydroxide", acidic=False, pKas=[8.3])
Ytterbium_III_Hydroxide = ts.Compound(name="Ytterbium_III_hydroxide", acidic=False, pKas=[8.3])
Hydroxylamine = ts.Compound(name="Hydroxylamine", acidic=False, pKas=[8.2])
LutetiumHydroxide = ts.Compound(name="Lutetiumhydroxide", acidic=False, pKas=[8.2])
Ethylhydrazine = ts.Compound(name="Ethylhydrazine", acidic=False, pKas=[7.99])
Hydrazine = ts.Compound(name="Hydrazine", acidic=False, pKas=[7.93])
Methylhydrazine = ts.Compound(name="Methylhydrazine", acidic=False, pKas=[7.87])
Peroxodiphosphate = ts.Compound(name="Peroxodiphosphate", acidic=False, pKas=[7.67])
Iron_III_Hydroxide = ts.Compound(name="Iron_III_hydroxide", acidic=False, pKas=[6.89])
Uranyl_VI_Hydroxide = ts.Compound(name="Uranyl_VI_hydroxide", acidic=False, pKas=[6.8])
Plutonium_IV_Hydroxide = ts.Compound(name="Plutonium_IV_hydroxide", acidic=False, pKas=[6.7])
ScandiumHydroxide = ts.Compound(name="Scandiumhydroxide", acidic=False, pKas=[6.4])
Bismuth_III_Hydroxide = ts.Compound(name="Bismuth_III_hydroxide", acidic=False, pKas=[6.38])
Vanadyl_IV_hydroxide_VO = ts.Compound(name="Vanadyl_IV_hydroxide_VO", acidic=False, pKas=[6.34])
AluminumHydroxide = ts.Compound(name="Aluminumhydroxide", acidic=False, pKas=[5.86])
Thorium_IV_Hydroxide = ts.Compound(name="Thorium_IV_hydroxide", acidic=False, pKas=[5.8])
Chromium_III_Hydroxide = ts.Compound(name="Chromium_III_hydroxide", acidic=False, pKas=[5.7])
Uranium_IV_Hydroxide = ts.Compound(name="Uranium_IV_hydroxide", acidic=False, pKas=[5.65])
Neptunium_IV_Hydroxide = ts.Compound(name="Neptunium_IV_hydroxide", acidic=False, pKas=[5.3])
Rutherfordium_IV_Hydroxide = ts.Compound(name="Rutherfordium_IV_hydroxide", acidic=False, pKas=[5.3])
Phenylhydrazine = ts.Compound(name="Phenylhydrazine", acidic=False, pKas=[5.21])
Indium_III_hydroxide_In = ts.Compound(name="Indium_III_hydroxide_In", acidic=False, pKas=[5.16])
GalliumHydroxide = ts.Compound(name="Galliumhydroxide", acidic=False, pKas=[4.75])
aniline = ts.Compound(name="aniline", acidic=False, pKas=[4.6])
Vanadium_III_hydroxide_V = ts.Compound(name="Vanadium_III_hydroxide_V", acidic=False, pKas=[4.1])
Plutonyl_VI_Hydroxide = ts.Compound(name="Plutonyl_VI_hydroxide", acidic=False, pKas=[4.05])
Gold_I_Hydroxide = ts.Compound(name="Gold_I_hydroxide", acidic=False, pKas=[3.8])
Tin_II_Hydroxide = ts.Compound(name="Tin_II_hydroxide", acidic=False, pKas=[3.66])
Tin_IV_Hydroxide = ts.Compound(name="Tin_IV_hydroxide", acidic=False, pKas=[3.32])
Triphenylphosphine = ts.Compound(name="Triphenylphosphine", acidic=False, pKas=[2.73])
Methylphosphine = ts.Compound(name="Methylphosphine", acidic=False, pKas=[2.7])
Mercury_II_Hydroxide = ts.Compound(name="Mercury_II_hydroxide", acidic=False, pKas=[2.5])
Palladium_II_Hydroxide = ts.Compound(name="Palladium_II_hydroxide", acidic=False, pKas=[2.46])
Technetyl_IV_Hydroxide = ts.Compound(name="Technetyl_IV_hydroxide", acidic=False, pKas=[2.43])
Titanyl_IV_dihydroxide = ts.Compound(name="Titanyl_IV_dihydroxide", acidic=False, pKas=[2.4])
Cerium_IV_Hydroxide = ts.Compound(name="Cerium_IV_hydroxide", acidic=False, pKas=[2.29])
Thallium_III_Hydroxide = ts.Compound(name="Thallium_III_hydroxide", acidic=False, pKas=[1.9])
Astatine_I_Hydroxide = ts.Compound(name="Astatine_I_hydroxide", acidic=False, pKas=[1.5])
Antimony_III_Hydroxide = ts.Compound(name="Antimony_III_hydroxide", acidic=False, pKas=[1.42])
Protactinium_IV_Hydroxide = ts.Compound(name="Protactinium_IV_hydroxide", acidic=False, pKas=[1.25])
Diphenylamine = ts.Compound(name="Diphenylamine", acidic=False, pKas=[0.78])
Hafnium_IV_Hydroxide = ts.Compound(name="Hafnium_IV_hydroxide", acidic=False, pKas=[0.52])
Zirconium_IV_Hydroxide = ts.Compound(name="Zirconium_IV_hydroxide", acidic=False, pKas=[0.5])

# Lists of compound

acids = [
    Hydrochloric,
    Hydroiodic,
    Nitric,
    Hydrobromic,
    Hydroperchloric,
    P_Toluenesulfonic,
    Propane1sulfonic,
    Propane2sulfonic,
    Amidosulfonic,
    Benzenesulfonic,
    Bromic,
    Hydrobromic,
    Butanesulfonic,
    Chlorous,
    Chlorosulfonic,
    Chloric,
    Chromic,
    Dibromoacetic,
    Dichloroacetic,
    Dichromic,
    Difluoroacetic,
    Difluorophosphoric,
    Diiodoacetic,
    Dimethylphosphonic,
    Disulfuric,
    Dithionic,
    Ethanesulfonic,
    Fluorosulfonic,
    Heptafluoropropanesulfonic,
    EDTA,
    Citric,
    Carbonic,
    Acetic,
    Ammonium,
    Malic,
    Enanthic,
    Acrylic,
    Adipic,
    Alanine,
    Formic,
    Amidophosphonic,
    Arsenic,
    Azelaic,
    Benzoic,
    Succinic,
    Hydrocyanic,
    Bromoacetic,
    Brominous,
    Butanethiol,
    Butyric,
    Butylarsonic,
    Butylphosphinic,
    Butylphosphonic,
    Capric,
    Caproic,
    Caprylic,
    Chloroacetic,
    Citric,
    Crotonic,
    Cyanic,
    Diamidophosphonic,
    Dihydrogenperoxodiphosphate,
    Disulfane,
    Dithioarsenic,
    Iron_VI,
    Acetic,
    Ethanethiol,
    Ethylarsonic,
    Ethylhydroperoxide,
    Ethylphosphinic,
    Ethylphosphonic,
    Fluoroacetic,
    Hydrofluoric,
    Glycine,
    Glycolic,
    Hexafluoroantimonic,
    Hexafluoroarsenic,
    Hexafluorophosphoric,
    Hexafluorotitan_IV,
    Hexafluorosilicic,
    Hexasulfane,
    Hydrazidosulfonic,
    Hydrogenperoxodiphosphate,
    Hypobromous,
    Hypochlorous,
    Hypodiphosphoric,
    Hypoiodous,
    Hypophosphorous,
    Hypo_nitrous,
    Hypothiocyanitic,
    Imidodiphosphoric,
    Iodic,
    Iodoacetic,
    Hydroiodic,
    Isocyanic,
    Isopropylhydroperoxide,
    Isopropyloxonium,
    Isothiocyanic,
    Carbonic,
    Suberic,
    Malonic,
    Manganese_VI,
    Mellitic,
    Metaarsenous,
    Metaboric,
    Metagermanic,
    Metasilicic,
    Metaniobic,
    Metaperiodic,
    Metatantalic,
    Metavanadium_V,
    Methanal,
    Methaneselenol,
    Methanesulfonic,
    Methanethiol,
    Methylarsonic,
    Methylhydroperoxide,
    Methylphosphinic,
    Methylphosphonic,
    Methylsulfinic,
    Lactic,
    Molybdic,
    Monofluorophosphoric,
    Nitramine,
    Nitromethane,
    Octanesulfonic,
    Ortho_periodic,
    Orthoantimonic,
    Orthoboric,
    Orthogermanic,
    Orthosilicic,
    Orthotelluric,
    Orthovanadic,
    Oxalic,
    Pelargonic,
    Pentacarbonylmanganese,
    Pentafluoroethanesulfonic,
    Pentasulfane,
    Perchlorylamide,
    Perchlorylamine,
    Perchromic,
    Permanganic,
    Perosmic,
    Peroxoformic,
    Peroxobutyric,
    Peroxodiphosphoric,
    Peroxodisulfuric,
    Peroxyacetic,
    Peroxohypositrous,
    Peroxopropionic,
    Peroxonitric,
    Peroxo_nitrous,
    Peroxosulphuric,
    Perrhenic,
    Perruthenic,
    Pertechnetic,
    Phenol,
    Phenylphosphonic,
    Phenylsulfinic,
    Phosphorous,
    Phosphoric,
    Pimelic,
    Poly,
    Propanethiol,
    Propionic,
    Propylarsonic,
    Propylphosphinic,
    Propylphosphonic,
    Salicylic,
    Nitric,
    Nitrous,
    Hydrochloric,
    Sulfuric,
    Hydrogensulfide,
    Sulphurous,
    Seaborgium_VI,
    Sebacic,
    Selenous,
    Selenophenol,
    Selenophosphoric,
    Selenic,
    Hydroselenic,
    Hydrazoic,
    Tartronic,
    Telluric,
    Tetracarbonyliron,
    Tetrafluoroboric,
    Tetraphosphoric,
    Tetrasulfane,
    Tetrathiophosphoric,
    Thioarsenic,
    Thiocyanic,
    Thiophenol,
    Thiophosphoric,
    Thiosulfuric,
    Thioselenic,
    Tribromoacetic,
    Trichloroacetic,
    Trifluoroacetic,
    Trifluoromethanesulfonic,
    Trihydrogenperoxodiphosphate,
    Triiodoacetic,
    Trioxide,
    Triphosphoric,
    Triselenocarbonic,
    Trisulfane,
    Trithiocarbonic,
    Valeric,
    HydrogenHyperoxide,
    HydrogenOzonide,
    HydrogenPeroxide,
    Tartaric,
    Tungstic,
    Xenon_VI,
    Xenon_VIII,
]

bases = [
    CesiumHydroxide,
    FranciumHydroxide,
    RubidiumHydroxide,
    LithiumHydroxide,
    CalciumHydroxide,
    RadiumHydroxide,
    BariumHydroxide,
    SodiumHydroxide,
    StrontiumHydroxide,
    PotassiumHydroxide,
    Thallium_I_Hydroxide,
    MagnesiumHydroxide,
    Manganese_II_Hydroxide,
    Indium_I_Hydroxide,
    SilverHydroxide,
    Neptunyl_V_Hydroxide,
    Protactinyl_V_Hydroxide,
    ActiniumHydroxide,
    Americium_III_Hydroxide,
    Curium_III_Hydroxide,
    Plutonium_III_Hydroxide,
    Iron_II_Hydroxide,
    Triethylamine,
    Dipropylamine,
    ethylamine,
    Dimethylamine,
    Methylamine,
    Tripropylamine,
    Propylamine,
    Hydrogenxenonate_VIII_,
    Diethylamine,
    CadmiumHydroxide,
    Nickel_II_Hydroxide,
    Trimethylamine,
    LanthanumHydroxide,
    Plutonyl_V_Hydroxide,
    Cobalt_II_Hydroxide,
    Lead_II_Hydroxide,
    Cerium_III_Hydroxide,
    YttriumHydroxide,
    Neodymium_III_Hydroxide,
    Praseodymium_III_Hydroxide,
    Promethium_III_Hydroxide,
    Samarium_III_Hydroxide,
    ammonia,
    Platinum_II_Hydroxide,
    ZincHydroxide,
    Europium_III_Hydroxide,
    Terbium_III_Hydroxide,
    Trimethylphosphine,
    BerylliumHydroxide,
    Perchlorylimide,
    Dysprosium_III_Hydroxide,
    Copper_II_Hydroxide,
    Holmium_III_Hydroxide,
    Erbium_III_Hydroxide,
    GadoliniumHydroxide,
    Thulium_III_Hydroxide,
    Ytterbium_III_Hydroxide,
    Hydroxylamine,
    LutetiumHydroxide,
    Ethylhydrazine,
    Hydrazine,
    Methylhydrazine,
    Peroxodiphosphate,
    Iron_III_Hydroxide,
    Uranyl_VI_Hydroxide,
    Plutonium_IV_Hydroxide,
    ScandiumHydroxide,
    Bismuth_III_Hydroxide,
    Vanadyl_IV_hydroxide_VO,
    AluminumHydroxide,
    Thorium_IV_Hydroxide,
    Chromium_III_Hydroxide,
    Uranium_IV_Hydroxide,
    Neptunium_IV_Hydroxide,
    Rutherfordium_IV_Hydroxide,
    Phenylhydrazine,
    Indium_III_hydroxide_In,
    GalliumHydroxide,
    aniline,
    Vanadium_III_hydroxide_V,
    Plutonyl_VI_Hydroxide,
    Gold_I_Hydroxide,
    Tin_II_Hydroxide,
    Tin_IV_Hydroxide,
    Triphenylphosphine,
    Methylphosphine,
    Mercury_II_Hydroxide,
    Palladium_II_Hydroxide,
    Technetyl_IV_Hydroxide,
    Titanyl_IV_dihydroxide,
    Cerium_IV_Hydroxide,
    Thallium_III_Hydroxide,
    Astatine_I_Hydroxide,
    Antimony_III_Hydroxide,
    Protactinium_IV_Hydroxide,
    Diphenylamine,
    Hafnium_IV_Hydroxide,
    Zirconium_IV_Hydroxide,
]

acids.sort(key=lambda x: x.pKas[0])
bases.sort(key=lambda x: x.pKas[0])

strong_acids = [x for x in acids if x.acidic and len(x.pKas) == 1 and x.pKas[0] <= 0]
strong_bases = [x for x in bases if not x.acidic and len(x.pKas) == 1 and x.pKas[0] >= 14]

weak_acids = [x for x in acids if x not in strong_acids]
weak_bases = [x for x in bases if x not in strong_bases]
