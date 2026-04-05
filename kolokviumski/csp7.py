from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lecture_slots_AI = int(input())
    lecture_slots_ML = int(input())
    lecture_slots_R = int(input())
    lecture_slots_BI = int(input())

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                         "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_exercises_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Add the variables here--------------------
    AI_lec_vars = [f'AI_lecture_{i+1}' for i in range(int(lecture_slots_AI))]
    ML_lec_vars = [f'ML_lecture_{i+1}' for i in range(int(lecture_slots_ML))]
    R_lec_vars = [f'R_lecture_{i+1}' for i in range(int(lecture_slots_R))]
    BI_lec_vars = [f'BI_lecture_{i+1}' for i in range(int(lecture_slots_BI))]

    problem.addVariables(AI_lec_vars, AI_lectures_domain)
    problem.addVariables(ML_lec_vars, ML_lectures_domain)
    problem.addVariables(R_lec_vars, R_lectures_domain)
    problem.addVariables(BI_lec_vars, BI_lectures_domain)

    AI_ex_var = "AI_exercises"
    ML_ex_var = "ML_exercises"
    BI_ex_var = "BI_exercises"

    problem.addVariable(AI_ex_var, AI_exercises_domain)
    problem.addVariable(ML_ex_var, ML_exercises_domain)
    problem.addVariable(BI_ex_var, BI_exercises_domain)

    variables = AI_lec_vars + ML_lec_vars + R_lec_vars + BI_lec_vars + [AI_ex_var, ML_ex_var, BI_ex_var]

    # ---Add the constraints here----------------
    # 1) da ne se preklopuvaat
    def cons(lec1, lec2):
        dl1, hl1 = lec1.split("_")
        dl2, hl2 = lec2.split("_")

        hl1, hl2 = int(hl1) , int(hl2)
        if dl1 != dl2:
            return True

        if abs(hl1 - hl2) >= 2:
            return True

        return False

    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            problem.addConstraint(cons, [variables[i] ,variables[j]])

    # 2) masinko ucenje vezbi i pred mora da zapocnuvaat vo razlicno vreme, pr ako ima cas vo pon od 12 , ne smee da ima cas od 12 vo bilo koj drug den
    def cons2(m1, m2):
        dm1, hm1 = m1.split("_")
        dm2, hm2 = m2.split("_")

        if hm1 == hm2:
            return False

        return True

    ml_all_var = ML_lec_vars + [ML_ex_var]

    for i in range(len(ml_all_var)):
        for j in range(i, len(ml_all_var)):
            if i != j:
                problem.addConstraint(cons, [ml_all_var[i], ml_all_var[j]])



    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)