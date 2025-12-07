

def split_at_first_digit(formula):
    i = 0
    while i < len(formula) and not formula[i].isdigit():
      i += 1
    
    if i == len(formula):
      return (formula, 1)
        
    prefix = formula[:i]
    number = int(formula[i:])
    
    return (prefix, number)

def split_before_each_uppercases(formula):
   
    if not formula:
        return []

    segments = []
    start = 0
    
    
    for i in range(1, len(formula)):
        if formula[i].isupper():
            segments.append(formula[start:i])
            start = i
            
  
    segments.append(formula[start:])
    
    return segments


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    result = {} # Step 1: Initialize an empty dictionary to store atom counts

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        result[atom_name] = atom_count # Step 2: Update the dictionary with the atom name and count

    return result# Step 3: Return the completed dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
