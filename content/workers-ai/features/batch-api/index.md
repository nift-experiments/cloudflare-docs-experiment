<p>Asynchronous batch processing lets you send a collection (batch) of inference requests in a single call. Instead of expecting immediate responses for every request, the system queues them for processing and returns the results later.</p>
<p>Batch processing is useful for large workloads such as summarization or embeddings when there is no human interaction. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if Cloudflare does not have enough capacity at a given time.</p>
<p>When you send a batch request, the API immediately acknowledges receipt with a status like <code>queued</code> and provides a unique <code>request_id</code>. This ID is later used to poll for the final responses once the processing is complete.</p>
<p>You can use the Batch API by either creating and deploying a Cloudflare Worker that leverages the <a href="/workers-ai/features/batch-api/workers-binding/">Batch API with the AI binding</a>, using the <a href="/workers-ai/features/batch-api/rest-api/">REST API</a> directly or by starting from a <a href="https://github.com/craigsdennis/batch-please-workers-ai">template</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/15828.md")
</aside>
<h2 id="demo-application">Demo application</h2>
<p>If you want to get started quickly, click the button below:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/craigsdennis/batch-please-workers-ai"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>This will create a repository in your GitHub account and deploy a ready-to-use Worker that demonstrates how to use Cloudflare's Asynchronous Batch API. The template includes preconfigured AI bindings, and examples for sending and retrieving batch requests with and without external references. Once deployed, you can visit the live Worker and start experimenting with the Batch API immediately.</p>
<h2 id="supported-models">Supported Models</h2>
<p>Refer to our <a href="/workers-ai/models/?capabilities=Batch">model catalog</a> for supported models.</p>
