import titration_class as ts

"""pK values and names taken from http://www.periodensystem-online.de/index.php (tyty)"""

acidic_water = ts.Compound(name="Water", acidic=True, pKs=[14.0], strong=False)
basic_water = ts.Compound(name="Water", acidic=False, pKs=[14.0], strong=False)

# Acids
HCl = ts.Compound(name="HCl", acidic=True, pKs=[-6.5], strong=True)
HI = ts.Compound(name="HI", acidic=True, pKs=[-10], strong=True)
HNO3 = ts.Compound(name="HNO3", acidic=True, pKs=[-1.4], strong=True)
HBr = ts.Compound(name="HBr", acidic=True, pKs=[-8.7], strong=True)
HCLO4 = ts.Compound(name="Perchloric Acid", acidic=True, pKs=[-8], strong=True)
TsOH = ts.Compound(name="p-Toluenesolfonic Acid", acidic=True, pKs=[-2.8], strong=True)
propane1sulfonicacid = ts.Compound(name="1-propanesulfonicacid", acidic=True, pKs=[-1.49], strong=True)
propane2sulfonicacid = ts.Compound(name="2-propanesulfonicacid", acidic=True, pKs=[-1.79], strong=True)
Amidosulfonicacid = ts.Compound(name="Amidosulfonicacid", acidic=True, pKs=[0.99], strong=True)
Benzenesulfonicacid = ts.Compound(name="Benzenesulfonicacid", acidic=True, pKs=[-2.5], strong=True)
Bromicacid = ts.Compound(name="Bromicacid", acidic=True, pKs=[0.0], strong=True)
Hydrobromicacid = ts.Compound(name="Hydrobromicacid", acidic=True, pKs=[-8.72], strong=True)
Butanesulfonicacid = ts.Compound(name="Butanesulfonicacid", acidic=True, pKs=[-1.68], strong=True)
Chlorousacid = ts.Compound(name="Chlorousacid", acidic=True, pKs=[1.97], strong=True)
Chlorosulfonicacid = ts.Compound(name="Chlorosulfonicacid", acidic=True, pKs=[-10.43], strong=True)
Chloricacid = ts.Compound(name="Chloricacid", acidic=True, pKs=[-2.7], strong=True)
Chromicacid = ts.Compound(name="Chromicacid", acidic=True, pKs=[-0.61], strong=True)
Dibromoaceticacid = ts.Compound(name="Dibromoaceticacid", acidic=True, pKs=[1.39], strong=True)
Dichloroaceticacid = ts.Compound(name="Dichloroaceticacid", acidic=True, pKs=[1.29], strong=True)
Dichromicacid = ts.Compound(name="Dichromicacid", acidic=True, pKs=[-4.5], strong=True)
Difluoroaceticacid = ts.Compound(name="Difluoroaceticacid", acidic=True, pKs=[1.24], strong=True)
Difluorophosphoricacid = ts.Compound(name="Difluorophosphoricacid", acidic=True, pKs=[-1.5], strong=True)
Diiodoaceticacid = ts.Compound(name="Diiodoaceticacid", acidic=True, pKs=[1.49], strong=True)
Dimethylphosphonicacid = ts.Compound(name="Dimethylphosphonicacid", acidic=True, pKs=[1.29], strong=True)
Disulfuricacid = ts.Compound(name="Disulfuricacid", acidic=True, pKs=[-12.0], strong=True)
Dithionicacid = ts.Compound(name="Dithionicacid", acidic=True, pKs=[-3.4, 0.35], strong=True)
Ethanesulfonicacid = ts.Compound(name="Ethanesulfonicacid", acidic=True, pKs=[-1.68], strong=True)
Fluorosulfonicacid = ts.Compound(name="Fluorosulfonicacid", acidic=True, pKs=[-14.0], strong=True)
Heptafluoropropanesulfonicacid = ts.Compound(name="Heptafluoropropanesulfonicacid", acidic=True, pKs=[-5.0],
                                             strong=True)
