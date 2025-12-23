Coding / Scripting	
System Deigning	
Unix Internal	
Troubleshooting	
Role Based - DevOps	
	
5 topic	
	
if -else	
loop	
list	
dictionary	
function	
file handing - linux	
	
scripting 	https://docs.google.com/document/d/1VkgXJOoLHwQ5BmfWTksgSq_gGMlypdZ9NzXSNJFQ-3k/edit?tab=t.0
	
system design	consistent hashing
	load balancing
	data shardimg
	publihser submishing
	
unix internal	cat command type kya hota h
	ls
	fork
	content switcher
	10 system calls 
	cp internal call kaise hota h
	
trouble shooting	
	
network	top 20 
	
	
Array	
String	
searching	
sorting	
Stack , Queue	
DP	
###

'''
🟢 EASY (50 QUESTIONS)

Focus: File I/O, strings, loops, basic Linux awareness

Log & File Parsing

Read a log file and print all lines containing the word ERROR

Count total number of lines in a file

Count total number of words in a file

Extract only IP addresses from an access log

Print only HTTP status codes from a log file

Find unique IP addresses in a log file

Count how many times each IP appears

Print lines starting with a given prefix

Print lines ending with .log

Find empty lines in a file

File System

Check if a file exists

Print file size in bytes

Print file creation and modification time

Rename a file using Python

Copy contents of one file to another

Delete a file safely (with existence check)

List all files in a directory

Count number of files in a directory

Print only .txt files from a directory

Find the largest file in a directory

Linux / OS Basics

Print current working directory

Print environment variables

Read input from STDIN

Exit program with custom error code

Sleep for N seconds

Execute a shell command from Python

Capture output of ls command

Check Python version programmatically

Print system hostname

Print system uptime (via command)

Strings & Basics

Reverse each line of a file

Convert all text to lowercase

Remove duplicate lines from a file

Count occurrences of a word

Replace a word in a file

Trim whitespace from each line

Split CSV file into columns

Print first N lines of a file

Print last N lines of a file

Merge two files line by line

Error Handling

Handle missing file exception

Handle permission denied error

Skip corrupted lines gracefully

Validate numeric input

Ignore comment lines (#)

Handle empty file input

Handle UnicodeDecodeError

Handle keyboard interrupt

Print meaningful error messages

Add basic logging to script

🟡 MEDIUM (50 QUESTIONS)

Focus: Log analytics, efficiency, Linux internals, production mindset

Log Analysis

Find top 10 IPs by request count

Count HTTP 4xx and 5xx errors

Find most frequent endpoint

Detect traffic spike per minute

Extract timestamps and group requests per minute

Identify slow requests (>2s response time)

Find requests causing 500 errors

Extract user agents and count top 5

Find IPs accessing /admin

Detect brute force login attempts

File Processing

Compare sizes of multiple files

Identify duplicate files by size

Split large log file into chunks

Rotate logs based on size

Compress old log files

Delete files older than N days

Archive logs by date

Validate log file format

Count lines without loading file into memory

Stream process a 10GB file

Linux / OS

Find top CPU consuming process

Kill a process by name

Detect zombie processes

Identify orphan processes

Monitor disk usage and alert if >80%

Monitor memory usage

Parse output of df -h

Parse output of ps aux

Detect file descriptor leaks

Find open ports on system

Automation

Read list of servers from file and ping them

SSH into multiple hosts and collect output

Retry failed command execution

Add timeout to shell command

Implement exponential backoff

Read config from environment variables

Read config from JSON/YAML

Send email alert on failure

Write script with CLI arguments

Add dry-run mode

Data Structures

Find duplicates efficiently

Use dictionary for frequency count

Use set for uniqueness

Sort results by frequency

Limit output to top N

Handle malformed input lines

Use generators for memory efficiency

Use context managers correctly

Write reusable functions

Add unit test for script

🔴 HARD (30 QUESTIONS)

Focus: Scale, reliability, system thinking, SRE mindset

Large-Scale Log Processing

Process 100GB log file efficiently

Find top IPs without loading file into memory

Distributed log aggregation strategy

Detect anomalies in traffic pattern

Identify DDoS behavior heuristically

Find unique users across multiple log files

Correlate logs from multiple services

Detect cascading failures from logs

Identify error spikes correlated with deploy

Build rate-limiting detector

Performance & Reliability

Implement producer-consumer log processing

Parallelize log parsing safely

Handle partial file writes

Handle log rotation during processing

Implement checkpointing for long jobs

Detect disk full condition early

Gracefully degrade script under load

Add structured logging

Add metrics to script

Implement retry + circuit breaker

Linux Internals

Explain fork-exec-wait with example

Explain copy-on-write

Diagnose high load average

Debug IO wait issues

Identify kernel vs user CPU usage

Investigate file system inode exhaustion

Debug memory leak using /proc

Detect network socket exhaustion

Explain context switching impact

Design a health check system

'''