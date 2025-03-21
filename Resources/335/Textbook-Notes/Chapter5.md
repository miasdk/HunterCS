### **Hashing**
### 5.1 General Idea 
Hashing is a technique used for performing insertions, deletions, and finds in constant average time. 

The ideal hash table data structure is merely an array of some fixed size containing the
items.

Key: data member in the data structure the search operation is performed on 

Each key is mapped to a number in TableSize from in the range 0 - TableSize-1

Hash function: The process of mapping a data member to an index in the Hash Table 
should ensure each unique key is mapped to a different cell. (Ideal situation - typically impossible) 

Collision: when two keys hash to the same value  

Size of hash table should be a prime number. 

secondary hash goves us an interval to check if original bucket is full and we cannot insert key there 
also called rehash 

### 5.2 Hash Function 
Often a good idea to ensure table size is prime
Collision resolution -> seperate chaining 

### 5.3 Seperate Chaining 
The first strategy, commonly known as separate chaining, is to keep a list of all elements
that hash to the same value.

To perform a search, we use the hash function to determine which list to traverse. We
then search the appropriate list. To perform an insert, we check the appropriate list to see
whether the element is already in place. If the
element turns out to be new, it can be inserted at the front of the list, since it is convenient
and also because frequently it happens that recently inserted elements are the most likely
to be accessed in the near future.

Hash function object template: 
` 
template<typename Key>
class hash
{ 
    public: size_t operator() (const Key & k) const;
};

//Example implementation 

template <>
class hash<string>
{
    public; 
    size_t operator()( const string & key )
    {
        size_t hashVal = 0; 

        for( char ch : key )
            hashVal = 37 * hashVal + ch; // 37 is aribitrary 

            return hashVal; 
    }
}

`

he general rule
for separate chaining hashing is to make the table size about as large as the number of
elements expected (in other words, let λ ≈ 1)

Load factor: measure of how full a hash table is

Again, it is a good idea to keep table size prime to ensure good distribution. 

