
# Maximum Spatial Service Overlap (part of the Pizza Relegalisation Road Map)

This is a Python implementation — part of the wider API project who seeks to help the mayor of Z-city, a great pizza lover — to find the city's block where he can have the greatest selection of pizzas. After the recent relegalisation of pizza production and sale and the explosive growth of new pizzerias, **the ***Maximum Spatial Service Overlap*** algorithm's goal is to calculate that maximum amount of pizzerias' service cover overlap**. 

## Table of contents
* [Requirements](#requirements)
* [Usage](#usage)
  - [Algorithm](#algorithm)
  - [Unit Testing](#unit-testing)
  - [AWS solution deployment](#aws-solution-deployment)
* [Roadmap](#roadmap)

## Requirements

1. To implement our solution, your machine should have installed any Python 3.x version
Prerequisite libraries

1. Clone the repo
```bash
git clone https://github.com/gtsa/Maximum_Spatial_Service_Overlap---Python-AWS-
```

3. *NumPy* is the only prerequisite library to execute our main python algorithm. You can do it, installing the content of our *requirements.txt* file

```bash
pip install -r requirements.txt
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If, for any reason, you face some kind of problem

```bash
pip install numpy==1.21.4
```

4. For the *unit testing* part you will also need to install *pytest on your work environment. Similarily, you can do it, installing the content of our *tests/testing_requirements.txt* file
```bash
pip install -r tests/testing_requirements.txt
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If, for any reason, you face some kind of problem

```bash
pip install numpy==1.21.4
pip install pytest==6.2.5
```

## Usage

### Algorithm

Our solution, which is developed with a functional approach (see [Roadmap](#roadmap)), consists of the three .py files:
- main.py
- load_data.py
- functions.py

The last two contain respectively the helper functions to load the data via the console input and perform the elementary processes of the *get_max_pizza_overlap()* function, the unique function of the *main.py*. 

All you need to do is to execute *main.py* file:

```python
python main.py
```
and load your data as in the following example (\**due to the fact, that we haven't used a prompt input message — so as to end up with an output format closer to the demo example given to us — you should take care of the fact that the console will wait for your input directly after hitting ENTER*):

```
python main.py
2 5
3 3 2
1 1 2
2
```

As we can see, in accordance with the demo example given to us, when the input is 2 pizzerias for a square town of 5-blocks side, where the first pizzeria is located in the (3, 3) cartesian block, the second one in the (1, 1) cartesian block and both have a delivery radius of 2 blocks, the maximum we're looking for, i.e. the maximum number of pizzerias that can cover the same block is 2.

### Unit Testing

For the unit testing, all we need to do is to execute the following command:
```python
pytest -k 'not slow'
```
That way, we will have run the 25 out of 26 unit tests that we have designed (80 out of 81 test inputs).
These ones deal with successful common and edge cases as well as unsuccessful cases due to TypeErrors, ValueErrors or exception errors due to disrespect of the problem's input delimitations (i.e. M, N, X, Y, K ∈ [1, 1000]).

The 26th test (*test_main_stress()* in *tests/test_main.py* file) is essentially a ***stress test*** that calls the execution of our main function for a the edge case input of N, M = 1000 and X, Y, K ∈ [1, 1000]. In this sense, due to its very nature — even though it supports/proves the very functionality of our solution — it's much more time- and resources-consuming compared to the rest and we should be more careful with its execution. In order to run this one, we should just omit the keyword expression, i.e.
```python
pytest
```

### AWS solution deployment

## Roadmap
The target of our project has been to deliver an algorithm to get the maximum pizza delivery cover overlap, and we did it. But where it is located? And wouldn't it be useful along the way of our algorithm's calculations to maintain some of the info that a functional solution, despite its straightforwardness, cannot but let it go? Modeling Z-town's world and info implementing an object-oriented class-based solution would definitely be useful for future projects in the course of Z-town's original and brave endeavour for pizza relegalisation. This is why in the *draft/* folder we have saved a solution approach (*main_obj_orient.py*) that we didn't finally consider as the most appropriate (less straightforward and to-the-point). 

For what it's worth, and a bit ironically, we have also saved in the same folder a one-function solution (*main_one_func.py*).

Finally, in the *draft/* folder we have saved a non-perfected algorithm that would computationally approximate the order of complexity of our solution (*order_comput_calcul.py*).
