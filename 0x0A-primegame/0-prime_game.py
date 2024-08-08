#!/usr/bin/python3

""" Prime Game Algorithm Python """


def sieve_of_primes(n):
    """ Generate a list indicating whether each number up to n is prime """
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    Args:
        x (int): Number of rounds.
        nums (List[int]): List of upper bounds for each round.
    Returns:
        str: Name of the player with the most wins
        ("Maria" or "Ben") or None if there's a tie.
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_primes(max_n)

    players_wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = sum(primes[2:n + 1])
        if prime_count % 2 == 1:
            players_wins["Maria"] += 1
        else:
            players_wins["Ben"] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
