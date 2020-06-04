flight(from, airline, to, price, duration)

flight(toronto, aircanada, madrid, 950, 540).
flight(toronto, united, madrid, 1000, 600).
flight(toronto, iberia, madrid, 850, 540).
flight(madrid, aircanada, toronto, 975, 525).
flight(madrid, united, toronto, 1025, 585).
flight(madrid, ibreria, toronto, 875, 525).

flight(toronto, aircanada, london, 550, 420).
flight(toronto, united, london, 700, 480).
flight(london, aircanada, toronto, 575, 440).
flight(london, united, toronto, 725, 500).

flight(london, iberia, barcelona, 295, 320).
flight(barcelona, iberia, london, 260, 270).

flight(barcelona, iberia, madrid, 160, 95).
flight(barcelona, aircanada, madrid, 140, 90).
flight(madrid, iberia, barcelona, 195, 110).
flight(madrid, aircanada, barcelona, 175, 105).

flight(barcelona, iberia, valencia, 150, 105).
flight(valencia, iberia, barcelona, 150, 95).

flight(madrid, iberia, valencia, 115, 95).
flight(valencia, iberia, madrid, 80, 70).

flight(madrid, iberia, malaga, 125, 105).
flight(malaga, iberia, madrid, 100, 90).

flight(valencia, iberia, malaga, 120, 140).
flight(malaga, iberia, valencia, 130, 150).

flight(paris, united, toulose, 85, 180).
flight(toulose, united, paris, 75, 150).

airport(city, airporttax, minsecuritydelay).

airport(london, 75, 80).

airport(toronto, 50, 60).

airport(barcelona, 40, 30).

airport(madrid, 75, 45).

airport(valencia, 40, 20).

airport(malaga, 50, 30).

airport(paris, 50, 60).

airport(toulose, 40, 30).


is_flight_from(X, Y) :- flight(X, _, Y, _, _). 

is_cheap(A, C, B) :- flight(A, C, B, P, _), P < 400.    

is_possible_from_x_to_y_in_two_flight(A, B):-flight(A, _,Z, _, _),flight(Z, _, B, _, _), Z \== A, Z \== B. 

is_cheap_is_aircanada(A, C, B):-flight(A, C, B, P, _), P < 400; C == aircanada. 

is_united_is_aircanada(A, B):-flight(A, C, B, _, _), C \== united.

is_united_is_aircanada(A, B):-flight(A, C, B, _, _), C == united -> flight(A, D, B, _, _), D==aircanada.





