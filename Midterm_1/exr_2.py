from constraint import *


def availablecheck(s, e, n, d, m, o, r, y):
    suma1 = s * 1000 + e * 100 + n * 10 + d * 1
    suma2 = m * 1000 + o * 100 + r * 10 + e * 1

    return (suma1 + suma2) == (m * 10000 + o * 1000 + n * 100 + e * 10 + y * 1)


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(availablecheck, variables)

    # ----------------------------------------------------

    print(problem.getSolution())