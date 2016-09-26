## Overview
The point of this repository is to outline and store common data structures and sorting algorithms.
Of course these are readily available for anyone to use, though these are very basic implementations
written in python. These are solely for educational purposes. 

## Datastructures

#### Average Scenario
| Data Structure | Access | Search | Insertion | Deletion | 
| ---: | :---: | :---: | :---: | :---: |
| [Array](#array) | `O(1)` | `O(n)` | `O(n)` | `O(n)` | 
| [Linked List](#llist) | `O(n)` | `O(n)` | `O(1)` | `O(1)` |
| [BST](#bst) | `O(log(n))` | `O(log(n))` | `O(log(n))` | `O(log(n))` |
| [Heap](#heap) | `O(log n)` | `O(1)` | `O(log n)` | `O(n)` | `O(n)` |
| [Hash Table](#hash) | `N/A` | `O(1)` | `O(1)` | `O(1)` |
| [Stack](#stack) | `O(1)` | `O(n)` | `O(1)` | `O(1)` |
| [Queue](#queue) | `O(n)` | `O(n)` | `O(1)` | `O(1)` |
| [Trie](#trie) | `O(m)` | `O(m)` | `O(m)` | `O()` |
| [Graph](#graph) | `O()` | `O()` | `O()` | `O()` |

#### Worst Case Scenario
| Data Structure | Access | Search | Insertion | Deletion | Space |
| ---: | :---: | :---: | :---: | :---: | :---: |
| [Array](#array) | `O(1)` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |
| [Linked List](#llist) | `O(n)` | `O(n)` | `O(1)` | `O(1)` | `O(n)` |
| [BST](#bst) | `O(n)` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |
| [Heap](#heap) | `O(log n)` | `O(1)` | `O(log n)` | `O(n)` | `O(n)` |
| [Hash Table](#hash) | `N/A` | `O(n)` | `O(n)` | `O(n)` | `O(n)` |
| [Stack](#stack) | `O(1)` | `O(n)` | `O(1)` | `O(1)` | `O(n)` |
| [Queue](#queue) | `O(n)` | `O(n)` | `O(1)` | `O(1)` | `O(n)` |
| [Trie](#trie) | `O(m)` | `O(m)` | `O(n*m)` | `O(m)` | `O(n+m)` |
| [Graph](#graph) | `O()` | `O()` | `O()` | `O()` | `O(n)` |


**<a name="trie"></a>Trie**

A trie is a tree like data structure, in which the leafs for a given node fan out wide. 
This creates short trees that are very wide. Tries are great data structures for performance
driven applications wherein you need to lookup data from a given set, this is due to the fact
that the complexity for searching is related directly to the number of characters in the word
being looked up. The worst case for insertion is n*m*c or `nodes * keySize * characterSetSize`  

A depth-first strategy is implemented until the desired depth is reached.
 
 

## Sorting
These are just a few of many sorting algorithms - below you will find the algo and the space
and time complexity as well as the average case and worst case scenario run complexities

| Algo             | Time Complexity | Time Complexity | Space Complexity |
| ---: | :---:           | :---:           | :---:            |
|                  | **Average**     | **Worst**       | **Worst**        |
| [Radix](#radix)  | `O(nk)`       |`O(nk)`          |`O(n+k)`|
| [Bucket](#bucket) | `O(nk)`       |`O(nk)`          |`O(n+k)`|
| [Quick](#quick)  | `O(n log(n))` |`O(n^2)`         |`O(log(n))`|
| [Bubble](#bubble) | `O(n^2)`      |`O(n^2)`         |`O(1)`|
| [Merge](#merge)  | `O(n log(n))` |`O(n log(n))`    |`O(n)`|


**<a name="radix"></a>Radix Sort**

**<a name="bucket"></a>Bucket Sort**

**<a name="quick"></a>Quick Sort**

**<a name="bubble"></a>Bubble Sort**

**<a name="merge"></a>Merge Sort**


## Searching

**Depth-First-Search DFS**

Depth first searches are a means for searching graphs / matrices / trees by means of searching all 
connected vertices downwards and traversing back up before moving to a neighbor node. Typically
starting at the root; however, it can be done from any particular node (search node). 

```
     A
   B   C
 D    E  F
 
A DFS Search would return A, B, D, C, E, F
```

Particularly a DFS does its work with a `stack`, as you would grab the root A, and push the child
nodes onto the stack. then recursively call the work on B (LIFO - last in first out) and traverse 
down the tree until all nodes had traversed before returning to C and continuing so and so forth. 



**Breadth-First-Search BFS**

Conversely the Breadth first searches all neighbor nodes (starting from the root node or a provided
search node) across a tree before traversing down a level.
  
```
     A
   B   C
 D    E  F
 
A DFS Search would return A, B, C, D, E, F
```

A BFS performs its work with a `queue` wherein the data is processed FIFO (first in first out). 
Wherein we push the children nodes of A into the queue and process them before continuing to 
any subsequent children found. 

**DFS vs. BFS**

Using one vs the other depends greatly on the structure of the data stored in the tree or graph. 


Typically DFS is favored against shorter wider trees, where BFS is favored against taller narrower
trees.  Additionally if memory is a concern the DFS search does not require a separate data structure
to store the visited nodes when written recursively. 