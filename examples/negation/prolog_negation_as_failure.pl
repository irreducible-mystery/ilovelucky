% Negation as Failure: the Closed World Assumption, live.
% Run: swipl -q -s prolog_negation_as_failure.pl -g demo -t halt
%
% Prolog's \+ means "I cannot prove this", NOT "this is false".
% Watch knowledge get RETRACTED BY LEARNING (non-monotonicity).

bird(tweety).
bird(pingu).
penguin(pingu).

% flies/1 uses negation as failure: a bird flies unless proven abnormal.
flies(X) :- bird(X), \+ abnormal(X).
abnormal(X) :- penguin(X).

% The scope trap: \+ with an unbound variable does NOT mean
% "there exists no X such that...". It means the naive query fails.
somebody_flies :- flies(_).

demo :-
    format("Does tweety fly? "), (flies(tweety) -> writeln(yes) ; writeln(no)),
    format("Does pingu fly?  "), (flies(pingu)  -> writeln(yes) ; writeln(no)),
    % Now the system LEARNS something, and a former truth dies:
    assertz(penguin(tweety)),
    format("...we learn tweety is a penguin...~n"),
    format("Does tweety fly now? "), (flies(tweety) -> writeln(yes) ; writeln(no)),
    % Classical logic can never do this: adding facts only ever adds theorems.
    % Prolog's world is non-monotonic: learning can DESTROY truths.
    format("~nThe 'no' above never meant 'false in the world'.~n"),
    format("It meant: 'absent from my file.' Bureaucratic metaphysics.~n").
