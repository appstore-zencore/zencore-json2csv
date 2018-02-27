zencore-json2csv
================

Convert json data to csv data.


Example 1
---------

**INPUT:**

::

    [
        [1,2,3],
        [2,3,4]
    ]

**OUTPUT:**

::

    1,2,3
    2,3,4

**COMMAND:**

::

    cat input.txt | json2csv -o output.txt

Example 2
---------

**INPUT:**

::

    [
        {"f1": 11, "f2": 12, "f3": 13},
        {"f1": 21, "f3": 23, "f2": 22}
    ]

**OUTPUT:**

::

    11,12,13
    21,22,23

**COMMAND:**

::

    cat input.txt | json2csv -o output.txt -k f1,f2,f3

Example 3
---------
**INPUT:**

::

    {
        "data": {
            "list": [
                [1,2,3],
                [2,3,4],
            ]
        }
    }

**OUTPUT:**

::

    1,2,3
    2,3,4

**COMMAND:**

::

    cat input.txt | json2csv -o output.txt -p data.list
