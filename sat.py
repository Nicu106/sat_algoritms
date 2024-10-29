import time
import random


# Base class for SAT algorithms
class SATAlgorithm:
    def __init__(self, clauses):
        self.clauses = clauses
        self.assignment = {}

    def solve(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


# Implementation of the DPLL algorithm
class DPLL(SATAlgorithm):
    def solve(self):
        result, assignment = self._dpll(self.clauses, {})
        self.assignment = assignment  # Update self.assignment with final result
        return result, assignment

    def _dpll(self, clauses, assignment):
        if all(self._is_clause_satisfied(clause, assignment) for clause in clauses):
            return True, assignment
        if any(self._is_clause_unsatisfied(clause, assignment) for clause in clauses):
            return False, assignment

        var = self._select_unassigned_variable(clauses, assignment)
        for value in [True, False]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            result, final_assignment = self._dpll(clauses, new_assignment)
            if result:
                return True, final_assignment  # Return satisfying assignment
        return False, assignment

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var) == val for var, val in clause)

    def _is_clause_unsatisfied(self, clause, assignment):
        return all(assignment.get(var) is not None and assignment[var] != val for var, val in clause)

    def _select_unassigned_variable(self, clauses, assignment):
        for clause in clauses:
            for var, _ in clause:
                if var not in assignment:
                    return var
        return None


# Simplified implementation of the CDCL algorithm
class CDCL(SATAlgorithm):
    def solve(self):
        result, assignment = self._cdcl(self.clauses, {})
        self.assignment = assignment  # Update self.assignment with final result
        return result, assignment

    def _cdcl(self, clauses, assignment):
        while True:
            unsatisfied_clauses = [clause for clause in clauses if not self._is_clause_satisfied(clause, assignment)]
            if not unsatisfied_clauses:
                return True, assignment  # All clauses satisfied
            conflict_clause = unsatisfied_clauses[0]
            for var, val in conflict_clause:
                if var not in assignment:
                    assignment[var] = not val  # Flip assignment on first conflict
                    break
            else:
                return False, assignment  # Return unsatisfiable if stuck in a conflict cycle

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var) == val for var, val in clause)


# Implementation of the Max-SAT algorithm
class MaxSAT(SATAlgorithm):
    def solve(self):
        satisfied_clauses, best_assignment = 0, {}
        for _ in range(50):  # Increased to 50 iterations
            temp_assignment = {var: random.choice([True, False]) for var, _ in self.clauses[0]}
            count = sum(self._is_clause_satisfied(clause, temp_assignment) for clause in self.clauses)
            if count > satisfied_clauses:
                satisfied_clauses, best_assignment = count, temp_assignment
        self.assignment = best_assignment
        return satisfied_clauses == len(self.clauses), best_assignment

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var) == val for var, val in clause)


# Implementation of the GSAT algorithm
class GSAT(SATAlgorithm):
    def solve(self, max_flips=500):
        # Initialize assignment for each variable in the first clause
        assignment = {var: random.choice([True, False]) for var, _ in self.clauses[0]}

        for _ in range(max_flips):
            if all(self._is_clause_satisfied(clause, assignment) for clause in self.clauses):
                self.assignment = assignment
                return True, assignment

            clause = self._select_unsatisfied_clause(assignment)
            if clause is None:
                break

            var = random.choice(clause)
            if var[0] not in assignment:
                assignment[var[0]] = random.choice([True, False])  # Initialize if not present

            assignment[var[0]] = not assignment[var[0]]  # Flip the variable's value
        self.assignment = assignment
        return False, assignment

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var) == val for var, val in clause)

    def _select_unsatisfied_clause(self, assignment):
        unsatisfied = [clause for clause in self.clauses if not self._is_clause_satisfied(clause, assignment)]
        return random.choice(unsatisfied) if unsatisfied else None


# Class for comparing SAT algorithms
class SATComparison:
    def __init__(self, clauses):
        self.clauses = clauses
        self.algorithms = {
            "DPLL": DPLL(clauses),
            "CDCL": CDCL(clauses),
            "Max-SAT": MaxSAT(clauses),
            "GSAT": GSAT(clauses)
        }

    def run_and_compare(self, max_flips=500):
        results = {}
        for name, algo in self.algorithms.items():
            start_time = time.time()
            if name == "GSAT":
                result, assignment = algo.solve(max_flips=max_flips)
            else:
                result, assignment = algo.solve()
            end_time = time.time()
            results[name] = {
                "Result": result,
                "Time": end_time - start_time,
                "Assignment": assignment
            }
        return results


# Parameters for generating a massive dataset
num_clauses = 1000  # Number of clauses
num_variables = 10  # Number of distinct variables


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

# Run comparison
comparison = SATComparison(clauses)
results = comparison.run_and_compare()

# Print results
for name, data in results.items():
    print(f"Algorithm: {name}")
    print(f"Result: {'Satisfiable' if data['Result'] else 'Unsatisfiable'}")
    print(f"Time: {data['Time']:.4f} seconds")
    print(f"Assignment: {data['Assignment']}")
    print("----------")