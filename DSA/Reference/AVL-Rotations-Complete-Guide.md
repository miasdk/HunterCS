# AVL Tree Rotations: Complete Exam Guide

## 🎯 **Question 7: AVL Tree Rotations (10 points)**

**Question**: Explain and diagram AVL tree rotations (LL, RR, LR, RL)

---

## 📚 **AVL Tree Balance Property**

**Key Property**: The height difference between the left and right subtrees of any node must be at most 1.

```
|Height(Left Subtree) - Height(Right Subtree)| ≤ 1
```

When this property is violated (|BF| > 1), we need **rotations** to restore balance.

---

## 🔄 **The Four Rotation Types**

### **1. LL (Left-Left) Rotation - Single Rotation**

**When to use**: Node has BF = -2 (right-heavy) and right child has BF = -1 or 0

**Visual Example:**
```
Before (Unbalanced):
    A (BF = -2)
     \
      B (BF = -1)
       \
        C

After (Balanced):
      B (BF = 0)
     / \
    A   C
```

**Code Implementation:**
```cpp
void LL_rotation(AvlNode*& A) {
    AvlNode* B = A->right;
    A->right = B->left;
    B->left = A;
    
    // Update heights
    A->height = std::max(height(A->left), height(A->right)) + 1;
    B->height = std::max(height(B->left), A->height) + 1;
    
    A = B;  // B becomes new root
}
```

---

### **2. RR (Right-Right) Rotation - Single Rotation**

**When to use**: Node has BF = +2 (left-heavy) and left child has BF = +1 or 0

**Visual Example:**
```
Before (Unbalanced):
        C (BF = +2)
       /
      B (BF = +1)
     /
    A

After (Balanced):
      B (BF = 0)
     / \
    A   C
```

**Code Implementation:**
```cpp
void RR_rotation(AvlNode*& A) {
    AvlNode* B = A->left;
    A->left = B->right;
    B->right = A;
    
    // Update heights
    A->height = std::max(height(A->left), height(A->right)) + 1;
    B->height = std::max(height(B->left), A->height) + 1;
    
    A = B;  // B becomes new root
}
```

---

### **3. LR (Left-Right) Rotation - Double Rotation**

**When to use**: Node has BF = +2 (left-heavy) and left child has BF = -1

**Two-Step Process:**
1. **Left rotation** on left child
2. **Right rotation** on original node

**Visual Example:**
```
Step 1 - Left Rotation on A:
    C (BF = +2)          C (BF = +2)
   /                     /
  A (BF = -1)    →      B (BF = +1)
   \                   /
    B                 A

Step 2 - Right Rotation on C:
      B (BF = 0)
     / \
    A   C
```

**Code Implementation:**
```cpp
void LR_rotation(AvlNode*& A) {
    // Step 1: Left rotation on left child
    LL_rotation(A->left);
    
    // Step 2: Right rotation on original node
    RR_rotation(A);
}

// Alternative direct implementation:
void LR_rotation(AvlNode*& A) {
    AvlNode* B = A->left;
    AvlNode* C = B->right;
    
    // Perform rotation
    B->right = C->left;
    A->left = C->right;
    C->left = B;
    C->right = A;
    
    // Update heights
    A->height = std::max(height(A->left), height(A->right)) + 1;
    B->height = std::max(height(B->left), height(B->right)) + 1;
    C->height = std::max(height(C->left), height(C->right)) + 1;
    
    A = C;  // C becomes new root
}
```

---

### **4. RL (Right-Left) Rotation - Double Rotation**

**When to use**: Node has BF = -2 (right-heavy) and right child has BF = +1

**Two-Step Process:**
1. **Right rotation** on right child
2. **Left rotation** on original node

**Visual Example:**
```
Step 1 - Right Rotation on C:
A (BF = -2)          A (BF = -2)
 \                    \
  C (BF = +1)   →      B (BF = -1)
 /                      \
B                        C

Step 2 - Left Rotation on A:
      B (BF = 0)
     / \
    A   C
```

