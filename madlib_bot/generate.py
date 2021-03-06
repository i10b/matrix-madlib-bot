import random


def generate(source: str, adj: list, verbs: list, adverbs: list,
             nouns: list, pronouns: list, places: list) -> str:

    for category in [adj, verbs, adverbs, nouns, pronouns, places]:
        category = random.shuffle(category)

    words_list: list =  []
    for word in source.split():
        matches = {
            '%aj': adj,
            '%vb': verbs,
            '%av': adverbs,
            '%nn': nouns,
            '%pn': pronouns,
            '%pl': places
        }
        for string, category in matches.items():
            if string in word:
                word = word.replace(string, category.pop())

        words_list.append(word)

    return " ".join(words_list)
