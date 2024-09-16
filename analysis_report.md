Provide a rigorous analysis of the average-case time complexity of Randomized Quicksort.
- Clearly explain why the average-case time complexity is \(O(n \log n)\).
- Use concepts such as indicator random variables or recurrence relations in your analysis to demonstrate your understanding.
As in the average case of the randomized quicksort, we choose an element which is evenly balanced and recursion divides the array into two equal parts. the recursion depth will be O(logn), as the problem size reduces by approximately half at each step.
Let T(n) be the expected running time of Randomized Quicksort on an input of size nnn.
T(n)=T(k)+T(n−k−1)+O(n)
kkk is the number of elements in one partition,
Since we are making k as random, average value of k is n/2 so,
T(n)=2T(2n)+O(n)
According to master theorem: T(n)=O(nlogn)

Analyze the expected search, insert, and delete times under the assumption of simple uniform hashing.
As the name suggests, with uniform hashing, hash function distributes keys uniformly across the hash table’s buckets. 
Search
-	In a hash table with uniform hashing, searching involves:
-	Computing the hash of the key, which is O(1) in average time.
Insert
-	Compute the hash of the key, which is O(1)
-	On average, this list has x keys, so insertion time involves traversing the list up to x elements in the worst case
Delete
-	Compute the hash of the key, which is O(1).
-	Find the key in the appropriate bucket (x elements traversing)
-	Remove the key from the linked list O(1)

- Explain how the load factor (the ratio of the number of elements to the number of slots) affects the performance of these operations.
Search (
-	Low Load)
o	With a low load factor, there are many more buckets than elements. This leads to shorter chains, therefore having constant runtime
-	High load =1, >1
o	Number of elements closer to exceeds number of buckets. In this case, more collisions, longer time. 
Insert
-	Low load 
o	a low load factor typically means that the element will be placed in a bucket with few other elements
o	Constant time
-	High Load
o	inserting an element means adding it to a bucket that may already contain many elements. This could involve traversing a longer chain to insert the new element correctly.
o	Higher time as we need to traverse
Delete
-	Low load
o	low load factor generally involves finding and removing an element from a short chain.
o	Constant time
-	High load
o	Deleting an element from a hash table with a high load factor involves locating the element in a potentially long chain and then removing it.
o	Time complexity would increase to be able to traverse the chain

Discuss strategies for maintaining a low load factor and minimizing collisions, including dynamic resizing of the hash table.
First possible strategy is dynamic resizing. 
-	This involves threshold-based resizing, resize the hash table with a predefined threshold 
-	As soon as this threshold is reached, the number of buckets can be increased by doubling it. This also reduces the load factor. 
Another possible strategy is effective hash function
We chose to do a hash function based on a prime number. 
In this case, we can choose a function with good statistical properties. For example, a cryptographic hash function such as SHA-256. 
