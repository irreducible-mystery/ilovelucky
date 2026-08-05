% Stable models: truth as self-supporting equilibrium, possibly PLURAL.
% Run: clingo asp_plural_worlds.lp 0
%
% Each answer set is a self-justifying belief system.
% The solver doesn't return "the answer" -- it returns THE POSSIBLE WORLDS.

% A classic even cycle: each belief is justified by the other's absence.
day   :- not night.
night :- not day.

% => TWO stable models: {day} and {night}. Both are coherent worlds.
% The output's plurality is itself the finding: the axioms underdetermine reality.

% Add an odd cycle and a world can become UNLIVABLE:
% p :- not p.        % uncomment: with only this, NO stable model exists.
% A worldview that denies itself has no equilibrium. The solver reports:
% UNSATISFIABLE -- "there is no way for reality to be, given your beliefs."

#show day/0.
#show night/0.
