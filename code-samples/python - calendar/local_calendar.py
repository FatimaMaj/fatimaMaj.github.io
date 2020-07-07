
from datetime import date
import datetime

def find_conflicts(events):
    conflictsList = []
    for idx1, eventA in enumerate(events):
        for idx2, eventB in enumerate(events):
            # this condition is to avoid comparing the same pair
            if idx1 >= idx2:
                continue
            # condition to check is there conflict between two events
            if eventA['start'] <= eventB['end'] and eventB['start'] <= eventA['end']:
                if eventA['name'] not in conflictsList:
                    conflictsList.append(eventA['name'])
                if eventB['name'] not in conflictsList:
                    conflictsList.append(eventB['name'])
    return conflictsList

# This function takes a list of events just like the one in find_conflicts. It should return the total cost of all events, based on this price list:
#
# - An event that lasts for a single day costs $500.
# - An event that lasts for more than one day costs $400 per day, including the first day.
# - An event that lasts for more than one week costs $300 per day, including the first week.
#
# Important: an event that lasts for one day should have the same start and end date.
# For example:
#
# - An single-day event taking place on May 10th should have the start date (2020, 5, 10) and the end date (2020, 5, 10).
# - A two-day event taking place from May 10th to May 11th should have the start date (2020, 5, 10) and the end date (2020, 5, 11).
# - A seven-day event taking place from May 10th to May 16th should have the start date (2020, 5, 10) and the end date (2020, 5, 16).
#
# This makes sure the data and behavior is consistent with that in find_conflicts.


def total_cost(events):
    days = []
    diffDays = []
    for event in events:
        eventStart = event['start']
        eventEnd = event['end']
        startDate = date(eventStart[0], eventStart[1], eventStart[2])
        endDate = date(eventEnd[0], eventEnd[1], eventEnd[2])
        diffDays.append((endDate - startDate).days)
# I added another list to the code: "days". We fill this list by looping over our existing
# "diffDays" list and just increasing the value by one, then adding it to "days". We then use
# this list instead, later when we are calculating the costs.
    for diffDay in diffDays:
        # compute number of days
        # an event that lasts for one day should have the same start and end date.
        diffDay = diffDay + 1
        days.append(diffDay)
    costA = 0
    costB = 0
    costC = 0
    for NumOfDays in days:
        if NumOfDays == 1:
            costA = 500
        if NumOfDays > 1 and NumOfDays <= 7:
            costB = NumOfDays * 400
        if NumOfDays > 7:
            costC = NumOfDays * 300
    totalCost = costA+costB+costC
    return totalCost
