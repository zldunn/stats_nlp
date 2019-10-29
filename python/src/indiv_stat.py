
'''
This is a class to represent pulling statistics on one particular player. This
can be any stat for some specific time period. It has certain 'slot' values,
and a set of required stat values self. Ideally it will first be classified,
then use slots to decide the stat type
SLOTS:
 - Player[required] - player referenced (first or last or both)
 - Stat Type[optional] = passing yards, rushing yards, TDs etc
 - Time range[optional] = this can be a date range
 - Season[optional] = it might be easier to seperate this from time range
 '''
