#include <iostream> 
#include <string>

//Node delcarations for trees 
template <typename Object>

struct TreeNode {
    Object element; 
    TreeNode *firstChild;
    TreeNode *nextSibling;
};

//Binary tree node class
template <typename Object>
 
struct BinaryNode
{
Object element; // The data in the node
BinaryNode *left; // Left child
BinaryNode *right; // Right child
};