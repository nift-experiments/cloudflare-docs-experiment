<p class="article-summary">Parse and transform large JSON request and response bodies using streaming.</p>
<p>Use the <a href="/workers/runtime-apis/streams/">Streams API</a> to process JSON payloads that would exceed a Worker's 128 MB memory limit if fully buffered. Streaming allows you to parse and transform JSON data incrementally as it arrives. This is faster than buffering the entire payload into memory, as your Worker can start processing data incrementally, and allows your Worker to handle multi-gigabyte payloads or files within its memory limits.</p>
<p>The <a href="https://www.npmjs.com/package/@streamparser/json-whatwg"><code>@streamparser/json-whatwg</code></a> library provides a streaming JSON parser compatible with the Web Streams API.</p>
<p>Install the dependency:</p>
<pre><code class="language-sh">npm install @streamparser/json-whatwg&#10;</code></pre>
<h2 id="stream-a-json-request-body">Stream a JSON request body</h2>
<p>This example parses a large JSON request body and extracts specific fields without loading the entire payload into memory.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16333.md")
</div></div>
<h2 id="stream-and-transform-a-json-response">Stream and transform a JSON response</h2>
<p>This example fetches a large JSON response from an upstream API, transforms specific fields, and streams the modified response to the client.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16336.md")
</div></div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/runtime-apis/streams/">Streams API</a> - Learn more about streaming in Workers</li>
<li><a href="/workers/runtime-apis/streams/transformstream/">TransformStream</a> - Create custom stream transformations</li>
<li><a href="https://www.npmjs.com/package/@streamparser/json-whatwg">@streamparser/json-whatwg</a> - Streaming JSON parser documentation</li>
</ul>
