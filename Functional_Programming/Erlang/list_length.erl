-module(list_length).
-export([main/0]).

calculate_length() -> calculate_length(0).
calculate_length(Acc) ->
	case io:fread("", "~d") of
		eof -> Acc;
		{ok, [_]} -> calculate_length(Acc+1)
	end.

main() ->
	io:format("~p", [calculate_length()])
	.
