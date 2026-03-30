from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # 1) site da se razlicni brojki,
    problem.addConstraint(AllDifferentConstraint(), variables)

    # 2) go pisas izrazo
    # \ e za da moze u nov red da pisas
    problem.addConstraint(lambda S,E,N,D,M,O,R,Y: \
                          ((S*1000 + E*100 + N*10 + D) + (M*1000 + O*100 + R*10 + E) )== (M*10000+O*1000+N*100+E*10+Y) ,variables)


    # ----------------------------------------------------

    print(problem.getSolution())