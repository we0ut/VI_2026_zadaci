from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

B = 'budget'
M = 'marketing'
I = 'interested'
R = 'reviews'
T = 'testdrive'
D = 'discount'
C = 'purchase'

model = DiscreteBayesianNetwork([
    (B, I),
    (M, I),
    (I, R),
    (I, T),
    (R, C),
    (T, C),
    (D, C),
])
# verojatnosti
cpd_B = TabularCPD(
    variable=B,
    variable_card=2,
    values=[
        [0.65], # B = 0
        [0.35]
    ]
)
cpd_M = TabularCPD(
    variable=M,
    variable_card=2,
    values=[
        [0.55], # M = 0
        [0.45]
    ]
)
cpd_D = TabularCPD(
    variable=D,
    variable_card=2,
    values=[
        [0.75],
        [0.25]
    ]
)

#P(I=1 | B,M):
cpd_I = TabularCPD(
    variable=I,
    variable_card=2,
    values=[
        [1-0.12, 1-0.65, 1-0.72, 1-0.93],  # I=0
        [0.12, 0.65, 0.72, 0.93]  # I=1
    ],
    evidence=[B, M],
    evidence_card=[2, 2]
)

#P(R=? | I=?)
cpd_R = TabularCPD(
    variable=R,
    variable_card=2,
    values=[
        [0.8, 0.2], # R=0
        [0.2, 0.8]  # R=1
    ],
    evidence=[I],
    evidence_card=[2]
)

#P(T=? | I=?)
cpd_T = TabularCPD(
    variable=T,
    variable_card=2,
    values=[
        [0.7, 0.15], # R=0
        [0.3, 0.85]  # R=1
    ],
    evidence=[I],
    evidence_card=[2]
)

#P(C=? | R,T,D):
cpd_C = TabularCPD(
    variable=C,
    variable_card=2,
    values=[
        [1-0.04, 1-0.32, 1-0.48, 1-0.75, 1-0.55, 1-0.78, 1-0.88, 1-0.97], # C=0
        [0.04, 0.32, 0.48, 0.75, 0.55, 0.78, 0.88, 0.97] # C=1
    ],
    evidence=[R, T, D],
    evidence_card=[2, 2, 2]
)

cpds =[cpd_C, cpd_D, cpd_I, cpd_R, cpd_B, cpd_M, cpd_T]

model.add_cpds(*cpds)

# print("Model valid:", model.check_model())
infer = VariableElimination(model)

# 1) P(I=1 | B=1, M=1):
q1 = infer.query(
    variables=[I],
    evidence={B:1, M:1}
)
print(F"P(I=1 | B=1, M=1) = {q1.values[1]}")

# 2) P(R=1 | I=1):
q2 = infer.query(
    variables=[R],
    evidence={I:1}
)
print(f"P(R=1 | I=1) = {q2.values[1]}")

# 3) P(C=1 | T=1):
q3 = infer.query(
    variables=[C],
    evidence={T:1}
)
print(f"P(C=1 | T=1) = {q3.values[1]}")

# 4) P(B=1 | I=1)
q4 = infer.query(
    variables=[B],
    evidence={I:1}
)
print(f"P(B=1 | I=1) = {q4.values[1]}")

# 5) P(M=1 | I=1)
q5 = infer.query(
    variables=[M],
    evidence={I:1}
)
print(f"P(M=1 | I=1) = {q5.values[1]}")

# 6) P(T=1 | C=1, R=0)
q6 = infer.query(
    variables=[T],
    evidence={C:1, R:0}
)
print(f"P(T=1 | C=1, R=0) = {q6.values[1]}")


