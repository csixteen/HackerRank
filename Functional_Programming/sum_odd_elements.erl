-module(sum_odd_elements).
-export([main/0]).

calculate_sum() -> calculate_sum(0).
calculate_sum(Acc) ->
	case io:fread("", "~d") of
		eof -> Acc;
		{ok, [X]} ->
			if X rem 2 /= 0 -> calculate_sum(X+Acc);
				 true -> calculate_sum(Acc)
			end
	end.

main() ->
	io:format("~p", [calculate_sum()])
	.
