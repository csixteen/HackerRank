-module(reverse_list).
-export([main/0]).

read_list() ->
	case io:fread("", "~d") of
		eof -> [];
		{ok, [X]} -> [X|read_list()]
	end.

reverse(L) -> reverse(L,[]).
reverse([], Acc) -> Acc;
reverse([X|Xs], Acc) -> reverse(Xs, [X|Acc]).

print_list([]) -> ok;
print_list([X|Xs]) ->
	io:format("~p~n", [X]),
	print_list(Xs).

main() ->
	L = read_list(),
	print_list(reverse(L))
	.

