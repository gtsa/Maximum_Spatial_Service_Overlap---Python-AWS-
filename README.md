
# Maximum Spatial Service Overlap

This is a Python implementation — part of the wider API project who seeks to help the mayor of Z-city, a great pizza lover — to find the city's block where he can have the greatest selection of pizzas. After the recent relegalisation of pizza production and sale and the explosive growth of new pizzerias, **the ***Maximum Spatial Service Overlap*** algorithm's goal is to calculate that maximum amount of pizzerias' service cover overlap**. 

## Table of contents
* [Requirements](#requirements)
* [Usage](#usage)
  * [Algorithm](#algorithm)
  * [Unit Testing](#unit-testing)
  * [AWS solution deployment](#aws-solution-deployment)
    * [How to use](#how-to-use)
    * [How to deploy](#how-to-deploy)
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

4. For the *unit testing* part we will also need to install *pytest on your work environment. Similarly, we can do it, installing the content of our *tests/testing_requirements.txt* file
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

In order to be able to be processed by our algorithm, and in accordance with our instructions the input we use have to be of the following form:

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

The 26th test (*test_main_stress()* in *tests/test_main.py* file) is essentially a ***stress test*** that calls the execution of our main function for a the edge case input of N, M = 1000 and X, Y, K ∈ [1, 1000]. In this sense, due to its very nature — even though it supports/proves the very functionality of our solution — it's much more time- and resource-consuming compared to the rest and we should be more careful with its execution. In order to run this one, we should just omit the keyword expression, i.e.
```python
pytest
```

### AWS solution

#### How to use

We choose to deploy our solution via AWS Lambda, a serverless, event-driven, only-pay-for-what-you-use AWS compute service that lets us run code without provisioning or managing servers. Lambda automatically runs our code, and automatically as well scales our application by running code in response to each trigger. Our code runs in parallel and processes each triggers individually scaling precisely with the size of the workload while we are charged only for the amount of time that our code is running.

The only change we made was the assumption that the .json (and no longer .txt) file which we will use as input data will not any more contain the number M of pizzerias. Adding another API that would convert the same .txt files used as input for the local solution in json format and feed our API by automating and simplifying pipelines would be a good immediate next step.

In each case the API that we deploy is called *max_pizza_overlap*,  via a *POST* request it accepts as data input two variables  N and P, equal to [[X_1, Y_1, K_1], ..., [X_M, Y_M, K_M]], while its public endpoint is at: ***https://d4bhu5x3ag.execute-api.eu-west-2.amazonaws.com/dev/api/max_pizza_overlap***

In order now to send a POST request to our API with some json input, the simplest way is via *cURL*.  So, for either inline or a file json data, we should run something like so:


```
curl -X POST \
     -H "Content-Type: application/json" \
     -d  json inline \
     https://d4bhu5x3ag.execute-api.eu-west-2.amazonaws.com/dev/api/max_pizza_overlap

curl -X POST \
     -H "Content-Type: application/json" \
     -d  @./filepath/file.json \
     https://d4bhu5x3ag.execute-api.eu-west-2.amazonaws.com/dev/api/max_pizza_overlap

```
so for example:
```
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"N": 5, "P": [[3, 3, 2], [3, 3, 3], [1, 1, 2]]}' \
     https://d4bhu5x3ag.execute-api.eu-west-2.amazonaws.com/dev/api/max_pizza_overlap

curl -X POST \
     -H "Content-Type: application/json" \
     -d  @./input_sample.json \
     https://d4bhu5x3ag.execute-api.eu-west-2.amazonaws.com/dev/api/max_pizza_overlap
```


#### How to deploy

In case we want to check the deployment via AWS CLI of our Lambda function application, we should follow the following steps:

(\**In order to get started with Serverless Framework’s AWS, we should first install it with NPM, so in case we don’t already have [Node](#https://nodejs.org/en/download/package-manager/) on our machine, we should install it first;  it is recommended by the service to use the latest LTS version of NodeJS*)

1. We should first install the serverless CLI via NPM:
```
npm install -g serverless
```
2. We have slightly adapted our basic python code to the one in the *src/handler.py* file, that can handle the POST request and the json input values
3. We have to create a *serverless.yml* configuration file (where we should not ommit to include a *Lambda layer* that would contain the libraries we want to use, in our case we use *AWSLambda-Python37-SciPy1x:113* so as to be able to import numpy)
4. Finally, the *sls deploy* command (re)deploys our entire service via CloudFormation. But to do so, we have first to go to the *aws/* directory 
```
cd aws
serverless deploy
```
\* The *sls remove* command could remove the deployed service



## Roadmap
The target of our project has been to deliver an algorithm to get the maximum pizza delivery cover overlap, and we did it. But where it is located? And wouldn't it be useful along the way of our algorithm's calculations to maintain some of the info that a functional/procedural solution, despite its straightforwardness and intuitiveness, cannot but let it go? Modeling Z-town's world and info implementing an object-oriented class-based solution would definitely be useful for future projects in the course of Z-town's original and brave endeavour for pizza relegalisation. This is why in the *draft/* folder we have saved a solution approach (*main_object-oriented.py*) that we didn't finally consider as the most appropriate (less straightforward and to-the-point). 

Finally, in the *draft/* folder we have saved a non-perfected algorithm that would computationally approximate the order of complexity of our solution (*order_comput_calcul.py*).
