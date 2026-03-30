from constraint import Problem, BacktrackingSolver, AllDifferentConstraint


def read_input():
    num_families = int(input())
    families = {}
    for _ in range(num_families):
        name, size, reqs_string = input().split()
        reqs = reqs_string.split('-')
        families[name] = {'size': int(size), 'requirements': reqs}

    num_rooms = int(input())
    rooms = {}
    for _ in range(num_rooms):
        room_id, capacity, amenities_string = input().split()
        floor = room_id[0]
        amenities = amenities_string.split('-')
        rooms[int(room_id)] = {'floor': int(floor), 'capacity': int(capacity), 'amenities': amenities}

    return families, rooms



if __name__ == '__main__':
    problem = Problem(solver=BacktrackingSolver())

    families, rooms = read_input()

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.
    variables = [k for k in families.keys()]
    domains = [k for k in rooms.keys()]

    brsoba=1
    for name in variables:
        temp = []
        for dom in domains:
            flag = True

            if families[name]['size'] <= rooms[dom]['capacity']:
                for i in families[name]['requirements']:
                    if i not in rooms[dom]['amenities']:
                        flag = False
                        break

            else:
                continue

            if flag:
                temp.append(dom)

        temp.append(f'Soba{brsoba}')
        brsoba+=1
        problem.addVariable(name, temp)
    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.

    problem.addConstraint(AllDifferentConstraint(), variables)

    solutions = problem.getSolutions()  # Ne menuvaj! Do not modify!

    # Ispechatete go najdobroto reshenie vo baraniot format.
    # Print the best solution in the required format.
    if solutions is not None:

        best_sol = None
        max_lugje = -1

        for sol in solutions:
            temp = 0
            remove = []
            for name, room in sol.items():
                if not "Soba" in str(sol[name]):
                    temp += families[name]['size']
                else:
                    remove.append(name)

            if temp > max_lugje:
                max_lugje = temp
                best_sol = sol

            for name in remove:
                del sol[name]

        if best_sol is not None:
            print("Best assignment:")

            lista = []

            for name, room in best_sol.items():
                if room in rooms:
                    lista.append((room, name))

            lista.sort()

            for room, name in lista:
                print(f"{name}->{room}")
    else:
        print("No Solution!")