**Code Implementation:**
```cpp
void RL_rotation(AvlNode*& A) {
    // Step 1: Right rotation on right child
    RR_rotation(A->right);
    
    // Step 2: Left rotation on original node
    LL_rotation(A);
}

// Alternative direct implementation:
void RL_rotation(AvlNode*& A) {
    AvlNode* B = A->right;
    AvlNode* C = B->left;
    
    // Perform rotation
    B->left = C->right;
    A->right = C->left;
    C->left = A;
    C->right = B;
    
    // Update heights
    A->height = std::max(height(A->left), height(A->right)) + 1;
    B->height = std::max(height(B->left), height(B->right)) + 1;
    C->height = std::max(height(C->left), height(C->right)) + 1;
    
    A = C;  // C becomes new root
}
```

---

## 🎯 **Rotation Decision Table**

| Node BF | Child BF | Rotation Type | Description |
|---------|----------|---------------|-------------|
| **+2** | **+1 or 0** | **RR** | Left-heavy node with left-heavy child |
| **+2** | **-1** | **LR** | Left-heavy node with right-heavy left child |
| **-2** | **-1 or 0** | **LL** | Right-heavy node with right-heavy child |
| **-2** | **+1** | **RL** | Right-heavy node with left-heavy right child |

---

## 📝 **Complete Example: Insertion with Rotations**

### **Scenario**: Insert values [30, 20, 40, 10, 25, 35, 50, 5] into an empty AVL tree

**Step-by-step process:**

```
1. Insert 30:    30

2. Insert 20:    30
                /
               20

3. Insert 40:    30
                /  \
               20   40

4. Insert 10:    30
                /  \
               20   40
              /
             10

5. Insert 25:    30
                /  \
               20   40
              /  \
             10   25

6. Insert 35:    30
                /  \
               20   40
              /  \  /
             10   25 35

7. Insert 50:    30
                /  \
               20   40
              /  \  /  \
             10   25 35  50

8. Insert 5:     30
                /  \
               20   40
              /  \  /  \
             10   25 35  50
            /
           5
```

**Check balance factors after inserting 5:**
- Node 5: BF = 0 ✓
- Node 10: BF = +1 ✓
- Node 20: BF = +2 ✗ **UNBALANCED**
- Node 25: BF = 0 ✓
- Node 30: BF = +3 ✗ **UNBALANCED**
- Node 35: BF = 0 ✓
- Node 40: BF = 0 ✓
- Node 50: BF = 0 ✓

**Identify rotation needed:**
- Node 20 is first unbalanced (BF = +2)
- Node 10 (left child) has BF = +1
- This is an **RR case**

**Perform RR rotation on node 20:**
```
Before:        30              After:        30
              /  \                          /  \
             20   40                       10   40
            /  \  /  \                    /  \  /  \
           10   25 35  50                5    20 35  50
          /                              \
         5                               25
```

---

## 🧠 **Why Rotations Work**

### **Mathematical Analysis:**
1. **Single Rotations (LL, RR)**: Reduce tree height by 1
2. **Double Rotations (LR, RL)**: Reduce tree height by 1
3. **Balance restored**: All nodes have |BF| ≤ 1

### **Height Analysis:**
- **Before rotation**: Unbalanced subtree has height h+2
- **After rotation**: Balanced subtree has height h+1
- **Result**: Height reduced by 1, balance restored

---

## 🎯 **Exam Answer Templates**

### **For Single Rotation (LL/RR):**
```
[Rotation Type] is a single rotation used to fix [left/right]-heavy AVL tree imbalances.

When to use:
- Node A has BF = [±2] ([left/right] subtree 2 levels higher)
- [Left/Right] child B has BF = [±1 or 0]

Process:
1. B becomes the new root
2. A becomes B's [right/left] child  
3. B's [right/left] subtree becomes A's [left/right] subtree

Example:
Before:    A (BF = [±2])    After:      B (BF = 0)
          [direction]                        / \
         B (BF = [±1])                     [children]
        [direction]
       [child]
```

