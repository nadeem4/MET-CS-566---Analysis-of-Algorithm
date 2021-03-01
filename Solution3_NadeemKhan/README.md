# Assignment 3

## Course: MET CS 566 - Analysis of Algorithm

- **BU ID:** _U03225602_
- **Name:** _Nadeem Khan_
- **Solution File:** _[assignment3_nadeem_khan.py](assignment3_nadeem_khan.py)_

## Questions 1: To sort or not to sort. Outline a reasonable method of solving each of following problems. Give the order of the worst-case complexity of your methods

### You are given a pile of thousands of telephone bills and thousands of checks sent in to pay the bills. Assume telephone numbers are on the checks. Find out who didn’t pay

_In this function, we will assume that tel_bills is an Array of Dictionary._

```json
[
  {
    "customer_id": "1",
    "tel_number": "+1 765 165 1654"
  },
  {
    "customer_id": "2",
    "tel_number": "+1 365 165 1654"
  }
]
```

_We will convert the Array of Dictionary to a flat dictionary i.e., tel_number as key and customer_id as value. After conversion it will look like:_

```json
{
  "+1 365 165 1654": "1",
  "+1 765 165 1654": "2"
}
```

_Similarly checks is also an Array of dictionary and this dictionary also has tel_number as one of the key._

```json
[
  {
    "check_number": "1111111111",
    "tel_number": "+1 765 165 1654"
  },
  {
    "check_number": "21223567654",
    "tel_number": "+1 365 165 1654"
  }
]
```

_In order to find who did not paid, we will find who paid bills and then we will subtract from total customer._

*Converting Array of dictionary to flat dictionary takes O(n), and then looping over checks will also take O(n) in worst case, since we are only using 1 for loop.*

**Worst-Case Time Complexity:** O(n)

<br>

<hr>

<br>

### You are given an array in which entry contains the title, author, call number, and publisher of all books in a school library and another array of 30 publishers. Find out how many of the books where published by each of those 30 companies

_In this books are an array of dictionary having title, cell number, author and publisher as keys._

```json
[
  {
    "title": "ABC",
    "author": "XYZ",
    "publisher": "PQR"
  },
  {
    "title": "q23",
    "author": "sdr",
    "publisher": "PQR"
  },
  {
    "title": "wse",
    "author": "23ed",
    "publisher": "RST"
  },
  {
    "title": "QAW",
    "author": "SED",
    "publisher": "MNO"
  }
]
```

_Publishers is an array._

```json
["PQR", "RST", "MNO", "QAW", "OIU"]
```

_We will convert the array of dictionary of books to flat dictionary have publisher as key and title as value._

*We are only looping once on array of books to find out the count of published books by publishers.*

**Worst-Case Time Complexity:** O(n)

<br>

<hr>

<br>

### You are given an array containing checkout records of all books checked out of the campus library during the past year. Determine how many distinct people check out at least one book

*In this function, we will assume that books is an Array of dictionary having email, name, book_name as keys.*

```json
[
  {
    "title": "ABC",
    "author": "XYZ",
    "email": "xyz@gmail.com"
  },
  {
    "title": "q23",
    "author": "sdr",
    "email": "pqr@gmail.com"
  },
  {
    "title": "wse",
    "author": "23ed",
    "email": "pwr@gmail.com"
  },
  {
    "title": "QAW",
    "author": "SED",
    "email": "pwr@gmail.com"
  }
]
```

*We are only looping once on array of books to find out the count of books read by any person.*

**Worst-Case Time Complexity:** O(n)