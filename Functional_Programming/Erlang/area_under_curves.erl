-module(area_under_curves).
-export([main/0,calc/4,calc_aux/4,str_to_list/1]).

%% Takes a string and returns a list of integers.
%% It's basically list(map(int, S.split(" "))) in Python
str_to_list(S) ->
	[X || {X,_} <- [string:to_integer(Z) || Z <- string:tokens(S," ")]].

%% Need to implement this, but I don't have the time
%% to go read the tutorial about the formula. This was
%% supposed to be a Functional Programming problem, not
%% a Math one. That's why there is the Math domain, or
%% Project Euler.
calc(A,B,X) -> ok.

%% Prints the calculated values
print_values(_,_,[]) -> ok;
print_values(A,B,[L|R]) ->
	io:format("~p~n", [calc(A,B,L)]),
	print_values(A,B,R).

main() ->
	{ok, [A]} = io:fread("", "~s"),
	{ok, [B]} = io:fread("", "~s"),
	{ok, [LR]} = io:fread("", "~s"),
	print_values(str_to_list(A), str_to_list(B), str_to_list(LR))
	.
