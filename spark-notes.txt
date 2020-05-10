What is Spark ? 
	- Scalable
	- Massively Parellel
	- In Memory Execution
Data can be loaded into memory and analyzed in parellel
Distribute data in cluster and then analyzed
Very fast as compared to Hadoop as Spark is IN Memory

Features 
	- Speed 
	- Powerful Caching 
	- Realtime DataAnalysis
	- Deployment
	- Polyglot (Scala | Java | Python | R)

Spark Component
	- Spark Core  (Basic IO | Scheduling | Monitoring | API)
	- Library (SparkSQL | GraphX | SparkStreaming | SparkMLib)
	- Programming Language Supports (Scala | Java | Python | R)
	- Storage (LocalFS | HDFS | AmazonS3 | RDBMS | NoSQL)

 
RDD (Resilient Distributed Data)
Hadoop stored data in multiple distributed storage disk such as HDFS and multiple IO makes it slow.
Spark came up with In Memory Data Sharing that made it very fast which became 100 times faster than network or disk sharing 
RDD tried to solve this problem by fault tolerant distributed in-memory computation.
	- Fundamental Data Structure
	- All Data are in RDD format
	- Each Data in RDD can be partitioned logically and can run on parellel on different node on cluster.
	- Spark takes care of RDD Partition distribution
	- Highly Resilient (Able to recover quickly as same data chunk are replicated across multiple node)

Features of RDD
	- In Memory computation
	- Lazy Evaluation (Does not evaluate quickly until the action is applied)
	- Fault Tolerant (Rebuild last data)
	- Immutable
	- Partitioning (Fundamental unit of parellelism)
	- Persistence
	- Coarse Grained Operation

Ways to Create RDDs
	- Parellelized Collection (sc.parellelize)
	- From RDDs 
	- External Data (HDFS | AmazonS3)




