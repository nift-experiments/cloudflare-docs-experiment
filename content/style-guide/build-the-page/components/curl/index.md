<p>The <code>CURL</code> component is used to display a cURL command for making HTTP requests.</p>
<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { CURL } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre><code class="language-mdx">import { CURL } from &quot;~/components&quot;;&#10;&#10;&lt;CURL&#10;	url=&quot;https://httpbin.org/anything&quot;&#10;	method=&quot;POST&quot;&#10;	json={{&#10;		key: &quot;va&#x27;l&#x27;ue&quot;,&#10;	}}&#10;	query={{&#10;		foo: &quot;bar&quot;,&#10;		bar: [&quot;baz&quot;, &quot;qux&quot;],&#10;	}}&#10;	code={{&#10;		mark: &quot;value&quot;,&#10;	}}&#10;/&gt;&#10;&#10;&lt;CURL&#10;	url=&quot;https://httpbin.org/anything&quot;&#10;	method=&quot;POST&quot;&#10;	form={{&#10;		key: &quot;value&quot;,&#10;	}}&#10;	code={{&#10;		mark: &quot;value&quot;,&#10;	}}&#10;/&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;CURL&gt;</code> Props</h2>
<h3 id="url"><code>url</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>string</code></p>
<p>The URL to make the request to.</p>
<h3 id="method"><code>method</code></h3>
<p><strong>type:</strong> <code>&quot;GET&quot; | &quot;HEAD&quot; | &quot;POST&quot; | &quot;PUT&quot; | &quot;DELETE&quot; | &quot;OPTIONS&quot; | &quot;PATCH&quot;</code></p>
<p><strong>default:</strong> <code>&quot;GET&quot;</code></p>
<p>The HTTP method to use for the request.</p>
<h3 id="headers"><code>headers</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, string&gt;</code></p>
<p>The headers to include in the request.</p>
<h3 id="json"><code>json</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt; | Record&lt;string, any&gt;[]</code></p>
<p>JSON data to include in the request.</p>
<h3 id="form"><code>form</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, any&gt;</code></p>
<p>The FormData payload to send.</p>
<h3 id="query"><code>query</code></h3>
<p><strong>type:</strong> <code>Record&lt;string, string | string[]&gt;</code></p>
<p>URL query parameters to append to the request URL.</p>
<h3 id="code"><code>code</code></h3>
<p><strong>type:</strong> <code>object</code></p>
<p>An object of Astro <code>Code</code> props. Refer to the <a href="https://docs.astro.build/en/reference/api-reference/#code-">Astro <code>Code</code> component documentation</a> for available props.</p>
