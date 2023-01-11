from Line import Line
from Network import Network

line_a = Line("A", [
    "Le Haillan Rostand", "Les Pins", "Frères Robinson", "Hôtel de Ville Mérignac", "Pin Galant", "Mérignac Centre",
    "Lycées de Mérignac", "Quatre Chemins", "Pierre Mendès-France", "Alfred de Vigny", "Fontaine d'Arlac",
    "Peychotte", "François Mitterrand", "Saint-Augustin", "Hôpital Pellegrin", "Stade Chaban-Delmas", "Gaviniès",
    "Hôtel de Police", "Saint-Bruno - Hôtel de Région", "Mériadeck", "Palais de Justice", "Hôtel de Ville",
    "Sainte-Catherine", "Place du Palais", "Porte de Bourgogne", "Stalingrad", "Jardin botanique",
    "Thiers - Benauge", "Galin", "Jean Jaurès", "Cenon Gare", "Carnot - Mairie de Cenon", "Buttinière"
])

line_a_one = Line("A-1", [
    "Buttinière", "Iris",
    "Gravières", "Bois Fleuri", "Lormont Lauriers"
])

line_a_two = Line("A-2", [
    "Buttinière", "Palmer",
    "Pelletan", "Cenon La Morlette"
])

line_b = Line("B", [
    "Quinconces", "Grand Théâtre", "Gambetta", "Hôtel de Ville", "Musée d'Aquitaine", "Victoire", "Saint-Nicolas",
    "Bergonié", "Barrière Saint-Genès", "Roustaing", "Forum", "Peixotto", "Béthanie", "Arts et Métiers",
    "François Bordes", "Doyen Brus", "Montaigne-Montesquieu", "UNITEC", "Saige", "Pessac Bougnard"
])

line_c = Line("C", [
    "Quinconces", "Place de la Bourse", "Porte de Bourgogne", "Saint-Michel", "Sainte-Croix", "Tauzia",
    "Gare Saint-Jean"
])

network = Network([line_a, line_a_one, line_a_two, line_b, line_c])

if __name__ == '__main__':
    departure = input("Quel est votre arrêt de départ ? ")
    arrival = input("Quel est votre arrêt d'arrivée ? ")

    departureLine = network.find_stop(departure)
    arrivalLine = network.find_stop(arrival)

    connection = network.find_connection_between_two_stops(departure, arrival)
    print(connection)

    nb_stops = network.find_stops_number_on_travel(departure, arrival)
    print("le trajet comporte " + str(nb_stops) + " arrêts")