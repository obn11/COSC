listtran([], []).
listtran(G, E) :- [GN|T1] = G, [EN|T2] = E, tran(GN,EN), listtran(T1, T2).

twice([], []).
twice(In, Out) :- [H1|Inr] = In, [H1|T] = Out, [H1|Outr] = T, twice(Inr, Outr).

remove(X, [], []).
remove(X, [X|ListIn], ListOut) :- remove(X, ListIn, ListOut).
remove(X, [A|ListIn], [A|ListOut]) :- A \= X, remove(X, ListIn, ListOut).

split_odd_even([], [], []).
split_odd_even([X], [X], []).
split_odd_even([A|[B|ListIn]], [A|ListA], [B|ListB]) :- split_odd_even(ListIn, ListA, ListB).

preorder(leaf(X), [X]).
preorder(tree(Root, L, R), [Root|RR]) :- append(T1, T2, RR), preorder(L, T1), preorder(R, T2).

has_cycle([A|R]) :- has_cycle(R).
has_cycle([A|R]) :- member(A, R).

requires(learn, [php, sql]).

installed([php, gcc]).

installed2([]).
installed2([H|T]) :- member(H, List), installed(List), T = [].
installed2([H|T]) :- member(H, List), installed(List), installed2(T).
can_be_installed(Software) :- requires(Software, List), installed2(List).

inorder(leaf(X), [X]).
inorder(tree(Root, Left, Right), R) :- inorder(Left, R1), inorder(Right, R2), append(R1, [Root|R2], R).

test_answer :- inorder(tree(1, leaf(2), leaf(3)), T), writeln(T).


