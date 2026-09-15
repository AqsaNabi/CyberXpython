<h3> Concurrency </h3>
<h2>Introduction to concurrency </h2>
Concurrency is one approach to drastically increase the performance of your Python programs. Concurrency allows several processes to be completed concurrently, maximizing the utilization of your system's resources. Concurrency can be achieved in Python by the use of numerous methods and modules, such as threading, multiprocessing, and asynchronous programming. In this article, we will learn about What is concurrency in Python, the processes required to implement it, some good examples, and the output results. <br>
<h2> Concurrent Programming</h2>
It refers to the ability of the computer to manage multiple tasks at the same time. These tasks might not be compulsory to execute at the exact same moment but they might interleaved or executed in overlapping periods of time. The main goal of concurrency is to handle multiple user inputs, manage several I/O tasks, or process multiple independent tasks. <br>
<h2>Parallelisom</h2>
Parallelism is a subset of concurrency where tasks or processes are executed simultaneously, As we know concurrency is about dealing with multiple tasks, whereas parallelism is about executing them simultaneously to speed computation. The primary goal is to improve computational efficiency and speed up the performance of the system. <br>
Thread-Based Concurrency: Threading is a technique for producing lightweight threads (sometimes known as "worker threads") in a single step. Because these threads share the same memory region, they are ideal for I/O-bound activities. <br>
Process-Based Concurrency: Multiprocessing entails the execution of several processes, each with its own memory space. Because it can use several CPU cores, this is appropriate for CPU-bound activities.<br>
Coroutine-Based Concurrency: Asynchronous programming, with 'asyncio' , 'async', and 'await' keywords, is ideal for efficiently managing I/O-bound processes. It enables tasks to pause and hand over control to other tasks during I/O operations without causing the entire program to crash.<br>
<h2>Threads</h2>
They are ordered streams of instruction, can can bee scheduled to run by operating system and can be run either in parallely across multiple core or concurrently across a single core. They consists of a program center, stack and set of registers and an identifier. These threads within the o/s are typically able to interact with sharedd resources so.
<br>
There are mainly two types of threads<br>
User-level: that which we create and play with our private programming <br>
kernel-level: low level threads that act on behalf of the operating system
<br>
