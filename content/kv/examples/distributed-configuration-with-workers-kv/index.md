<p class="article-summary">Use Workers KV to as a geo-distributed, low-latency configuration store for your Workers application</p>
<p>Storing application configuration data is an ideal use case for Workers KV. Configuration data can include data to personalize an application for each user or tenant, enable features for user groups, restrict access with allow-lists/deny-lists, etc. These use-cases can have high read volumes that are highly cacheable by Workers KV, which can ensure low-latency reads from your Workers application.</p>
<p>In this example, application configuration data is used to personalize the Workers application for each user. The configuration data is stored in an external application and database, and written to Workers KV using the REST API.</p>
<h2 id="write-your-configuration-from-your-external-application-to-workers-kv">Write your configuration from your external application to Workers KV</h2>
<p>In some cases, your source-of-truth for your configuration data may be stored elsewhere than Workers KV.
If this is the case, use the Workers KV REST API to write the configuration data to your Workers KV namespace.</p>
<p>The following external Node.js application demonstrates a simple scripts that reads user data from a database and writes it to Workers KV using the REST API library.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9515.md")
</div></div>
<p>In this code snippet, the Node.js application reads user data from a Postgres database and writes the user data to be used for configuration in our Workers application to Workers KV using the Cloudflare REST API Node.js library.
The application also uses exponential backoff to handle retries in case of errors.</p>
<h2 id="use-configuration-data-from-workers-kv-in-your-worker-application">Use configuration data from Workers KV in your Worker application</h2>
<p>With the configuration data now in the Workers KV namespace, we can use it in our Workers application to personalize the application for each user.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9518.md")
</div></div>
<p>This code will use the path within the URL and find the file associated to the path within the KV store. It also sets the proper MIME type in the response to inform the browser how to handle the response. To retrieve the value from the KV store, this code uses <code>arrayBuffer</code> to properly handle binary data such as images, documents, and video/audio files.</p>
<h2 id="optimize-performance-for-configuration">Optimize performance for configuration</h2>
<p>To optimize performance, you may opt to consolidate values in fewer key-value pairs. By doing so, you may benefit from higher caching efficiency and lower latency.</p>
<p>For example, instead of storing each user's configuration in a separate key-value pair, you may store all users' configurations in a single key-value pair. This approach may be suitable for use-cases where the configuration data is small and can be easily managed in a single key-value pair (the <a href="/kv/platform/limits/">size limit for a Workers KV value is 25 MiB</a>).</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a></li>
<li><a href="/kv/get-started/">Using KV in Workers</a></li>
</ul>
