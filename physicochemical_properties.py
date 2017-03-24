import numpy as np
import ipdb


# Below are the entries from the AA Index site that I want to use
PHYSICOCHEMCIAL_PROPERTIES = {}

# H MCMT640101
# D Refractivity (McMeekin et al., 1964), Cited by Jones (1975)
# R 
# A McMeekin, T.L., Groves, M.L. and Hipp, N.J.
# T 
# J In "Amino Acids and Serum Proteins" (Stekol, J.A., ed.), American Chemical 
#   Society, Washington, D.C., p. 54 (1964)
# C CHAM820101    0.871  ROSG850101    0.857  FAUJ880103    0.847
#   FASG760101    0.845  CHOC750101    0.822  GRAR740103    0.817
#   BIGC670101    0.814  GOLD730102    0.814  KRIW790103    0.810
#   CHOC760101    0.809  FUKS010111   -0.806  RADA880103   -0.833
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#     4.34   26.66   13.28   12.00   35.77   17.56   17.26    0.00   21.81   19.06
#    18.78   21.29   21.64   29.40   10.93    6.35   11.01   42.53   31.53   13.92
# //
PHYSICOCHEMCIAL_PROPERTIES['refractivity'] = [
     4.34,   26.66,   13.28,  12.00,  35.77,  17.56,  17.26,   0.00,  21.81,  19.06, 
    18.78,   21.29,   21.64,  29.40,  10.93,   6.35,  11.01,  42.53,  31.53,  13.92
    ]

# H KARP850103
# D Flexibility parameter for two rigid neighbors (Karplus-Schulz, 1985)
# R
# A Karplus, P.A. and Schulz, G.E.
# T Prediction of chain flexibility in proteins
# J Naturwiss. 72, 212-213 (1985)
# C 
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#    0.892   0.901   0.930   0.932   0.925   0.885   0.933   0.923   0.894   0.872
#    0.921   1.057   0.804   0.914   0.932   0.923   0.934   0.803   0.837   0.913
# //
PHYSICOCHEMCIAL_PROPERTIES['flexibility'] = [
    0.892,  0.901,  0.930,  0.932,  0.925,  0.885,  0.933,  0.923,  0.894,  0.872,
    0.921,  1.057,  0.804,  0.914,  0.932,  0.923,  0.934,  0.803,  0.837,  0.913
    ]


# H TSAJ990101
# D Volumes including the crystallographic waters using the ProtOr (Tsai et al., 
#   1999)
# R PMID:10388571
# A Tsai, J., Taylor, R., Chothia, C. and Gerstein, M.
# T The packing density in proteins: standard radii and volumes
# J J. Mol. Biol. 290, 253-266 (1999) (Cyh 112.8)
# C TSAJ990102    1.000  CHOC750101    0.995  BIGC670101    0.993
#   GOLD730102    0.993  KRIW790103    0.988  FAUJ880103    0.983
#   GRAR740103    0.979  CHAM820101    0.977  CHOC760101    0.968
#   HARY940101    0.964  PONJ960101    0.960  FASG760101    0.935
#   LEVM760105    0.922  ROSG850101    0.914  LEVM760102    0.910
#   DAWD720101    0.903  CHAM830106    0.889  FAUJ880106    0.879
#   ZHOH040102    0.874  LEVM760107    0.866  RADA880106    0.861
#   LEVM760106    0.849  RADA880103   -0.875
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#     89.3   190.3   122.4   114.4   102.5   146.9   138.8    63.8   157.5   163.0
#    163.1   165.1   165.8   190.8   121.6    94.2   119.6   226.4   194.6   138.2
# //

PHYSICOCHEMCIAL_PROPERTIES['volume'] = [
     89.3,  190.3,  122.4,  114.4,  102.5,  146.9,  138.8,   63.8,  157.5,  163.0,
    163.1,  165.1,  165.8,  190.8,  121.6,   94.2,  119.6,  226.4,  194.6,  138.2
    ]


