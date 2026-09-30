<pre><code class="language-mermaid">graph LR&#10;A[Set up your&lt;br&gt;Cloudflare Account] --&gt; B[Verify your&lt;br&gt;AI crawler]&#10;B --&gt; C[Discover&lt;br&gt;payable content]:::highlight&#10;C --&gt; D[Connect to&lt;br&gt;Stripe]&#10;D --&gt; E[Crawl pages]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>The Pay Per Crawl Discovery API allows verified AI crawlers to discover which domains offer paid content access. This enables your crawler to proactively identify sites participating in Pay Per Crawl before making crawl requests.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before using the Pay Per Crawl Discovery API, you must:</p>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/set-up-cloudflare-account/">Set up your Cloudflare account</a></li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/">Verify your AI crawler</a></li>
</ul>
<h2 id="authenticate-with-web-bot-auth">Authenticate with Web Bot Auth</h2>
<p>All requests to the Discovery API must be authenticated using HTTP message signatures with Web Bot Auth headers. This ensures that only verified crawlers can access the list of participating domains.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2771.md")
</div>
<h2 id="discover-participating-domains">Discover participating domains</h2>
<h3 id="api-endpoint">API endpoint</h3>
<pre><code class="language-txt">GET https://crawlers-api.ai-audit.cfdata.org/charged_zones&#10;</code></pre>
<h3 id="request-parameters">Request parameters</h3>
<ul>
<li><code>cursor</code> (optional): Cursor returned from a previous call for pagination</li>
<li><code>limit</code> (optional): Number of results to return per request</li>
</ul>
<h3 id="request-headers">Request headers</h3>
<p>Include the HTTP message signature headers generated using Web Bot Auth:</p>
<pre><code class="language-txt">Signature: &lt;your-signature&gt;&#10;Signature-Input: &lt;signature-metadata&gt;&#10;Signature-Agent: &lt;agent-information&gt;&#10;</code></pre>
<h3 id="example-request">Example request</h3>
<pre><code class="language-sh">curl -X GET &quot;https://crawlers-api.ai-audit.cfdata.org/charged_zones?limit=50&quot; \&#10;  &#45;H &quot;Signature: &lt;your-signature&gt;&quot; \&#10;  &#45;H &quot;Signature-Input: &lt;signature-metadata&gt;&quot; \&#10;  &#45;H &quot;Signature-Agent: &lt;agent-information&gt;&quot;&#10;</code></pre>
<h3 id="response-format">Response format</h3>
<p>The API returns a list of zones (domains) that have Pay Per Crawl enabled and are accepting payments from your crawler.</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;zones&quot;: [&#10;			{&#10;				&quot;domain&quot;: &quot;example.com&quot;&#10;			},&#10;			{&#10;				&quot;domain&quot;: &quot;news-site.com&quot;&#10;			}&#10;		]&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="response-fields">Response fields</h3>
<ul>
<li><code>result.zones</code>: Array of zone objects containing domains with Pay Per Crawl enabled</li>
<li><code>result.zones[].domain</code>: The domain name offering Pay Per Crawl content</li>
<li><code>success</code>: Boolean indicating whether the request was successful</li>
<li><code>errors</code>: Array of error messages (empty if successful)</li>
<li><code>messages</code>: Array of informational messages</li>
</ul>
<h2 id="use-discovery-data">Use discovery data</h2>
<p>The Discovery API returns domains where site owners have specifically configured your crawler to be charged for content access. If a domain does not appear in the response, the site owner has not enabled Pay Per Crawl charging for your crawler. Site owners may also block or allow your crawler through WAF rules or set directives in their robots.txt file, which you should check and respect.</p>
<p>Cache discovery results locally and refresh periodically to stay up-to-date with domains joining or leaving Pay Per Crawl.</p>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/">Crawl pages</a></li>
</ul>
