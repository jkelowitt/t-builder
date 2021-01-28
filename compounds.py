import titration_class as ts

"""pK values and names taken from http://www.periodensystem-online.de/index.php (tyty)"""

acidic_water = ts.Compound(name="Water", acidic=True, pKs=[14.0], strong=False)
basic_water = ts.Compound(name="Water", acidic=False, pKs=[14.0], strong=False)

# Acids
Hydrochloric = ts.Compound(name="HCl", acidic=True, pKs=[-6.5], strong=True)
Hydroiodic= ts.Compound(name="HI", acidic=True, pKs=[-10], strong=True)
Nitric = ts.Compound(name="HNO3", acidic=True, pKs=[-1.4], strong=True)
Hydrobromic = ts.Compound(name="HBr", acidic=True, pKs=[-8.7], strong=True)
Hydroperchloric= ts.Compound(name="Perchloric Acid", acidic=True, pKs=[-8], strong=True)
P_toluenesulfonic= ts.Compound(name="p-Toluenesolfonic Acid", acidic=True, pKs=[-2.8], strong=True)
Propane1sulfonic = ts.Compound(name="1-propanesulfonicacid", acidic=True, pKs=[-1.49], strong=True)
Propane2sulfonic = ts.Compound(name="2-propanesulfonicacid", acidic=True, pKs=[-1.79], strong=True)
Amidosulfonic = ts.Compound(name="Amidosulfonic", acidic=True, pKs=[0.99], strong=True)
Benzenesulfonic = ts.Compound(name="Benzenesulfonic", acidic=True, pKs=[-2.5], strong=True)
Bromic = ts.Compound(name="Bromic", acidic=True, pKs=[0.0], strong=True)
Butanesulfonic = ts.Compound(name="Butanesulfonic", acidic=True, pKs=[-1.68], strong=True)
Chlorous = ts.Compound(name="Chlorous", acidic=True, pKs=[1.97], strong=True)
Chlorosulfonic = ts.Compound(name="Chlorosulfonic", acidic=True, pKs=[-10.43], strong=True)
Chloric = ts.Compound(name="Chloric", acidic=True, pKs=[-2.7], strong=True)
Chromic = ts.Compound(name="Chromic", acidic=True, pKs=[-0.61], strong=True)
Dibromoacetic = ts.Compound(name="Dibromoacetic", acidic=True, pKs=[1.39], strong=True)
Dichloroacetic = ts.Compound(name="Dichloroacetic", acidic=True, pKs=[1.29], strong=True)
Dichromic = ts.Compound(name="Dichromic", acidic=True, pKs=[-4.5], strong=True)
Difluoroacetic = ts.Compound(name="Difluoroacetic", acidic=True, pKs=[1.24], strong=True)
Difluorophosphoric = ts.Compound(name="Difluorophosphoric", acidic=True, pKs=[-1.5], strong=True)
Diiodoacetic = ts.Compound(name="Diiodoacetic", acidic=True, pKs=[1.49], strong=True)
Dimethylphosphonic = ts.Compound(name="Dimethylphosphonic", acidic=True, pKs=[1.29], strong=True)
Disulfuric = ts.Compound(name="Disulfuric", acidic=True, pKs=[-12.0], strong=True)
Dithionic = ts.Compound(name="Dithionic", acidic=True, pKs=[-3.4, 0.35], strong=True)
Ethanesulfonic = ts.Compound(name="Ethanesulfonic", acidic=True, pKs=[-1.68], strong=True)
Fluorosulfonic = ts.Compound(name="Fluorosulfonic", acidic=True, pKs=[-14.0], strong=True)
Heptafluoropropanesulfonic = ts.Compound(name="Heptafluoropropanesulfonic", acidic=True, pKs=[-5.0],strong=True)
EDTA = ts.Compound(name="EDTA", acidic=True, pKs=[0.0, 1.5, 2.00, 2.69, 6.13, 10.37], strong=False)  # Pg 268 QCA
Citric = ts.Compound(name="Citric Acid", acidic=True, pKs=[3.13, 4.76, 6.40], strong=False)
Carbonic = ts.Compound(name="Carbonic Acid", acidic=True, pKs=[6.37, 10.25], strong=False)
Acetic = ts.Compound(name="Acetic Acid", acidic=True, pKs=[4.75], strong=False)
Ammonium = ts.Compound(name="Phenol", acidic=True, pKs=[9.2], strong=False)
Malic = ts.Compound(name="Malic", acidic=True, pKs=[3.46], strong=False)
Enanthic = ts.Compound(name="Enanthic", acidic=True, pKs=[4.89], strong=False)
Acrylic = ts.Compound(name="Acrylic", acidic=True, pKs=[4.23], strong=False)
Adipic = ts.Compound(name="Adipic", acidic=True, pKs=[4.43], strong=False)
Alanine = ts.Compound(name="Alanine", acidic=True, pKs=[9.87], strong=False)
Formic = ts.Compound(name="Formic", acidic=True, pKs=[3.75], strong=False)
Amidophosphonic = ts.Compound(name="Amidophosphonic", acidic=True, pKs=[2.74], strong=False)
Arsenic = ts.Compound(name="Arsenic", acidic=True, pKs=[2.25], strong=False)
Azelaic = ts.Compound(name="Azelaic", acidic=True, pKs=[4.53], strong=False)
Benzoic = ts.Compound(name="Benzoic", acidic=True, pKs=[4.21], strong=False)
Succinic = ts.Compound(name="Succinic", acidic=True, pKs=[4.16], strong=False)
Hydrocyanic = ts.Compound(name="Hydrocyanic", acidic=True, pKs=[9.21], strong=False)
Bromoacetic = ts.Compound(name="Bromoacetic", acidic=True, pKs=[2.87], strong=False)
Brominous = ts.Compound(name="Brominous", acidic=True, pKs=[2.85], strong=False)
Butanethiol = ts.Compound(name="Butanethiol", acidic=True, pKs=[10.66], strong=False)
Butyric = ts.Compound(name="Butyric", acidic=True, pKs=[4.82], strong=False)
Butylarsonic = ts.Compound(name="Butylarsonic", acidic=True, pKs=[4.23], strong=False)
Butylphosphinic = ts.Compound(name="Butylphosphinic", acidic=True, pKs=[3.41], strong=False)
Butylphosphonic = ts.Compound(name="Butylphosphonic", acidic=True, pKs=[2.79], strong=False)
Capric = ts.Compound(name="Capric", acidic=True, pKs=[4.9], strong=False)
Caproic = ts.Compound(name="Caproic", acidic=True, pKs=[4.88], strong=False)
Caprylic = ts.Compound(name="Caprylic", acidic=True, pKs=[4.89], strong=False)
Chloroacetic = ts.Compound(name="Chloroacetic", acidic=True, pKs=[2.83], strong=False)
Crotonic = ts.Compound(name="Crotonic", acidic=True, pKs=[4.69], strong=False)
Cyanic = ts.Compound(name="Cyanic", acidic=True, pKs=[3.46], strong=False)
Diamidophosphonic = ts.Compound(name="Diamidophosphonic", acidic=True, pKs=[4.83], strong=False)
Dihydrogenperoxodiphosphate = ts.Compound(name="Dihydrogenperoxodiphosphate", acidic=True, pKs=[5.18], strong=False)
Disulfane = ts.Compound(name="Disulfane", acidic=True, pKs=[5.0], strong=False)
Dithioarsenic = ts.Compound(name="Dithioarsenic", acidic=True, pKs=[2.4], strong=False)
Iron_VI_ = ts.Compound(name="Iron_VI_", acidic=True, pKs=[3.5], strong=False)
Ethanethiol = ts.Compound(name="Ethanethiol", acidic=True, pKs=[10.5], strong=False)
Ethylarsonic = ts.Compound(name="Ethylarsonic", acidic=True, pKs=[3.89], strong=False)
Ethylhydroperoxide = ts.Compound(name="Ethylhydroperoxide", acidic=True, pKs=[11.8], strong=False)
Ethylphosphinic = ts.Compound(name="Ethylphosphinic", acidic=True, pKs=[3.29], strong=False)
Ethylphosphonic = ts.Compound(name="Ethylphosphonic", acidic=True, pKs=[2.43], strong=False)
Fluoroacetic = ts.Compound(name="Fluoroacetic", acidic=True, pKs=[2.57], strong=False)
Hydrofluoric = ts.Compound(name="Hydrofluoric", acidic=True, pKs=[3.14], strong=False)
Glycine = ts.Compound(name="Glycine", acidic=True, pKs=[9.6], strong=False)
Glycolic = ts.Compound(name="Glycolic", acidic=True, pKs=[3.83], strong=False)
Hexafluoroantimonic = ts.Compound(name="Hexafluoroantimonic", acidic=True, pKs=[-17.0], strong=True)
Hexafluoroarsenic = ts.Compound(name="Hexafluoroarsenic", acidic=True, pKs=[-13.0], strong=True)
Hexafluorophosphoric = ts.Compound(name="Hexafluorophosphoric", acidic=True, pKs=[-10.0], strong=True)
Hexafluorotitan_IV_ = ts.Compound(name="Hexafluorotitan_IV_", acidic=True, pKs=[2.14], strong=False)
Hexafluorosilicic = ts.Compound(name="Hexafluorosilicic", acidic=True, pKs=[-3.0], strong=True)
Hexasulfane = ts.Compound(name="Hexasulfane", acidic=True, pKs=[3.2], strong=False)
Hydrazidosulfonic = ts.Compound(name="Hydrazidosulfonic", acidic=True, pKs=[3.85], strong=False)
Hydrogenperoxodiphosphate = ts.Compound(name="Hydrogenperoxodiphosphate", acidic=True, pKs=[7.67], strong=False)
Hypobromous = ts.Compound(name="Hypobromous", acidic=True, pKs=[8.68], strong=False)
Hypochlorous = ts.Compound(name="Hypochlorous", acidic=True, pKs=[7.54], strong=False)
Hypodiphosphoric = ts.Compound(name="Hypodiphosphoric", acidic=True, pKs=[2.22], strong=False)
Hypoiodous = ts.Compound(name="Hypoiodous", acidic=True, pKs=[10.64], strong=False)
Hypophosphorous = ts.Compound(name="Hypophosphorous", acidic=True, pKs=[2.23], strong=False)
Hypo_nitrous = ts.Compound(name="Hypo-nitrousacid", acidic=True, pKs=[7.21], strong=False)
Hypothiocyanitic = ts.Compound(name="Hypothiocyanitic", acidic=True, pKs=[5.3], strong=False)
Imidodiphosphoric = ts.Compound(name="Imidodiphosphoric", acidic=True, pKs=[2.0], strong=False)
Iodic = ts.Compound(name="Iodic", acidic=True, pKs=[0.804], strong=True)
Iodoacetic = ts.Compound(name="Iodoacetic", acidic=True, pKs=[3.13], strong=False)
Isocyanic = ts.Compound(name="Isocyanic", acidic=True, pKs=[3.92], strong=False)
Isopropylhydroperoxide = ts.Compound(name="Isopropylhydroperoxide", acidic=True, pKs=[12.1], strong=False)
Isopropyloxonium = ts.Compound(name="Isopropyloxonium", acidic=True, pKs=[-3.2], strong=True)
Isothiocyanic = ts.Compound(name="Isothiocyanic", acidic=True, pKs=[-1.28], strong=True)
Suberic = ts.Compound(name="Suberic", acidic=True, pKs=[4.51], strong=False)
Malonic = ts.Compound(name="Malonic", acidic=True, pKs=[2.83], strong=False)
Manganese_VI_ = ts.Compound(name="Manganese_VI_", acidic=True, pKs=[5.0], strong=False)
Mellitic = ts.Compound(name="Mellitic", acidic=True, pKs=[1.4], strong=True)
Metaarsenous = ts.Compound(name="Metaarsenous", acidic=True, pKs=[9.28], strong=False)
Metaboric = ts.Compound(name="Metaboric", acidic=True, pKs=[9.12], strong=False)
Metagermanic = ts.Compound(name="Metagermanic", acidic=True, pKs=[8.59], strong=False)
Metasilicic = ts.Compound(name="Metasilicic", acidic=True, pKs=[9.51], strong=False)
Metaniobic = ts.Compound(name="Metaniobic", acidic=True, pKs=[7.4], strong=False)
Metaperiodic = ts.Compound(name="Metaperiodic", acidic=True, pKs=[1.64], strong=True)
Metatantalic = ts.Compound(name="Metatantalic", acidic=True, pKs=[9.6], strong=False)
Metavanadium_V_ = ts.Compound(name="Metavanadium_V_", acidic=True, pKs=[3.8], strong=False)
Methanal = ts.Compound(name="Methanal", acidic=True, pKs=[13.3], strong=False)
Methaneselenol = ts.Compound(name="Methaneselenol", acidic=True, pKs=[5.2], strong=False)
Methanesulfonic = ts.Compound(name="Methanesulfonic", acidic=True, pKs=[-1.92], strong=True)
Methanethiol = ts.Compound(name="Methanethiol", acidic=True, pKs=[10.4], strong=False)
Methylarsonic = ts.Compound(name="Methylarsonic", acidic=True, pKs=[3.41], strong=False)
Methylhydroperoxide = ts.Compound(name="Methylhydroperoxide", acidic=True, pKs=[11.5], strong=False)
Methylphosphinic = ts.Compound(name="Methylphosphinic", acidic=True, pKs=[3.08], strong=False)
Methylphosphonic = ts.Compound(name="Methylphosphonic", acidic=True, pKs=[2.38], strong=False)
Methylsulfinic = ts.Compound(name="Methylsulfinic", acidic=True, pKs=[2.28], strong=False)
Lactic = ts.Compound(name="Lactic", acidic=True, pKs=[3.9], strong=False)
Molybdic = ts.Compound(name="Molybdic", acidic=True, pKs=[3.7], strong=False)
Monofluorophosphoric = ts.Compound(name="Monofluorophosphoric", acidic=True, pKs=[0.5], strong=True)
Nitramine = ts.Compound(name="Nitramine", acidic=True, pKs=[6.6], strong=False)
Nitromethane = ts.Compound(name="Nitromethane", acidic=True, pKs=[10.2], strong=False)
Octanesulfonic = ts.Compound(name="Octanesulfonic", acidic=True, pKs=[-1.41], strong=True)
Ortho_periodic = ts.Compound(name="Ortho-periodicacid", acidic=True, pKs=[3.29], strong=False)
Orthoantimonic = ts.Compound(name="Orthoantimonic", acidic=True, pKs=[2.55], strong=False)
Orthoboric = ts.Compound(name="Orthoboric", acidic=True, pKs=[9.25], strong=False)
Orthogermanic = ts.Compound(name="Orthogermanic", acidic=True, pKs=[8.68], strong=False)
Orthosilicic = ts.Compound(name="Orthosilicic", acidic=True, pKs=[9.66], strong=False)
Orthotelluric = ts.Compound(name="Orthotelluric", acidic=True, pKs=[7.7], strong=False)
Orthovanadic = ts.Compound(name="Orthovanadic", acidic=True, pKs=[2.6], strong=False)
Oxalic = ts.Compound(name="Oxalic", acidic=True, pKs=[1.23], strong=True)
p_Toluenesulfonic = ts.Compound(name="p-Toluenesulfonicacid", acidic=True, pKs=[-2.8], strong=True)
Pelargonic = ts.Compound(name="Pelargonic", acidic=True, pKs=[4.95], strong=False)
Pentacarbonylmanganese = ts.Compound(name="Pentacarbonylmanganese", acidic=True, pKs=[7.1], strong=False)
Pentafluoroethanesulfonic = ts.Compound(name="Pentafluoroethanesulfonic", acidic=True, pKs=[-5.1], strong=True)
Pentasulfane = ts.Compound(name="Pentasulfane", acidic=True, pKs=[3.5], strong=False)
Perchlorylamide = ts.Compound(name="Perchlorylamide", acidic=True, pKs=[8.6], strong=False)
Perchlorylamine = ts.Compound(name="Perchlorylamine", acidic=True, pKs=[3.7], strong=False)
Perchromic = ts.Compound(name="Perchromic", acidic=True, pKs=[4.95], strong=False)
Permanganic = ts.Compound(name="Permanganic", acidic=True, pKs=[-2.25], strong=True)
Perosmic = ts.Compound(name="Perosmic", acidic=True, pKs=[7.2], strong=False)
Peroxoformic = ts.Compound(name="Peroxoformic", acidic=True, pKs=[7.1], strong=False)
Peroxobutyric = ts.Compound(name="Peroxobutyric", acidic=True, pKs=[8.2], strong=False)
Peroxodiphosphoric = ts.Compound(name="Peroxodiphosphoric", acidic=True, pKs=[-3.0], strong=True)
Peroxodisulfuric = ts.Compound(name="Peroxodisulfuric", acidic=True, pKs=[-3.5], strong=True)
Peroxyacetic = ts.Compound(name="Peroxyacetic", acidic=True, pKs=[8.2], strong=False)
Peroxohypositrous = ts.Compound(name="Peroxohypositrous", acidic=True, pKs=[2.51], strong=False)
Peroxopropionic = ts.Compound(name="Peroxopropionic", acidic=True, pKs=[8.1], strong=False)
Peroxonitric = ts.Compound(name="Peroxonitric", acidic=True, pKs=[-5.0], strong=True)
Peroxo_nitrous = ts.Compound(name="Peroxo-nitrousacid", acidic=True, pKs=[6.8], strong=False)
Peroxosulphuric = ts.Compound(name="Peroxosulphuric", acidic=True, pKs=[0.8], strong=True)
Perrhenic = ts.Compound(name="Perrhenic", acidic=True, pKs=[-1.25], strong=True)
Perruthenic = ts.Compound(name="Perruthenic", acidic=True, pKs=[11.2], strong=False)
Pertechnetic = ts.Compound(name="Pertechnetic", acidic=True, pKs=[0.3], strong=True)
Phenol = ts.Compound(name="Phenol", acidic=True, pKs=[9.99], strong=False)
Phenylphosphonic = ts.Compound(name="Phenylphosphonic", acidic=True, pKs=[1.83], strong=True)
Phenylsulfinic = ts.Compound(name="Phenylsulfinic", acidic=True, pKs=[1.84], strong=True)
Phosphorous = ts.Compound(name="Phosphorous", acidic=True, pKs=[1.92], strong=True)
Phosphoric = ts.Compound(name="Phosphoric", acidic=True, pKs=[2.13], strong=False)
Pimelic = ts.Compound(name="Pimelic", acidic=True, pKs=[4.47], strong=False)
Poly = ts.Compound(name="Poly", acidic=True, pKs=[4.09], strong=False)
Propanethiol = ts.Compound(name="Propanethiol", acidic=True, pKs=[10.65], strong=False)
Propionic = ts.Compound(name="Propionic", acidic=True, pKs=[4.87], strong=False)
Propylarsonic = ts.Compound(name="Propylarsonic", acidic=True, pKs=[4.21], strong=False)
Propylphosphinic = ts.Compound(name="Propylphosphinic", acidic=True, pKs=[3.46], strong=False)
Propylphosphonic = ts.Compound(name="Propylphosphonic", acidic=True, pKs=[2.49], strong=False)
Salicylic = ts.Compound(name="Salicylic", acidic=True, pKs=[2.75], strong=False)
Nitrous = ts.Compound(name="Nitrous", acidic=True, pKs=[3.35], strong=False)
Sulfuric = ts.Compound(name="Sulfuric", acidic=True, pKs=[-3.0], strong=True)
Hydrogensulfide = ts.Compound(name="Hydrogensulfide", acidic=True, pKs=[7.06], strong=False)
Sulphurous = ts.Compound(name="Sulphurous", acidic=True, pKs=[1.92], strong=True)
Seaborgium_VI_ = ts.Compound(name="Seaborgium_VI_", acidic=True, pKs=[3.75], strong=False)
Sebacic = ts.Compound(name="Sebacic", acidic=True, pKs=[4.72], strong=False)
Selenous = ts.Compound(name="Selenous", acidic=True, pKs=[2.62], strong=False)
Selenophenol = ts.Compound(name="Selenophenol", acidic=True, pKs=[5.9], strong=False)
Selenophosphoric = ts.Compound(name="Selenophosphoric", acidic=True, pKs=[0.02], strong=True)
Selenic = ts.Compound(name="Selenic", acidic=True, pKs=[-3.0], strong=True)
Hydroselenic = ts.Compound(name="Hydroselenic", acidic=True, pKs=[3.73], strong=False)
Hydrazoic = ts.Compound(name="Hydrazoic", acidic=True, pKs=[4.76], strong=False)
Tartronic = ts.Compound(name="Tartronic", acidic=True, pKs=[2.3], strong=False)
Telluric = ts.Compound(name="Telluric", acidic=True, pKs=[2.64, 2.7], strong=False)
Tetracarbonyliron = ts.Compound(name="Tetracarbonyliron", acidic=True, pKs=[4.4], strong=False)
Tetrafluoroboric = ts.Compound(name="Tetrafluoroboric", acidic=True, pKs=[-0.4], strong=True)
Tetraphosphoric = ts.Compound(name="Tetraphosphoric", acidic=True, pKs=[0.5], strong=True)
Tetrasulfane = ts.Compound(name="Tetrasulfane", acidic=True, pKs=[3.8], strong=False)
Tetrathiophosphoric = ts.Compound(name="Tetrathiophosphoric", acidic=True, pKs=[1.5], strong=True)
Thioarsenic = ts.Compound(name="Thioarsenic", acidic=True, pKs=[3.3], strong=False)
Thiocyanic = ts.Compound(name="Thiocyanic", acidic=True, pKs=[-1.85], strong=True)
Thiophenol = ts.Compound(name="Thiophenol", acidic=True, pKs=[6.52], strong=False)
Thiophosphoric = ts.Compound(name="Thiophosphoric", acidic=True, pKs=[1.79], strong=True)
Thiosulfuric = ts.Compound(name="Thiosulfuric", acidic=True, pKs=[0.6], strong=True)
Thioselenic = ts.Compound(name="Thioselenic", acidic=True, pKs=[0.99], strong=True)
Tribromoacetic = ts.Compound(name="Tribromoacetic", acidic=True, pKs=[0.72], strong=True)
Trichloroacetic = ts.Compound(name="Trichloroacetic", acidic=True, pKs=[0.65], strong=True)
Trifluoroacetic = ts.Compound(name="Trifluoroacetic", acidic=True, pKs=[0.23], strong=True)
Trifluoromethanesulfonic = ts.Compound(name="Trifluoromethanesulfonic", acidic=True, pKs=[-5.21], strong=True)
Trihydrogenperoxodiphosphate = ts.Compound(name="Trihydrogenperoxodiphosphate", acidic=True, pKs=[0.5], strong=True)
Triiodoacetic = ts.Compound(name="Triiodoacetic", acidic=True, pKs=[0.9], strong=True)
Trioxide = ts.Compound(name="Trioxide", acidic=True, pKs=[9.5], strong=False)
Triphosphoric = ts.Compound(name="Triphosphoric", acidic=True, pKs=[1.0], strong=True)
Triselenocarbonic = ts.Compound(name="Triselenocarbonic", acidic=True, pKs=[1.16], strong=True)
Trisulfane = ts.Compound(name="Trisulfane", acidic=True, pKs=[4.2], strong=False)
Trithiocarbonic = ts.Compound(name="Trithiocarbonic", acidic=True, pKs=[2.68], strong=False)
Valeric = ts.Compound(name="Valeric", acidic=True, pKs=[4.84], strong=False)
Hydrogenhyperoxide = ts.Compound(name="Hydrogenhyperoxide", acidic=True, pKs=[4.7], strong=False)
Hydrogenozonide = ts.Compound(name="Hydrogenozonide", acidic=True, pKs=[8.2], strong=False)
Hydrogenperoxide = ts.Compound(name="Hydrogenperoxide", acidic=True, pKs=[11.62], strong=False)
Tartaric = ts.Compound(name="Tartaric", acidic=True, pKs=[2.98], strong=False)
Tungstic = ts.Compound(name="Tungstic", acidic=True, pKs=[3.8], strong=False)
Xenon_VI_ = ts.Compound(name="Xenon_VI_", acidic=True, pKs=[10.5], strong=False)
Xenon_VIII = ts.Compound(name="Xenon_VIII_", acidic=True, pKs=[2.0], strong=False)

