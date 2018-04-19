-module(fibonacci_sum).
-export([main/0]).

elem(L,0) -> hd(L);
elem([_|T],I) -> elem(T,I-1).

%% Generates all the combinations in a list
combos(1, L) -> [[X] || X <- L];
combos(K, L) when K == length(L) -> [L];
combos(K, [H|T]) ->
	[[H | Subcombos] || Subcombos <- combos(K-1,T)] ++ (combos(K,T)).

%% Fibonacci
fib(0) -> 0;
fib(1) -> 1;
fib(N) when N >= 2 -> fib(N-1) + fib(N-2).

%% Calculates fibonacci for (1,1), (2,2), etc.
individual_fib(A) -> individual_fib(A,0).
individual_fib([],Acc) -> Acc;
individual_fib([H|T],Acc) -> individual_fib(T,Acc+fib(H)).

calc_g_combos(A,Combos) -> calc_g_combos(A,Combos,0).
calc_g_combos(_,[],Acc) -> Acc;
calc_g_combos(A,[H|T],Acc) ->
	Start = elem(H,0),
	Length = elem(H,1)-elem(H,0)+1,
	F = fib(lists:sum(lists:sublist(A, Start, Length))),
	calc_g_combos(A,T,Acc+F).

calculate_g(N,A) ->
	I = individual_fib(A),
	Combos = combos(2, lists:seq(1,N)),
	G = calc_g_combos(A, Combos),
	io:format("~p~n", [(G + I) rem 1000000007]).

%% The main cycle that reads 2 lines per query.
fibonacci_sum(0) -> ok;
fibonacci_sum(Q) ->
	{ok, [N]} = io:fread("", "~d"),
	S = string:strip(io:get_line(""),both,$\n),
	A = [X || {X,_} <- [string:to_integer(Z) || Z <- string:tokens(S," ")]],
	calculate_g(N,A),
	fibonacci_sum(Q-1)
	.

main() ->
	{ok, [Q]} = io:fread("", "~d"),
	fibonacci_sum(Q)
	.
