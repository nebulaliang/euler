1. A sample of the output
   See the running result of problem42.py

2. Why you chose the problem?
   This problem is more like daily work: parsing file, transforming information, get required result.
 
3. A description of the process to solve the problem
   Initially, I tried to load all the words in memory and build a list to store the triangle numbers. However, I have no idea hong big the list should be. It actually depends on the length of the word. Suppose we have word with long string, we can not estimate the length of list.
   Therefore, I used two strategies to solve this problem for further using:
   1. Not use list to store triangle number. Just use a function to check whether given number is triangle number. The function takes very little time and we can save memory.
   2. Not load all words in memory and since the file doesn't contain lines. I read the file character by character and get the words. If the file will be large in the future, this method would be helpful to save memory.

4. What reference sources used
   http://www.mathblog.dk/project-euler-solutions/
   http://www.s-anand.net/euler.html
   http://code.jasonbhill.com/project-euler/

5. How much time I spend on the exercise?
   3 hours