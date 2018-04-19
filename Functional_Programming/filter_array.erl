-module(filter_array).
-export([main/0]).

read_input(X) ->
	case io:fread("", "~d") of
		eof -> ok;
		{ok, [N]} ->
			if N < X -> io:format("~p~n", [N]);
				N >= X -> ok
			end,
			read_input(X)
	end.

main() ->
	{ok,[X]} = io:fread("", "~d"),
	read_input(X).
