class Network:

    def __init__(self, lines):
        self.lines = lines

    def find_stop(self, stop_name):
        lines = []

        for line in self.lines:
            for stop_line in line.stops:
                if stop_line == stop_name:
                    lines.append(line)
        
        return lines

    def are_stops_on_same_line(self, departure, arrival):
        lines_with_same_stops = []

        for line in self.lines:
            hasDeparture = False
            hasArrival = False

            for stop_line in line.stops:
                if stop_line == departure:
                    hasDeparture = True

                if stop_line == arrival:
                    hasArrival = True

            if (hasArrival and hasDeparture):
                lines_with_same_stops.append(line)

        return lines_with_same_stops

    def find_connection_between_two_stops(self, departure, arrival):
        departureLine = self.find_stop(departure)
        arrivalLine = self.find_stop(arrival)

        connection = departureLine[0].find_connections_with_line(arrivalLine[0])

        print(departureLine[0].find_direction(departure, connection[0]))
        print(arrivalLine[0].find_direction(connection[0], arrival))

        return connection
        # if ():
            
