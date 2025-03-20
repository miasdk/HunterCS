Hashing
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

