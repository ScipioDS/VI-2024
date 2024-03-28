from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19, 20])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(lambda a, b: a == 1 and b in [13, 14, 16, 19],
                          ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(lambda a, b, c:
                          ((a == 1 and c in [14, 15, 18]) or (a == 0 and c not in [14, 15, 18])) and
                          ((b == 1 and c in [12, 13, 16, 17, 18, 19, 20]) or (b == 0 and c not in [12, 13, 16, 17, 18])),
                          ("Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"))
    problem.addConstraint(lambda a, b, c: a == 1 and (b == 1 or c == 1),
                          ("Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"))
    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]
    for solution in problem.getSolutions():
        print('{', end='')
        print(f"'Simona_prisustvo': {solution.get('Simona_prisustvo')}, ", end="")
        print(f"'Marija_prisustvo': {solution.get('Marija_prisustvo')}, ", end="")
        print(f"'Petar_prisustvo': {solution.get('Petar_prisustvo')}, ", end="")
        print(f"'vreme_sostanok': {solution.get('vreme_sostanok')}", end="")
        print('}')