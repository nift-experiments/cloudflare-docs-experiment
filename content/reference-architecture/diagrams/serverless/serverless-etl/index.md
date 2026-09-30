<h2 id="introduction">Introduction</h2>
<p>Extract, Transform, Load (ETL) pipelines are a cornerstone in the realm of data engineering, facilitating the seamless flow of data from its raw state to a structured, usable format. ETL pipelines are instrumental in the data processing journey, particularly in scenarios where data needs to be collected, cleansed, and transformed before being loaded into a target destination.</p>
<p>The process begins with extraction, where data is gathered from various sources such as databases, files, or streams. This raw data is often disparate and unstructured, necessitating the next step: transformation. During transformation, the data undergoes a series of operations to standardize formats, clean inconsistencies, and enrich with additional context or calculations. This phase is critical for ensuring data quality and consistency, as well as aligning it with the requirements of downstream applications and analytics.</p>
<p>Finally, the transformed data is loaded into a destination, which could be a data warehouse, database, or any other storage solution. The loading phase involves efficiently moving the processed data to its intended destination, where it can be readily accessed and utilized for various purposes such as reporting, analysis, or feeding into machine learning models.</p>
<p>ETL pipelines play a pivotal role in data-driven decision-making processes across industries, enabling organizations to derive insights and value from their data assets. By automating and streamlining the journey from raw data to actionable insights, ETL pipelines empower businesses to make informed decisions, optimize processes, and gain competitive advantages in today's data-driven landscape.</p>
<p>Examples of ETL pipelines in action include scenarios like extracting sales data from multiple retail stores, transforming it to a standardized format, and loading it into a centralized data warehouse for analysis and reporting purposes. Similarly, ETL pipelines are utilized in data migration projects, where legacy data needs to be migrated to modern systems while ensuring data integrity and consistency throughout the process.</p>
<p>Cloudflare allows for the deployment of fully serverless ETL pipelines, which can reduce complexity, time to production and overall cost. The following diagrams demonstrate different methods of how Cloudflare can be used in common ETL pipeline deployments.</p>
<h2 id="etl-pipeline-with-http-based-ingest">ETL pipeline with HTTP-based ingest</h2>
<p><img src="/assets/upstream/images/reference-architecture/serverless-etl/serverless-etl-http-based.svg" alt="Figure 1: Serverless: HTTP-based ingest" title="Figure 1: ETL pipeline with HTTP-based ingest" /></p>
<p>This architecture shows a fully serverless ETL pipeline with an API endpoint as ingest. Clients send data via HTTP request to be processed. Common examples include click-stream data or analytics.</p>
<ol>
<li><strong>Client request</strong>: Send POST request with data to be ingested. Examples would include click-stream data, analytics endpoints.</li>
<li><strong>Input processing</strong>: Process incoming request using <a href="/workers/">Workers</a> and send messages to <a href="/queues/">Queues</a> to add to processing backlog.</li>
<li><strong>Data processing</strong>: Use <a href="/queues/">Queues</a> to trigger a <a href="/queues/reference/how-queues-works/#consumers">consumer</a> that process input data in batches to prevent downstream overload and increase efficiency. The consumer performs all data cleaning, transformation and standardization operations.</li>
<li><strong>Object storage</strong>: Upload processed data to <a href="/r2/">R2</a> for persistent storage.</li>
<li><strong>Ack/Retry mechanism</strong>: Signal success/error by using the <a href="/queues/configuration/javascript-apis/#message">Queues Runtime API</a> in the consumer for each document. <a href="/queues/">Queues</a> will schedule retries, if needed.</li>
<li><strong>Data querying</strong>: Access processed data from external services for further data usage.</li>
</ol>
<h2 id="etl-pipeline-with-object-storage-ingest">ETL pipeline with object storage ingest</h2>
<p><img src="/assets/upstream/images/reference-architecture/serverless-etl/serverless-etl-object-storage.svg" alt="Figure 2: Serverless: Object storage ingest" title="Figure 2: ETL pipeline with object storage ingest" /></p>
<p>This architecture shows a fully serverless ETL pipeline with object storage as ingest. Common examples include log and unstructured document processing.</p>
<ol>
<li><strong>Client request</strong>: Upload raw data to R2 via S3-compatible API. Common examples include log and analytics data.</li>
<li><strong>Input processing</strong>: Send messages to <a href="/queues/">Queues</a> using <a href="/r2/buckets/event-notifications/">R2 event notifications</a> upon object upload.</li>
<li><strong>Data processing</strong>: Use <a href="/queues/">Queues</a> to trigger a <a href="/queues/reference/how-queues-works/#consumers">consumer</a> that process input data in batches to prevent downstream overload and increase efficiency. The consumer performs all data cleaning, transformation and standardization operations.</li>
<li><strong>Object storage</strong>: Upload processed data to <a href="/r2/">R2</a> for persistent storage.</li>
<li><strong>Ack/Retry mechanism</strong>: Signal success/error by using the <a href="/queues/configuration/javascript-apis/#message">Queues Runtime API</a> in the consumer for each document. <a href="/queues/">Queues</a> will schedule retries, if needed.</li>
<li><strong>Data querying</strong>: Access processed data from external services for further data usage.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/get-started/guide/">Workers: Get started</a></li>
<li><a href="/queues/get-started/">Queues: Get started</a></li>
<li><a href="/r2/get-started/">R2: Get started</a></li>
</ul>