# Bases
KOH = ts.Compound(name="KOH", acidic=False, pKs=[0.5], strong=True)
LiOH = ts.Compound(name="LiOH", acidic=False, pKs=[-0.36], strong=True)
NaOH = ts.Compound(name="NaOH", acidic=False, pKs=[0.2], strong=True)
RbOH = ts.Compound(name="RbOH", acidic=False, pKs=[-1.4], strong=True)
CsOH = ts.Compound(name="CsOH", acidic=False, pKs=[-1.76], strong=True)
FrOH = ts.Compound(name="FrOH", acidic=False, pKs=[-1.7], strong=True)
Ammonia = ts.Compound(name="ammonia", acidic=False, pKs=[4.75], strong=False)
Calcium_hydroxide = ts.Compound(name="calcium_hydroxide", acidic=False, pKs=[1.4, 2.43], strong=False)
Ethylamine = ts.Compound(name="ethylamine", acidic=False, pKs=[3.25], strong=False)
Aniline = ts.Compound(name="aniline", acidic=False, pKs=[9.4], strong=False)
Actiniumhydroxide = ts.Compound(name="Actiniumhydroxide", acidic=False, pKs=[2.9], strong=False)
Aluminumhydroxide = ts.Compound(name="Aluminumhydroxide", acidic=False, pKs=[8.14], strong=False)
Americium_III_hydroxide = ts.Compound(name="Americium_III_hydroxide", acidic=False, pKs=[2.9], strong=False)
Antimony_III_hydroxide = ts.Compound(name="Antimony_III_hydroxide", acidic=False, pKs=[12.58], strong=False)
Astatine_I_hydroxide = ts.Compound(name="Astatine_I_hydroxide", acidic=False, pKs=[12.5], strong=False)
Bariumhydroxide = ts.Compound(name="Bariumhydroxide", acidic=False, pKs=[0.15], strong=True)
Berylliumhydroxide = ts.Compound(name="Berylliumhydroxide", acidic=False, pKs=[5.4], strong=False)
Lead_II_hydroxide = ts.Compound(name="Lead_II_hydroxide", acidic=False, pKs=[4.38], strong=False)
Cesiumhydroxide = ts.Compound(name="Cesiumhydroxide", acidic=False, pKs=[-1.76], strong=True)
Cadmiumhydroxide = ts.Compound(name="Cadmiumhydroxide", acidic=False, pKs=[3.6], strong=False)
Calciumhydroxide = ts.Compound(name="Calciumhydroxide", acidic=False, pKs=[1.37], strong=True)
Cerium_III_hydroxide = ts.Compound(name="Cerium_III_hydroxide", acidic=False, pKs=[4.4], strong=False)
Cerium_IV_hydroxide = ts.Compound(name="Cerium_IV_hydroxide", acidic=False, pKs=[11.71], strong=False)
Chromium_III_hydroxide = ts.Compound(name="Chromium_III_hydroxide", acidic=False, pKs=[8.3], strong=False)
Curium_III_hydroxide = ts.Compound(name="Curium_III_hydroxide", acidic=False, pKs=[2.9], strong=False)
Diethylamine = ts.Compound(name="Diethylamine", acidic=False, pKs=[3.51], strong=False)
Dimethylamine = ts.Compound(name="Dimethylamine", acidic=False, pKs=[3.27], strong=False)
Diphenylamine = ts.Compound(name="Diphenylamine", acidic=False, pKs=[13.22], strong=False)
Dipropylamine = ts.Compound(name="Dipropylamine", acidic=False, pKs=[3.09], strong=False)
Dysprosium_III_hydroxide = ts.Compound(name="Dysprosium_III_hydroxide", acidic=False, pKs=[5.5], strong=False)
Iron_II_hydroxide = ts.Compound(name="Iron_II_hydroxide", acidic=False, pKs=[2.93], strong=False)
Iron_III_hydroxide = ts.Compound(name="Iron_III_hydroxide", acidic=False, pKs=[7.11], strong=False)
Erbium_III_hydroxide = ts.Compound(name="Erbium_III_hydroxide", acidic=False, pKs=[5.7], strong=False)
Ethylhydrazine = ts.Compound(name="Ethylhydrazine", acidic=False, pKs=[6.01], strong=False)
Europium_III_hydroxide = ts.Compound(name="Europium_III_hydroxide", acidic=False, pKs=[5.2], strong=False)
Franciumhydroxide = ts.Compound(name="Franciumhydroxide", acidic=False, pKs=[-1.76], strong=True)
Gadoliniumhydroxide = ts.Compound(name="Gadoliniumhydroxide", acidic=False, pKs=[5.7], strong=False)
Galliumhydroxide = ts.Compound(name="Galliumhydroxide", acidic=False, pKs=[9.25], strong=False)
Gold_I_hydroxide = ts.Compound(name="Gold_I_hydroxide", acidic=False, pKs=[10.2], strong=False)
Hafnium_IV_hydroxide = ts.Compound(name="Hafnium_IV_hydroxide", acidic=False, pKs=[13.48], strong=False)
Urea = ts.Compound(name="Urea", acidic=False, pKs=[13.82], strong=False)
Holmium_III_hydroxide = ts.Compound(name="Holmium_III_hydroxide", acidic=False, pKs=[5.6], strong=False)
Hydrazine = ts.Compound(name="Hydrazine", acidic=False, pKs=[6.07], strong=False)
Hydrogenxenonate_VIII_ = ts.Compound(name="Hydrogenxenonate_VIII_", acidic=False, pKs=[3.5], strong=False)
Hydroxylamine = ts.Compound(name="Hydroxylamine", acidic=False, pKs=[5.8], strong=False)
Indium_I_hydroxide_InOH_ = ts.Compound(name="Indium_I_hydroxide_InOH_", acidic=False, pKs=[2.17], strong=False)
Indium_III_hydroxide_In = ts.Compound(name="Indium_III_hydroxide_In", acidic=False, pKs=[8.84], strong=False)
Potassiumhydroxide = ts.Compound(name="Potassiumhydroxide", acidic=False, pKs=[-1.1], strong=True)
Cobalt_II_hydroxide = ts.Compound(name="Cobalt_II_hydroxide", acidic=False, pKs=[4.37], strong=False)
Copper_II_hydroxide = ts.Compound(name="Copper_II_hydroxide", acidic=False, pKs=[5.5], strong=False)
Lanthanumhydroxide = ts.Compound(name="Lanthanumhydroxide", acidic=False, pKs=[4.2], strong=False)
Lithiumhydroxide = ts.Compound(name="Lithiumhydroxide", acidic=False, pKs=[0.18], strong=True)
Lutetiumhydroxide = ts.Compound(name="Lutetiumhydroxide", acidic=False, pKs=[5.8], strong=False)
Magnesiumhydroxide = ts.Compound(name="Magnesiumhydroxide", acidic=False, pKs=[1.8], strong=True)
Manganese_II_hydroxide = ts.Compound(name="Manganese_II_hydroxide", acidic=False, pKs=[2.0], strong=False)
Methylamine = ts.Compound(name="Methylamine", acidic=False, pKs=[3.34], strong=False)
Methylhydrazine = ts.Compound(name="Methylhydrazine", acidic=False, pKs=[6.13], strong=False)
Methylphosphine = ts.Compound(name="Methylphosphine", acidic=False, pKs=[11.3], strong=False)
Sodiumhydroxide = ts.Compound(name="Sodiumhydroxide", acidic=False, pKs=[-0.56], strong=True)
Neodymium_III_hydroxide = ts.Compound(name="Neodymium_III_hydroxide", acidic=False, pKs=[4.5], strong=False)
Neptunium_IV_hydroxide = ts.Compound(name="Neptunium_IV_hydroxide", acidic=False, pKs=[8.7], strong=False)
Neptunyl_V_hydroxide = ts.Compound(name="Neptunyl_V_hydroxide", acidic=False, pKs=[2.7], strong=False)
Nickel_II_hydroxide = ts.Compound(name="Nickel_II_hydroxide", acidic=False, pKs=[3.78], strong=False)
Palladium_II_hydroxide = ts.Compound(name="Palladium_II_hydroxide", acidic=False, pKs=[11.54], strong=False)
Perchlorylimide = ts.Compound(name="Perchlorylimide", acidic=False, pKs=[5.4], strong=False)
Peroxodiphosphate = ts.Compound(name="Peroxodiphosphate", acidic=False, pKs=[6.33], strong=False)
Phenylhydrazine = ts.Compound(name="Phenylhydrazine", acidic=False, pKs=[8.79], strong=False)
Platinum_II_hydroxide = ts.Compound(name="Platinum_II_hydroxide", acidic=False, pKs=[4.8], strong=False)
Plutonium_III_hydroxide = ts.Compound(name="Plutonium_III_hydroxide", acidic=False, pKs=[2.9], strong=False)
Plutonium_IV_hydroxide = ts.Compound(name="Plutonium_IV_hydroxide", acidic=False, pKs=[7.3], strong=False)
Plutonyl_V_hydroxide = ts.Compound(name="Plutonyl_V_hydroxide", acidic=False, pKs=[4.3], strong=False)
Plutonyl_VI_hydroxide = ts.Compound(name="Plutonyl_VI_hydroxide", acidic=False, pKs=[9.95], strong=False)
Praseodymium_III_hydroxide = ts.Compound(name="Praseodymium_III_hydroxide", acidic=False, pKs=[4.6], strong=False)
Promethium_III_hydroxide = ts.Compound(name="Promethium_III_hydroxide", acidic=False, pKs=[4.6], strong=False)
Propylamine = ts.Compound(name="Propylamine", acidic=False, pKs=[3.43], strong=False)
Protactinium_IV_hydroxide = ts.Compound(name="Protactinium_IV_hydroxide", acidic=False, pKs=[12.75], strong=False)
Protactinyl_V_hydroxide = ts.Compound(name="Protactinyl_V_hydroxide", acidic=False, pKs=[2.81], strong=False)
Mercury_II_hydroxide = ts.Compound(name="Mercury_II_hydroxide", acidic=False, pKs=[11.5], strong=False)
Radiumhydroxide = ts.Compound(name="Radiumhydroxide", acidic=False, pKs=[0.0], strong=True)
Rubidiumhydroxide = ts.Compound(name="Rubidiumhydroxide", acidic=False, pKs=[-1.4], strong=True)
Rutherfordium_IV_hydroxide = ts.Compound(name="Rutherfordium_IV_hydroxide", acidic=False, pKs=[8.7], strong=False)
Samarium_III_hydroxide = ts.Compound(name="Samarium_III_hydroxide", acidic=False, pKs=[4.6], strong=False)
Scandiumhydroxide = ts.Compound(name="Scandiumhydroxide", acidic=False, pKs=[7.6], strong=False)
Silverhydroxide = ts.Compound(name="Silverhydroxide", acidic=False, pKs=[2.5], strong=False)
Strontiumhydroxide = ts.Compound(name="Strontiumhydroxide", acidic=False, pKs=[0.3], strong=True)
Technetyl_IV_hydroxide = ts.Compound(name="Technetyl_IV_hydroxide", acidic=False, pKs=[11.57], strong=False)
Terbium_III_hydroxide = ts.Compound(name="Terbium_III_hydroxide", acidic=False, pKs=[5.2], strong=False)
Thallium_I_hydroxide = ts.Compound(name="Thallium_I_hydroxide", acidic=False, pKs=[0.64], strong=True)
Thallium_III_hydroxide = ts.Compound(name="Thallium_III_hydroxide", acidic=False, pKs=[12.1], strong=False)
Thorium_IV_hydroxide = ts.Compound(name="Thorium_IV_hydroxide", acidic=False, pKs=[8.2], strong=False)
Thulium_III_hydroxide = ts.Compound(name="Thulium_III_hydroxide", acidic=False, pKs=[5.7], strong=False)
Titanyl_IV_dihydroxide = ts.Compound(name="Titanyl_IV_dihydroxide", acidic=False, pKs=[11.6], strong=False)
Triethylamine = ts.Compound(name="Triethylamine", acidic=False, pKs=[2.99], strong=False)
Trimethylamine = ts.Compound(name="Trimethylamine", acidic=False, pKs=[4.19], strong=False)
Trimethylphosphine = ts.Compound(name="Trimethylphosphine", acidic=False, pKs=[5.35], strong=False)
Triphenylphosphine = ts.Compound(name="Triphenylphosphine", acidic=False, pKs=[11.27], strong=False)
Tripropylamine = ts.Compound(name="Tripropylamine", acidic=False, pKs=[3.34], strong=False)
Uranium_IV_hydroxide = ts.Compound(name="Uranium_IV_hydroxide", acidic=False, pKs=[8.35], strong=False)
Uranyl_VI_hydroxide = ts.Compound(name="Uranyl_VI_hydroxide", acidic=False, pKs=[7.2], strong=False)
Vanadium_III_hydroxide_V = ts.Compound(name="Vanadium_III_hydroxide_V", acidic=False, pKs=[9.9], strong=False)
Vanadyl_IV_hydroxide_VO = ts.Compound(name="Vanadyl_IV_hydroxide_VO", acidic=False, pKs=[7.66], strong=False)
Bismuth_III_hydroxide = ts.Compound(name="Bismuth_III_hydroxide", acidic=False, pKs=[7.62], strong=False)
Ytterbium_III_hydroxide = ts.Compound(name="Ytterbium_III_hydroxide", acidic=False, pKs=[5.7], strong=False)
Yttriumhydroxide = ts.Compound(name="Yttriumhydroxide", acidic=False, pKs=[4.4], strong=False)
Zinchydroxide = ts.Compound(name="Zinchydroxide", acidic=False, pKs=[5.01], strong=False)
Tin_II_hydroxide = ts.Compound(name="Tin_II_hydroxide", acidic=False, pKs=[10.34], strong=False)
Tin_IV_hydroxide = ts.Compound(name="Tin_IV_hydroxide", acidic=False, pKs=[10.68], strong=False)
Zirconium_IV_hydroxide = ts.Compound(name="Zirconium_IV_hydroxide", acidic=False, pKs=[13.5], strong=False)

