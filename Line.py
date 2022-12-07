class Line:
    def __init__(self, name, stops):
        self.name = name
        self.stops = stops
        self.connections = []
        self.last_stops = []

    def find_last_stops(self):
        return [self.stops[0], self.stops[len(self.stops) - 1]]

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

    def isStopOnLine(self, stop):
        for line_stop in self.stops:
            if stop == line_stop:
                return True

        return False
