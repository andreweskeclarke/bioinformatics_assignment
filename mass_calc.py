
# http://www.ionsource.com/Card/aatable/aatable.htm
# 'U' at https://pubchem.ncbi.nlm.nih.gov/compound/selenocysteine
MASSES =  {
  # Amino Acids
  'G': 57.05,
  'A': 71.08,
  'S': 87.08,
  'P': 97.12,
  'V': 99.07,
  'T': 101.1,
  'C': 103.1,
  'L': 113.2,
  'I': 113.2,
  'N': 114.1,
  'D': 115.1,
  'Q': 128.1,
  'K': 128.2,
  'E': 129.1,
  'M': 131.2,
  'H': 137.1,
  'F': 147.2,
  'R': 156.2,
  'Y': 163.2,
  'W': 186.2,
  # Special codes
  'U': 167.057,
  'B': 114.6, # D or N, average together
  'X': 0,
  '-': 0,
  }

def calc_mass(sequence):
  return sum([MASSES[a] for a in sequence])

