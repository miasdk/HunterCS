"""
Standard Problem Set Version 2 - Meme Problems
Each function includes a docstring, time/space complexity rationale, and example usage.
"""

def filter_meme_lengths(memes, max_length):
    """
    Filters out memes whose lengths exceed max_length.
    Time: O(n), Space: O(n).
    """
    return [meme for meme in memes if len(meme) <= max_length]


def count_meme_creators(memes):
    """
    Counts the number of memes per creator.
    Time: O(n), Space: O(k) where k is number of unique creators.
    """
    creator_count = {}
    for meme in memes:
        creator = meme["creator"]
        creator_count[creator] = creator_count.get(creator, 0) + 1
    return creator_count


def find_trending_memes(memes):
    """
    Returns a list of memes that appear more than once.
    Time: O(n), Space: O(n).
    """
    from collections import Counter
    counts = Counter(memes)
    return [meme for meme, count in counts.items() if count > 1]


def reverse_memes(memes):
    """
    Returns a new list with memes in reverse order.
    Time: O(n), Space: O(n).
    """
    return memes[::-1]


def find_trending_meme_pairs(meme_posts):
    """
    Finds meme pairs that appear together in posts more than once.
    Time: O(p * m^2), Space: O(k) where p is posts, m is memes per post, k is unique pairs.
    """
    from collections import Counter
    pair_count = Counter()
    for post in meme_posts:
        unique_memes = set(post)
        pairs = [(min(a, b), max(a, b)) for i, a in enumerate(post) for b in post[i+1:] if a != b]
        for pair in set(pairs):
            pair_count[pair] += 1
    return [pair for pair, count in pair_count.items() if count >= 2]


def simulate_meme_reposts(memes, reposts):
    """
    Simulates meme reposts and returns the final order processed.
    Time: O(n + sum(reposts)), Space: O(n + sum(reposts)).
    """
    result = []
    for meme, count in zip(memes, reposts):
        result.extend([meme] * count)
    return result


def find_closest_meme_pair(memes, target):
    """
    Finds two memes whose combined popularity is closest to target.
    Time: O(n), Space: O(1).
    """
    left, right = 0, len(memes) - 1
    closest = None
    min_diff = float('inf')
    while left < right:
        total = memes[left][1] + memes[right][1]
        diff = abs(total - target)
        if diff < min_diff:
            min_diff = diff
            closest = (memes[left][0], memes[right][0])
        if total < target:
            left += 1
        else:
            right -= 1
    return closest


def find_trending_meme(memes, start_day, end_day):
    """
    Finds the meme with the highest average reposts in the given range.
    Time: O(m * d), Space: O(1), m=memes, d=days in range.
    """
    max_avg = -1
    trending = None
    for meme in memes:
        reposts = meme["reposts"][start_day:end_day+1]
        avg = sum(reposts) / len(reposts) if reposts else 0
        if avg > max_avg:
            max_avg = avg
            trending = meme["name"]
    return trending 