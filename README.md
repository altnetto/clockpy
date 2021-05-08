# ClockPy
## _A library that enables you an easy way to verify your code time consumption_

With ClockPy you are able to quickly:

- Calculate the time spent between Checkpoints
- See the steps that spend more and less time in your code
- Tag checkpoints with some specified labels

Available Methods:

- checkpoint(label = None): place a checkpoint
- checkpoints(): list all checkpoints (dictionary)
- total(): returns the total time spent from the Clockpy() to the last checkpoint() declared
- shorter(): prints the shorter checkpoint
- longer(): prints the longer checkpoint
- describe(): prints the total time, the longer and shorter times.

Available Properties

- start: timestamp representing when it started to count time
- values: list of timestamp values starting from... well, the start
- times: list containing all checkpoint times
- labels: list containing all the labels given to the checkpoints (None if nothing was declared in checkpoint method)

## Compatible with

- Python 3.6+

## Installation

Just do it by pip

```sh
pip install clockpy
```

## Startkick

#### Basic Usage

```py
from clockpy import Clockpy

test = Clockpy()
print('Hello World!')
test.checkpoint('Testing Print')
print(test.checkpoints()
```
```
>> {'Checkpoint 1 (Testing Print)': 0.11759400367736816}
```
Try the next code, for better usage:
```py
from clockpy import Clockpy
from time import sleep
import random

test = Clockpy()

for i in range(5):
    get_random_time = random.random()*3
    print(get_random_time)
    sleep(get_random_time)
    test.checkpoint()

sleep(0.5)
test.checkpoint('Sleep')
print(test.checkpoints())
```
```
>> 2.270756884340154
>> 2.5198100932405696
>> 0.09423308904036198
>> 2.5932391928335283
>> 2.5916096569135103
>> {'Checkpoint 1': 2.2857015132904053, 'Checkpoint 2': 2.527977466583252, 'Checkpoint 3': 0.09659266471862793, 'Checkpoint 4': 2.6009044647216797, 'Checkpoint 5': 2.5935676097869873, 'Checkpoint 6 (Sleep)': 0.5115058422088623}
```
```py
test.describe()
```
```
>> Total time: 10.616249561309814
>> Max time: 2.6009044647216797
>> Min time: 0.09659266471862793
```
```py
test.longer()
```
```
>> Checkpoint 4: 2.6009044647216797
```
```py
test.shorter()
```
```
>> Checkpoint 3: 0.09659266471862793
```
