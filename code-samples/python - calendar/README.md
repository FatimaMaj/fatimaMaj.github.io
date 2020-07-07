# This is a scheduling system for a company that rents a building to different clients hosting events there. Clients rent the entire building for one or more days, so there can never be two events taking place in the same time period. If an event takes place at the same time as another event, we call that a scheduling conflict.
#
# This function work as follows:
#
# - The parameter is a list of events. Each event is a dictionary consisting of three values:
#   - The name of the event. ('name')
#   - The start date of the event. ('start')
#   - The end date of the event. ('end')
#   - Each date is a tuple consisting of the year, the month, and the day. Hours, minutes, and seconds are not relevant.
#   - For example, this is a job fair taking place between August 1st, 2020 and August 5th, 2020:
#   - { 'name': 'Job fair', 'start': (2020, 8, 1), 'end': (2020, 8, 5) }
#   - There is also a test file which test all the possible schedult to check if scheduling is conflict.