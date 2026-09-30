<h2 id="introduction">Introduction</h2>
<p>Object storage is a modern data storage approach that stores data as objects rather than in a hierarchical structure like traditional file systems, making object storage highly scalable and flexible for managing vast amounts of data across diverse applications and environments.</p>
<p>Oftentimes organizations leverage multiple cloud providers to distribute their workloads across different platforms, mitigating risks associated with vendor lock-in, enhancing resilience, and optimizing performance and cost. However, managing data across multiple clouds introduces challenges related to data mobility and interoperability, particularly when it comes to transferring data between cloud providers or on-premises environments.</p>
<p>Egress fees are charges incurred when data is transferred out of a cloud provider's network, either to another cloud provider, on-premises infrastructure, or external services. These fees can vary depending on factors such as the volume of data transferred, the destination of the data, and the network bandwidth utilized.</p>
<p><a href="/r2/">R2</a> offers an enticing value proposition by not charging the costly egress bandwidth fees associated with typical cloud storage services. This can be very advantageous in the context of multi-cloud environments, especially when you want to run compute-intensive workloads such as AI model training, query engines, and other data science tools.</p>
<h2 id="r2-multi-cloud-setup">R2 multi-cloud setup</h2>
<p><img src="/assets/upstream/images/reference-architecture/r2-multi-cloud/r2-multi-cloud.svg" alt="Figure 1: R2 multi-cloud setup" title="Figure 1: R2-multi-cloud setup" /></p>
<ol>
<li><strong>Worker and R2 interaction</strong>: Use R2's <a href="/r2/api/workers/workers-api-reference/">Workers API</a> to interact with R2 from a Worker. Alternatively, for improved portability, use R2's <a href="/r2/api/s3/">S3 API</a> from a Worker. No R2 egress fees apply.</li>
<li><strong>External service and R2 interaction</strong>: Use R2's <a href="/r2/api/s3/">S3 API</a> to interact with R2 from external services. No R2 egress fees apply.</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/r2/get-started">R2: Get started</a></li>
<li><a href="/r2/api/s3/">R2: S3 API</a></li>
<li><a href="/r2/api/workers/">R2: Workers API</a></li>
<li><a href="/r2/examples/aws/aws4fetch/">R2: Configure aws4fetch for R2</a></li>
</ul>
