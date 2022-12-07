class Network:

    def __init__(self, lines):
        self.lines = lines

    def find_stop(self, stop_name):
        return [
            tram_line
            for tram_line, line_stop in self.lines.items()
            if stop_name in line_stop
        ]

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
