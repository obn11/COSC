even_length([]).
even_length([_|T]) :- odd_length(T).

odd_length(List) :- List \= [], [_|T] = List, even_length(T).

same_evens([]).
same_evens([_|T]) :- T = [_|T2], T2 = []. 
same_evens([_|T0]) :- T0 = [H1|T1], T1 = [_|T2], T2 = [H3|_], H1 == H3, same_evens(T1).

asbs([]).
asbs([H0|T0]) :- T0 = [H1|_], H0 == a, H1 == a, asbs(T0).
asbs([H0|T0]) :- bs(T0), H0 == a.
asbs([H0|T0]) :- bs(T0), H0 == b.
asbs([H0|T0]) :- T0 = [H1|_], H0 == a, H1 == b, bs(T0).

bs([]).
bs([H0|T0]) :- H0 == b, bs(T0).


	
test_answer :-
    asbs([b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b]),
    asbs([a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b]),
    asbs([a,a,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b]),
    asbs([a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]),
    asbs([a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b]),
    writeln('OK').