# H BULH740101
# D Transfer free energy to surface (Bull-Breese, 1974)
# R PMID:4839053
# A Bull, H.B. and Breese, K.
# T Surface tension of amino acid solutions: A hydrophobicity scale of the amino 
#   acid residues
# J Arch. Biochem. Biophys. 161, 665-670 (1974)
# C WOLS870101    0.929  PARJ860101    0.909  MIYS990101    0.884
#   MIYS990102    0.880  GRAR740102    0.822  GUYH850103    0.820
#   COWR900101   -0.804  ROBB790101   -0.813  BROC820101   -0.815
#   LEVM760106   -0.818  ZHOH040103   -0.828  CIDH920104   -0.829
#   FAUJ830101   -0.830  BASU050103   -0.833  EISD860101   -0.833
#   MIYS850101   -0.838  WILM950101   -0.845  BASU050102   -0.845
#   CIDH920103   -0.848  CIDH920102   -0.851  JOND750101   -0.853
#   ARGP820101   -0.854  BASU050101   -0.854  RADA880102   -0.856
#   ZHOH040102   -0.860  BLAS910101   -0.860  TAKK010101   -0.865
#   CIDH920105   -0.871  GOLD730101   -0.874  MEEJ800102   -0.875
#   ZHOH040101   -0.876  MEEJ810101   -0.876  ZIMJ680105   -0.879
#   MEEJ810102   -0.880  ROSM880104   -0.884  NOZY710101   -0.892
#   SIMZ760101   -0.894  VENT840101   -0.907  PLIV810101   -0.912
#   GUOD860101   -0.922  SWER830101   -0.923  CORJ870102   -0.923
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#    -0.20   -0.12    0.08   -0.20   -0.45    0.16   -0.30    0.00   -0.12   -2.26
#    -2.46   -0.35   -1.47   -2.33   -0.98   -0.39   -0.52   -2.01   -2.24   -1.56
# //
PHYSICOCHEMCIAL_PROPERTIES['free_energy'] = [
    -0.20,  -0.12,   0.08,  -0.20,  -0.45,   0.16,  -0.30,   0.00,  -0.12,  -2.26,
    -2.46,  -0.35,  -1.47,  -2.33,  -0.98,  -0.39,  -0.52,  -2.01,  -2.24,  -1.56
    ]


# H COSI940101
# D Electron-ion interaction potential values (Cosic, 1994)
# R PMID:7851912
# A Cosic, I.
# T Macromolecular bioactivity: is it resonant interaction between 
#   macromolecules?--Theory and applications
# J IEEE Trans Biomed Eng. 41, 1101-1114 (1994) (values are cited from Protein 
#   Eng. 15:193-203)
# C VELV850101    1.000
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#   0.0373  0.0959  0.0036  0.1263  0.0829  0.0761  0.0058  0.0050  0.0242  0.0000
#   0.0000  0.0371  0.0823  0.0946  0.0198  0.0829  0.0941  0.0548  0.0516  0.0057
# //
PHYSICOCHEMCIAL_PROPERTIES['electron_ion_interaction'] = [
   0.0373, 0.0959, 0.0036, 0.1263, 0.0829, 0.0761, 0.0058, 0.0050, 0.0242, 0.0000,
   0.0000, 0.0371, 0.0823, 0.0946, 0.0198, 0.0829, 0.0941, 0.0548, 0.0516, 0.0057
    ]


