# Assignment 2

## Course: MET CS 566 - Analysis of Algorithm.

- **BU ID:** _U03225602_
- **Name:** _Nadeem Khan_
- **Solution File:** _[assignment2_nadeem_khan.py](assignment2_nadeem_khan.py)_

### 1. _Write an algorithm for Maxsort assuming an array E contains n elements to be sorted, with indexes 0, 1, …, n-1._

_Check out the solution in [assignment2_nadeem_khan.py](assignment2_nadeem_khan.py)_

### 2. How many comparisons of keys does Maxsort do in the worst case and on average?

**On worst case:**

Algorithm will comparison only for finding maximum element, and in worst case element to matched is the last element, so it will perform n matching for every element.

Therefore,

| **Array** | **Operation** |
| --------- | ------------- |
| **n**     | n             |
| **n - 1** | n – 1         |
|           |               |
| **1**     | 1             |

**_Hence total comparison, 1 + 2 + 3 + 4 + … + n-1 + n = n (n + 1) / 2_**

On average case:

Algorithm will comparison only for finding maximum element, and in average case element to matched is the middle element, so it will perform n/2 matching for every element.

Therefore,

| **Array** | **Operation** |
| --------- | ------------- |
| **n**     | n / 2         |
| **n - 1** | n – 1 / 2     |
|           |               |
| **1**     | 1 / 2         |

__*Hence total comparison, 1/ 2 + 2 / 2 + 3 / 2 + 4 / 2 + … + n-1 / 2 + n / 2 = n (n + 1) / 4*__
