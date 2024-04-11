from constraint import *


def overlap(t1, t2):
    t1 = t1.split("_")
    t2 = t2.split("_")
    if t1[0] != t2[0]:
        return True
    if abs(int(t1[1]) - int(t2[1])) < 2:
        return False
    return True

def ml_equal(t1, t2):
    t1 = t1.split("_")
    t2 = t2.split("_")
    if t1[1] != t2[1]:
        return True
    else:
        return False

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    variables = []
    ml_variables = []

    for i in range(1, int(casovi_AI)+1):
        problem.addVariable(f'AI_cas_{i}', AI_predavanja_domain)
        variables.append(f'AI_cas_{i}')
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    variables.append("AI_vezbi")

    for i in range(1, int(casovi_ML)+1):
        problem.addVariable(f'ML_cas_{i}', ML_vezbi_domain)
        variables.append(f'ML_cas_{i}')
        ml_variables.append(f'ML_cas_{i}')
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    variables.append("ML_vezbi")
    ml_variables.append("ML_vezbi")

    for i in range(1, int(casovi_BI)+1):
        problem.addVariable(f'BI_cas_{i}', BI_predavanja_domain)
        variables.append(f'BI_cas_{i}')
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    variables.append("BI_vezbi")

    for i in range(1, int(casovi_R)+1):
        problem.addVariable(f'R_cas_{i}', R_predavanja_domain)
        variables.append(f'R_cas_{i}')

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    for i in range(0, len(ml_variables)):
        for j in range(i+1, len(ml_variables)):
            problem.addConstraint(ml_equal, (ml_variables[i], ml_variables[j]))
    for i in range(0, len(variables)):
        for j in range(i + 1, len(variables)):
            problem.addConstraint(overlap, (variables[i], variables[j]))

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)