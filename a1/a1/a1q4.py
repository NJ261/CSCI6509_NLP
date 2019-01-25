from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
    input_symbols={'a', 'b'},
    transitions={
        # Use '' as the key name for empty string (lambda/epsilon) transitions
        'q0': {'a': {'q3'}, '': {'q1'}},
        'q1': {'a': {'q4'}, '': {'q2'}},
        'q2': {'b': {'q5'}, '': {'q0'}},
        'q3': {'b': {'q6'}},
        'q4': {'a': {'q7'}},
        'q5': {'b': {'q8'}},
        'q6': {},
        'q7': {'': {'q8'}},
        'q8': {'': {'q2'}}

    },
    initial_state='q0',
    final_states={'q6'}
)

dfa = DFA.from_nfa(nfa)  # returns an equivalent DFA

print("DFA table")
print(dfa.transitions, "\n")

print("Intial State: ", dfa.initial_state)
print("Final State: ", dfa.final_states, "\n")

print("check whether the string is accepted or not")
print(nfa.accepts_input('bbab'))

