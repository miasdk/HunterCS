#!/usr/bin/env python3
"""
Standard Problem Set Version 1 - Implementation Skeleton
"""

# ============================================================================
# PROBLEMS 1-12
# ============================================================================

# Problem 1: Festival Lineup
def lineup(artists, set_times):
    """Map each artist to their set time using a dictionary."""
    pass


# Problem 2: Planning App
def get_artist_info(artist, festival_schedule):
    """Return artist's info dict or error message if not found."""
    pass


# Problem 3: Ticket Sales
def total_sales(ticket_sales):
    """Return the total number of tickets of all types sold."""
    pass


# Problem 4: Scheduling Conflict
def identify_conflicts(venue1_schedule, venue2_schedule):
    """Return dictionary of identical key-value pairs from both venues."""
    pass


# Problem 5: Best Set
def best_set(votes):
    """Return the artist with the most votes."""
    pass


# Problem 6: Performances with Maximum Audience
def max_audience_performances(audiences):
    """Return combined audience size of all performances with maximum audience size."""
    pass


# Problem 7: Performances with Maximum Audience II (Alternative Implementation)
def max_audience_performances_alt(audiences):
    """Alternative implementation of max_audience_performances using different approach."""
    pass


# Problem 8: Popular Song Pairs
def num_popular_pairs(popularity_scores):
    """Count pairs (i,j) where i < j and scores[i] == scores[j]."""
    pass


# Problem 9: Stage Arrangement Difference Between Two Performances
def find_stage_arrangement_difference(s, t):
    """Return sum of absolute differences between indices of elements in both arrays."""
    pass


# Problem 10: VIP Passes and Guests
def num_VIP_guests(vip_passes, guests):
    """Count how many characters from guests are present in vip_passes."""
    pass


# Problem 11: Performer Schedule Pattern (IMPLEMENTED - with bug fixes)
def schedule_pattern(pattern, schedule):
    """Return True if schedule words follow the same pattern as pattern string."""
    genres = schedule.split()
    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True


# Problem 12: Sort the Performers
def sort_performers(performer_names, performance_times):
    """Return performer names sorted by performance times in descending order."""
    pass


# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    """Run all test cases to verify implementations."""
    
    print("=" * 70)
    print("STANDARD PROBLEM SET VERSION 1 TEST SUITE")
    print("=" * 70)
    
    # Test 1: Festival Lineup
    print("\n1. Festival Lineup")
    artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
    set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]
    artists2 = []
    set_times2 = []
    result1 = lineup(artists1, set_times1)
    result2 = lineup(artists2, set_times2)
    print(f"lineup(artists1, set_times1) = {result1}")
    print("Expected: {'Kendrick Lamar': '9:30 PM', 'Chappell Roan': '5:00 PM', 'Mitski': '2:00 PM', 'Rosalia': '7:30 PM'}")
    print(f"lineup([], []) = {result2} (expected: {{}})")
    
    # Test 2: Planning App
    print("\n2. Planning App")
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
    
    # Test 3: Ticket Sales
    print("\n3. Ticket Sales")
    ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
    result = total_sales(ticket_sales)
    print(f"total_sales({ticket_sales}) = {result} (expected: 4500)")
    
    # Test 4: Scheduling Conflict
    print("\n4. Scheduling Conflict")
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
    
    # Test 5: Best Set
    print("\n5. Best Set")
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
    
    # Test 6: Performances with Maximum Audience
    print("\n6. Performances with Maximum Audience")
    audiences1 = [100, 200, 200, 150, 100, 250]
    audiences2 = [120, 180, 220, 150, 220]
    result1 = max_audience_performances(audiences1)
    result2 = max_audience_performances(audiences2)
    print(f"max_audience_performances([100, 200, 200, 150, 100, 250]) = {result1} (expected: 250)")
    print(f"max_audience_performances([120, 180, 220, 150, 220]) = {result2} (expected: 440)")
    
    # Test 7: Performances with Maximum Audience II
    print("\n7. Performances with Maximum Audience II (Alternative)")
    result1 = max_audience_performances_alt(audiences1)
    result2 = max_audience_performances_alt(audiences2)
    print(f"max_audience_performances_alt([100, 200, 200, 150, 100, 250]) = {result1} (expected: 250)")
    print(f"max_audience_performances_alt([120, 180, 220, 150, 220]) = {result2} (expected: 440)")
    
    # Test 8: Popular Song Pairs
    print("\n8. Popular Song Pairs")
    popularity_scores1 = [1, 2, 3, 1, 1, 3]
    popularity_scores2 = [1, 1, 1, 1]
    popularity_scores3 = [1, 2, 3]
    result1 = num_popular_pairs(popularity_scores1)
    result2 = num_popular_pairs(popularity_scores2)
    result3 = num_popular_pairs(popularity_scores3)
    print(f"num_popular_pairs([1, 2, 3, 1, 1, 3]) = {result1} (expected: 4)")
    print(f"num_popular_pairs([1, 1, 1, 1]) = {result2} (expected: 6)")
    print(f"num_popular_pairs([1, 2, 3]) = {result3} (expected: 0)")
    
    # Test 9: Stage Arrangement Difference
    print("\n9. Stage Arrangement Difference")
    s1 = ["Alice", "Bob", "Charlie"]
    t1 = ["Bob", "Alice", "Charlie"]
    s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
    t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
    result1 = find_stage_arrangement_difference(s1, t1)
    result2 = find_stage_arrangement_difference(s2, t2)
    print(f"find_stage_arrangement_difference(s1, t1) = {result1} (expected: 2)")
    print(f"find_stage_arrangement_difference(s2, t2) = {result2} (expected: 12)")
    
    # Test 10: VIP Passes and Guests
    print("\n10. VIP Passes and Guests")
    vip_passes1 = "aA"
    guests1 = "aAAbbbb"
    vip_passes2 = "z"
    guests2 = "ZZ"
    result1 = num_VIP_guests(vip_passes1, guests1)
    result2 = num_VIP_guests(vip_passes2, guests2)
    print(f"num_VIP_guests('aA', 'aAAbbbb') = {result1} (expected: 3)")
    print(f"num_VIP_guests('z', 'ZZ') = {result2} (expected: 0)")
    
    # Test 11: Performer Schedule Pattern (IMPLEMENTED)
    print("\n11. Performer Schedule Pattern (IMPLEMENTED)")
    pattern1 = "abba"
    schedule1 = "rock jazz jazz rock"
    pattern2 = "abba"
    schedule2 = "rock jazz jazz blues"
    pattern3 = "aaaa"
    schedule3 = "rock jazz jazz rock"
    result1 = schedule_pattern(pattern1, schedule1)
    result2 = schedule_pattern(pattern2, schedule2)
    result3 = schedule_pattern(pattern3, schedule3)
    print(f"schedule_pattern('abba', 'rock jazz jazz rock') = {result1} (expected: True)")
    print(f"schedule_pattern('abba', 'rock jazz jazz blues') = {result2} (expected: False)")
    print(f"schedule_pattern('aaaa', 'rock jazz jazz rock') = {result3} (expected: False)")
    
    # Test 12: Sort the Performers
    print("\n12. Sort the Performers")
    performer_names1 = ["Mary", "John", "Emma"]
    performance_times1 = [180, 165, 170]
    performer_names2 = ["Alice", "Bob", "Bob"]
    performance_times2 = [155, 185, 150]
    result1 = sort_performers(performer_names1, performance_times1)
    result2 = sort_performers(performer_names2, performance_times2)
    print(f"sort_performers(names1, times1) = {result1} (expected: ['Mary', 'Emma', 'John'])")
    print(f"sort_performers(names2, times2) = {result2} (expected: ['Bob', 'Alice', 'Bob'])")
    
    print("\n" + "=" * 70)
    print("TEST SUITE COMPLETE")
    print("=" * 70)
    print("\nNOTE: Problem 11 (Performer Schedule Pattern) is already implemented with bug fixes.")
    print("All other problems need implementation - replace 'pass' with your solutions.")


if __name__ == "__main__":
    run_tests()