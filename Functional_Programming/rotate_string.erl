-module(rotate_string).
-export([main/0]).

%% Rotates a string N times
rotate(S,0) -> S;
rotate([X|Xs], N) -> rotate(Xs ++ [X], N-1).

%% Prints a string and rotates it
print_rotate(S) -> print_rotate(S, length(S)).
print_rotate(_,0) -> io:format("~n"), ok;
print_rotate(S,N) ->
	NewS = rotate(S,1),
	io:format("~s ", [NewS]),
	print_rotate(NewS,N-1).

%% Reads the string from STDIN
rotate_string() ->
	case io:fread("", "~s") of
		eof -> ok;
		{ok, [S]} -> print_rotate(S), rotate_string()
	end.

main() ->
	{ok, [_]} = io:fread("", "~d"),
	rotate_string()
	.
