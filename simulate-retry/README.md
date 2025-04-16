# simulate-retry
Just trying something

## Runtime Test Results

## Test Environment

* OS X El Capitan 10.11.6
* 3.1 GHz Intel Core i7 CPU
* Python 2.7
* 16 GB 1867 MHz DDR3 RAM

### Big Interval (1000000), 1000 Small Events([100, 200])

|Data Structure|Result(secs)|
|--------------|------------|
|Dummy         |0.0869      |
|Fenwick Tree  |0.1010      |
|Linked List   |0.1140      |

### Medium Interval (100000), 20000 Long Events([900, 1000])

|Data Structure|Result(secs)|
|--------------|------------|
|Dummy         |1.9600      |
|Fenwick Tree  |0.1275      |
|Linked List   |91.2197     |

### Big Interval (1000000), 100000 Events With a Big Range of Duration ([100, 10000])

|Data Structure|Result(secs)|
|--------------|------------|
|Dummy         |51.5447     |
|Fenwick Tree  |0.7408      |
|Linked List   | :(         |