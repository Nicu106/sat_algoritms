import time
import random

# Clasa de bază pentru algoritmii SAT
class SATAlgorithm:
    def __init__(self, clauses):
        self.clauses = clauses
        self.assignment = {}

    def solve(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Implementarea algoritmului DPLL
class DPLL(SATAlgorithm):
    def solve(self):
        return self._dpll(self.clauses, {})

    def _dpll(self, clauses, assignment):
        if all(self._is_clause_satisfied(clause, assignment) for clause in clauses):
            return True, assignment
        if any(self._is_clause_unsatisfied(clause, assignment) for clause in clauses):
            return False, assignment
        var = self._select_unassigned_variable(clauses, assignment)
        for value in [True, False]:
            assignment[var] = value
            result, new_assignment = self._dpll(clauses, assignment)
            if result:
                return True, new_assignment
            assignment[var] = None
        return False, assignment

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var, val) == val for var, val in clause)

    def _is_clause_unsatisfied(self, clause, assignment):
        return all(assignment.get(var, val) != val for var, val in clause)

    def _select_unassigned_variable(self, clauses, assignment):
        for clause in clauses:
            for var, _ in clause:
                if var not in assignment:
                    return var
        return None

# Implementarea algoritmului CDCL (simplificată)
class CDCL(SATAlgorithm):
    def solve(self):
        return self._cdcl(self.clauses, {})

    def _cdcl(self, clauses, assignment):
        # Similar to DPLL, but uses conflict-driven clause learning
        # Placeholder for real implementation of CDCL
        # Example: detect conflicts, backjump, and learn new clauses
        return True, assignment  # placeholder result

# Implementarea algoritmului Max-SAT
class MaxSAT(SATAlgorithm):
    def solve(self):
        satisfied_clauses, best_assignment = 0, {}
        for _ in range(10):  # Repeat to find the best assignment
            temp_assignment = {var: random.choice([True, False]) for var, _ in self.clauses[0]}
            count = sum(self._is_clause_satisfied(clause, temp_assignment) for clause in self.clauses)
            if count > satisfied_clauses:
                satisfied_clauses, best_assignment = count, temp_assignment
        return satisfied_clauses == len(self.clauses), best_assignment

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var, val) == val for var, val in clause)

# Implementarea algoritmului GSAT
class GSAT(SATAlgorithm):
    def solve(self, max_flips=100):
        assignment = {var: random.choice([True, False]) for var, _ in self.clauses[0]}
        for _ in range(max_flips):
            if all(self._is_clause_satisfied(clause, assignment) for clause in self.clauses):
                return True, assignment
            clause = self._select_unsatisfied_clause(assignment)
            var = random.choice(clause)
            assignment[var[0]] = not assignment[var[0]]
        return False, assignment

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var, val) == val for var, val in clause)

    def _select_unsatisfied_clause(self, assignment):
        unsatisfied = [clause for clause in self.clauses if not self._is_clause_satisfied(clause, assignment)]
        return random.choice(unsatisfied) if unsatisfied else None

# Clasa de comparație pentru a evalua algoritmii
class SATComparison:
    def __init__(self, clauses):
        self.clauses = clauses
        self.algorithms = {
            "DPLL": DPLL(clauses),
            "CDCL": CDCL(clauses),
            "Max-SAT": MaxSAT(clauses),
            "GSAT": GSAT(clauses)
        }

    def run_and_compare(self):
        results = {}
        for name, algo in self.algorithms.items():
            start_time = time.time()
            result, assignment = algo.solve()
            end_time = time.time()
            results[name] = {
                "Result": result,
                "Time": end_time - start_time,
                "Assignment": assignment
            }
        return results

#<begin section where are generated datas for dataset>
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
#<end section where are generated datas for dataset>

comparison = SATComparison(clauses)
results = comparison.run_and_compare()

for name, data in results.items():
    print(f"Algorithm: {name}")
    print(f"Result: {'Satisfiable' if data['Result'] else 'Unsatisfiable'}")
    print(f"Time: {data['Time']:.4f} seconds")
    print(f"Assignment: {data['Assignment']}")
    print("----------")


#gg