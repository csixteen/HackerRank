-module(chocolate_feast).
-export([main/0,calc/5]).

calculate_chocolates(N,C,M) -> calc(N,C,M,0,0).
calc(N,C,M,W,Acc) when C > N, W < M -> Acc;
calc(N,C,M,W,Acc) when C > N, W >= M ->
	Choc = W div M,	
	calc(N,C,M,(W rem M) + Choc,Acc + Choc);
calc(N,C,M,_,Acc) -> 
	Choc = N div C,
	calc(N rem C,C,M,Choc,Acc+Choc).

%% Reads in the 3 values and calculates the number
%% of chocolates eaten during the trip
chocolate_feast() ->
	case io:fread("", "~d ~d ~d") of
		eof -> ok;
		{ok, [N,C,M]} -> 
			io:format("~p~n", [calculate_chocolates(N,C,M)]),
			chocolate_feast()
	end.

main() ->
	{ok, [_]} = io:fread("", "~d"),
	chocolate_feast()
	.
