-module(list_replication).
-export([main/0]).

replicate(_,0) -> ok;
replicate(X, N) when N > 0 ->
	io:format("~p~n", [X]),
	replicate(X, N-1).

read_input(N) ->
	case io:fread("", "~d") of
		eof -> ok;
		{ok, [X]} -> replicate(X, N), read_input(N)
	end.

main() ->
	{ok, [N]} = io:fread("", "~d"),
	read_input(N).
