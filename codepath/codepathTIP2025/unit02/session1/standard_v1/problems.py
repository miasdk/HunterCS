#!/usr/bin/env python3
"""
Unit 2 Standard Problem Set - Implementation Skeleton
"""

# ============================================================================
# PROBLEMS 1-12
# ============================================================================

def lineup(artists, set_times):
    """Create dictionary mapping artists to their set times."""
    
    pass


def get_artist_info(artist, festival_schedule):
    """Return artist's info dict or error message if not found."""
    pass


def total_sales(ticket_sales):
    """Return the sum of all ticket sales values."""
    pass


def identify_conflicts(venue1_schedule, venue2_schedule):
    """Return dictionary of identical key-value pairs from both venues."""
    pass


def best_set(votes):
    """Return the most frequently voted artist."""
    pass


def max_audience_performances(audiences):
    """Return sum of all maximum values in the audience array."""
    
    pass


def max_audience_performances_alt(audiences):
    """Alternative implementation of max_audience_performances."""
    pass


def num_popular_pairs(popularity_scores):
    """Count pairs (i,j) where i < j and scores[i] == scores[j]."""
    pass


def find_stage_arrangement_difference(s, t):
    """Return sum of absolute differences between indices of elements in both arrays."""
    pass


def num_VIP_guests(vip_passes, guests):
    """Count how many characters from guests are present in vip_passes."""
    pass


def schedule_pattern(pattern, schedule):
    """Return True if schedule words follow the same pattern as pattern string."""
    pass


def sort_performers(performer_names, performance_times):
    """Return performer names sorted by performance times in descending order."""
    pass


# ============================================================================
# PROBLEMS 13-24
# ============================================================================

def space_crew(crew, position):
    """Create dictionary mapping crew members to their positions."""
    pass


# Global variable for planet lookup
planetary_info = {
    "Mercury": {"Moons": 0, "Orbital Period": 88},
    "Earth": {"Moons": 1, "Orbital Period": 365.25},
    "Mars": {"Moons": 2, "Orbital Period": 687},
    "Jupiter": {"Moons": 79, "Orbital Period": 10592}
}

def planet_lookup(planet_name):
    """Return formatted string with planet info or error message."""
    pass


def check_oxygen_levels(oxygen_levels, min_val, max_val):
    """Return list of keys whose values are outside the given range."""
    pass


def data_difference(experiment1, experiment2):
    """Return key-value pairs in experiment1 but not in experiment2."""
    pass


def get_winner(votes):
    """Return the most frequently appearing vote."""
    pass


def check_if_complete_transmission(transmission):
    """Return True if transmission contains every letter a-z at least once."""
    pass


def max_number_of_string_pairs(signals):
    """Return maximum number of pairs where one string is reverse of another."""
    pass


def find_difference(signals1, signals2):
    """Return [elements in signals1 not in signals2, elements in signals2 not in signals1]."""
    pass


def find_common_signals(signals1, signals2):
    """Return [count of signals1 elements in signals2, count of signals2 elements in signals1]."""
    pass


def find_common_signals_alt(signals1, signals2):
    """Alternative implementation of find_common_signals."""
    pass


def frequency_sort(signals):
    """Sort by frequency (ascending) then by value (descending) as tiebreaker."""
    pass


