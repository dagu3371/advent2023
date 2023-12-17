from collections import deque, defaultdict

cards = []
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        cards.append(line)
res = 0
def convert_str_ints(strs):
    return [int(num) for num in strs.split()]
scratchcards = {}

def original_scoring(winning, numbers, res):
    fact = -1
    for winner in winning:
        if winner in numbers:
            fact += 1
    if fact > -1:
        res += 2 ** (fact)
    return res

game = 1
for card in cards:
    winning, numbers = card.split('|')
    winning = winning.split(':')[1]
    winning = convert_str_ints(winning)
    numbers = convert_str_ints(numbers)
    scratchcards[game] = [winning, numbers]
    res = original_scoring(winning, numbers, res)
    game += 1

def process_winners(game_number, winning, numbers):
    winner_count = 0
    for winner in winning:
        if winner in numbers:
            winner_count += 1
    if winner_count > 0:
        res = [game_number + index + 1 for index, _ in enumerate(range(winner_count))]
    else:
        res = []
    return res

queue = deque()
queue.append(scratchcards.keys())
copies = defaultdict(int)
while queue:
    games = queue.pop()
    for game in games:
        if game in scratchcards.keys():
            copies[game] += 1
            winning = scratchcards[game][0]
            numbers = scratchcards[game][1]
            queue.append(process_winners(game, winning, numbers))

print(sum(copies.values()))
print(res)