-module(evaluate_x).
-export([main/0]).

fac(N) -> fac(N,1).
fac(0,Acc) -> Acc;
fac(N,Acc) -> fac(N-1,N*Acc).

%% Calculates the Nth term
calculate_term(X,N) -> math:pow(X,N) / fac(N).

%% Evaluates e^x
evaluate_x(X) -> evaluate_x(X,9,0).
evaluate_x(_,-1,Acc) -> Acc;
evaluate_x(X,N,Acc) -> evaluate_x(X,N-1,calculate_term(X,N)+Acc).

%% Read the value of X for each test case
read_x() ->
	case io:fread("", "~f") of
		eof -> ok;
		{ok, [X]} -> 
			io:format("~p~n", [evaluate_x(X)]), 
			read_x()
	end.

main() ->
	{ok, [_]} = io:fread("", "~d"),
	read_x()
	.
