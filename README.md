
# Maximum Spatial Service Overlap

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

3. *NumPy* is the only prerequisite library to execute our main python algorithm. We can do it, installing the content of our *requirements.txt* file

```bash
pip install -r requirements.txt
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If, for any reason, we face some kind of problem, we can simply type:

```bash
pip install numpy==1.21.4
```

4. For the *unit testing* part we will also need to install *pytest on your work environment. Similarily, we can do it, installing the content of our *tests/testing_requirements.txt* file
```bash
pip install -r tests/testing_requirements.txt
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If, for any reason, we face some kind of problem, we can simply type:

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

The last two contain respectively the helper functions to load the data via the standard input and perform the elementary processes of the *get_max_pizza_overlap()* function, the unique function of the *main.py*. 

All we need to do is to execute *main.py* file feeding them with a txt file as standard input, i.e.:

```python
python main.py < input_sample.txt
```

In order to be able to be processed by our algorith, and in accordance with our instructions the input we use have to be of the following form:

The first line of the standard input contains the two numbers ​**N** and **​M**​, and both numbers are
on the interval [1, 1000]. The number **​N** represents the dimension of the city in blocks (the
city has N​x​N blocks). ​**M** is the number of pizzerias in the city. The following ​M lines contain
information about each pizzeria, given by the three numbers **​X**​, **​Y**​, **​K**​. The numbers **​X** and **​Y** represent the block where the pizzeria is located, (1 <= **​X**​, **​Y** <= ​N​) and the number **​K**
represents the maximum distance that the given pizzeria's delivery guy will travel to deliver
pizza (1 <= **​K** <= 1000). 

i.e

2 5
3 3 2
1 1 2

As we can see, in accordance with the demo example given to us, when the input is 2 pizzerias for a square town of 5-blocks side, where the first pizzeria is located in the (3, 3) cartesian block, the second one in the (1, 1) cartesian block and both have a delivery radius of 2 blocks, the maximum we're looking for, i.e. the maximum number of pizzerias that can cover the same block is 2.

### Unit Testing

For the unit testing, all we need to do is to execute the following command:
```python
pytest -k 'not slow'
```
That way, we will have run the 73 out of 74 unit tests that we have designed.
These ones deal with successful common and edge cases as well as unsuccessful cases due to TypeErrors, ValueErrors or exception errors due to disrespect of the problem's input limits (i.e. M, N, X, Y, K ∈ [1, 1000]).

The 26th test (*test_main_stress()* in *tests/test_main.py* file) is essentially a ***stress test*** that calls the execution of our main function for a the edge case input of N, M = 1000 and X, Y, K ∈ [1, 1000]. In this sense, due to its very nature — even though it supports/proves the very functionality of our solution — it's much more time- and resources-consuming compared to the rest and we should be more careful with its execution. In order to run this one, we should just omit the keyword expression, i.e.
```python
pytest
```

### AWS solution deployment
We choose to deploy our solution via AWS Lambda, a serverless, event-driven, only-pay-for-what-you-use compute service that lets us run code for virtually any type of application or backend service without provisioning or managing servers.

(*In order to get started with Serverless Framework’s AWS, we should first install it with NPM, so in case we don’t already have [Node](#https://nodejs.org/en/download/package-manager/) on our machine, we should install it first;  it is recommended by the service to use the latest LTS version of NodeJS*)

So, let's install the serverless CLI via NPM:
```
npm install -g serverless
```
The *sls deploy* command deploys our entire service via CloudFormation. But to do so, we have first to go to the *aws/* directory 
```
cd aws
serverless deploy
```
In order now to post a request to our API we should run:
```
curl -X POST [options] [URL]
```
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "linuxize", "email": "linuxize@example.com"}' \
    https://example/contact
```

You can post a json file with curl like so:

```
curl -X POST -H "Content-Type: application/json" -d @FILENAME DESTINATION
```
so for example:

```
curl -X POST -H "Content-Type: application/json" -d @../data/cats.json http://localhost:8080/mSfvMwNAfj
```
The *sls remove* command will remove the deployed service
```
serverless remove
```
serverless deploy
serverless remove
change top level


## Roadmap
The target of our project has been to deliver an algorithm to get the maximum pizza delivery cover overlap, and we did it. But where it is located? And wouldn't it be useful along the way of our algorithm's calculations to maintain some of the info that a functional/procedural solution, despite its straightforwardness and intuitiveness, cannot but let it go? Modeling Z-town's world and info implementing an object-oriented class-based solution would definitely be useful for future projects in the course of Z-town's original and brave endeavour for pizza relegalisation. This is why in the *draft/* folder we have saved a solution approach (*main_object-oriented.py*) that we didn't finally consider as the most appropriate (less straightforward and to-the-point). 

Finally, in the *draft/* folder we have saved a non-perfected algorithm that would computationally approximate the order of complexity of our solution (*order_comput_calcul.py*).
