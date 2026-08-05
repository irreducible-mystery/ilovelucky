%% No global now: identity as mortal, message-receiving process.
%% Run: erl -noshell -s erlang_no_global_now demo -s init stop
%%      (or in erl shell: c(erlang_no_global_now), erlang_no_global_now:demo().)
-module(erlang_no_global_now).
-export([demo/0, counter/1]).

%% A process: state is INACCESSIBLE from outside. Identity = PID =
%% an address for conversation, not a location of state.
counter(N) ->
    receive
        {get, From}  -> From ! {count, N}, counter(N);
        increment    -> counter(N + 1);
        die          -> exit(normal)      %% death is real and social:
    end.                                  %% linked processes get notified.

demo() ->
    Pid = spawn(?MODULE, counter, [0]),

    %% Asynchronous sends: we do NOT know when these arrive.
    Pid ! increment,
    Pid ! increment,

    %% The only truth available is LOCAL and OBTAINED BY ASKING:
    Pid ! {get, self()},
    receive {count, N} -> io:format("counter says: ~p~n", [N]) end,

    %% Monitor the process: its death will be an EVENT we witness.
    Ref = monitor(process, Pid),
    Pid ! die,
    receive
        {'DOWN', Ref, process, Pid, Reason} ->
            io:format("process ~p died (~p). Its identity died with it.~n",
                      [Pid, Reason])
    end,

    %% Send to the dead: message vanishes silently. No error. The
    %% universe does not confirm delivery -- there is no global truth
    %% about who exists. Only timeouts and silence.
    Pid ! {get, self()},
    receive {count, _} -> io:format("impossible~n")
    after 200 -> io:format("silence. Absence of reply is all we ever get.~n")
    end.
