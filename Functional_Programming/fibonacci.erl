-module(fibonacci).
-export([main/0]).

fib(0) -> 0;
fib(1) -> 1;
fib(N) when N >= 2 -> fib(N-1) + fib(N-2).

main() ->
	{ok, [N]} = io:fread("", "~d"),
	io:format("~p", [fib(N-1)])
	.
