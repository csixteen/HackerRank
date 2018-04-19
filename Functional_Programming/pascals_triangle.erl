-module(pascals_triangle).
-export([main/0]).

%% Factorial with tail recursion
fac(N) -> fac(N, 1).
fac(0, Acc) -> Acc;
fac(N, Acc) when N > 0 -> fac(N-1, N*Acc).

%% Calculates the value of a column in a row.
column(N, M) -> fac(N) div (fac(M) * fac(N-M)).

%% Builds a row
build_row(N) -> build_row(N,1).
build_row(N,M) when N rem 2 == 1, M == N div 2 + 1 -> [column(N-1,M-1)];
build_row(N,M) when N rem 2 == 0, M-1 == N div 2 -> [];
build_row(N,M) when N > M ->
	C = column(N-1,M-1),
	[C] ++ build_row(N,M+1) ++ [C].

%% Print a row
print_row([]) -> io:format("~n");
print_row([X|Xs]) ->
	io:format("~p ", [X]),
	print_row(Xs).

%% Build the triangle
pascal(N,M) when N < M -> ok;
pascal(N,I) ->
	R = build_row(I),
	print_row(R),
	pascal(N,I+1).

main() ->
	{ok, [N]} = io:fread("", "~d"),
	pascal(N,1)
	.
