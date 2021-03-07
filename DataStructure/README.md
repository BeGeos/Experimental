# Binary Search Trees and AVL

A follow up of the MIT lessons at 6.006 "Algorithm and Data Structures".

### BSTs
A binary search tree is a tree with specific conditions:
* The left node is smaller than the root node, and the right node is greater than the root node;
* It's binary, so there are only 2 nodes for every given node. Nodes without left or right nodes are leaves;

For the insertion I opted for a recursive method and I also implemented an *is_available()* method to be used as a checker for 
other conditions. Since this type of data structure is specifically aimed to this kind of tasks, namely insertion under specific conditions.

One of these conditions is there cannot be 2 nodes with the same key, or value. Similar to a set. 

In the class, the following methods are provided and fully functional:
* *insert()*  : During the insertion in the tree there will be a check to the following conditions:
    * there is no other node with the same value;
    * the value is without a constant value k to all the other values;
* *search()*  : Search through the nodes for a specific value;
* *minimum()*  : Return the minimum value in the tree;
* *maximum()*  : Return the maximum value in the tree.

All these methods return an object of type *Node*. 
A node has attributes: 
* **key**: indicates the value of the node;
* **parent**: indicates the parent node; 
* **height**: the steps for insertion;
* **left**: indicates the left child;
* **right**: indicates the right child.

###AVLs
This type of tree inherits from the BST, therefore is binary and follows the same rule for insertion.
In this case, the method are the aforementioned from the BST class as well as:
* *avl_insert()*  : It differs from *insert()* because it keeps track of the steps of each node to be inserted, 
in order to compute the height of a particular node;
* *height()*  : It is a method and returns the height of a node.

Both of these classes build a tree that has the *root* attribute. The value of the root's height in the AVL class
is simply stored in the **root.height** attribute. 

The main difference between BSTs and AVLs is the fact that BSTs can be unbalanced, which means the complexity for 
insert operation as well as search and delete is not *O(lg(n))* but could be *O(n)*. 

AVLs maintain the balance through an additional rule:
* The difference between the left child's and the right child's height must not be greater than 1. If such 
condition were to happen the tree has to be fixed.

This *fix()* method hasn't been implemented, yet. 

### TODO
* Implement the *fix()* method in AVLs with rotation;
* *Delete()* method to remove nodes fro tree;
* Add docstrings to methods.