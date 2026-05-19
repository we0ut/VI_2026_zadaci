from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Define the variables
    #print(papers)
    variables=[]
    for title, topic in papers.items():
        variables.append(f"{title} ({topic})")

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Change this section if necessary
    problem.addVariables(variables, domain)

    # Add the constraints
    # 1) najmnogu 4 trudovi po topic
    # problem.addConstraint(MaxSumConstraint(4), variables)
    def cons1(*vars):
        count = {}
        for v in vars:
            count[v] = count.get(v, 0) + 1
            if count[v] > 4:
                return False
        return True
    problem.addConstraint(cons1, variables)

    # 2) sekoj od trudovite mora da se vo svoj termin, t.e. ne moze Paper1 (AI) == T1 , Paper2 (AI) == T2
    trudovi = {}
    # for var in variables:
    #     topic = var.split(' (')[:-1]
    #     if topic not in trudovi:
    #         trudovi[topic] = []
    #     trudovi[topic].append(var)
    for title, topic in papers.items():
        var= f"{title} ({topic})"

        if topic not in trudovi:
            trudovi[topic]=[]
        trudovi[topic].append(var)

    for topic, var in trudovi.items():
        if len(var) <= 4:
            problem.addConstraint(AllEqualConstraint(), var)



    result = problem.getSolution()

    # Add the required print section
    if result:
        sort_vars=sorted(variables, key=lambda x: int(x.split(' ')[0].replace('Paper', '')))

        for var in sort_vars:
            print(f"{var}: {result[var]}")