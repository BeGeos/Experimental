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
* *maximum()*  : Return the maximum value in the tree;

All these methods (apart from *_height()*) return an object of type *Node*. 
A node has attributes: 
* **key**: indicates the value of the node;
* **parent**: indicates the parent node; 
* **height**: the steps for insertion;
    * ***UPDATE (9/03)*** : the height is no more an attribute of the node.
    Since the height is a dynamic attribute it would be extremely inefficient
     to try and keep track of it. Instead, I have implemented a new method in the BST
      class, namely *_height()* which recursively yields the height of a node, as integer;
* **left**: indicates the left child;
* **right**: indicates the right child.

### AVLs
This type of tree inherits from the BST, therefore is binary and follows the same rule for insertion.
In this case, the method are the aforementioned from the BST class as well as:
* *avl_insert()*  : It differs from *insert()* because it keeps track of the steps of each node to be inserted, 
in order to compute the height of a particular node;
* *height()*  : It is a method and returns the height of a node.

Both of these classes build a tree that has a **root** attribute. 

The main difference between BSTs and AVLs is the fact that BSTs can be unbalanced, which means the complexity for 
insert operation as well as search and delete is not *O(lg(n))* but could be *O(n)*. 

AVLs maintain the balance through an additional rule:
* The difference between the left child's and the right child's height must not be greater than 1. If such 
condition were to happen the tree has to be fixed.

This *fix()* method hasn't been implemented, yet. 

##### Recent Additions:
* *_height()*  :  Return the height of an object of class Node, as integer. 
It recursively calculate the height which is defined as the longest path from 
a given node A to a leaf. In addition, the BST object has the **height** attribute
 which indicates the height of the root;
*  the entire class has been remodeled as inheritance of the BST class, therefore 
all the previous methods have been included from it;
* A new method has been added:
    * *is_balanced()*  :  It executes a rapid check based on the height of every given 
    node. In this case, balanced indicates that the difference between the right and left nodes' height 
    must not be greater than 1;
* also a **height** attribute has been added to the classes. 
Read above to know more about it.

### TODO
* Implement the *fix()* method in AVLs with rotation;
* *Delete()* method to remove nodes from tree;
* Add docstrings to methods.