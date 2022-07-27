all_distinct(List) :- List = [].
all_distinct(List) :- List = [H|T], not_member(H,T), all_distinct(T).

has_cycle(Path) :- \+all_distinct(Path).

not_member(_, []). 
not_member(X, [H|T]) :- X \= H, not_member(X,T).

inorder(leaf(X), [X]).
inorder(tree(Root, L, R), T) :- inorder(L, LT), inorder(R, RT), append(LT, [Root|RT], T).

can_be_installed(Software) :- requires(Software, ListA), is_all_installed(ListA).
is_all_installed([]).
is_all_installed([H|T]) :- installed(ListB), member(H, ListB), is_all_installed(T).
member(X, [X]).
member(X, [H|T]) :- X = H.
member(X, [H|T]) :- member(X,T).

requires(learn, [php, sql]).

installed([php, gcc]).

test_answer :- 
    \+ can_be_installed(learn),
    writeln("OK").

test_answer :-
    can_be_installed(learn),
    writeln("Wrong!").