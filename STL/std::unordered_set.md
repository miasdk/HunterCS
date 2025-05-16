# Unordered Set

Containers that store unique elements in no particular order, which allow for fast retrieval of individual elements based on their value.

## Member Functions

### Constructors/Destructors
- `(constructor)` - Construct unordered_set (public member function)
- `(destructor)` - Destroy unordered set (public member function)
- `operator=` - Assign content (public member function)

### Capacity
- `empty` - Test whether container is empty (public member function)
- `size` - Return container size (public member function)
- `max_size` - Return maximum size (public member function)

### Iterators
- `begin` - Return iterator to beginning (public member type)
- `end` - Return iterator to end (public member type)
- `cbegin` - Return const_iterator to beginning (public member function)
- `cend` - Return const_iterator to end (public member function)

### Element Lookup
- `find` - Get iterator to element (public member function)
- `count` - Count elements with a specific key (public member function)
- `equal_range` - Get range of elements with a specific key (public member function)

### Modifiers
- `emplace` - Construct and insert element (public member function)
- `emplace_hint` - Construct and insert element with hint (public member function)
- `insert` - Insert elements (public member function)
- `erase` - Erase elements (public member function)
- `clear` - Clear content (public member function)
- `swap` - Swap content (public member function)

### Buckets
- `bucket_count` - Return number of buckets (public member function)
- `max_bucket_count` - Return maximum number of buckets (public member function)
- `bucket_size` - Return bucket size (public member type)
- `bucket` - Locate element's bucket (public member function)

### Hash Policy
- `load_factor` - Return load factor (public member function)
- `max_load_factor` - Get or set maximum load factor (public member function)
- `rehash` - Set number of buckets (public member function)
- `reserve` - Request a capacity change (public member function)

### Observers
- `hash_function` - Get hash function (public member type)
- `key_eq` - Get key equivalence predicate (public member type)
- `get_allocator` - Get allocator (public member function)