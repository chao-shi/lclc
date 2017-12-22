Q: What if negative numbers are allowed in the given array?
   How does it change the problem?

A: The total number will be infinite. For example, numbers have both -1 and 1
   Even though it has p and -q, we need q instance of p and p instance of -q to make zero,
   the answer is still infite.

Q: What limitation we need to add to the question to allow negative numbers?

A: The array length should be bounded

Q: How to solve it

A: better use recursion with memory table

