According to the C++ standard, for the vector, a call to push_back, pop_back, insert, or erase invalidates (potentially makes stale) all iterators viewing the vector. Why?
-A call to push_back, pop_back, insert, or erase might upset the order of all vectors viewing the object invalidating all vectors pointing to the object operated on. 

List 3 things that must be done in a move assignment operator that don't need to be done in a move constructor
-1. Check to make sure you're not performing a self-assignment 
-2. Delete any dynamically allocated memory from the target destination before overwriting the pointer to it. 
-3. Return a pointer to itself 


Calculating the smallest size of an AVL tree given a height: 
The recurrence relation of this is simple: 
1. S(h) = S(h-1) + S(h-2) + 1 where h is height 

2. The base cases are S(0) = 1 and S(1) = 2. 

3. Compute S(h) iteratively using the recurrence relation

Write the move constructor for AlgorithmsCourse class with the following data members. Assume the Student class is already fully implemented and functional, and that gradeData_ points to a dynamically allocated integer array. 
`
std::string syllabus_; 
std::vector<Student> roster_; 
int courseNumber_; 
int* gradeData_; 

THE BIG FIVE: 
