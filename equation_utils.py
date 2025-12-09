from sympy import Eq, symbols, solve

ELEMENTS = {
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Uue', 'Ubn', 'Ubu', 'Ubb', 'Ubt', 'Ubq', 'Ubp', 'Ubh', 'Ubs', 'Ubo', 'Ube'
}

def generate_equation_for_element(compounds, coefficients, element):
    """Generates a symbolic equation for the given element from compounds and coefficients.
    Example: For H in reactants ([{'H': 2, 'O': 1}, {'H': 2}], [a0, a1], 'H') returns 2*a0 + 2*a1"""
    equation = 0
    for i, compound in enumerate(compounds):
        if element in compound:
            equation += coefficients[i] * compound[element]
    return equation

def build_equations(reactant_atoms, product_atoms):
    """Builds a list of symbolic equations for each element to balance a chemical reaction.
    Example: For H2 + O2 -> H2O, returns equations [2*a0 = 2*a2, 2*a1 = 1*a2]
    """
    ## coefficients ##
    reactant_coefficients = list(symbols(f'a{i}' for i in range(len(reactant_atoms))))
    product_coefficients = list(symbols(f'b{i}' for i in range(len(product_atoms))[:-1]))
    product_coefficients = product_coefficients + [1] # Ensure the last coefficient is 1

    ## equations ##
    equations = []
    for element in ELEMENTS:
        lhs = generate_equation_for_element(reactant_atoms, reactant_coefficients, element)
        rhs = generate_equation_for_element(product_atoms, product_coefficients, element)
        if lhs != 0 or rhs != 0:
            equations.append(Eq(lhs, rhs))
            
    coefficients = reactant_coefficients + product_coefficients
    
    return equations, coefficients
