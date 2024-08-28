transitions = {
    "U": {"a": "T", "b": "R"},
    "R": {"a": "S", "b": "U"},
    "S": {"a": "R", "b": "T"},
    "T": {"a": "U", "b": "S"},
}


def check_path(sequence, initial_state="R"):
    state = initial_state
    path = [state]

    for action in sequence:
        if action in transitions[state]:
            state = transitions[state][action]
            path.append(state)
        else:
            return False, path

    return state == initial_state, path


sequence = input("Digite a sequencia de ações (a ou b): ").lower()
returns_to_initial, path = check_path(sequence)

print("Sequencia:", sequence)
print("Retorna para o estado inicial:", returns_to_initial)
print("Caminho:", " -> ".join(path))
