def slicing_special_cases():
    """Üben von Slicings in Python."""

    # Liste für alle Übungen
    lst = [1, 2, 3, 4, 5]

    # Extrahiere die ersten drei Elemente der Liste [1, 2, 3, 4, 5].
    first_three = ...

    # Extrahiere die letzten zwei Elemente der Liste [1, 2, 3, 4, 5].
    last_two = ...

    # Kehre die Liste [1, 2, 3, 4, 5] um.
    reversed_lst = ...

    # Extrahiere jeden zweiten Wert der Liste [1, 2, 3, 4, 5].
    every_second = ...

    # Extrahiere die Elemente zwischen den Indizes -4 und -1 der Liste [1, 2, 3, 4, 5].
    between_neg4_and_neg1 = ...

    # Extrahiere die ersten drei Elemente der Liste [1, 2, 3, 4, 5] und kehre sie um.
    first_three_reversed = ...

    # Extrahiere die letzten zwei Elemente der Liste [1, 2, 3, 4, 5] und kehre sie um.
    last_two_reversed = ...

    # Kehre die Liste [1, 2, 3, 4, 5] um und nimm nur jeden zweiten Wert.
    reversed_every_second = ...

    # Extrahiere die Elemente zwischen den Indizes -4 und -1 der Liste [1, 2, 3, 4, 5], kehre sie um und nimm nur jeden zweiten Wert.
    between_neg4_and_neg1_reversed_every_second = ...

    return {
        'first_three': first_three,
        'last_two': last_two,
        'reversed_lst': reversed_lst,
        'every_second': every_second,
        'between_neg4_and_neg1': between_neg4_and_neg1,
        'first_three_reversed': first_three_reversed,
        'last_two_reversed': last_two_reversed,
        'reversed_every_second': reversed_every_second,
        'between_neg4_and_neg1_reversed_every_second': between_neg4_and_neg1_reversed_every_second
    }


if __name__ == '__main__':
    print(slicing_special_cases())