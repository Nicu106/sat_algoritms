import time  # Importă modulul time pentru a măsura timpul de execuție
import random  # Importă modulul random pentru a genera valori aleatorii

# Clasa de bază pentru algoritmii SAT
class SATAlgorithm:
    def __init__(self, clauses):
        """
        Inițializează un algoritm SAT.

        :param clauses: Lista de clauze care reprezintă formula SAT.
        """
        self.clauses = clauses  # Stochează clauzele
        self.assignment = {}  # Dicționar pentru a păstra asignările variabilelor

    def solve(self):
        """
        Metodă abstractă pentru a rezolva problema SAT.
        Aceasta trebuie să fie implementată în subclase.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

# Implementarea algoritmului DPLL (Davis-Putnam-Logemann-Loveland)
class DPLL(SATAlgorithm):
    def solve(self):
        """
        Soluționează formula SAT folosind algoritmul DPLL.

        :return: Un tuplu (rezultat, asignare), unde rezultat este True dacă formula este satisfiabilă,
                 și asignarea este un dicționar al variabilelor și valorilor lor.
        """
        return self._dpll(self.clauses, {})  # Apelează metoda DPLL recursiv

    def _dpll(self, clauses, assignment):
        """
        Implementarea recursivă a algoritmului DPLL.

        :param clauses: Lista de clauze de verificat.
        :param assignment: Dicționar cu asignările curente ale variabilelor.
        :return: (rezultat, asignare)
        """
        # Verifică dacă toate clauzele sunt satisfăcute
        if all(self._is_clause_satisfied(clause, assignment) for clause in clauses):
            return True, assignment  # Formula este satisfiabilă

        # Verifică dacă există vreo clauză nesatisfăcută
        if any(self._is_clause_unsatisfied(clause, assignment) for clause in clauses):
            return False, assignment  # Formula este nesatisfiabilă

        # Alege o variabilă nealocată
        var = self._select_unassigned_variable(clauses, assignment)
        for value in [True, False]:
            assignment[var] = value  # Asignează o valoare variabilei
            result, new_assignment = self._dpll(clauses, assignment)  # Apelează recursiv
            if result:
                return True, new_assignment  # Găsim o soluție

            assignment[var] = None  # Revine și încearcă cealaltă valoare
        return False, assignment  # Nu am găsit o soluție

    def _is_clause_satisfied(self, clause, assignment):
        """
        Verifică dacă o clauză este satisfăcută de asignările curente.

        :param clause: Clauza de verificat.
        :param assignment: Asignările curente ale variabilelor.
        :return: True dacă clauza este satisfăcută, altfel False.
        """
        return any(assignment.get(var, val) == val for var, val in clause)

    def _is_clause_unsatisfied(self, clause, assignment):
        """
        Verifică dacă o clauză este nesatisfăcută.

        :param clause: Clauza de verificat.
        :param assignment: Asignările curente ale variabilelor.
        :return: True dacă clauza este nesatisfăcută, altfel False.
        """
        return all(assignment.get(var, val) != val for var, val in clause)

    def _select_unassigned_variable(self, clauses, assignment):
        """
        Alege prima variabilă care nu a fost încă asignată.

        :param clauses: Lista de clauze.
        :param assignment: Asignările curente ale variabilelor.
        :return: O variabilă nealocată sau None dacă nu există.
        """
        for clause in clauses:
            for var, _ in clause:
                if var not in assignment:
                    return var
        return None  # Dacă toate variabilele sunt asignate

# Implementarea algoritmului CDCL (Conflict-Driven Clause Learning)
class CDCL(SATAlgorithm):
    def solve(self):
        """
        Soluționează formula SAT folosind algoritmul CDCL.

        :return: Un tuplu (rezultat, asignare).
        """
        return self._cdcl(self.clauses, {})  # Apelează metoda CDCL recursiv

    def _cdcl(self, clauses, assignment):
        """
        Implementarea algoritmului CDCL.

        :param clauses: Lista de clauze de verificat.
        :param assignment: Dicționar cu asignările curente ale variabilelor.
        :return: (rezultat, asignare)
        """
        # Placeholder pentru implementarea reală a CDCL
        return True, assignment  # Aici ar trebui să fie implementat CDCL

# Implementarea algoritmului Max-SAT
class MaxSAT(SATAlgorithm):
    def solve(self):
        """
        Soluționează problema Max-SAT.

        :return: Un tuplu (rezultat, asignare), unde rezultat indică dacă toate clauzele sunt satisfăcute,
                 iar asignarea este cea mai bună găsită.
        """
        satisfied_clauses, best_assignment = 0, {}
        for _ in range(10):  # Repetă pentru a găsi cea mai bună asignare
            # Generează o asignare aleatoare
            temp_assignment = {var: random.choice([True, False]) for var, _ in self.clauses[0]}
            # Numără câte clauze sunt satisfăcute
            count = sum(self._is_clause_satisfied(clause, temp_assignment) for clause in self.clauses)
            if count > satisfied_clauses:
                satisfied_clauses, best_assignment = count, temp_assignment  # Salvează cea mai bună asignare
        return satisfied_clauses == len(self.clauses), best_assignment  # Verifică dacă toate clauzele sunt satisfăcute

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var, val) == val for var, val in clause)

# Implementarea algoritmului GSAT
class GSAT(SATAlgorithm):
    def solve(self, max_flips=100):
        """
        Soluționează formula SAT folosind algoritmul GSAT.

        :param max_flips: Numărul maxim de flip-uri aleatorii.
        :return: Un tuplu (rezultat, asignare).
        """
        # Începe cu o asignare aleatorie
        assignment = {var: random.choice([True, False]) for var, _ in self.clauses[0]}
        for _ in range(max_flips):
            # Verifică dacă toate clauzele sunt satisfăcute
            if all(self._is_clause_satisfied(clause, assignment) for clause in self.clauses):
                return True, assignment  # Găsim o soluție

            # Alege o clauză nesatisfăcută
            clause = self._select_unsatisfied_clause(assignment)
            var = random.choice(clause)  # Alege o variabilă din clauza nesatisfăcută
            assignment[var[0]] = not assignment[var[0]]  # Schimbă valoarea variabilei
        return False, assignment  # Returnează dacă nu am găsit o soluție

    def _is_clause_satisfied(self, clause, assignment):
        return any(assignment.get(var, val) == val for var, val in clause)

    def _select_unsatisfied_clause(self, assignment):
        """
        Selectează o clauză nesatisfăcută din lista de clauze.

        :param assignment: Asignările curente ale variabilelor.
        :return: O clauză nesatisfăcută sau None dacă nu există.
        """
        unsatisfied = [clause for clause in self.clauses if not self._is_clause_satisfied(clause, assignment)]
        return random.choice(unsatisfied) if unsatisfied else None

# Clasa de comparație pentru a evalua algoritmii
class SATComparison:
    def __init__(self, clauses):
        """
        Inițializează comparația între algoritmii SAT.

        :param clauses: Lista de clauze care reprezintă formula SAT.
        """
        self.clauses = clauses  # Stochează clauzele
        # Inițializează algoritmii
        self.algorithms = {
            "DPLL": DPLL(clauses),
            "CDCL": CDCL(clauses),
            "Max-SAT": MaxSAT(clauses),
            "GSAT": GSAT(clauses)
        }

    def run_and_compare(self):
        """
        Rulează fiecare algoritm și compară rezultatele.

        :return: Un dicționar cu rezultatele fiecărui algoritm.
        """
        results = {}  # Dicționar pentru a stoca rezultatele
        for name, algo in self.algorithms.items():
            start_time = time.time()  # Începe cronometrul
            result, assignment = algo.solve()  # Rezolvă problema
            end_time = time.time()  # Oprește cronometrul
            # Stochează rezultatele
            results[name] = {
                "Result": result,  # Satisfiabilitate
                "Time": end_time - start_time,  # Timpul de execuție
                "Assignment": assignment  # Asignarea variabilelor
            }
        return results

# Generarea datelor pentru dataset
num_clauses = 1000  # Numărul de clauze
num_variables = 10   # Numărul de variabile distincte

def generate_clauses(num_clauses, num_variables):
    """
    Generează o listă de clauze random.

    :param num_clauses: Numărul de clauze de generat.
    :param num_variables: Numărul de variabile distincte utilizate în clauze.
    :return: Lista de clauze generate.
    """
    clauses = []  # Lista pentru a stoca clauzele
    for _ in range(num_clauses):
        clause_length = random.randint(2, 4)  # Lungimea clauzei între 2 și 4
        # Generează o clauză random
        clause = [(random.randint(1, num_variables), random.choice([True, False])) for _ in range(clause_length)]
        clauses.append(clause)  # Adaugă clauza la lista de clauze
    return clauses

# Generarea dataset-ului
clauses = generate_clauses(num_clauses, num_variables)

# Compararea algoritmilor
comparison = SATComparison(clauses)  # Creează o instanță pentru comparație
results = comparison.run_and_compare()  # Rulează algoritmii și obține rezultatele

# Afișarea rezultatelor
for name, data in results.items():
    print(f"Algorithm: {name}")  # Numele algoritmului
    print(f"Result: {'Satisfiable' if data['Result'] else 'Unsatisfiable'}")  # Satisfiabilitate
    print(f"Time: {data['Time']:.4f} seconds")  # Timpul de execuție
    print(f"Assignment: {data['Assignment']}")  # Asignarea variabilelor
    print("----------")