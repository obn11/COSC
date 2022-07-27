eats(Person, Thing) :- likes(Person, Thing).
eats(Person, Thing) :- hungry(Person), edible(Thing).

reflection(point(X, Y), point(Y, X)).

word(article,a).
word(article,every).
word(noun,criminal).
word(noun,'big kahuna burger').
word(verb,eats).
word(verb,likes).

sentence(Word1,Word2,Word3,Word4,Word5) :-
        word(article, Word1),
        word(noun,Word2),
        word(verb,Word3),
        word(article,Word4),
        word(noun,Word5).

f(a).
f(b).
f(c).
g(b).
g(c).
h(c).
k(X):-f(X), g(X), h(X).