EDTA = ts.Compound(name="EDTA", acidic=True, pKs=[0.0, 1.5, 2.00, 2.69, 6.13, 10.37], strong=False)  # Pg 268 QCA
Citric = ts.Compound(name="Citric Acid", acidic=True, pKs=[3.13, 4.76, 6.40], strong=False)
Carbonic = ts.Compound(name="Carbonic Acid", acidic=True, pKs=[6.37, 10.25], strong=False)
Acetic = ts.Compound(name="Acetic Acid", acidic=True, pKs=[4.75], strong=False)
Ammonium = ts.Compound(name="Phenol", acidic=True, pKs=[9.2], strong=False)
MalicAcid = ts.Compound(name="MalicAcid", acidic=True, pKs=[3.46], strong=False)
Enanthicacid = ts.Compound(name="Enanthicacid", acidic=True, pKs=[4.89], strong=False)
Acrylicacid = ts.Compound(name="Acrylicacid", acidic=True, pKs=[4.23], strong=False)
Adipicacid = ts.Compound(name="Adipicacid", acidic=True, pKs=[4.43], strong=False)
Alanine = ts.Compound(name="Alanine", acidic=True, pKs=[9.87], strong=False)
Formicacid = ts.Compound(name="Formicacid", acidic=True, pKs=[3.75], strong=False)
Amidophosphonicacid = ts.Compound(name="Amidophosphonicacid", acidic=True, pKs=[2.74], strong=False)
Arsenicacid = ts.Compound(name="Arsenicacid", acidic=True, pKs=[2.25], strong=False)
AzelaicAcid = ts.Compound(name="AzelaicAcid", acidic=True, pKs=[4.53], strong=False)
Benzoicacid = ts.Compound(name="Benzoicacid", acidic=True, pKs=[4.21], strong=False)
Succinicacid = ts.Compound(name="Succinicacid", acidic=True, pKs=[4.16], strong=False)
Hydrocyanicacid = ts.Compound(name="Hydrocyanicacid", acidic=True, pKs=[9.21], strong=False)
Bromoaceticacid = ts.Compound(name="Bromoaceticacid", acidic=True, pKs=[2.87], strong=False)
Brominousacid = ts.Compound(name="Brominousacid", acidic=True, pKs=[2.85], strong=False)
Butanethiol = ts.Compound(name="Butanethiol", acidic=True, pKs=[10.66], strong=False)
Butyricacid = ts.Compound(name="Butyricacid", acidic=True, pKs=[4.82], strong=False)
Butylarsonicacid = ts.Compound(name="Butylarsonicacid", acidic=True, pKs=[4.23], strong=False)
Butylphosphinicacid = ts.Compound(name="Butylphosphinicacid", acidic=True, pKs=[3.41], strong=False)
Butylphosphonicacid = ts.Compound(name="Butylphosphonicacid", acidic=True, pKs=[2.79], strong=False)
Capricacid = ts.Compound(name="Capricacid", acidic=True, pKs=[4.9], strong=False)
Caproicacid = ts.Compound(name="Caproicacid", acidic=True, pKs=[4.88], strong=False)
Caprylicacid = ts.Compound(name="Caprylicacid", acidic=True, pKs=[4.89], strong=False)
Chloroaceticacid = ts.Compound(name="Chloroaceticacid", acidic=True, pKs=[2.83], strong=False)
Citricacid = ts.Compound(name="Citricacid", acidic=True, pKs=[3.13], strong=False)
Crotonicacid = ts.Compound(name="Crotonicacid", acidic=True, pKs=[4.69], strong=False)
Cyanicacid = ts.Compound(name="Cyanicacid", acidic=True, pKs=[3.46], strong=False)
Diamidophosphonicacid = ts.Compound(name="Diamidophosphonicacid", acidic=True, pKs=[4.83], strong=False)
Dihydrogenperoxodiphosphate = ts.Compound(name="Dihydrogenperoxodiphosphate", acidic=True, pKs=[5.18], strong=False)
Disulfane = ts.Compound(name="Disulfane", acidic=True, pKs=[5.0], strong=False)
Dithioarsenicacid = ts.Compound(name="Dithioarsenicacid", acidic=True, pKs=[2.4], strong=False)
Iron_VI_acid = ts.Compound(name="Iron_VI_acid", acidic=True, pKs=[3.5], strong=False)
Aceticacid = ts.Compound(name="Aceticacid", acidic=True, pKs=[4.76], strong=False)
Ethanethiol = ts.Compound(name="Ethanethiol", acidic=True, pKs=[10.5], strong=False)
Ethylarsonicacid = ts.Compound(name="Ethylarsonicacid", acidic=True, pKs=[3.89], strong=False)
Ethylhydroperoxide = ts.Compound(name="Ethylhydroperoxide", acidic=True, pKs=[11.8], strong=False)
Ethylphosphinicacid = ts.Compound(name="Ethylphosphinicacid", acidic=True, pKs=[3.29], strong=False)
Ethylphosphonicacid = ts.Compound(name="Ethylphosphonicacid", acidic=True, pKs=[2.43], strong=False)
Fluoroaceticacid = ts.Compound(name="Fluoroaceticacid", acidic=True, pKs=[2.57], strong=False)
Hydrofluoricacid = ts.Compound(name="Hydrofluoricacid", acidic=True, pKs=[3.14], strong=False)
Glycine = ts.Compound(name="Glycine", acidic=True, pKs=[9.6], strong=False)
Glycolicacid = ts.Compound(name="Glycolicacid", acidic=True, pKs=[3.83], strong=False)
Hexafluoroantimonicacid = ts.Compound(name="Hexafluoroantimonicacid", acidic=True, pKs=[-17.0], strong=True)
Hexafluoroarsenicacid = ts.Compound(name="Hexafluoroarsenicacid", acidic=True, pKs=[-13.0], strong=True)
Hexafluorophosphoricacid = ts.Compound(name="Hexafluorophosphoricacid", acidic=True, pKs=[-10.0], strong=True)
Hexafluorotitan_IV_acid = ts.Compound(name="Hexafluorotitan_IV_acid", acidic=True, pKs=[2.14], strong=False)
Hexafluorosilicicacid = ts.Compound(name="Hexafluorosilicicacid", acidic=True, pKs=[-3.0], strong=True)
Hexasulfane = ts.Compound(name="Hexasulfane", acidic=True, pKs=[3.2], strong=False)
Hydrazidosulfonicacid = ts.Compound(name="Hydrazidosulfonicacid", acidic=True, pKs=[3.85], strong=False)
Hydrogenperoxodiphosphate = ts.Compound(name="Hydrogenperoxodiphosphate", acidic=True, pKs=[7.67], strong=False)
Hypobromousacid = ts.Compound(name="Hypobromousacid", acidic=True, pKs=[8.68], strong=False)
Hypochlorousacid = ts.Compound(name="Hypochlorousacid", acidic=True, pKs=[7.54], strong=False)
Hypodiphosphoricacid = ts.Compound(name="Hypodiphosphoricacid", acidic=True, pKs=[2.22], strong=False)
HypoiodousAcid = ts.Compound(name="HypoiodousAcid", acidic=True, pKs=[10.64], strong=False)
Hypophosphorousacid = ts.Compound(name="Hypophosphorousacid", acidic=True, pKs=[2.23], strong=False)
Hypo_nitrousacid = ts.Compound(name="Hypo-nitrousacid", acidic=True, pKs=[7.21], strong=False)
Hypothiocyaniticacid = ts.Compound(name="Hypothiocyaniticacid", acidic=True, pKs=[5.3], strong=False)
Imidodiphosphoricacid = ts.Compound(name="Imidodiphosphoricacid", acidic=True, pKs=[2.0], strong=False)
Iodicacid = ts.Compound(name="Iodicacid", acidic=True, pKs=[0.804], strong=True)
Iodoaceticacid = ts.Compound(name="Iodoaceticacid", acidic=True, pKs=[3.13], strong=False)
HydroiodicAcid = ts.Compound(name="HydroiodicAcid", acidic=True, pKs=[-9.5], strong=True)
Isocyanicacid = ts.Compound(name="Isocyanicacid", acidic=True, pKs=[3.92], strong=False)
Isopropylhydroperoxide = ts.Compound(name="Isopropylhydroperoxide", acidic=True, pKs=[12.1], strong=False)
Isopropyloxonium = ts.Compound(name="Isopropyloxonium", acidic=True, pKs=[-3.2], strong=True)
Isothiocyanicacid = ts.Compound(name="Isothiocyanicacid", acidic=True, pKs=[-1.28], strong=True)
Carbonicacid = ts.Compound(name="Carbonicacid", acidic=True, pKs=[6.46], strong=False)
Subericacid = ts.Compound(name="Subericacid", acidic=True, pKs=[4.51], strong=False)
Malonicacid = ts.Compound(name="Malonicacid", acidic=True, pKs=[2.83], strong=False)
Manganese_VI_acid = ts.Compound(name="Manganese_VI_acid", acidic=True, pKs=[5.0], strong=False)
Melliticacid = ts.Compound(name="Melliticacid", acidic=True, pKs=[1.4], strong=True)
Metaarsenousacid = ts.Compound(name="Metaarsenousacid", acidic=True, pKs=[9.28], strong=False)
Metaboricacid = ts.Compound(name="Metaboricacid", acidic=True, pKs=[9.12], strong=False)
Metagermanicacid = ts.Compound(name="Metagermanicacid", acidic=True, pKs=[8.59], strong=False)
Metasilicicacid = ts.Compound(name="Metasilicicacid", acidic=True, pKs=[9.51], strong=False)
Metaniobicacid = ts.Compound(name="Metaniobicacid", acidic=True, pKs=[7.4], strong=False)
Metaperiodicacid = ts.Compound(name="Metaperiodicacid", acidic=True, pKs=[1.64], strong=True)
Metatantalicacid = ts.Compound(name="Metatantalicacid", acidic=True, pKs=[9.6], strong=False)
Metavanadium_V_acid = ts.Compound(name="Metavanadium_V_acid", acidic=True, pKs=[3.8], strong=False)
Methanal = ts.Compound(name="Methanal", acidic=True, pKs=[13.3], strong=False)
Methaneselenol = ts.Compound(name="Methaneselenol", acidic=True, pKs=[5.2], strong=False)
Methanesulfonicacid = ts.Compound(name="Methanesulfonicacid", acidic=True, pKs=[-1.92], strong=True)
Methanethiol = ts.Compound(name="Methanethiol", acidic=True, pKs=[10.4], strong=False)
Methylarsonicacid = ts.Compound(name="Methylarsonicacid", acidic=True, pKs=[3.41], strong=False)
Methylhydroperoxide = ts.Compound(name="Methylhydroperoxide", acidic=True, pKs=[11.5], strong=False)
Methylphosphinicacid = ts.Compound(name="Methylphosphinicacid", acidic=True, pKs=[3.08], strong=False)
Methylphosphonicacid = ts.Compound(name="Methylphosphonicacid", acidic=True, pKs=[2.38], strong=False)
Methylsulfinicacid = ts.Compound(name="Methylsulfinicacid", acidic=True, pKs=[2.28], strong=False)
Lacticacid = ts.Compound(name="Lacticacid", acidic=True, pKs=[3.9], strong=False)
Molybdicacid = ts.Compound(name="Molybdicacid", acidic=True, pKs=[3.7], strong=False)
Monofluorophosphoricacid = ts.Compound(name="Monofluorophosphoricacid", acidic=True, pKs=[0.5], strong=True)
Nitramine = ts.Compound(name="Nitramine", acidic=True, pKs=[6.6], strong=False)
Nitromethane = ts.Compound(name="Nitromethane", acidic=True, pKs=[10.2], strong=False)
Octanesulfonicacid = ts.Compound(name="Octanesulfonicacid", acidic=True, pKs=[-1.41], strong=True)
Ortho_periodicacid = ts.Compound(name="Ortho-periodicacid", acidic=True, pKs=[3.29], strong=False)
Orthoantimonicacid = ts.Compound(name="Orthoantimonicacid", acidic=True, pKs=[2.55], strong=False)
Orthoboricacid = ts.Compound(name="Orthoboricacid", acidic=True, pKs=[9.25], strong=False)
Orthogermanicacid = ts.Compound(name="Orthogermanicacid", acidic=True, pKs=[8.68], strong=False)
Orthosilicicacid = ts.Compound(name="Orthosilicicacid", acidic=True, pKs=[9.66], strong=False)
Orthotelluricacid = ts.Compound(name="Orthotelluricacid", acidic=True, pKs=[7.7], strong=False)
Orthovanadicacid = ts.Compound(name="Orthovanadicacid", acidic=True, pKs=[2.6], strong=False)
Oxalicacid = ts.Compound(name="Oxalicacid", acidic=True, pKs=[1.23], strong=True)
p_Toluenesulfonicacid = ts.Compound(name="p-Toluenesulfonicacid", acidic=True, pKs=[-2.8], strong=True)
Pelargonicacid = ts.Compound(name="Pelargonicacid", acidic=True, pKs=[4.95], strong=False)
Pentacarbonylmanganese = ts.Compound(name="Pentacarbonylmanganese", acidic=True, pKs=[7.1], strong=False)
Pentafluoroethanesulfonicacid = ts.Compound(name="Pentafluoroethanesulfonicacid", acidic=True, pKs=[-5.1], strong=True)
Pentasulfane = ts.Compound(name="Pentasulfane", acidic=True, pKs=[3.5], strong=False)
Perchlorylamide = ts.Compound(name="Perchlorylamide", acidic=True, pKs=[8.6], strong=False)
Perchlorylamine = ts.Compound(name="Perchlorylamine", acidic=True, pKs=[3.7], strong=False)
Perchromicacid = ts.Compound(name="Perchromicacid", acidic=True, pKs=[4.95], strong=False)
Permanganicacid = ts.Compound(name="Permanganicacid", acidic=True, pKs=[-2.25], strong=True)
Perosmicacid = ts.Compound(name="Perosmicacid", acidic=True, pKs=[7.2], strong=False)
Peroxoformicacid = ts.Compound(name="Peroxoformicacid", acidic=True, pKs=[7.1], strong=False)
Peroxobutyricacid = ts.Compound(name="Peroxobutyricacid", acidic=True, pKs=[8.2], strong=False)
Peroxodiphosphoricacid = ts.Compound(name="Peroxodiphosphoricacid", acidic=True, pKs=[-3.0], strong=True)
Peroxodisulfuricacid = ts.Compound(name="Peroxodisulfuricacid", acidic=True, pKs=[-3.5], strong=True)
Peroxyaceticacid = ts.Compound(name="Peroxyaceticacid", acidic=True, pKs=[8.2], strong=False)
Peroxohypositrousacid = ts.Compound(name="Peroxohypositrousacid", acidic=True, pKs=[2.51], strong=False)
Peroxopropionicacid = ts.Compound(name="Peroxopropionicacid", acidic=True, pKs=[8.1], strong=False)
Peroxonitricacid = ts.Compound(name="Peroxonitricacid", acidic=True, pKs=[-5.0], strong=True)
Peroxo_nitrousacid = ts.Compound(name="Peroxo-nitrousacid", acidic=True, pKs=[6.8], strong=False)
Peroxosulphuricacid = ts.Compound(name="Peroxosulphuricacid", acidic=True, pKs=[0.8], strong=True)
Perrhenicacid = ts.Compound(name="Perrhenicacid", acidic=True, pKs=[-1.25], strong=True)
Perruthenicacid = ts.Compound(name="Perruthenicacid", acidic=True, pKs=[11.2], strong=False)
Pertechneticacid = ts.Compound(name="Pertechneticacid", acidic=True, pKs=[0.3], strong=True)
Phenol = ts.Compound(name="Phenol", acidic=True, pKs=[9.99], strong=False)
Phenylphosphonicacid = ts.Compound(name="Phenylphosphonicacid", acidic=True, pKs=[1.83], strong=True)
Phenylsulfinicacid = ts.Compound(name="Phenylsulfinicacid", acidic=True, pKs=[1.84], strong=True)
Phosphorousacid = ts.Compound(name="Phosphorousacid", acidic=True, pKs=[1.92], strong=True)
Phosphoricacid = ts.Compound(name="Phosphoricacid", acidic=True, pKs=[2.13], strong=False)
Pimelicacid = ts.Compound(name="Pimelicacid", acidic=True, pKs=[4.47], strong=False)
Polyacid = ts.Compound(name="Polyacid", acidic=True, pKs=[4.09], strong=False)
Propanethiol = ts.Compound(name="Propanethiol", acidic=True, pKs=[10.65], strong=False)
Propionicacid = ts.Compound(name="Propionicacid", acidic=True, pKs=[4.87], strong=False)
Propylarsonicacid = ts.Compound(name="Propylarsonicacid", acidic=True, pKs=[4.21], strong=False)
Propylphosphinicacid = ts.Compound(name="Propylphosphinicacid", acidic=True, pKs=[3.46], strong=False)
Propylphosphonicacid = ts.Compound(name="Propylphosphonicacid", acidic=True, pKs=[2.49], strong=False)
SalicylicAcid = ts.Compound(name="SalicylicAcid", acidic=True, pKs=[2.75], strong=False)
Nitricacid = ts.Compound(name="Nitricacid", acidic=True, pKs=[-1.33], strong=True)
Nitrousacid = ts.Compound(name="Nitrousacid", acidic=True, pKs=[3.35], strong=False)
Hydrochloricacid = ts.Compound(name="Hydrochloricacid", acidic=True, pKs=[-6.0], strong=True)
Sulfuricacid = ts.Compound(name="Sulfuricacid", acidic=True, pKs=[-3.0], strong=True)
Hydrogensulfide = ts.Compound(name="Hydrogensulfide", acidic=True, pKs=[7.06], strong=False)
Sulphurousacid = ts.Compound(name="Sulphurousacid", acidic=True, pKs=[1.92], strong=True)
Seaborgium_VI_acid = ts.Compound(name="Seaborgium_VI_acid", acidic=True, pKs=[3.75], strong=False)
Sebacicacid = ts.Compound(name="Sebacicacid", acidic=True, pKs=[4.72], strong=False)
Selenousacid = ts.Compound(name="Selenousacid", acidic=True, pKs=[2.62], strong=False)
Selenophenol = ts.Compound(name="Selenophenol", acidic=True, pKs=[5.9], strong=False)
Selenophosphoricacid = ts.Compound(name="Selenophosphoricacid", acidic=True, pKs=[0.02], strong=True)
Selenicacid = ts.Compound(name="Selenicacid", acidic=True, pKs=[-3.0], strong=True)
Hydroselenicacid = ts.Compound(name="Hydroselenicacid", acidic=True, pKs=[3.73], strong=False)
Hydrazoicacid = ts.Compound(name="Hydrazoicacid", acidic=True, pKs=[4.76], strong=False)
Tartronicacid = ts.Compound(name="Tartronicacid", acidic=True, pKs=[2.3], strong=False)
Telluricacid = ts.Compound(name="Telluricacid", acidic=True, pKs=[2.64, 2.7], strong=False)
Tetracarbonyliron = ts.Compound(name="Tetracarbonyliron", acidic=True, pKs=[4.4], strong=False)
Tetrafluoroboricacid = ts.Compound(name="Tetrafluoroboricacid", acidic=True, pKs=[-0.4], strong=True)
Tetraphosphoricacid = ts.Compound(name="Tetraphosphoricacid", acidic=True, pKs=[0.5], strong=True)
Tetrasulfane = ts.Compound(name="Tetrasulfane", acidic=True, pKs=[3.8], strong=False)
Tetrathiophosphoricacid = ts.Compound(name="Tetrathiophosphoricacid", acidic=True, pKs=[1.5], strong=True)
Thioarsenicacid = ts.Compound(name="Thioarsenicacid", acidic=True, pKs=[3.3], strong=False)
Thiocyanicacid = ts.Compound(name="Thiocyanicacid", acidic=True, pKs=[-1.85], strong=True)
Thiophenol = ts.Compound(name="Thiophenol", acidic=True, pKs=[6.52], strong=False)
Thiophosphoricacid = ts.Compound(name="Thiophosphoricacid", acidic=True, pKs=[1.79], strong=True)
Thiosulfuricacid = ts.Compound(name="Thiosulfuricacid", acidic=True, pKs=[0.6], strong=True)
Thioselenicacid = ts.Compound(name="Thioselenicacid", acidic=True, pKs=[0.99], strong=True)
Tribromoaceticacid = ts.Compound(name="Tribromoaceticacid", acidic=True, pKs=[0.72], strong=True)
Trichloroaceticacid = ts.Compound(name="Trichloroaceticacid", acidic=True, pKs=[0.65], strong=True)
Trifluoroaceticacid = ts.Compound(name="Trifluoroaceticacid", acidic=True, pKs=[0.23], strong=True)
Trifluoromethanesulfonicacid = ts.Compound(name="Trifluoromethanesulfonicacid", acidic=True, pKs=[-5.21], strong=True)
Trihydrogenperoxodiphosphate = ts.Compound(name="Trihydrogenperoxodiphosphate", acidic=True, pKs=[0.5], strong=True)
Triiodoaceticacid = ts.Compound(name="Triiodoaceticacid", acidic=True, pKs=[0.9], strong=True)
Trioxide = ts.Compound(name="Trioxide", acidic=True, pKs=[9.5], strong=False)
Triphosphoricacid = ts.Compound(name="Triphosphoricacid", acidic=True, pKs=[1.0], strong=True)
Triselenocarbonicacid = ts.Compound(name="Triselenocarbonicacid", acidic=True, pKs=[1.16], strong=True)
Trisulfane = ts.Compound(name="Trisulfane", acidic=True, pKs=[4.2], strong=False)
Trithiocarbonicacid = ts.Compound(name="Trithiocarbonicacid", acidic=True, pKs=[2.68], strong=False)
Valericacid = ts.Compound(name="Valericacid", acidic=True, pKs=[4.84], strong=False)
Hydrogenhyperoxide = ts.Compound(name="Hydrogenhyperoxide", acidic=True, pKs=[4.7], strong=False)
Hydrogenozonide = ts.Compound(name="Hydrogenozonide", acidic=True, pKs=[8.2], strong=False)
Hydrogenperoxide = ts.Compound(name="Hydrogenperoxide", acidic=True, pKs=[11.62], strong=False)
Tartaricacid = ts.Compound(name="Tartaricacid", acidic=True, pKs=[2.98], strong=False)
Tungsticacid = ts.Compound(name="Tungsticacid", acidic=True, pKs=[3.8], strong=False)
Xenon_VI_acid = ts.Compound(name="Xenon_VI_acid", acidic=True, pKs=[10.5], strong=False)
Xenon_VIII_acid = ts.Compound(name="Xenon_VIII_acid", acidic=True, pKs=[2.0], strong=False)

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

