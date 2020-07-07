from local_calendar import find_conflicts
from local_calendar import total_cost
import unittest

class CalendarTests(unittest.TestCase):
    def test_One_Event(self):
        events = [{'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 2, 7)}]
        conflicts = find_conflicts(events)
        self.assertEqual([], conflicts)

    def test_No_Event(self):
        events = []
        conflicts = find_conflicts(events)
        self.assertEqual([], conflicts)

    def test_No_Conflict(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 2, 7)},
            {'name': 'B', 'start': (2020, 2, 8), 'end': (2020, 3, 9)},
            {'name': 'C', 'start': (2020, 3, 10), 'end': (2020, 5, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual([], conflicts)

    def test_ABC_Conflict(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 3, 7)},
            {'name': 'B', 'start': (2020, 2, 5), 'end': (2020, 4, 9)},
            {'name': 'C', 'start': (2020, 3, 5), 'end': (2020, 5, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual(['A', 'B', 'C'], conflicts)

    def test_C_StartBefore_B(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 2, 7)},
            {'name': 'B', 'start': (2020, 3, 7), 'end': (2020, 6, 9)},
            {'name': 'C', 'start': (2020, 2, 8), 'end': (2020, 5, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual(['B', 'C'], conflicts)

    def test_A_StartBefore_B(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 3, 7)},
            {'name': 'B', 'start': (2020, 2, 5), 'end': (2020, 4, 9)},
            {'name': 'C', 'start': (2020, 4, 10), 'end': (2020, 5, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual(['A', 'B'], conflicts)

    # What should we call this test? Maybe we should even change or remove it?
    def test_AB_Conflict(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 1, 7)},
            {'name': 'B', 'start': (2020, 1, 5), 'end': (2020, 1, 9)},
            {'name': 'C', 'start': (2020, 1, 10), 'end': (2020, 1, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual(['A', 'B'], conflicts)

    def test_AB_startSameDay(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 1, 7)},
            {'name': 'B', 'start': (2020, 1, 1), 'end': (2020, 1, 9)},
            {'name': 'C', 'start': (2020, 1, 10), 'end': (2020, 1, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual(['A', 'B'], conflicts)

    def test_ABC_startSameDay(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 1, 7)},
            {'name': 'B', 'start': (2020, 1, 1), 'end': (2020, 1, 9)},
            {'name': 'C', 'start': (2020, 1, 1), 'end': (2020, 1, 15)}
        ]
        conflicts = find_conflicts(events)
        self.assertEqual(['A', 'B', 'C'], conflicts)

    def test_totalCost_noEvents(self):
        events = []
        totalCost = total_cost(events)
        self.assertEqual(0, totalCost)

    def test_totalcost(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 1, 1)},
            {'name': 'B', 'start': (2020, 2, 8), 'end': (2020, 2, 10)},
            {'name': 'C', 'start': (2020, 3, 1), 'end': (2020, 3, 8)}
        ]
        totalCost = total_cost(events)
        self.assertEqual(4100, totalCost)

    def test_singleDayEvent(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 10), 'end': (2020, 1, 10)}
        ]
        totalCost = total_cost(events)
        self.assertEqual(500, totalCost)

    def test_totalCost_twoDaysEvent(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 1), 'end': (2020, 1, 2)}
        ]
        totalCost = total_cost(events)
        self.assertEqual(800, totalCost)

    def test_totalCost_sevenDaysEvent(self):
        events = [
            {'name': 'A', 'start': (2020, 1, 10), 'end': (2020, 1, 16)}
        ]
        totalCost = total_cost(events)
        self.assertEqual(2800, totalCost)
unittest.main()
