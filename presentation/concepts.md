## Concurrency vs Parallelism

- Parallelism is ability to run multiple tasks at the same time. 
    - Usually achieved by using multiple cores of a processor.
- Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. 
    - It doesn't necessarily mean they'll ever both be running at the same instant. 
    - For example, multitasking on a single-core machine.
    
    
## Python concurrency support
[python_concurrency]: ./python_concurrency_parallelism.jpg
![alt text][python_concurrency]

Python supports concurrency with the following packages:
- multiprocessing
  - Swapns multiple process.
  - Data sharing is tricker than threads.
  - Best suited for CPU intensive workloads.
- threading
  - achieves concurrency using threads.
  - shared memory access.
  - GIL prevents multiple threads executing python bytecode at once. [Code](../code/factorial.py)
  - So best suited for I/O workloads.
- asyncio

