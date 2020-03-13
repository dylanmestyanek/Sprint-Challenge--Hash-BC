## Interview Questions

Explain in detail the workings of a dynamic array:

**Answer:** A dynamic array is a way to store data of the same type in a "list" format. These values positions are referenced in the computer's memory by their index in the array, which points to a specific block of memory.

* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

**Answer:** 
- **Accessing Array:** The runtime complexity to access an array at an index is Constant or O(1). This is due to the fact that accessing an index refers to a specific block of the computer's memory, which is an extremely fast operation. 
- **Add/Remove From Front:** The runtime complexity of adding/removing items from the front of an array is Linear or O(n). This is due to the fact that when inserting a new item in the array, all bits of memory need to be transferred one by one. For example, in an array of 16 bytes, adding another 4 byte element would require the system to request an entirely new block of memory that is 20 bytes in size to accommodate for the new value being added. The copying of these values 1 by 1 is what causes the Linear runtime. 
- **Add/Remove From Back:** - The runtime complexity of adding/removing items from the back of an array is best case Constant or O(1). 

* What is the worse case scenario if you try to extend the storage size of a dynamic array?
**Answer:** The worst case scenario of extending the storage size of a dynamic array would be Linear or O(n). This is due to the fact that if there is not any reserved memory on the end of the array, then an entirely new block of memory needs to be requested, which need to be the size of the old array, plus the size of the value being added. Copying these values over 1 by 1 causes this process to have a Linear runtime. 

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

## Dynamic Arrays
