## Objective

Share understanding of asycio library with examples and content put together from different blogs/tutorials/docs.


## Concurrency vs Parallelism

- Parallelism is ability to run multiple tasks at the same time. 
    - Usually achieved by using multiple cores of a processor.
- Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. 
    - It doesn't necessarily mean they'll ever both be running at the same instant. 
    - For example, multitasking on a single-core machine.

## When Is Concurrency Useful?
Source: https://realpython.com/python-concurrency/

Concurrency can make a big difference for two types of problems. These are generally called CPU-bound and I/O-bound.

## I/O bound
I/O-bound problems cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource. 

They arise frequently when your program is working with things that are much slower than your CPU.

[io_bound]: io_bound.jpg
![alt text][io_bound]


## CPU bound

There are classes of programs that do significant computation without talking to the network or accessing a file. 

These are the CPU-bound programs, because the resource limiting the speed of your program is the CPU, not the network or the file system.


[cpu_bound]: ./cpu_bound.png
![alt text][cpu_bound]

    
## Process vs Threads
### Process
- Created by the operating system to run programs
- Process can have multiple threads
- Two processes can execute code simultaneously in the same python program
- Processes have more overhead than threads as opening and closing processes takes more time
- Sharing information between processes is slower than sharing between threads as processes do not share memory space. In python they share information by pickling data structures like arrays which requires IO time.

### Thread
- Threads are like mini-processes that live inside a process
- They share memory space and efficiently read and write to the same variables

## Python concurrency support
[python_concurrency]: ./python_concurrency_parallelism.jpg
![alt text][python_concurrency]

Python supports concurrency with the following packages:
- threading
  - achieves concurrency using threads.
  - GIL (Global Interpreter Lock) prevents multiple threads executing python bytecode at once. 
  - however, and libraries like Numpy bypass GIL limitation by running external code in C.
  - So best suited for I/O workloads.
- multiprocessing
  - Swapns multiple process.
  - Best suited for CPU intensive workloads. 
- asyncio

[CPU-Bound Code](../code/factorial.py)

[Next](2_asyncio.md)
