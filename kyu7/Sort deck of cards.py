"""Write a function sort_cards() that sorts a shuffled list of cards, so that any given list of cards is sorted by rank, no matter the starting collection.

All cards in the list are represented as strings, so that sorted list of cards looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
Hint: Tests will have many occurrences of same rank cards, as well as vary in length. You can assume though, that input list is always going to have at least 1 element."""
def sort_cards(cards):
    order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    sorted_list = sorted(cards, key=lambda x: order.index(x) if x in order else float('inf'))
    return sorted_list

my_cards = ['K', '7', 'A', '3', 'J']
sorted_cards = sort_cards(my_cards)
print(sorted_cards)
