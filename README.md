# OpTC Data Analysis Challenge

Included in this repository is a sample set of data from the
[OpTC Data Release](https://github.com/FiveDirections/OpTC-data). The data
in `data.json` is a small snippet of host-based eCAR data.

## Objectives

Answer the following questions based on the data provided in `data.json`:
1. How many unique `"action"` values are there?
2. List the number of occurrences of each `"action"` value in the sample data.
3. Give a breakdown on how many `"src_ip"`s are IPv4 vs IPv6. (Hint: you may
   need to also keep track of cases where this does not apply for cases of
   missing or invalid data)
4. How many records are there with the `"dest_ip"` in the 224.0.0.0/8 subnet.

Answers should be printed to standard output when running your solution program.
Be sure each question response is clearly labeled.

**Optional Bonus**

Create a dockerized API that will provide answers the 4 questions above. 
Provide a Dockerfile, and scripts to build and run the image. The API
should accept requests as follows (port numbers can vary), where the endpoint
maps to the objective above:

```
GET:
http://localhost:8000/1

GET:
http://localhost:8000/2

GET:
http://localhost:8000/3

GET:
http://localhost:8000/4
```

The responses for each of these calls should contain the answer of the objective.
For example, `http://localhost:8000/1` should return the number of unique `"action"`
values in the data.
JSON formatted output is recommended, but any reasonable output will be accepted.

Be sure to document how to build and run the API. It can be assumed that the
API will only be reached from `localhost`

## Submission

Fork this repository for your own work, and submit a GitHub Pull Request (PR)
to this repository containing your solution.
The solution PR should consist of the following:

1. Source code containing the solution
2. A build/install script, if necessary, to install dependencies, compile,
   or package the solution. Give instructions in this `README.md` file
   to include installation steps (even if it is just the execution of a
   provided script).
3. Additional documentation, included in the "Execution" section of this
   `README.md` file, to specify exactly how the solution should be
   executed. For the instructions, assume your starting location is the root
   directory of this repository.

## Solution

### Installation

1) Run the following command: 'python3 setup.py install --user'

### Execution

1) Run the following command: 'python3 eCar.py'