# Lists of compound

acids = [Hydrochloric,
         Hydroiodic,
         Nitric,
         Hydrobromic,
         Hydroperchloric,
         p_Toluenesulfonic,
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
         Iron_VI_,
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
         Hexafluorotitan_IV_,
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
         Manganese_VI_,
         Mellitic,
         Metaarsenous,
         Metaboric,
         Metagermanic,
         Metasilicic,
         Metaniobic,
         Metaperiodic,
         Metatantalic,
         Metavanadium_V_,
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
         p_Toluenesulfonic,
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
         Seaborgium_VI_,
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
         Hydrogenhyperoxide,
         Hydrogenozonide,
         Hydrogenperoxide,
         Tartaric,
         Tungstic,
         Xenon_VI_,
         Xenon_VIII]

bases = [KOH,
         LiOH,
         NaOH,
         RbOH,
         CsOH,
         FrOH,
         Ammonia,
         Calcium_hydroxide,
         Ethylamine,
         Aniline,
         Actiniumhydroxide,
         Aluminumhydroxide,
         Americium_III_hydroxide,
         Antimony_III_hydroxide,
         Astatine_I_hydroxide,
         Bariumhydroxide,
         Berylliumhydroxide,
         Lead_II_hydroxide,
         Cesiumhydroxide,
         Cadmiumhydroxide,
         Calciumhydroxide,
         Cerium_III_hydroxide,
         Cerium_IV_hydroxide,
         Chromium_III_hydroxide,
         Curium_III_hydroxide,
         Diethylamine,
         Dimethylamine,
         Diphenylamine,
         Dipropylamine,
         Dysprosium_III_hydroxide,
         Iron_II_hydroxide,
         Iron_III_hydroxide,
         Erbium_III_hydroxide,
         Ethylhydrazine,
         Europium_III_hydroxide,
         Franciumhydroxide,
         Gadoliniumhydroxide,
         Galliumhydroxide,
         Gold_I_hydroxide,
         Hafnium_IV_hydroxide,
         Urea,
         Holmium_III_hydroxide,
         Hydrazine,
         Hydrogenxenonate_VIII_,
         Hydroxylamine,
         Indium_I_hydroxide_InOH_,
         Indium_III_hydroxide_In,
         Potassiumhydroxide,
         Cobalt_II_hydroxide,
         Copper_II_hydroxide,
         Lanthanumhydroxide,
         Lithiumhydroxide,
         Lutetiumhydroxide,
         Magnesiumhydroxide,
         Manganese_II_hydroxide,
         Methylamine,
         Methylhydrazine,
         Methylphosphine,
         Sodiumhydroxide,
         Neodymium_III_hydroxide,
         Neptunium_IV_hydroxide,
         Neptunyl_V_hydroxide,
         Nickel_II_hydroxide,
         Palladium_II_hydroxide,
         Perchlorylimide,
         Peroxodiphosphate,
         Phenylhydrazine,
         Platinum_II_hydroxide,
         Plutonium_III_hydroxide,
         Plutonium_IV_hydroxide,
         Plutonyl_V_hydroxide,
         Plutonyl_VI_hydroxide,
         Praseodymium_III_hydroxide,
         Promethium_III_hydroxide,
         Propylamine,
         Protactinium_IV_hydroxide,
         Protactinyl_V_hydroxide,
         Mercury_II_hydroxide,
         Radiumhydroxide,
         Rubidiumhydroxide,
         Rutherfordium_IV_hydroxide,
         Samarium_III_hydroxide,
         Scandiumhydroxide,
         Silverhydroxide,
         Strontiumhydroxide,
         Technetyl_IV_hydroxide,
         Terbium_III_hydroxide,
         Thallium_I_hydroxide,
         Thallium_III_hydroxide,
         Thorium_IV_hydroxide,
         Thulium_III_hydroxide,
         Titanyl_IV_dihydroxide,
         Triethylamine,
         Trimethylamine,
         Trimethylphosphine,
         Triphenylphosphine,
         Tripropylamine,
         Uranium_IV_hydroxide,
         Uranyl_VI_hydroxide,
         Vanadium_III_hydroxide_V,
         Vanadyl_IV_hydroxide_VO,
         Bismuth_III_hydroxide,
         Ytterbium_III_hydroxide,
         Yttriumhydroxide,
         Zinchydroxide,
         Tin_II_hydroxide,
         Tin_IV_hydroxide,
         Zirconium_IV_hydroxide]

strong_acids = [i for i in acids if i.strong is True]
weak_acids = [i for i in acids if i.strong is False]
strong_bases = [i for i in bases if i.strong is True]
weak_bases = [i for i in bases if i.strong is False]