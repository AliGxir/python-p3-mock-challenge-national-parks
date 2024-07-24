class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be in string format")
        elif hasattr(self, "_name"):
            raise ValueError("name cannot be reset")
        elif not len(name) >= 3:
            raise ValueError("name must be greater or equal to 3 char")
        self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        all_parks = [trip for trip in Trip.all if trip.national_park is self]
        return len(all_parks)

    def best_visitor(self):
        # max_count = 0
        # max_visitor = None
        # # Returns the Visitor instance that has visited that park the most
        all_visitors = [trip.visitor for trip in self.trips()]
        # for current_visitor in all_visitors:
        #     current_count = all_visitors.count(current_visitor)
        #     if current_count > max_count:
        #         max_count = current_count
        #         max_visitor = current_visitor
        # return max_visitor
        #     # [visitor.name for visitor in all_visitors]
        return max(
            all_visitors,
            default=None,
            key=lambda visitor: all_visitors.count(visitor),
        )


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, str):
            raise TypeError("start date must be in string format")
        elif not len(start_date) >= 7:
            raise ValueError("start date must be greater or equal to 7 char")
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, str):
            raise TypeError("end date must be in string format")
        elif not len(end_date) >= 7:
            raise ValueError("end date must be greater or equal to 7 char")
        self._end_date = end_date


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be in string format")
        elif len(name) not in range(1, 16):
            raise ValueError("name must be between 1-15 char")
        self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        all_parks = [trip.park for trip in self.trips() if trip.park is park]
        return len(all_parks)


# v = NationalPark("test")
# v.name = "gr"
# print("done")
