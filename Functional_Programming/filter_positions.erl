-module(filter_positions).
-export([main/0]).

read_input(I) ->
	case io:fread("", "~d") of
		eof -> ok;
		{ok, [N]} ->
			if I rem 2 == 1 -> ok;
				true -> io:format("~p~n", [N])
			end,
			read_input(I+1)
	end.

main() ->
	read_input(1)
	.
