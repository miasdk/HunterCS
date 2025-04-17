template <typename HashedObj>
class HashTable
{
    public:
        // Constructor: Initializes the hash table with a given size (default is 101).
        explicit HashTable(int size = 101); 

        // Checks if the hash table contains the given object `x`.
        bool contains(const HashedObj & x) const;
        
        // Empties the hash table by clearing all elements.
        void makeEmpty(); 

        // Inserts a new object `x` into the hash table (by copy).
        // Returns true if the insertion is successful, false if `x` already exists.
        bool insert(const HashedObj & x);

        // Inserts a new object `x` into the hash table (by move semantics for efficiency).
        // Returns true if the insertion is successful, false if `x` already exists.
        bool insert(HashedObj && x); 

        // Removes the object `x` from the hash table.
        // Returns true if the removal is successful, false if `x` is not found.
        bool remove(const HashedObj & x); 

    private: 
        // The array of lists (buckets) used for separate chaining to resolve collisions.
        vector<list<HashedObj>> theLists; 

        // The current number of elements in the hash table.
        int currentSize; 

        // Rehashes the table when the load factor becomes too high.
        // This involves creating a larger table and reinserting all elements.
        void rehash(); 

        // Computes the hash value for the given object `x`.
        // Ensures the hash value is within the bounds of the table size.
        size_t myhash(const HashedObj & x) const;
};