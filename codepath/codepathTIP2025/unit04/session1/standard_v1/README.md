# Unit 4 Session 1 - Standard Problem Set Version 1

## NFT Problem Set

This problem set focuses on basic and intermediate Python skills using NFT-themed problems. Each function is implemented in `problems.py` with docstrings, time/space complexity explanations, and example usages.

### Problems

1. **NFT Name Extractor**
   - Extract the names of NFTs from a list of dictionaries.
2. **NFT Collection Review**
   - Debug and explain a buggy function for extracting NFT names.
3. **Identify Popular Creators**
   - Find creators with more than one NFT in the collection.
4. **NFT Collection Statistics**
   - Compute the average value of NFTs, handling empty collections.
5. **NFT Tag Search**
   - Search nested NFT collections for NFTs with a specific tag.
6. **NFT Queue Processing**
   - Process NFTs in FIFO order and return their names.
7. **Validate NFT Addition**
   - Check if a sequence of 'add' and 'remove' actions is balanced.
8. **Find Closest NFT Values**
   - Find the two NFT values closest to a given budget in a sorted list.

## How to Use

- All problems are in `problems.py`.
- Each function includes example usage at the bottom of the file.
- To test, run:

```bash
python problems.py
```

Or copy/paste the function and example into a Python shell or notebook.

## Notes
- Each function includes a docstring with time and space complexity analysis.
- For the buggy function in Problem 2, see the comments and compare with the correct implementation.

## Key Concepts
- Asymptotic Analysis (Big O)
- Time Complexity: O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n)
- Space Complexity
- Constant, Linear, Quadratic, Exponential complexities
- Built-in function complexities (len, sort, append, etc.)

## Tips & Pitfalls
- Always consider worst-case performance unless otherwise stated
- Drop constants and lower-order terms in Big O
- Use built-in functions efficiently
- Test with large inputs to check performance

## Testing
- [ ] All problems have test cases
- [ ] Edge cases considered

--- 