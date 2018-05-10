-module(hello_n_times).
-export([main/0, print_hello/1]).

print_hello(0) -> ok;
print_hello(N) when N > 0 ->
	io:format("Hello World~n"),
	print_hello(N-1).

main() ->
	{ok, [X]} = io:fread("", "~d"),
	print_hello(X).