def find_final_hub(paths):
    """Find the destination with no outgoing path."""
    pass


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Run all test cases to verify implementations."""
    
    print("=" * 70)
    print("UNIT 2 STANDARD PROBLEMS TEST SUITE")
    print("=" * 70)
    
    print("\n" + "=" * 40)
    print("PROBLEMS 1-12")
    print("=" * 40)
    
    # Test 1: Create Dictionary from Two Lists
    print("\n1. Create Dictionary from Two Lists")
    artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
    set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
    artists2 = []
    set_times2 = []
    result1 = lineup(artists1, set_times1)
    result2 = lineup(artists2, set_times2)
    print(f"lineup(artists1, set_times1) = {result1}")
    print("Expected: {'Kendrick Lamar': '9:30 PM', 'Chappell Roan': '5:00 PM', 'Mitski': '2:00 PM', 'Rosalia': '7:30 PM'}")
    print(f"lineup([], []) = {result2} (expected: {{}})")
    
    # Test 2: Dictionary Lookup with Default
    print("\n2. Dictionary Lookup with Default")
    festival_schedule = {
        "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
        "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
        "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
        "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
    }
    result1 = get_artist_info("Blood Orange", festival_schedule)
    result2 = get_artist_info("Taylor Swift", festival_schedule)
    print(f"get_artist_info('Blood Orange', schedule) = {result1}")
    print("Expected: {'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}")
    print(f"get_artist_info('Taylor Swift', schedule) = {result2}")
    print("Expected: {'message': 'Artist not found'}")
    
    # Test 3: Sum Dictionary Values
    print("\n3. Sum Dictionary Values")
    ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
    result = total_sales(ticket_sales)
    print(f"total_sales({ticket_sales}) = {result} (expected: 4500)")
    
    # Test 4: Find Common Key-Value Pairs
    print("\n4. Find Common Key-Value Pairs")
    venue1_schedule = {
        "Stromae": "9:00 PM",
        "Janelle Monáe": "8:00 PM",
        "HARDY": "7:00 PM",
        "Bruce Springsteen": "6:00 PM"
    }
    venue2_schedule = {
        "Stromae": "9:00 PM",
        "Janelle Monáe": "10:30 PM",
        "HARDY": "7:00 PM",
        "Wizkid": "6:00 PM"
    }
    result = identify_conflicts(venue1_schedule, venue2_schedule)
    print(f"identify_conflicts(venue1, venue2) = {result}")
    print("Expected: {'Stromae': '9:00 PM', 'HARDY': '7:00 PM'}")
    
    # Test 5: Find Most Frequent Value
    print("\n5. Find Most Frequent Value")
    votes1 = {
        1234: "SZA", 
        1235: "Yo-Yo Ma",
        1236: "Ethel Cain",
        1237: "Ethel Cain",
        1238: "SZA",
        1239: "SZA"
    }
    votes2 = {
        1234: "SZA", 
        1235: "Yo-Yo Ma",
        1236: "Ethel Cain",
        1237: "Ethel Cain",
        1238: "SZA"
    }
    result1 = best_set(votes1)
    result2 = best_set(votes2)
    print(f"best_set(votes1) = {result1} (expected: SZA)")
    print(f"best_set(votes2) = {result2} (expected: SZA or Ethel Cain)")
    
    # Test 6: Sum All Maximum Values
    print("\n6. Sum All Maximum Values")
    result1 = max_audience_performances([100, 200, 200, 150, 100, 250])
    result2 = max_audience_performances([120, 180, 220, 150, 220])
    print(f"max_audience_performances([100, 200, 200, 150, 100, 250]) = {result1} (expected: 250)")
    print(f"max_audience_performances([120, 180, 220, 150, 220]) = {result2} (expected: 440)")
    
    # Test 7: Alternative Implementation
    print("\n7. Alternative Implementation")
    result1 = max_audience_performances_alt([100, 200, 200, 150, 100, 250])
    result2 = max_audience_performances_alt([120, 180, 220, 150, 220])
    print(f"max_audience_performances_alt([100, 200, 200, 150, 100, 250]) = {result1} (expected: 250)")
    print(f"max_audience_performances_alt([120, 180, 220, 150, 220]) = {result2} (expected: 440)")
    
    # Test 8: Count Pairs with Same Value
    print("\n8. Count Pairs with Same Value")
    result1 = num_popular_pairs([1, 2, 3, 1, 1, 3])
    result2 = num_popular_pairs([1, 1, 1, 1])
    result3 = num_popular_pairs([1, 2, 3])
    print(f"num_popular_pairs([1, 2, 3, 1, 1, 3]) = {result1} (expected: 4)")
    print(f"num_popular_pairs([1, 1, 1, 1]) = {result2} (expected: 6)")
    print(f"num_popular_pairs([1, 2, 3]) = {result3} (expected: 0)")
    
    # Test 9: Sum of Index Differences
    print("\n9. Sum of Index Differences")
    s1 = ["Alice", "Bob", "Charlie"]
    t1 = ["Bob", "Alice", "Charlie"]
    s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
    t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
    result1 = find_stage_arrangement_difference(s1, t1)
    result2 = find_stage_arrangement_difference(s2, t2)
    print(f"find_stage_arrangement_difference(s1, t1) = {result1} (expected: 2)")
    print(f"find_stage_arrangement_difference(s2, t2) = {result2} (expected: 12)")
    
    # Test 10: Count Characters in Set
    print("\n10. Count Characters in Set")
    result1 = num_VIP_guests("aA", "aAAbbbb")
    result2 = num_VIP_guests("z", "ZZ")
    print(f"num_VIP_guests('aA', 'aAAbbbb') = {result1} (expected: 3)")
    print(f"num_VIP_guests('z', 'ZZ') = {result2} (expected: 0)")
    
    # Test 11: Word Pattern Matching
    print("\n11. Word Pattern Matching")
    result1 = schedule_pattern("abba", "rock jazz jazz rock")
    result2 = schedule_pattern("abba", "rock jazz jazz blues")
    result3 = schedule_pattern("aaaa", "rock jazz jazz rock")
    print(f"schedule_pattern('abba', 'rock jazz jazz rock') = {result1} (expected: True)")
    print(f"schedule_pattern('abba', 'rock jazz jazz blues') = {result2} (expected: False)")
    print(f"schedule_pattern('aaaa', 'rock jazz jazz rock') = {result3} (expected: False)")
    
    # Test 12: Sort by Custom Key
    print("\n12. Sort by Custom Key")
    performer_names1 = ["Mary", "John", "Emma"]
    performance_times1 = [180, 165, 170]
    performer_names2 = ["Alice", "Bob", "Bob"]
    performance_times2 = [155, 185, 150]
    result1 = sort_performers(performer_names1, performance_times1)
    result2 = sort_performers(performer_names2, performance_times2)
    print(f"sort_performers(names1, times1) = {result1} (expected: ['Mary', 'Emma', 'John'])")
    print(f"sort_performers(names2, times2) = {result2} (expected: ['Bob', 'Alice', 'Bob'])")
    
    print("\n" + "=" * 40)
    print("PROBLEMS 13-24")
    print("=" * 40)
    
    # Test 13: Create Dictionary from Two Lists
    print("\n13. Create Dictionary from Two Lists")
    exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
    exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", "Flight Engineer", "Flight Engineer"]
    ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
    ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]
    result1 = space_crew(exp70_crew, exp70_positions)
    result2 = space_crew(ax3_crew, ax3_positions)
    print(f"space_crew(exp70_crew, exp70_positions) = {result1}")
    print(f"space_crew(ax3_crew, ax3_positions) = {result2}")
    
    # Test 14: Nested Dictionary Lookup
    print("\n14. Nested Dictionary Lookup")
    result1 = planet_lookup("Jupiter")
    result2 = planet_lookup("Pluto")
    print(f"planet_lookup('Jupiter') = {result1}")
    print("Expected: 'Planet Jupiter has an orbital period of 10592 Earth days and has 79 moons.'")
    print(f"planet_lookup('Pluto') = {result2}")
    print("Expected: 'Sorry, I have no data on that planet.'")
    
    # Test 15: Filter Dictionary by Range
    print("\n15. Filter Dictionary by Range")
    oxygen_levels = {
        "Command Module": 21,
        "Habitation Module": 20,
        "Laboratory Module": 19,
        "Airlock": 22,
        "Storage Bay": 18
    }
    result = check_oxygen_levels(oxygen_levels, 19, 22)
    print(f"check_oxygen_levels(oxygen_levels, 19, 22) = {result} (expected: ['Storage Bay'])")
    
    # Test 16: Dictionary Difference
    print("\n16. Dictionary Difference")
    exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
    exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}
    result = data_difference(exp1_data, exp2_data)
    print(f"data_difference(exp1_data, exp2_data) = {result}")
    print("Expected: {'temperature': 22, 'humidity': 45}")
    
    # Test 17: Find Most Frequent Item
    print("\n17. Find Most Frequent Item")
    votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
    votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]
    result1 = get_winner(votes1)
    result2 = get_winner(votes2)
    print(f"get_winner(votes1) = {result1} (expected: Colbert)")
    print(f"get_winner(votes2) = {result2} (expected: Serenity or Colbert)")
    
    # Test 18: Check Complete Character Set
    print("\n18. Check Complete Character Set")
    result1 = check_if_complete_transmission("thequickbrownfoxjumpsoverthelazydog")
    result2 = check_if_complete_transmission("spacetravel")
    print(f"check_if_complete_transmission('thequickbrownfoxjumpsoverthelazydog') = {result1} (expected: True)")
    print(f"check_if_complete_transmission('spacetravel') = {result2} (expected: False)")
    
    # Test 19: Count String Pairs
    print("\n19. Count String Pairs")
    result1 = max_number_of_string_pairs(["cd", "ac", "dc", "ca", "zz"])
    result2 = max_number_of_string_pairs(["ab", "ba", "cc"])
    result3 = max_number_of_string_pairs(["aa", "ab"])
    print(f"max_number_of_string_pairs(['cd', 'ac', 'dc', 'ca', 'zz']) = {result1} (expected: 2)")
    print(f"max_number_of_string_pairs(['ab', 'ba', 'cc']) = {result2} (expected: 1)")
    print(f"max_number_of_string_pairs(['aa', 'ab']) = {result3} (expected: 0)")
    
    # Test 20: Find Array Differences
    print("\n20. Find Array Differences")
    result1 = find_difference([1, 2, 3], [2, 4, 6])
    result2 = find_difference([1, 2, 3, 3], [1, 1, 2, 2])
    print(f"find_difference([1, 2, 3], [2, 4, 6]) = {result1} (expected: [[1, 3], [4, 6]])")
    print(f"find_difference([1, 2, 3, 3], [1, 1, 2, 2]) = {result2} (expected: [[3], []])")
    
    # Test 21: Count Common Elements
    print("\n21. Count Common Elements")
    result1 = find_common_signals([2, 3, 2], [1, 2])
    result2 = find_common_signals([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6])
    result3 = find_common_signals([3, 4, 2, 3], [1, 5])
    print(f"find_common_signals([2, 3, 2], [1, 2]) = {result1} (expected: [2, 1])")
    print(f"find_common_signals([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]) = {result2} (expected: [3, 4])")
    print(f"find_common_signals([3, 4, 2, 3], [1, 5]) = {result3} (expected: [0, 0])")
    
    # Test 22: Alternative Implementation
    print("\n22. Alternative Implementation")
    result1 = find_common_signals_alt([2, 3, 2], [1, 2])
    result2 = find_common_signals_alt([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6])
    result3 = find_common_signals_alt([3, 4, 2, 3], [1, 5])
    print(f"find_common_signals_alt([2, 3, 2], [1, 2]) = {result1} (expected: [2, 1])")
    print(f"find_common_signals_alt([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]) = {result2} (expected: [3, 4])")
    print(f"find_common_signals_alt([3, 4, 2, 3], [1, 5]) = {result3} (expected: [0, 0])")
    
    # Test 23: Sort by Frequency
    print("\n23. Sort by Frequency")
    result1 = frequency_sort([1, 1, 2, 2, 2, 3])
    result2 = frequency_sort([2, 3, 1, 3, 2])
    result3 = frequency_sort([-1, 1, -6, 4, 5, -6, 1, 4, 1])
    print(f"frequency_sort([1, 1, 2, 2, 2, 3]) = {result1} (expected: [3, 1, 1, 2, 2, 2])")
    print(f"frequency_sort([2, 3, 1, 3, 2]) = {result2} (expected: [1, 3, 3, 2, 2])")
    print(f"frequency_sort([-1, 1, -6, 4, 5, -6, 1, 4, 1]) = {result3}")
    print("Expected: [5, -1, 4, 4, -6, -6, 1, 1, 1]")
    
    # Test 24: Find Final Destination
    print("\n24. Find Final Destination")
    paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
    paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
    paths3 = [["StationA", "StationZ"]]
    result1 = find_final_hub(paths1)
    result2 = find_final_hub(paths2)
    result3 = find_final_hub(paths3)
    print(f"find_final_hub(paths1) = {result1} (expected: Europa)")
    print(f"find_final_hub(paths2) = {result2} (expected: Delta)")
    print(f"find_final_hub(paths3) = {result3} (expected: StationZ)")
    
    print("\n" + "=" * 70)
    print("TEST SUITE COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()