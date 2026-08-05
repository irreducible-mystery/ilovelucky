% Answer Set Programming: TWO negations in one language.
% Run: clingo asp_two_negations.lp 0
%
%   not p   -- default negation: "no reason to believe p"  (ignorance)
%   -p      -- classical negation: "p is known to be false" (knowledge)
%
% The railroad crossing, three epistemic situations:

% Situation A: we know nothing about a train at crossing a.
crossing(a).

% Situation B: we KNOW there is no train at crossing b.
crossing(b).
-train(b).

% Situation C: we know there IS a train at crossing c.
crossing(c).
train(c).

% Policy 1 (reckless): cross when there's no EVIDENCE of a train.
cross_reckless(X) :- crossing(X), not train(X).

% Policy 2 (safe): cross only when we KNOW there is no train.
cross_safe(X) :- crossing(X), -train(X).

% At crossing a: reckless crosses (ignorance ≠ safety!), safe does not.
% Booleans cannot express this distinction. ASP can.

#show cross_reckless/1.
#show cross_safe/1.
