from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # 1) site bukvi da imat razlicna vrednost
    problem.addConstraint(AllDifferentConstraint(), variables)

    # 2) B, D i E da imat neparni vrednosti
    def cons_2(l1, l2, l3):
        return l1%2 != 0 and l2%2 != 0 and l3%2 != 0
    problem.addConstraint(cons_2, ["B", "D", "E"])

    # 3) Збирот на променливите A, B и C не смее да биде помал од 100.
    problem.addConstraint(lambda x1,x2,x3: x1+x2+x3 >= 100, ["A", "B", "C"])

    # 4) Збирот на променливите D и E треба да биде 150.
    problem.addConstraint(ExactSumConstraint(150), ["D", "E"])

    # 5) Променливата F треба да има вредност чија цифра на единици е број делив со 4.
    def cons_5(l1):
        temp = l1%10
        return temp%4 == 0
    problem.addConstraint(cons_5, ["F"])
    # ----------------------------------------------------

    print(problem.getSolution())