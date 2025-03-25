std::undordered_map  

### Unordered Map

Unordered maps are associative containers that store elements formed by the combination of a *key value* and a *mapped value*, and which allows for fast retrieval of individual elements based on their keys.

- Key Value: Used to uniquely identify the element. 

- Mapped Value: Object with the content associated to this key. 

*Types of key and map value may differ*

-Buckets: where elements in an unordered_map are organized depending on their hash value 

-Key values: allow for fast access to elements within the bucket 

Unordered maps implement the direct access operator (operator[]) which allows for direct access of the mapped value using its key value as argument.

## Properties 
1) Associative 
2) Unordered 
3) Map: Each element associates a key to a mapped value:
4) Unique keys: No two elements in the container can have equivalent keys 
5) Allocator-aware: The container uses an allocator object to dynamically handle its storage needs

## Members 