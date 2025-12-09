1 from string_utils import split_by_capitals, split_at_number, parse_chemical_reaction, count_atoms_in_molecule, count_atoms_in_reaction
2 from equation_utils import ELEMENTS, generate_equation_for_element, build_equations, my_solve
3 from sympy import Eq, symbols, solve
4
5 def balance_reaction(reaction): # "Fe2O3 + H2 -> Fe + H2O"
6
7     # 1.parse reaction
8     reactants, products = parse_chemical_reaction(reaction) # ["Fe2O3", "H2"], ["Fe", "H2O"]
9     reactant_atoms = count_atoms_in_reaction(reactants) # [{'Fe':2, 'O':1}, {'H':2}]
10    product_atoms = count_atoms_in_reaction(products)
11
12    # 2.build equation and solve
13    equations, coefficients = build_equations(reactant_atoms, product_atoms)
14    coefficients = my_solve(equations, coefficients) + [1]
15
16    return coefficients # [1/3, 1, 2/3, 1]
