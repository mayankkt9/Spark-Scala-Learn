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


RDD
Hadoop stored data in multiple distributed storage disk such as HDFS and multiple IO makes it slow.
Spark came up with In Memory Data Sharing that made it very fast which became 100 times faster than network or disk sharing 
RDD tried to solve this problem by fault tolerant distributed in-memory computation.

