-module(polygon_area).
-export([main/0]).

%% Gets an element from a list given its index. Counting starts
%% at zero (0). Erlang provides element/2 for tuples, but not for
%% lists, as far as I know.
elem(L,0) -> hd(L);
elem([_|Xs],I) -> elem(Xs,I-1).

%% Calculates the area of any polygon. The are certain limitations,
%% though, for example self-crossing polygons. The original algorithm
%% can be found here: http://www.mathopenref.com/coordpolygonarea2.html
%% X, Y - Lists with x and y coordinates of the points of the polygon.
%% N - the number of points
calculate_area(X,Y,N) -> calculate_area(X,Y,N,0,N-1,0).
calculate_area(_,_,0,_,_,A) -> abs(A / 2);
calculate_area(X,Y,N,I,J,A) ->
	C = (elem(X,J)+elem(X,I)) * (elem(Y,J)-elem(Y,I)),
	calculate_area(X,Y,N-1,I+1,I,A+C).

%% Reads the coordinates
read_points(0,X,Y) -> {X,Y};
read_points(N,X,Y) ->
	{ok, [Xi,Yi]} = io:fread("", "~d ~d"),
	read_points(N-1,X++[Xi],Y++[Yi]).

main() ->
	{ok, [N]} = io:fread("", "~d"),
	{X,Y} = read_points(N,[],[]),
	io:format("~p", [calculate_area(X,Y,N)])
	.
