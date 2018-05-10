-module(string_compression).
-export([main/0]).

print_char(C,1) -> io:format("~s", [[C]]);
print_char(C,N) -> io:format("~s~w", [[C],N]).

%% Main algorithm for string compression
compress_string(S) -> compress_string(S,1).
compress_string([X],N) -> print_char(X,N);
compress_string([X,Y|T],N) when X /= Y ->
	print_char(X,N),
	compress_string([Y|T],1);
compress_string([_,Y|T],N) -> compress_string([Y|T],N+1).

main() ->
	{ok, [S]} = io:fread("", "~s"),
	compress_string(S)
	.
