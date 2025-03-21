Chapter 5: Hashing
==================

5.1 General Idea
----------------

-   **Hashing** is a technique used for performing insertions, deletions, and finds in **constant average time**.

-   The ideal **hash table** data structure is an array of fixed size containing items.

-   **Key**: The data member in the data structure that the search operation is performed on.

-   Each key is mapped to a number in the range `[0, TableSize - 1]`.

-   **Hash Function**: Maps a data member to an index in the hash table. Ideally, each unique key should map to a different cell (though this is typically impossible).

-   **Collision**: Occurs when two keys hash to the same value.

-   **Table Size**: Should be a **prime number** for better distribution.

-   **Secondary Hash (Rehash)**: Provides an interval to check if the original bucket is full and the key cannot be inserted there.

* * * * *

5.2 Hash Function
-----------------

-   It is often a good idea to ensure the table size is **prime**.

-   **Collision Resolution**: Techniques like **separate chaining** are used.

* * * * *

5.3 Separate Chaining
---------------------

-   **Separate Chaining**: A strategy where each bucket contains a **list of all elements** that hash to the same value.

-   **Operations**:

    -   **Search**: Use the hash function to determine which list to traverse, then search the list.

    -   **Insert**: Check the appropriate list to see if the element is already present. If not, insert it at the front of the list (since recently inserted elements are likely to be accessed soon).

-   **Hash Function Object Template**:
-   
`template<typename Key>
class hash {
public:
    size_t operator() (const Key & k) const;
};

// Example implementation
template <>
class hash<string> {
public:
    size_t operator()(const string & key) {
        size_t hashVal = 0;
        for (char ch : key)
            hashVal = 37 * hashVal + ch; // 37 is arbitrary
        return hashVal;
    }
};`
-   **General Rule**: For separate chaining, the table size should be about as large as the number of elements expected (i.e., let **λ ≈ 1**).

-   **Load Factor**: A measure of how full the hash table is.

-   **Table Size**: Should be **prime** to ensure good distribution.

* * * * *

### Additional Methods for Separate Chaining Hash Table

`// makeEmpty()
void makeEmpty() {
    for (auto & thisList : theLists)
        thisList.clear();
}

// contains()
bool contains(const HashedObj & x) const {
    auto & whichList = theLists[myhash(x)];
    return find(begin(whichList), end(whichList), x) != end(whichList);
}

// remove()
bool remove(const HashedObj & x) {
    auto & whichList = theLists[myhash(x)];
    auto itr = find(begin(whichList), end(whichList), x);

    if (itr == end(whichList))
        return false;

    whichList.erase(itr);
    --currentSize;
    return true;
}

// insert()
bool insert(const HashedObj & x) {
    auto & whichList = theLists[myHash(x)];
    if (find(begin(whichList), end(whichList), x) != end(whichList))
        return false;

    whichList.push_back(x);

    // Rehash
    if (++currentSize > theLists.size())
        rehash();

    return true;
}`
* * * * *

5.4 Hash Tables Without Linked Lists
------------------------------------

-   **Probing Hash Tables**: Hash tables that do not use separate chaining.

-   **Load Factor (λ)**: Should be **below 0.5** for probing hash tables.

    -   **λ = Number of elements / Table size**.

    -   For probing hash tables, the load factor must be **strictly less than 1** because every element must occupy a unique slot.

### Probing Techniques

1.  **Linear Probing**:

    -   Upon collision, check the next available bucket.

2.  **Quadratic Probing**:

    -   The collision function is quadratic.

3.  **Double Hashing**:

    -   A second hash function is used to calculate the step size for probing.

* * * * *

5.5 Rehashing
-------------

-   **Rehashing**: The process of resizing a hash table and redistributing its elements when the load factor exceeds a certain threshold.

* * * * *

5.6 Hash Tables in the Standard Library
---------------------------------------

### `unordered_map`

-   **Definition**: An associative container that stores **key-value pairs**.

-   **Implementation**: Uses a hash table internally for fast average-case performance.

-   **Key Features**:

    -   **Keys are unique**: No two elements can have the same key.

    -   **Unordered**: Elements are not stored in any specific order (unlike `std::map`, which is ordered).

    -   **Fast access**: Average-case **O(1)** time complexity for insertion, deletion, and lookup.

### `unordered_set`

-   **Definition**: A container that stores **unique elements**.

-   **Implementation**: Uses a hash table internally for fast average-case performance.

-   **Key Features**:

    -   **Elements are unique**: No duplicates are allowed.

    -   **Unordered**: Elements are not stored in any specific order (unlike `std::set`, which is ordered).

    -   **Fast access**: Average-case **O(1)** time complexity for insertion, deletion, and lookup.

* * * * *

### Summary

-   **Hashing** enables fast average-case operations (**O(1)**) for insertion, deletion, and lookup.

-   **Collision Resolution**:

    -   **Separate Chaining**: Uses linked lists to handle collisions.

    -   **Probing**: Uses techniques like linear, quadratic, or double hashing.

-   **Load Factor**:

    -   **Separate Chaining**: Keep **λ ≈ 1**.

    -   **Probing Hash Tables**: Keep **λ < 0.5**.

-   **Rehashing**: Resizes the table to maintain efficiency.

-   **Standard Library**:

    -   **`unordered_map`**: For key-value pairs.

    -   **`unordered_set`**: For unique elements.