## Additional methods for seperate chaining hash table 
`
//makeEmpty() f
void makeEmpty()
{
    for ( auto & thisList: theLists )
        thisList.clear();
}

//contains() 
bool contains ( const HashedObj & x ) const 
{ 
    auto & whichList = theLists[ myhash(x) ]; 
    return find(begin ( whichList ), end (whichList ), x ) != end( whichList);
}

//remove()
bool remove( const HashedObj & x)
{
    auto & whichList = theLists[ myhash(x) ]; 
    auto itr = find( begin( whichList), end( whichList ), x); 

    if (itr == end( whichList ) )
        return false; 
    
    whichList.erase( itr ); 
    --currentSize; 
    return true;
}

//insert()
bool insert (const HashedObj& x )
{
    auto & whichList = theLists[ myHash(x) ]; 
    if( find(begin(whichList), end( whichList), x ) != end( whichList) )
        return false; 
    whichList.push_back( x ); 

    //Rehash 
    if ( ++currentSize > theLists.size())
        rehash(); 

    return true; 
}

### 5.4 Hash Tables without Linked Lists 
Generally, the load factor should be
below λ = 0.5 for a hash table that doesn’t use separate chaining. We call such tables
probing hash tables

probing hash table: hash table that doesn't use seperate chaining 

λ = Number of elements / Table size 
For probing hash tables, the load factor must be strictly less than 1 because every element must occupy a unique slot 

##Linear Probing 
Upon collision, check next available bucket 

##Quadratic Probing 
Collision function is quadratic 

##  Double Hashing 
A second hash function is used to calculate the step size for probling. 

### 5.5 Rehashing 
The process of resizing a hash table and redistributing its elements when the load factor exceeds a certain threshold. 

### 5.6 Hash Tables in the Standard Library 

unordered_map: 
Definition:

unordered_map is an associative container that stores key-value pairs.

It uses a hash table internally to achieve fast average-case performance.

Key Features:

Keys are unique: No two elements can have the same key.

Unordered: Elements are not stored in any specific order (unlike std::map, which is ordered).

Fast access: Average-case O(1) time complexity for insertion, deletion, and lookup.

unordered_set: Definition:

unordered_set is a container that stores unique elements.

It also uses a hash table internally for fast average-case performance.

Key Features:

Elements are unique: No duplicates are allowed.

Unordered: Elements are not stored in any specific order (unlike std::set, which is ordered).

Fast access: Average-case O(1) time complexity for insertion, deletion, and lookup.

Summary
unordered_map: A hash table-based container for key-value pairs.

unordered_set: A hash table-based container for unique elements.

Both provide average-case O(1) time complexity for insertion, deletion, and lookup.

They are ideal for use cases where fast access is required, and ordering is not important.

Summary (AI Generated): 
Chapter 5: Hashing
5.1 General Idea
Hashing is a technique for performing insertions, deletions, and finds in constant average time (O(1)).

A hash table is an array where keys are mapped to indices using a hash function.

Key: The data member used for searching.

Hash Function: Maps keys to indices in the range [0, TableSize - 1].

Collision: Occurs when two keys hash to the same index.

Table Size: Should be a prime number for better distribution.

Secondary Hash (Rehash): Used to find an alternative index when a collision occurs.

5.2 Hash Function
A good hash function ensures keys are distributed evenly across the table.

Collision Resolution: Techniques like separate chaining or probing are used to handle collisions.

5.3 Separate Chaining
Separate Chaining: Each bucket in the hash table contains a linked list of elements that hash to the same index.

Operations:

Search: Use the hash function to find the appropriate list and traverse it.

Insert: Check the list and insert at the front if the element is new.

Load Factor (λ): Should be kept close to 1 for separate chaining.

Table Size: Should be prime for better distribution.

Additional Methods for Separate Chaining
makeEmpty(): Clears all buckets.

contains(): Checks if an element exists in the hash table.

remove(): Deletes an element from the hash table.

insert(): Inserts an element and triggers rehashing if the load factor exceeds the threshold.

5.4 Hash Tables Without Linked Lists (Probing Hash Tables)
Probing Hash Tables: Use probing (e.g., linear, quadratic, or double hashing) to resolve collisions.

Load Factor (λ): Should be kept below 0.5 for probing hash tables.

Probing Techniques:

Linear Probing: Check the next available bucket.

Quadratic Probing: Use a quadratic function to find the next bucket.

Double Hashing: Use a second hash function to determine the step size.

5.5 Rehashing
Rehashing: Resizes the hash table and redistributes elements when the load factor exceeds a threshold.

Steps:

Create a new, larger table (typically double the size).

Recompute hash values for all elements.

Insert elements into the new table.

Deallocate the old table.

Time Complexity: O(n).

5.6 Hash Tables in the Standard Library
unordered_map:

A hash table-based container for key-value pairs.

Provides O(1) average-case time complexity for insertion, deletion, and lookup.

Keys are unique, and elements are unordered.

unordered_set:

A hash table-based container for unique elements.

Provides O(1) average-case time complexity for insertion, deletion, and lookup.

Elements are unordered.

Key Takeaways
Hashing enables fast average-case operations (O(1)) for insertion, deletion, and lookup.

Collision Resolution:

Separate Chaining: Uses linked lists to handle collisions.

Probing: Uses techniques like linear, quadratic, or double hashing.

Load Factor: Critical for maintaining performance:

Separate Chaining: Keep λ ≈ 1.

Probing Hash Tables: Keep λ < 0.5.

Rehashing: Resizes the table to maintain efficiency.

Standard Library:

unordered_map: For key-value pairs.

unordered_set: For unique elements.

This summary captures the key concepts and techniques discussed in your Chapter 5 notes. Let me know if you need further clarification or additional details!