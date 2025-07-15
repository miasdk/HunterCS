"""
Standard Problem Set Version 1 - NFT Problems
Each function includes a docstring, time/space complexity rationale, and example usage.
"""

def extract_nft_names(nft_collection):
    """
    Extracts the names of NFTs from a list of NFT dictionaries.
    Time Complexity: O(n), where n is the number of NFTs.
    Space Complexity: O(n) for the output list.
    Args:
        nft_collection (list): List of NFT dictionaries.
    Returns:
        list: List of NFT names.
    """
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]
print(extract_nft_names(nft_collection))


def extract_nft_names_buggy(nft_collection):
    """
    Buggy version for review. See README for explanation.
    """
    nft_names = []
    for nft in nft_collection:
        nft_names += nft["name"]
    return nft_names


def identify_popular_creators(nft_collection):
    """
    Identifies creators with more than one NFT in the collection.
    Time Complexity: O(n), Space: O(k) where k is number of unique creators.
    """
    creator_count = {}
    for nft in nft_collection:
        creator = nft["creator"]
        creator_count[creator] = creator_count.get(creator, 0) + 1
    return [creator for creator, count in creator_count.items() if count > 1]


def average_nft_value(nft_collection):
    """
    Returns the average value of NFTs, or 0 if empty.
    Time: O(n), Space: O(1).
    """
    if not nft_collection:
        return 0
    total = sum(nft["value"] for nft in nft_collection)
    return total / len(nft_collection)


def search_nft_by_tag(nft_collections, tag):
    """
    Returns a list of NFT names with the specified tag from nested collections.
    Time: O(n), Space: O(n).
    """
    result = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft.get("tags", []):
                result.append(nft["name"])
    return result


def process_nft_queue(nft_queue):
    """
    Returns the names of NFTs in the order they are processed (FIFO).
    Time: O(n), Space: O(n).
    """
    return [nft["name"] for nft in nft_queue]


def validate_nft_actions(actions):
    """
    Returns True if actions are balanced (every 'add' has a 'remove' and no 'remove' before 'add').
    Time: O(n), Space: O(1).
    """
    balance = 0
    for action in actions:
        if action == "add":
            balance += 1
        elif action == "remove":
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


def find_closest_nft_values(nft_values, budget):
    """
    Finds two NFT values closest to the budget (one below/equal, one above/equal).
    Time: O(n), Space: O(1).
    """
    below = None
    above = None
    for value in nft_values:
        if value <= budget:
            below = value
        if above is None and value >= budget:
            above = value
            break
    if below is None:
        below = nft_values[0]
    if above is None:
        above = nft_values[-1]
    return (below, above) 