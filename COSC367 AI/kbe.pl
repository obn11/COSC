/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

/* astigmatic related clauses */
yes(ASTIGMATIC) :- ASTIGMATIC = yes.
no(ASTIGMATIC) :- ASTIGMATIC = no.

/* main */
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = hard_lenses, young(Age), Astigmatic = yes, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = soft_lenses, young(Age), Astigmatic = no, normal_tear_rate(Tear_Rate).
diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- Recommend = no_lenses, Age = _, Astigmatic = _, low_tear_rate(Tear_Rate).

test_answer :-
    diagnosis(X, 45, no, 4),
    writeln(X).