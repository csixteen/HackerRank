-module(polygon_perimeter).
-export([main/0]).

%% Calculates the distance between two points in a 2D space.
distance(X1,Y1,X2,Y2) ->
	math:sqrt(math:pow(X2-X1,2)+math:pow(Y2-Y1,2)).

%% Calculates the perimeter
calculate_perimeter(X,Y) -> calc(X,Y,hd(X),hd(Y),0).
calc([],[],_,_,P) -> P;
calc([X],[Y],HX,HY,P) -> P + distance(X,Y,HX,HY);
calc([X1,X2|Xs],[Y1,Y2|Ys],HX,HY,P) ->
	calc([X2|Xs],[Y2|Ys],HX,HY,P+distance(X1,Y1,X2,Y2)).

%% Reads the coordinates
read_points(0,X,Y) -> {X,Y};
read_points(N,X,Y) ->
	{ok, [Xi,Yi]} = io:fread("", "~d ~d"),
	read_points(N-1,X++[Xi],Y++[Yi]).

main() ->
	{ok, [N]} = io:fread("", "~d"),
	{X,Y} = read_points(N,[],[]),
	io:format("~p", [calculate_perimeter(X,Y)])
	.
