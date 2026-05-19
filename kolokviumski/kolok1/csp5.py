from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # Add the domains
    problem.addVariable("Simona_attendance", [0, 1])
    problem.addVariable("Marija_attendance", [0,1])
    problem.addVariable("Petar_attendance", [0,1])
    problem.addVariable("time_meeting", list(range(12,20)))
    # ----------------------------------------------------

    # ---Add the constraints----------------
    # 1) simona mora da prisustvuva i mora da ima uste 1 so nea
    def cons1(marija, simona,petar, time):
        if simona == 0:
            return False

        if marija == 0 and petar == 0:
            return False

        return True
    problem.addConstraint(cons1, [ "Marija_attendance", "Simona_attendance", "Petar_attendance", "time_meeting"])

    # 2) mora da e vo nekoj od slobodnite termini
    def cons2(marija, simona, petar, time):
        if simona == 1 and time not in [13,14,16,19]:
            return False

        if marija == 1 and time not in [14,15,18]:
            return False

        if petar == 1 and time not in [12,13,16,17,18,19]:
            return False

        return True

    problem.addConstraint(cons2, ["Marija_attendance", "Simona_attendance" ,"Petar_attendance", "time_meeting"])


    #

    # ----------------------------------------------------

    #[print(solution) for solution in problem.getSolutions()]

    # tocna e zadacata i bez ova, ama taka mi go dade gemini i svetna mi zelena, sekak gi imate site poeni

    solutions = problem.getSolutions()

    # 1. Дефинирај ја листата со посакуваниот редослед на клучевите
    desired_order = ["Simona_attendance", "Marija_attendance", "Petar_attendance", "time_meeting"]

    # 2. Измини ги решенијата и препакувај ги
    for solution in solutions:
        # Креира нов речник каде вредностите се земаат по дадениот редослед
        ordered_solution = {key: solution[key] for key in desired_order}
        print(ordered_solution)