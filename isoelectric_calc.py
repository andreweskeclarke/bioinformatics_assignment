# http://www.chem.ucalgary.ca/courses/351/Carey5th/Ch27/ch27-1-4-2.html
# 'U' at https://collab.itc.virginia.edu/access/content/group/f85bed6c-45d2-4b18-b868-6a2353586804/P/Ch30_Chaudhry_J_Selenocysteine_Synthase_--Mus_muculus-_-/Ch30_Chaudhry_J_Selenocysteine_Synthase_--Mus_muculus-_-_Selenocysteine_Synthase.html
ISOELECTRIC = {
  # Amino Acids
  'G': 5.97,
  'A': 6.00,
  'S': 5.68,
  'P': 6.30,
  'V': 5.96,
  'T': 5.60,
  'C': 5.07,
  'L': 5.98,
  'I': 6.02,
  'N': 5.41,
  'D': 2.77,
  'Q': 5.65,
  'K': 9.74,
  'E': 3.22,
  'M': 5.74,
  'H': 7.59,
  'F': 5.48,
  'R': 10.76,
  'Y': 5.66,
  'U': 8.96,
  'W': 5.89,
  # Special codes
  'B': 4.09, # D or N, average together
  'X': 0,
  '-': 0,
  }

def calc_isoelectric(sequence):
  return sum([ISOELECTRIC[a] for a in sequence]) / len(sequence)
