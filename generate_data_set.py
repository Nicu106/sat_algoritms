import random

# Parameters for generating a massive dataset
num_clauses = 1000    # Number of clauses
num_variables = 10     # Number of distinct variables

# Function to generate random clauses
def generate_clauses(num_clauses, num_variables):
    clauses = []
    for _ in range(num_clauses):
        clause_length = random.randint(2, 4)  # Clause length between 2 and 4
        clause = [(random.randint(1, num_variables), random.choice([True, False])) for _ in range(clause_length)]
        clauses.append(clause)
    return clauses

# Generate the dataset
clauses = generate_clauses(num_clauses, num_variables)