# H HOPT810101
# D Hydrophilicity value (Hopp-Woods, 1981)
# R PMID:6167991
# A Hopp, T.P. and Woods, K.R.
# T Prediction of protein antigenic determinants from amino acid sequecces
# J Proc. Natl. Acad. Sci. USA 78, 3824-3828 (1981)
# C LEVM760101    0.985  WOEC730101    0.886  PUNT030102    0.886
#   FUKS010104    0.884  ENGD860101    0.882  PRAM900101    0.881
#   KIDA850101    0.881  GRAR740102    0.874  MIYS990105    0.862
#   VINM940101    0.859  PUNT030101    0.858  FUKS010102    0.854
#   VHEG790101    0.849  ROSM880101    0.848  MIYS990104    0.843
#   OOBM770103    0.833  WOLS870101    0.830  MIYS990103    0.825
#   PARJ860101    0.819  MIYS990102    0.804  MIYS990101    0.803
#   GUYH850101    0.802  MIYS850101   -0.800  NADH010103   -0.805
#   NAKH900110   -0.812  ZIMJ680105   -0.816  JACR890101   -0.816
#   NADH010102   -0.820  NISK860101   -0.822  ROSG850102   -0.825
#   MEEJ800102   -0.826  RADA880101   -0.829  ZHOH040103   -0.829
#   BASU050103   -0.830  RADA880108   -0.831  CASG920101   -0.839
#   EISD840101   -0.846  BIOV880101   -0.848  WIMW960101   -0.855
#   RADA880102   -0.859  BIOV880102   -0.864  BLAS910101   -0.877
#   EISD860101   -0.905  FAUJ830101   -0.909  ROSM880105   -0.955
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#     -0.5     3.0     0.2     3.0    -1.0     0.2     3.0     0.0    -0.5    -1.8
#     -1.8     3.0    -1.3    -2.5     0.0     0.3    -0.4    -3.4    -2.3    -1.5
# //
PHYSICOCHEMCIAL_PROPERTIES['hydrophilicity'] = [
     -0.5,    3.0,    0.2,    3.0,   -1.0,    0.2,    3.0,    0.0,   -0.5,   -1.8,
     -1.8,    3.0,   -1.3,   -2.5,    0.0,    0.3,   -0.4,   -3.4,   -2.3,   -1.5
     ]


# H ZIMJ680103
# D Polarity (Zimmerman et al., 1968)
# R PMID:5700434
# A Zimmerman, J.M., Eliezer, N. and Simha, R.
# T The characterization of amino acid sequences in proteins by statistical 
#   methods
# J J. Theor. Biol. 21, 170-201 (1968)
# C PRAM900101    0.854  ENGD860101    0.854  HOPA770101    0.815
#   JACR890101   -0.835
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#     0.00   52.00    3.38   49.70    1.48    3.53   49.90    0.00   51.60    0.13
#     0.13   49.50    1.43    0.35    1.58    1.67    1.66    2.10    1.61    0.13
# //
PHYSICOCHEMCIAL_PROPERTIES['polarity'] = [
     0.00,  52.00,   3.38,  49.70,   1.48,   3.53,  49.90,   0.00,  51.60,   0.13,
     0.13,  49.50,   1.43,   0.35,   1.58,   1.67,   1.66,   2.10,   1.61,   0.13
     ]

# H EISD840101
# D Consensus normalized hydrophobicity scale (Eisenberg, 1984)
# R PMID:6383201
# A Eisenberg, D.
# T Three-dimensional structure of membrane and surface proteins
# J Ann. Rev. Biochem. 53, 595-623 (1984) Original references: Eisenberg, D., 
#   Weiss, R.M., Terwilliger, T.C. and Wilcox, W. Faraday Symp. Chem. Soc. 17, 
#   109-120 (1982) Eisenberg, D., Weiss, R.M. and Terwilliger, T.C. The 
#   hydrophobic moment detects periodicity in protein hydrophobicity Proc. Natl. 
#   Acad. Sci. USA 81, 140-144 (1984)
# C RADA880101    0.968  JACR890101    0.938  RADA880107    0.927
#   ROSM880105    0.923  WOLR810101    0.914  WOLR790101    0.909
#   RADA880104    0.908  JANJ790102    0.900  JURD980101    0.895
#   NADH010102    0.887  CHOC760103    0.885  BLAS910101    0.884
#   EISD860101    0.884  KYTJ820101    0.878  FAUJ830101    0.875
#   JANJ780102    0.874  OLSK800101    0.869  COWR900101    0.863
#   NADH010101    0.861  NADH010103    0.840  NAKH900110    0.838
#   EISD860103    0.837  DESM900102    0.828  RADA880108    0.817
#   BIOV880102    0.814  BIOV880101    0.811  YUTK870101    0.809
#   NADH010104    0.809  ROSG850102    0.806  BASU050103    0.806
#   WOLS870101   -0.820  GRAR740102   -0.823  MEIH800102   -0.829
#   HOPT810101   -0.846  GUYH850101   -0.849  PUNT030102   -0.854
#   LEVM760101   -0.859  OOBM770101   -0.878  JANJ780103   -0.881
#   FAUJ880109   -0.890  GUYH850104   -0.892  CHOC760102   -0.892
#   KIDA850101   -0.900  JANJ780101   -0.907  KUHL950101   -0.907
#   PUNT030101   -0.914  VHEG790101   -0.924  ROSM880102   -0.925
#   ENGD860101   -0.936  PRAM900101   -0.936  ROSM880101   -0.947
#   GUYH850105   -0.951
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#     0.25   -1.76   -0.64   -0.72    0.04   -0.69   -0.62    0.16   -0.40    0.73
#     0.53   -1.10    0.26    0.61   -0.07   -0.26   -0.18    0.37    0.02    0.54
# //
PHYSICOCHEMCIAL_PROPERTIES['hydrophobicity'] = [
     0.25,  -1.76,  -0.64,  -0.72,   0.04,  -0.69,  -0.62,   0.16,  -0.40,   0.73,
     0.53,  -1.10,   0.26,   0.61,  -0.07,  -0.26,  -0.18,   0.37,   0.02,   0.54
    ]

