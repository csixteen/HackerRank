-module(gcd).
-export([main/0]).

gcd(X,0) -> X;
gcd(X,Y) -> gcd(Y, X rem Y).

main() ->
	{ok, [X,Y]} = io:fread("", "~d ~d"),
	io:format("~p", [gcd(X,Y)])
	.