acids = [HCl,
         HI,
         HNO3,
         HBr,
         HCLO4,
         TsOH,
         propane1sulfonicacid,
         propane2sulfonicacid,
         Amidosulfonicacid,
         Benzenesulfonicacid,
         Bromicacid,
         Hydrobromicacid,
         Butanesulfonicacid,
         Chlorousacid,
         Chlorosulfonicacid,
         Chloricacid,
         Chromicacid,
         Dibromoaceticacid,
         Dichloroaceticacid,
         Dichromicacid,
         Difluoroaceticacid,
         Difluorophosphoricacid,
         Diiodoaceticacid,
         Dimethylphosphonicacid,
         Disulfuricacid,
         Dithionicacid,
         Ethanesulfonicacid,
         Fluorosulfonicacid,
         Heptafluoropropanesulfonicacid,
         EDTA,
         Citric,
         Carbonic,
         Acetic,
         Ammonium,
         MalicAcid,
         Enanthicacid,
         Acrylicacid,
         Adipicacid,
         Alanine,
         Formicacid,
         Amidophosphonicacid,
         Arsenicacid,
         AzelaicAcid,
         Benzoicacid,
         Succinicacid,
         Hydrocyanicacid,
         Bromoaceticacid,
         Brominousacid,
         Butanethiol,
         Butyricacid,
         Butylarsonicacid,
         Butylphosphinicacid,
         Butylphosphonicacid,
         Capricacid,
         Caproicacid,
         Caprylicacid,
         Chloroaceticacid,
         Citricacid,
         Crotonicacid,
         Cyanicacid,
         Diamidophosphonicacid,
         Dihydrogenperoxodiphosphate,
         Disulfane,
         Dithioarsenicacid,
         Iron_VI_acid,
         Aceticacid,
         Ethanethiol,
         Ethylarsonicacid,
         Ethylhydroperoxide,
         Ethylphosphinicacid,
         Ethylphosphonicacid,
         Fluoroaceticacid,
         Hydrofluoricacid,
         Glycine,
         Glycolicacid,
         Hexafluoroantimonicacid,
         Hexafluoroarsenicacid,
         Hexafluorophosphoricacid,
         Hexafluorotitan_IV_acid,
         Hexafluorosilicicacid,
         Hexasulfane,
         Hydrazidosulfonicacid,
         Hydrogenperoxodiphosphate,
         Hypobromousacid,
         Hypochlorousacid,
         Hypodiphosphoricacid,
         HypoiodousAcid,
         Hypophosphorousacid,
         Hypo_nitrousacid,
         Hypothiocyaniticacid,
         Imidodiphosphoricacid,
         Iodicacid,
         Iodoaceticacid,
         HydroiodicAcid,
         Isocyanicacid,
         Isopropylhydroperoxide,
         Isopropyloxonium,
         Isothiocyanicacid,
         Carbonicacid,
         Subericacid,
         Malonicacid,
         Manganese_VI_acid,
         Melliticacid,
         Metaarsenousacid,
         Metaboricacid,
         Metagermanicacid,
         Metasilicicacid,
         Metaniobicacid,
         Metaperiodicacid,
         Metatantalicacid,
         Metavanadium_V_acid,
         Methanal,
         Methaneselenol,
         Methanesulfonicacid,
         Methanethiol,
         Methylarsonicacid,
         Methylhydroperoxide,
         Methylphosphinicacid,
         Methylphosphonicacid,
         Methylsulfinicacid,
         Lacticacid,
         Molybdicacid,
         Monofluorophosphoricacid,
         Nitramine,
         Nitromethane,
         Octanesulfonicacid,
         Ortho_periodicacid,
         Orthoantimonicacid,
         Orthoboricacid,
         Orthogermanicacid,
         Orthosilicicacid,
         Orthotelluricacid,
         Orthovanadicacid,
         Oxalicacid,
         p_Toluenesulfonicacid,
         Pelargonicacid,
         Pentacarbonylmanganese,
         Pentafluoroethanesulfonicacid,
         Pentasulfane,
         Perchlorylamide,
         Perchlorylamine,
         Perchromicacid,
         Permanganicacid,
         Perosmicacid,
         Peroxoformicacid,
         Peroxobutyricacid,
         Peroxodiphosphoricacid,
         Peroxodisulfuricacid,
         Peroxyaceticacid,
         Peroxohypositrousacid,
         Peroxopropionicacid,
         Peroxonitricacid,
         Peroxo_nitrousacid,
         Peroxosulphuricacid,
         Perrhenicacid,
         Perruthenicacid,
         Pertechneticacid,
         Phenol,
         Phenylphosphonicacid,
         Phenylsulfinicacid,
         Phosphorousacid,
         Phosphoricacid,
         Pimelicacid,
         Polyacid,
         Propanethiol,
         Propionicacid,
         Propylarsonicacid,
         Propylphosphinicacid,
         Propylphosphonicacid,
         SalicylicAcid,
         Nitricacid,
         Nitrousacid,
         Hydrochloricacid,
         Sulfuricacid,
         Hydrogensulfide,
         Sulphurousacid,
         Seaborgium_VI_acid,
         Sebacicacid,
         Selenousacid,
         Selenophenol,
         Selenophosphoricacid,
         Selenicacid,
         Hydroselenicacid,
         Hydrazoicacid,
         Tartronicacid,
         Telluricacid,
         Tetracarbonyliron,
         Tetrafluoroboricacid,
         Tetraphosphoricacid,
         Tetrasulfane,
         Tetrathiophosphoricacid,
         Thioarsenicacid,
         Thiocyanicacid,
         Thiophenol,
         Thiophosphoricacid,
         Thiosulfuricacid,
         Thioselenicacid,
         Tribromoaceticacid,
         Trichloroaceticacid,
         Trifluoroaceticacid,
         Trifluoromethanesulfonicacid,
         Trihydrogenperoxodiphosphate,
         Triiodoaceticacid,
         Trioxide,
         Triphosphoricacid,
         Triselenocarbonicacid,
         Trisulfane,
         Trithiocarbonicacid,
         Valericacid,
         Hydrogenhyperoxide,
         Hydrogenozonide,
         Hydrogenperoxide,
         Tartaricacid,
         Tungsticacid,
         Xenon_VI_acid,
         Xenon_VIII_acid]

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

strong_acids = [i for i in acids if i.strong == True]
weak_acids = [i for i in acids if i.strong == False]
strong_bases = [i for i in bases if i.strong == True]
weak_bases = [i for i in bases if i.strong == False]