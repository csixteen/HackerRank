-module(array_n_elements).
-export([main/0]).

%% Creates an array using tail recursion
create_array(N) -> create_array(N,[]).
create_array(0, Acc) -> Acc;
create_array(N, Acc) when N > 0 -> 
	create_array(N-1, [N|Acc]).

%% Not sure if Erlang has a function to output with
%% the desired format. Need to explore a bit more.
print_array(Arr) ->
	io:format("["),
	print_elements(Arr),
	io:format("]~n").

print_elements([X]) -> io:format("~p", [X]);
print_elements([X|Xs]) ->
	io:format("~p, ", [X]),
	print_elements(Xs).

main() ->
	{ok, [N]} = io:fread("", "~d"),
	Arr = create_array(N),
	print_array(Arr).
