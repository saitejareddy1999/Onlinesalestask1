# they are asking if we roll a dice or else if we do flip a coin have given
# occurrences we have to calculate how many times a particular one is coming

# we want random outcomes we are importing random module
import random


def event(probabilities, occurrences):
    outcomes = []  # we are getting how many probabilities for each input
    for probability_dict in probabilities:
        for outcome, probability in probability_dict.items():
            for _ in range(probability):
                outcomes.append(outcome)
    results = {}
    for _ in range(occurrences):
        outcome = random.choice(outcomes)
        results[outcome] = results.get(outcome, 0) + 1
    return results


coin_bias = [{1: 35}, {2: 65}]
occurrences = eval(input())
result = event(coin_bias, occurrences)
print(result)

