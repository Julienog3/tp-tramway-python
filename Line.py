class Line:
    def __init__(self, name, stops):
        self.name = name
        self.stops = stops
        self.connections = []
        self.last_stops = []

    def find_last_stops(self):
        return {"start": self.stops[0], "end": self.stops[len(self.stops) - 1]}

    def set_last_stops(self):
        self.last_stops = self.find_last_stops()

    def find_stops_count(self):
        return len(self.stops)

    def find_connections_with_line(self, line):
        connections = []

        for line_stop_1 in self.stops:
            for line_stop_2 in line.stops:
                if line_stop_1 == line_stop_2:
                    connections.append(line_stop_1)

        return connections

    def set_connections_with_line(self, line):
        self.connections = self.find_connections_with_line(line)

    def find_direction(self, departure, arrival):
        if (self.is_stop_on_line(departure) is not True or self.is_stop_on_line(departure) is not True):
            return

        self.set_last_stops()

        departurePosition = self.stops.index(departure)
        arrivalPosition = self.stops.index(arrival)

        res = departure + " -> " + arrival

        if (departurePosition > arrivalPosition):
            return res + " (direction " + self.last_stops["start"] + ")"

        elif (departurePosition < arrivalPosition):
            return res + " (direction " + self.last_stops["end"] + ")"

        else:
            return

    def find_stops_number_on_travel(self, departure, arrival):
        if (self.is_stop_on_line(departure) is not True or self.is_stop_on_line(departure) is not True):
            return

        departurePosition = self.stops.index(departure)
        arrivalPosition = self.stops.index(arrival)

        return abs(departurePosition - arrivalPosition)


    def is_stop_on_line(self, stop):
        for line_stop in self.stops:
            if stop == line_stop:
                return True

        return False
