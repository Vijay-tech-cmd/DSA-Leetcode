# 📝 Bottom View of Binary Tree (GeeksforGeeks)

🔗 [Problem Link](https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange) ![Language](https://img.shields.io/badge/Language-Python-blue)

### 💡 Tags
Tree

### 🚀 Performance
- **Runtime:** Successfully Evaluated
- **Memory:** N/A

---

### 📜 Problem Description

You are given the  **root**  of a binary tree, and your task is to return its  **bottom view** . The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.

**Note:** If there are  **multiple** bottom-most nodes for a horizontal distance from the root, then the  **latter** one in the level order traversal is considered.

**Examples :**

```
Input: root = [1, 2, 3, 4, 5, N, 6]
    
Output: [4, 2, 5, 3, 6]
Explanation: The Green nodes represent the bottom view of below binary tree.
    

```

```
Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
    
Output: [5, 10, 4, 28, 25]
Explanation: The Green nodes represent the bottom view of below binary tree.
    
```

**Constraints:** 
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105