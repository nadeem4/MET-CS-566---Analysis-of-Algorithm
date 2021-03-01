# Course: MET CS 566 A2 - Analysis of Algorithm
# BU ID: U03225602
# Name: Nadeem Khan

"""
In this function, we will assume that tel_bills is an Array of Dictionary.
[
{
 customer_id: "1",
 tel_number: "+1 765 165 1654",
 ...
},
{
 customer_id: "2",
 tel_number: "+1 365 165 1654",
 ...
},
...
]

We will convert the Array of Dictionary to a flat dictionary i.e., tel_number as key and customer_id as value.
After conversion it will look like:
{
"+1 365 165 1654" : "1",
"+1 765 165 1654" : "2"
}

Similarly checks is also an Array of dictionary and this dictionary also has tel_number as one of the key.
[
{
 check_number: "1111111111",
 tel_number: "+1 765 165 1654",
 ...
},
{
 check_number: "21223567654",
 tel_number: "+1 365 165 1654",
 ...
},
...
]

In order to find who did not paid, we will find who paid bills and then we will subtract from total customer.

"""


def find_who_did_not_pay_bills(tel_bills, checks):
    cnt_of_customer_who_did_not_paid = 0

    # this will convert the array of dictionary to a flat dictionary
    tel_dict = dict()
    for tel_bill in tel_bills:
        tel_dict[tel_bill['tel_number']] = tel_bill['customer_id']

    # Here we will check if bill has been paid or not.
    for check in checks:
        if check['tel_number'] not in tel_dict:
            cnt_of_customer_who_did_not_paid += 1

    return cnt_of_customer_who_did_not_paid


"""
In this books are an array of dictionary having title, cell number, author and publisher as keys.
Publishers is an array.

We will convert the array of dictionary of books to flat dictionary have publisher as key and title as value.
"""


def find_number_of_book_published_by_publisher(published_books, publishers_1):
    cnt_dict_of_book_published_by_publisher = dict()

    # this will set the cnt of each publisher as 0
    for publisher in publishers_1:
        cnt_dict_of_book_published_by_publisher[publisher] = 0

    for book in published_books:
        # here we will check if publisher has published any book or not and then we will check if have counted that book
        # or not
        if book['publisher'] in cnt_dict_of_book_published_by_publisher:
            cnt_dict_of_book_published_by_publisher[book['publisher']] += 1

    return cnt_dict_of_book_published_by_publisher


"""
In this function, we will assume that books is an Array of dictionary having email, name, book_name as keys.
"""


def find_out_how_many_people_read_at_least_one_book(checked_books):
    people_dict = dict()

    """
    In this we will add person's email to people_dict every time we find a record of that email, then we will find the 
    total number of keys in order to find the number of people who read at least one book
    """
    for book in checked_books:
        if book['email'] in people_dict:
            people_dict[book['email']] += 1
        else:
            people_dict[book['email']] = 1

    return len(people_dict.keys())


if __name__ == '__main__':
    """
    You are given a pile of thousands of telephone bills and thousands of checks sent in to pay the bills.
    Assume telephone numbers are on the checks. Find out who didn’t pay.
    """
    tel_bills = [
        {
            "customer_id": "12345",
            "tel_number": "+1 765 154 5142"
        },
        {
            "customer_id": "12345",
            "tel_number": "+1 765 134 5142"
        },
        {
            "customer_id": "12345",
            "tel_number": "+1 765 164 5142"
        }
    ]
    checks = [
        {
            "check_number": "1234590",
            "tel_number": "+1 765 154 5142"
        },
        {
            "check_number": "1234590",
            "tel_number": "+1 465 154 5142"
        },
        {
            "check_number": "1234590",
            "tel_number": "+1 865 154 5142"
        }
    ]
    cnt_of_cust_who_did_not_paid = find_who_did_not_pay_bills(tel_bills, checks)
    print("Count of customer who did not paid phone bills:", cnt_of_cust_who_did_not_paid)

    """
    You are given an array in which entry contains the title, author, call number, and publisher of all books in a 
    school library and another array of 30 publishers. Find out how many of the books where published by each of those 
    30 companies.
    """

    books = [
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
    publishers = ["PQR", "RST", "MNO", "QAW", "OIU"]
    cnt_of_book_published_by_publisher = find_number_of_book_published_by_publisher(books, publishers)
    print("Count of books published by each publishers:", cnt_of_book_published_by_publisher)

    """
    You are given an array containing checkout records of all books checked out of the campus 
    library during the past year. Determine how many distinct people check out at least one book
    """

    checked_out_books = [
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
    cnt_of_distinct_people_who_read_at_least_one_book = find_out_how_many_people_read_at_least_one_book(
        checked_out_books)
    print("Count of distinct people who read at least one book: ", cnt_of_distinct_people_who_read_at_least_one_book)
