from constraint import *

def MaxFour(v1, v2, v3, v4, v5, v6 , v7, v8, v9 , v10):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    temp = [v1, v2, v3, v4, v5, v6 , v7, v8, v9 , v10]

    for v in temp:
        if v == "T1":
            count1 += 1
        if v == "T2":
            count2 += 1
        if v == "T3":
            count3 += 1
        if v == "T4":
            count4 += 1
    return count1 <= 4 and count2 <= 4 and count3 <= 4 and count4 <= 4


if __name__ == '__main__':
    num = int(input())

    papers = dict()
    ai =[]
    ml=[]
    nlp = []

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []
    for paper in papers.keys():
        variables.append(f'{paper} ({papers[paper]})')
        if papers[paper] == "AI":
            ai.append(f'{paper} ({papers[paper]})')
        elif papers[paper] == "ML":
            ml.append(f'{paper} ({papers[paper]})')
        elif papers[paper] == "NLP":
            nlp.append(f'{paper} ({papers[paper]})')

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(MaxFour, variables)
    if 0 < len(ai) <= 4:
        problem.addConstraint(AllEqualConstraint(), ai)
    if 0 < len(ml) <= 4:
        problem.addConstraint(AllEqualConstraint(), ml)
    if 0 < len(nlp) <= 4:
        problem.addConstraint(AllEqualConstraint(), nlp)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    for r in result:
        print(r + ": " + result.get(r))
