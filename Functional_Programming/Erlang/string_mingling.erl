-module(string_mingling).
-export([main/0]).

%% Mingle strings (we assume they have the
%% same length)
mingle(P,Q) -> mingle(P,Q,[]).
mingle([],[],Acc) -> Acc;
mingle([X|Xs],[Y|Ys],Acc) -> mingle(Xs,Ys,[Acc,X,Y]).

main() ->
	{ok, [P]} = io:fread("", "~s"),
	{ok, [Q]} = io:fread("", "~s"),
	io:format("~s~n", [mingle(P,Q)])
	.