# H ZIMJ680104
# D Isoelectric point (Zimmerman et al., 1968)
# R PMID:5700434
# A Zimmerman, J.M., Eliezer, N. and Simha, R.
# T The characterization of amino acid sequences in proteins by statistical 
#   methods
# J J. Theor. Biol. 21, 170-201 (1968)
# C KLEP840101    0.941  FAUJ880111    0.813  FINA910103    0.805
# I    A/L     R/K     N/M     D/F     C/P     Q/S     E/T     G/W     H/Y     I/V
#     6.00   10.76    5.41    2.77    5.05    5.65    3.22    5.97    7.59    6.02
#     5.98    9.74    5.74    5.48    6.30    5.68    5.66    5.89    5.66    5.96
# //
PHYSICOCHEMCIAL_PROPERTIES['isoelectric_point'] = [
     6.00,  10.76,   5.41,   2.77,   5.05,   5.65,   3.22,   5.97,   7.59,   6.02,
     5.98,   9.74,   5.74,   5.48,   6.30,   5.68,   5.66,   5.89,   5.66,   5.96
     ]


AMINO_ACID_INDEXER = {
    'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5, 'E': 6, 'G': 7, 'H': 8, 'I': 9,
    'L': 10, 'K': 11, 'M': 12, 'F': 13, 'P': 14, 'S': 15, 'T': 16, 'W': 17, 'Y': 18, 'V': 19
    }


def amino_acid_property(amino_acid, properties):
  if amino_acid in ['X','-', 'U']:
    prop =  0
  elif amino_acid in 'B':
    prop = (properties[AMINO_ACID_INDEXER['D']] + properties[AMINO_ACID_INDEXER['N']]) / 2
  else:
    prop = properties[AMINO_ACID_INDEXER[amino_acid]]
  if prop is None:
    prop = 0
  return prop


def autocorr(x, t=1):
  if len(x) <= (t+4):
    return 0
  return np.corrcoef(np.array([x[0:len(x)-t], x[t:len(x)]]))[0,1]


def add_physicochemical_properties(data, sequences):
  keys = []
  keys.extend([k + '_sum' for k in PHYSICOCHEMCIAL_PROPERTIES.keys()])
  keys.extend([k + '_mean' for k in PHYSICOCHEMCIAL_PROPERTIES.keys()])
  for key, properties in PHYSICOCHEMCIAL_PROPERTIES.items():
    converted_sequence = [[amino_acid_property(a, properties) for a in s] for s in sequences]
    data[key + '_sum'] = [sum(s) for s in converted_sequence]
    data[key + '_mean'] = [sum(s)/len(s) for s in converted_sequence]
    for t in range(1,5):
      autocorr_key = '%s_autocorr%d' % (key, t)
      data[autocorr_key] = [autocorr(s, t) for s in converted_sequence]
      keys.append(autocorr_key)
  return data, keys


