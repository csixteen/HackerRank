-module(update_list).
-export([main/0]).

update_list() ->
	case io:fread("", "~d") of
		eof -> ok;
		{ok, [X]} ->
			io:format("~p~n", [abs(X)]),
			update_list()
	end.

main() ->
	update_list()
	.