### **For Double Rotation (LR/RL):**
```
[Rotation Type] is a double rotation used to fix [left/right]-heavy AVL tree imbalances.

When to use:
- Node A has BF = [±2] ([left/right] subtree 2 levels higher)
- [Left/Right] child B has BF = [∓1] (opposite imbalance)

Process:
1. [First rotation] on [left/right] child
2. [Second rotation] on original node

Example:
Step 1: [First rotation]    Step 2: [Second rotation]
[Show intermediate state]   [Show final balanced state]
```

---

## ⚡ **Quick Reference**

### **Memory Aids:**
- **LL**: **L**eft-heavy node needs **L**eft rotation
- **RR**: **R**ight-heavy node needs **R**ight rotation
- **LR**: **L**eft-heavy node with **R**ight-heavy left child
- **RL**: **R**ight-heavy node with **L**eft-heavy right child

### **Code Patterns:**
```cpp
// Single rotation pattern
B = A->[left/right];
A->[left/right] = B->[right/left];
B->[right/left] = A;
A = B;

// Double rotation pattern
[First rotation](A->[left/right]);
[Second rotation](A);
```

### **Height Updates:**
```cpp
// Always update heights after rotation
A->height = std::max(height(A->left), height(A->right)) + 1;
B->height = std::max(height(B->left), height(B->right)) + 1;
```

---

## 🚨 **Common Mistakes to Avoid**

### **1. Wrong Rotation Selection**
- Always check **both** the unbalanced node **and** its child
- Use the decision table to identify correct rotation

### **2. Forgetting Height Updates**
- Must recalculate heights after every rotation
- Heights affect future balance factor calculations

### **3. Confusing Double Rotations**
- LR and RL are **different** - don't mix them up
- LR: Left rotation first, then Right rotation
- RL: Right rotation first, then Left rotation

### **4. Wrong Node Identification**
- Find the **first** unbalanced node when traveling up from insertion
- Don't stop at the first node with |BF| > 1

### **5. Incorrect Balance Factor Calculation**
- BF = Height(Left) - Height(Right)
- Remember: |BF| ≤ 1 for balanced nodes

---

## 📋 **Practice Questions**

### **Question 1**: When do you use each rotation type?
**Answer**: 
- LL: Node BF = -2, right child BF = -1 or 0
- RR: Node BF = +2, left child BF = +1 or 0
- LR: Node BF = +2, left child BF = -1
- RL: Node BF = -2, right child BF = +1

### **Question 2**: What's the difference between single and double rotations?
**Answer**: Single rotations (LL, RR) fix simple imbalances, double rotations (LR, RL) fix complex imbalances that require two steps.

### **Question 3**: Do rotations always reduce tree height?
**Answer**: Yes, all rotations reduce the height of the affected subtree by 1.

---

## 🎯 **Exam Strategy**

### **1. Draw Clear Diagrams**
Always show before/after diagrams with balance factors labeled.

### **2. Use the Decision Table**
Quickly identify which rotation is needed based on balance factors.

### **3. Show Step-by-Step Process**
For double rotations, show the intermediate state.

### **4. Verify Your Answer**
Check that all balance factors are ≤ 1 after rotation.

### **5. Explain the Reasoning**
Don't just show the result - explain why this rotation fixes the imbalance.

---

## 🏆 **Complete Rotation Summary**

| Rotation | Trigger | Type | Process | Result |
|----------|---------|------|---------|--------|
| **LL** | BF = -2, right child BF = -1/0 | Single | Left rotation | Height -1, balanced |
| **RR** | BF = +2, left child BF = +1/0 | Single | Right rotation | Height -1, balanced |
| **LR** | BF = +2, left child BF = -1 | Double | Left then Right | Height -1, balanced |
| **RL** | BF = -2, right child BF = +1 | Double | Right then Left | Height -1, balanced |

---

*This comprehensive guide covers all four AVL rotation types. Practice drawing the diagrams and understanding the mathematical reasoning behind why each rotation works!* 