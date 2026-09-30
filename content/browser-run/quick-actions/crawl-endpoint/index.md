<p>The <code>/crawl</code> endpoint scrapes content from a starting URL and follows links across the site, up to a configurable depth or page limit. Responses can be returned as HTML, Markdown, or JSON.</p>
<p>The <code>/crawl</code> endpoint is available via the REST API. <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with the <code>Browser Rendering - Edit</code> permission.</p>
<h2 id="endpoint">Endpoint</h2>
<pre><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/browser-rendering/crawl&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<ul>
<li><code>url</code> (string)</li>
</ul>
<p>Refer to <a href="/browser-run/quick-actions/crawl-endpoint/#optional-parameters">optional parameters</a> for additional customization options.</p>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Building knowledge bases or training AI systems (such as <a href="/reference-architecture/diagrams/ai/ai-rag/">RAG applications</a>) with up-to-date web content</li>
<li>Scraping and analyzing content across multiple pages for research, summarization, or monitoring</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>There are two steps to using the <code>/crawl</code> endpoint:</p>
<ol>
<li><a href="/browser-run/quick-actions/crawl-endpoint/#initiate-the-crawl-job">Initiate the crawl job</a> — A <code>POST</code> request where you initiate the crawl and receive a response with a job <code>id</code>.</li>
<li><a href="/browser-run/quick-actions/crawl-endpoint/#request-results-of-the-crawl-job">Request results of the crawl job</a> — A <code>GET</code> request where you request the status or results of the crawl.</li>
</ol>
<p>Crawl jobs have a maximum run time of seven days. If a job does not finish within this time, it will be cancelled due to timeout. Job results are available for 14 days after the job completes, after which the job data is deleted.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="free-plan-limitations">Free plan limitations</h3>
@markup("md", "content/.markup/bodies/3640.md")
</aside>
<h2 id="initiate-the-crawl-job">Initiate the crawl job</h2>
<p>Send a <code>POST</code> request with a <code>url</code> to start a crawl job. The API responds immediately with a job <code>id</code> you will use to retrieve results. Refer to <a href="/browser-run/quick-actions/crawl-endpoint/#optional-parameters">optional parameters</a> for additional customization options.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://developers.cloudflare.com/workers/&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Example response:</p>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: &quot;c7f8s2d9-a8e7-4b6e-8e4d-3d4a1b2c3f4e&quot;&#10;}&#10;</code></pre>
<h2 id="request-results-of-the-crawl-job">Request results of the crawl job</h2>
<p>To check the status or request the results of your crawl job, use the job <code>id</code> you received:</p>
<pre><code class="language-bash">curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/c7f8s2d9-a8e7-4b6e-8e4d-3d4a1b2c3f4e&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer YOUR_API_TOKEN&#x27;&#10;</code></pre>
<p>The response includes a <code>status</code> field indicating the current state of the crawl job. The possible job statuses are:</p>
<ul>
<li><code>running</code> — The crawl job is currently in progress.</li>
<li><code>cancelled_due_to_timeout</code> — The crawl job exceeded the maximum run time of seven days.</li>
<li><code>cancelled_due_to_limits</code> — The crawl job was cancelled because it hit <a href="/browser-run/limits/">account limits</a>.</li>
<li><code>cancelled_by_user</code> — The crawl job was manually cancelled by the user.</li>
<li><code>errored</code> — The crawl job encountered an error.</li>
<li><code>completed</code> — The crawl job finished successfully.</li>
</ul>
<h3 id="polling-for-completion">Polling for completion</h3>
<p>Since crawl jobs run asynchronously, you can poll the endpoint periodically to check when the job finishes. Add <code>?limit=1</code> to the request URL so the response stays lightweight — you only need the job <code>status</code>, not the full set of crawled records.</p>
<pre><code class="language-javascript">async function waitForCrawl(accountId, jobId, apiToken) {&#10;	const maxAttempts = 60;&#10;	const delayMs = 5000;&#10;&#10;	for (let i = 0; i &lt; maxAttempts; i++) {&#10;		const response = await fetch(&#10;			`https://api.cloudflare.com/client/v4/accounts/${accountId}/browser-rendering/crawl/${jobId}?limit=1`,&#10;			{&#10;				headers: {&#10;					Authorization: `Bearer ${apiToken}`,&#10;				},&#10;			},&#10;		);&#10;&#10;		const data = await response.json();&#10;		const status = data.result.status;&#10;&#10;		if (status !== &quot;running&quot;) {&#10;			return data.result;&#10;		}&#10;&#10;		await new Promise((resolve) =&gt; setTimeout(resolve, delayMs));&#10;	}&#10;&#10;	throw new Error(&quot;Crawl job did not complete within timeout&quot;);&#10;}&#10;</code></pre>
<p>Once the job reaches a terminal status, fetch the full results without the <code>limit</code> parameter. You can also use the following query parameters to filter and paginate results:</p>
<ul>
<li><code>cursor</code> — Cursor for pagination. If the response exceeds 10 MB, a <code>cursor</code> value will be included. Pass it as a query parameter to retrieve the next page of results.</li>
<li><code>limit</code> — Maximum number of records to return.</li>
<li><code>status</code> — Filter by URL status: <code>queued</code>, <code>completed</code>, <code>disallowed</code>, <code>skipped</code>, <code>errored</code>, or <code>cancelled</code>.</li>
</ul>
<p>Example with query parameters:</p>
<pre><code class="language-bash">curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/c7f8s2d9-a8e7-4b6e-8e4d-3d4a1b2c3f4e?cursor=10&amp;limit=10&amp;status=completed&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer YOUR_API_TOKEN&#x27;&#10;</code></pre>
<p>Example response:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;c7f8s2d9-a8e7-4b6e-8e4d-3d4a1b2c3f4e&quot;,&#10;		&quot;status&quot;: &quot;completed&quot;,&#10;		&quot;browserSecondsUsed&quot;: 134.7,&#10;		&quot;total&quot;: 50,&#10;		&quot;finished&quot;: 50,&#10;		&quot;records&quot;: [&#10;			{&#10;				&quot;url&quot;: &quot;https://developers.cloudflare.com/workers/&quot;,&#10;				&quot;status&quot;: &quot;completed&quot;,&#10;				&quot;markdown&quot;: &quot;# Cloudflare Workers\nBuild and deploy serverless applications...&quot;,&#10;				&quot;metadata&quot;: {&#10;					&quot;status&quot;: 200,&#10;					&quot;title&quot;: &quot;Cloudflare Workers · Cloudflare Workers docs&quot;,&#10;					&quot;url&quot;: &quot;https://developers.cloudflare.com/workers/&quot;&#10;				}&#10;			},&#10;			{&#10;				&quot;url&quot;: &quot;https://developers.cloudflare.com/workers/get-started/quickstarts/&quot;,&#10;				&quot;status&quot;: &quot;completed&quot;,&#10;				&quot;markdown&quot;: &quot;## Quickstarts\nGet up and running with a simple Hello World...&quot;,&#10;				&quot;metadata&quot;: {&#10;					&quot;status&quot;: 200,&#10;					&quot;title&quot;: &quot;Quickstarts · Cloudflare Workers docs&quot;,&#10;					&quot;url&quot;: &quot;https://developers.cloudflare.com/workers/get-started/quickstarts/&quot;&#10;				}&#10;			}&#10;			// ... 48 more entries omitted for brevity&#10;		],&#10;		&quot;cursor&quot;: 10&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<h3 id="errored-and-blocked-pages">Errored and blocked pages</h3>
<p>If a crawled page returns an HTTP error (such as <code>402</code>, <code>403</code>, or <code>500</code>), the record for that URL will have <code>&quot;status&quot;: &quot;errored&quot;</code>.</p>
<p>This information is only available in the crawl results (step 2) — the <a href="/browser-run/quick-actions/crawl-endpoint/#initiate-the-crawl-job">initiation response</a> only returns the job <code>id</code>. Because crawl jobs run asynchronously, the crawler does not fetch page content at initiation time.</p>
<p>To view only errored records, filter by <code>status=errored</code>:</p>
<pre><code class="language-bash">curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}?status=errored&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer YOUR_API_TOKEN&#x27;&#10;</code></pre>
<p>The record's <code>status</code> field contains the HTTP status code returned by the origin server, and <code>html</code> contains the response body. This is useful for understanding site owners' intent when they block crawlers — for example, sites using <a href="https://blog.cloudflare.com/ai-crawl-control">AI Crawl Control</a> may return a custom status code and message.</p>
<h2 id="cancel-a-crawl-job">Cancel a crawl job</h2>
<p>To cancel a crawl job that is currently in progress, use the job <code>id</code> you received:</p>
<pre><code class="language-bash">curl -X DELETE &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/c7f8s2d9-a8e7-4b6e-8e4d-3d4a1b2c3f4e&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer YOUR_API_TOKEN&#x27;&#10;</code></pre>
<p>A successful cancellation will return a <code>200 OK</code> status code. The job status will be updated to cancelled, and all URLs that have been queued to be crawled will be cancelled.</p>
<h2 id="optional-parameters">Optional parameters</h2>
<p>The following optional parameters can be used in your crawl request, in addition to the required <code>url</code> parameter. These are parameters specific to the <code>/crawl</code> endpoint.</p>
<p>When <code>render</code> is <code>true</code> (the default), crawl jobs also support all standard Browser Run parameters such as <code>rejectResourceTypes</code>, <code>rejectRequestPattern</code>, <code>cookies</code>, and <code>setExtraHTTPHeaders</code>. When <code>render</code> is <code>false</code>, only the crawl-specific parameters listed in the table below are supported. For the full list, refer to the <a href="/api/resources/browser_rendering/subresources/crawl/methods/create/">API reference</a>.</p>
<table>
<thead>
<tr>
<th>Optional parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>limit</code></td>
<td>Number</td>
<td>Maximum number of pages to crawl (default is 10, maximum is 100,000).</td>
</tr>
<tr>
<td><code>depth</code></td>
<td>Number</td>
<td>Maximum link depth to crawl from the starting URL (default is 100,000, maximum is 100,000).</td>
</tr>
<tr>
<td><code>source</code></td>
<td>String</td>
<td>Source for discovering URLs. Options are <code>all</code>, <code>sitemaps</code>, or <code>links</code>. Default is <code>all</code>.</td>
</tr>
<tr>
<td><code>formats</code></td>
<td>Array of strings</td>
<td>Response format (default is HTML, other options are Markdown and JSON). The JSON format leverages <a href="/workers-ai/">Workers AI</a> by default for data extraction, which incurs usage on Workers AI. Refer to the <a href="/browser-run/quick-actions/json-endpoint/"><code>/json</code> endpoint</a> to learn more, including how to use a custom model and fallbacks.</td>
</tr>
<tr>
<td><code>render</code></td>
<td>Boolean</td>
<td>If false, does a fast HTML fetch without executing JavaScript (default is true, <a href="#render-parameter">learn more about <code>render</code></a>).</td>
</tr>
<tr>
<td><code>jsonOptions</code></td>
<td>Object</td>
<td>Only required if <code>formats</code> includes <code>json</code>. Contains <code>prompt</code>, <code>response_format</code>, and <code>custom_ai</code> properties (same types as the <a href="/browser-run/quick-actions/json-endpoint/"><code>/json</code> endpoint</a>).</td>
</tr>
<tr>
<td><code>maxAge</code></td>
<td>Number</td>
<td>Maximum length of time in seconds the crawler can use a cached resource before it must re-fetch it from the origin server (default is 86,400, maximum is 604,800). Cache is served from R2 only if the URL and parameters exactly match.</td>
</tr>
<tr>
<td><code>modifiedSince</code></td>
<td>Number</td>
<td>Unix timestamp (in seconds) indicating to only crawl pages that were modified since this time.</td>
</tr>
<tr>
<td><code>options.includeExternalLinks</code></td>
<td>Boolean</td>
<td>If true, follows links to external domains (default is false).</td>
</tr>
<tr>
<td><code>options.includeSubdomains</code></td>
<td>Boolean</td>
<td>If true, follows links to subdomains of the starting URL (default is false).</td>
</tr>
<tr>
<td><code>options.includePatterns</code></td>
<td>Array of strings</td>
<td>Only visits URLs that match one of these wildcard patterns. Use <code>*</code> to match any characters except <code>/</code>, or <code>**</code> to match any characters including <code>/</code>.</td>
</tr>
<tr>
<td><code>options.excludePatterns</code></td>
<td>Array of strings</td>
<td>Does not visit URLs that match any of these wildcard patterns. Use <code>*</code> to match any characters except <code>/</code>, or <code>**</code> to match any characters including <code>/</code>.</td>
</tr>
<tr>
<td><code>crawlPurposes</code></td>
<td>Array of strings</td>
<td>Declares the intended use of crawled content for <a href="https://contentsignals.org/">Content Signals</a> enforcement. Allowed values: <code>search</code>, <code>ai-input</code>, <code>ai-train</code>. Default is <code>[&quot;search&quot;, &quot;ai-input&quot;, &quot;ai-train&quot;]</code>. If a target site's <code>robots.txt</code> includes a <code>Content-Signal</code> directive that sets any of your declared purposes to <code>no</code>, the crawl request will be rejected with a <code>400</code> error. Refer to <a href="#content-signals">Content Signals</a> for details.</td>
</tr>
<tr>
<td><code>contentUse</code></td>
<td>String</td>
<td>Declares the intended content use level for the <code>use</code> <a href="https://contentsignals.org/">Content Signals</a> directive. Allowed values, from least to most permissive: <code>reference</code>, <code>full</code>. Default is <code>full</code>. If a target site sets a <code>use</code> directive more restrictive than your declared level, the crawl request will be rejected with a <code>400</code> error. Refer to <a href="#content-signals">Content Signals</a> for details.</td>
</tr>
</tbody>
</table>
<h3 id="pattern-behavior">Pattern behavior</h3>
<p><code>excludePatterns</code> has strictly higher priority. If a URL matches an exclude rule, it is skipped, regardless of whether it matches an include rule.</p>
<ul>
<li><strong>No rules</strong> — Everything is indexed.</li>
<li><strong>Exclude only</strong> — Everything is indexed except items matching the exclude patterns.</li>
<li><strong>Include only</strong> — Only items matching the include patterns are indexed; everything else is ignored.</li>
</ul>
<h3 id="viewing-skipped-urls">Viewing skipped URLs</h3>
<p>The <code>skipped</code> status applies to URLs that the crawler discovered and evaluated individually, but then chose not to fetch because they were excluded by your crawl configuration, such as <code>includeExternalLinks</code>, <code>includeSubdomains</code>, or <code>includePatterns</code>/<code>excludePatterns</code>. To view these URLs, query the crawl job results with <code>status=skipped</code>.</p>
<pre><code class="language-bash">curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}?status=skipped&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer YOUR_API_TOKEN&#x27;&#10;</code></pre>
<p>Because <code>skipped</code> only tracks URLs that were evaluated one by one, it applies mainly to crawls that use <code>source: links</code> (or <code>source: all</code>), where the crawler follows links scraped from pages and checks each one against your configuration. When crawling from a sitemap (<code>source: sitemaps</code>), URLs that fall outside your configuration are filtered out in bulk before they are evaluated individually, so they are omitted from the job entirely rather than recorded as <code>skipped</code>. As a result, the set of <code>skipped</code> URLs is not an exhaustive list of every URL that was left out of the crawl.</p>
<h3 id="render-parameter"><code>render</code> parameter</h3>
<p>If you use <code>render: true</code>, which is the default, the <code>crawl</code> endpoint spins up a headless browser and executes page JavaScript. If you use <code>render: false</code>, the <code>crawl</code> endpoint does a fast HTML fetch without executing JavaScript.</p>
<p>Use <code>render: true</code> when the page builds content in the browser. Use <code>render: false</code> when the content you need is already in the initial HTML response.</p>
<p>Crawls that use <code>render: true</code> use a headless browser and are billed under typical Browser Run pricing. Crawls that use <code>render: false</code> run on <a href="/workers/">Workers</a> instead of a headless browser. During the beta, <code>render: false</code> crawls are not billed. After the beta, they will be billed under <a href="/workers/platform/pricing/">Workers pricing</a>.</p>
<h3 id="example-with-all-optional-parameters">Example with all optional parameters</h3>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://www.exampledocs.com/docs/&quot;,&#10;    &quot;crawlPurposes&quot;: [&quot;search&quot;],&#10;    &quot;contentUse&quot;: &quot;reference&quot;,&#10;    &quot;limit&quot;: 50,&#10;    &quot;depth&quot;: 2,&#10;    &quot;formats&quot;: [&quot;markdown&quot;],&#10;    &quot;render&quot;: false,&#10;    &quot;maxAge&quot;: 7200,&#10;    &quot;modifiedSince&quot;: 1704067200,&#10;    &quot;source&quot;: &quot;all&quot;,&#10;    &quot;options&quot;: {&#10;      &quot;includeExternalLinks&quot;: true,&#10;      &quot;includeSubdomains&quot;: true,&#10;      &quot;includePatterns&quot;: [&#10;        &quot;**/api/v1/*&quot;&#10;      ],&#10;      &quot;excludePatterns&quot;: [&#10;        &quot;*/learning-paths/*&quot;&#10;      ]&#10;    }&#10;}&#x27;&#10;</code></pre>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3639.md")
</aside>
<h3 id="documentation-site-crawl">Documentation site crawl</h3>
<p>Crawl only documentation pages and exclude specific sections:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/docs&quot;,&#10;    &quot;limit&quot;: 200,&#10;    &quot;depth&quot;: 5,&#10;    &quot;formats&quot;: [&quot;markdown&quot;],&#10;    &quot;options&quot;: {&#10;      &quot;includePatterns&quot;: [&#10;        &quot;https://example.com/docs/**&quot;&#10;      ],&#10;      &quot;excludePatterns&quot;: [&#10;        &quot;https://example.com/docs/changelog/**&quot;,&#10;        &quot;https://example.com/docs/archive/**&quot;&#10;      ]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="product-catalog-extraction-with-ai">Product catalog extraction with AI</h3>
<p>Extract structured product data using the <code>json</code> format. This leverages <a href="/workers-ai/">Workers AI</a> by default. Refer to the <a href="/browser-run/quick-actions/json-endpoint/"><code>/json</code> endpoint</a> to learn more.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://shop.example.com/products&quot;,&#10;    &quot;limit&quot;: 50,&#10;    &quot;formats&quot;: [&quot;json&quot;],&#10;    &quot;jsonOptions&quot;: {&#10;      &quot;prompt&quot;: &quot;Extract product name, price, description, and availability&quot;,&#10;      &quot;response_format&quot;: {&#10;        &quot;type&quot;: &quot;json_schema&quot;,&#10;        &quot;json_schema&quot;: {&#10;          &quot;name&quot;: &quot;product&quot;,&#10;          &quot;properties&quot;: {&#10;            &quot;name&quot;: &quot;string&quot;,&#10;            &quot;price&quot;: &quot;number&quot;,&#10;            &quot;currency&quot;: &quot;string&quot;,&#10;            &quot;description&quot;: &quot;string&quot;,&#10;            &quot;inStock&quot;: &quot;boolean&quot;&#10;          }&#10;        }&#10;      }&#10;    },&#10;    &quot;options&quot;: {&#10;      &quot;includePatterns&quot;: [&#10;        &quot;https://shop.example.com/products/*&quot;&#10;      ]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="fast-static-content-fetch">Fast static content fetch</h3>
<p>Fetch static HTML without rendering for faster crawling of static sites:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;limit&quot;: 100,&#10;    &quot;render&quot;: false,&#10;    &quot;formats&quot;: [&quot;html&quot;, &quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<h3 id="crawl-with-authentication">Crawl with authentication</h3>
<p>Crawl pages behind HTTP authentication or with custom headers:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://secure.example.com&quot;,&#10;    &quot;limit&quot;: 50,&#10;    &quot;authenticate&quot;: {&#10;      &quot;username&quot;: &quot;user&quot;,&#10;      &quot;password&quot;: &quot;pass&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>You can also use cookies or custom headers for token-based authentication:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://api.example.com/docs&quot;,&#10;    &quot;limit&quot;: 100,&#10;    &quot;setExtraHTTPHeaders&quot;: {&#10;      &quot;X-API-Key&quot;: &quot;your-api-key&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="wait-for-dynamic-content">Wait for dynamic content</h3>
<p>Crawl single-page applications that load content dynamically:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://app.example.com&quot;,&#10;    &quot;limit&quot;: 50,&#10;    &quot;gotoOptions&quot;: {&#10;      &quot;waitUntil&quot;: &quot;networkidle2&quot;,&#10;      &quot;timeout&quot;: 60000&#10;    },&#10;    &quot;waitForSelector&quot;: {&#10;      &quot;selector&quot;: &quot;[data-content-loaded]&quot;,&#10;      &quot;timeout&quot;: 30000,&#10;      &quot;visible&quot;: true&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h3 id="block-unnecessary-resources">Block unnecessary resources</h3>
<p>Speed up crawling by blocking images and media. <code>rejectResourceTypes</code> is only available when <code>render</code> is <code>true</code> (the default).</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;limit&quot;: 100,&#10;    &quot;rejectResourceTypes&quot;: [&#10;      &quot;image&quot;,&#10;      &quot;media&quot;,&#10;      &quot;font&quot;,&#10;      &quot;stylesheet&quot;&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h2 id="crawler-behavior">Crawler behavior</h2>
<h3 id="how-the-crawler-discovers-urls">How the crawler discovers URLs</h3>
<p>The crawler discovers and processes URLs in the following order (when using <code>source: all</code>, the default):</p>
<ol>
<li><strong>Starting URL</strong> — The URL specified in your request.</li>
<li><strong>Sitemap links</strong> — URLs found in the site's sitemap.</li>
<li><strong>Page links</strong> — Links scraped from pages, if not already found in the sitemap.</li>
</ol>
<p>Use the <code>source</code> parameter to customize which sources the crawler uses. The available options are:</p>
<ul>
<li><code>all</code> — Uses both sitemaps and page links (default).</li>
<li><code>sitemaps</code> — Only crawls URLs found in the site's sitemap.</li>
<li><code>links</code> — Only crawls links found on pages, ignoring sitemaps.</li>
</ul>
<h3 id="robots-txt-and-bot-protection">robots.txt and bot protection</h3>
<p>The <code>/crawl</code> endpoint respects the directives of <code>robots.txt</code> files, including <code>crawl-delay</code>. If a site does not specify a <code>crawl-delay</code> in its <code>robots.txt</code>, the crawler uses a default delay of 0.5 seconds between requests to the same domain to avoid overwhelming the origin server. All URLs that <code>/crawl</code> is directed not to crawl are listed in the response with <code>&quot;status&quot;: &quot;disallowed&quot;</code>. For guidance on configuring <code>robots.txt</code> and sitemaps for sites you plan to crawl, refer to <a href="/browser-run/reference/robots-txt/">robots.txt and sitemaps</a>. If you want to block the <code>/crawl</code> endpoint from accessing your site, refer to <a href="/browser-run/reference/robots-txt/#blocking-crawlers-with-robotstxt">Blocking crawlers with robots.txt</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="bot-protection-may-block-crawling">Bot protection may block crawling</h3>
@markup("md", "content/.markup/bodies/3638.md")
</aside>
<h3 id="user-agent">User-Agent</h3>
<p>The <code>/crawl</code> endpoint uses <code>CloudflareBrowserRenderingCrawler/1.0</code> as its User-Agent, which is different from other <a href="/browser-run/quick-actions/">Quick Actions</a> endpoints. This User-Agent is not customizable. Unlike other Quick Actions endpoints, the <code>userAgent</code> parameter is not supported on the <code>/crawl</code> endpoint.</p>
<p>For a full list of default User-Agent strings, refer to <a href="/browser-run/reference/automatic-request-headers/#user-agent">Automatic request headers</a>.</p>
<h3 id="content-signals">Content Signals</h3>
<p>The <code>/crawl</code> endpoint respects <a href="https://contentsignals.org/">Content Signals</a> directives found in a target site's <code>robots.txt</code> file. Content Signals are a way for site owners to express preferences about how their content can be used by automated systems. For more background, refer to <a href="https://blog.cloudflare.com/content-signals-policy/">Giving users choice with Cloudflare's new Content Signals Policy</a>.</p>
<p>A site owner can include a <code>Content-Signal</code> directive in their <code>robots.txt</code> to allow or disallow specific categories of use:</p>
<ul>
<li><code>search</code> — Building a search index and providing search results with links and excerpts.</li>
<li><code>ai-input</code> — Inputting content into AI models at query time (for example, retrieval-augmented generation or grounding).</li>
<li><code>ai-train</code> — Training or fine-tuning AI models.</li>
</ul>
<p>For example, a <code>robots.txt</code> that allows search indexing but disallows AI training:</p>
<pre><code class="language-txt">User-Agent: *&#10;Content-Signal: search=yes, ai-train=no&#10;Allow: /&#10;</code></pre>
<p>A site owner can also declare a <code>use</code> directive to express the maximum level at which their content may be used. The levels, from least to most permissive, are:</p>
<ul>
<li><code>immediate</code> — Ephemeral, single-response use, where content is not retained.</li>
<li><code>reference</code> — Content may be retained, indexed, or cited.</li>
<li><code>full</code> — Unrestricted use, including AI training.</li>
</ul>
<p>For example, a <code>robots.txt</code> that limits use to <code>reference</code>:</p>
<pre><code class="language-txt">User-Agent: *&#10;Content-Signal: use=reference&#10;Allow: /&#10;</code></pre>
<h4 id="how-crawl-enforces-content-signals">How /crawl enforces Content Signals</h4>
<p>The <code>/crawl</code> endpoint enforces both the yes/no purpose directives (<code>search</code>, <code>ai-input</code>, <code>ai-train</code>) and the <code>use</code> level directive.</p>
<p><strong>Purpose directives</strong></p>
<p>By default, <code>/crawl</code> declares all three purposes: <code>[&quot;search&quot;, &quot;ai-input&quot;, &quot;ai-train&quot;]</code>. If a target site sets any of those content signals to <code>no</code>, the crawl request will be rejected at initiation with a <code>400 Bad Request</code> error unless you explicitly narrow your declared purposes using the <code>crawlPurposes</code> parameter to exclude the disallowed use.</p>
<p>This means:</p>
<ol>
<li><strong>Site has no Content Signals</strong> — The crawl proceeds normally.</li>
<li><strong>Site has Content Signals, and all your declared purposes are allowed</strong> — The crawl proceeds normally.</li>
<li><strong>Site sets a content signal to <code>no</code>, and that purpose is in your <code>crawlPurposes</code></strong> — The crawl request is rejected with a <code>400</code> error and the message <code>Crawl disallowed by Content-Signal directive (purpose or use level)</code>.</li>
</ol>
<p>To crawl a site that disallows AI training but allows search, set <code>crawlPurposes</code> to only the purposes you need:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;crawlPurposes&quot;: [&quot;search&quot;],&#10;    &quot;formats&quot;: [&quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<p>In this example, because the operator declared only <code>search</code> as their purpose, the crawl will succeed even if the site sets <code>ai-train=no</code>.</p>
<p><strong>Use level directive</strong></p>
<p>The <code>contentUse</code> parameter declares the level at which you intend to use the crawled content. Allowed values, from least to most permissive, are <code>reference</code> and <code>full</code>. The default is <code>full</code>.</p>
<p>The <code>immediate</code> level is not accepted as a <code>contentUse</code> value because the <code>/crawl</code> endpoint stores crawled content, which is not compatible with ephemeral, single-response use.</p>
<p>A crawl is rejected when your declared <code>contentUse</code> level is more permissive than the site's declared <code>use</code> level. For example:</p>
<ol>
<li><strong>Site sets <code>use=full</code> (or does not set <code>use</code>)</strong> — Any <code>contentUse</code> value is allowed.</li>
<li><strong>Site sets <code>use=reference</code></strong> — A crawl with <code>contentUse: &quot;reference&quot;</code> is allowed, but the default <code>contentUse: &quot;full&quot;</code> is rejected.</li>
<li><strong>Site sets <code>use=immediate</code></strong> — All crawls are rejected, because both <code>reference</code> and <code>full</code> exceed the declared level.</li>
</ol>
<p>To crawl a site that sets <code>use=reference</code>, set <code>contentUse</code> to <code>reference</code>:</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;contentUse&quot;: &quot;reference&quot;,&#10;    &quot;formats&quot;: [&quot;markdown&quot;]&#10;  }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3637.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="crawl-job-returns-no-results-or-all-urls-are-skipped">Crawl job returns no results or all URLs are skipped</h3>
<p>If your crawl job completes but returns an empty records array, or all URLs show <code>skipped</code> or <code>disallowed</code> status:</p>
<ul>
<li><strong>robots.txt blocking</strong> — The crawler respects <code>robots.txt</code> rules. The <code>/crawl</code> endpoint identifies itself as <code>CloudflareBrowserRenderingCrawler/1.0</code>. Check the target site's <code>robots.txt</code> file to verify this user agent is allowed. Blocked URLs appear with <code>&quot;status&quot;: &quot;disallowed&quot;</code>.</li>
<li><strong>Pattern filters too restrictive</strong> — Your <code>includePatterns</code> may not match any URLs on the site. Try crawling without patterns first to confirm URLs are discoverable, then add patterns.</li>
<li><strong>No links found</strong> — The starting URL may not contain links. Try using <code>source: &quot;sitemaps&quot;</code>, increasing the <code>depth</code> parameter, or setting <code>includeSubdomains</code> or <code>includeExternalLinks</code> to <code>true</code>.</li>
</ul>
<h3 id="crawl-rejected-by-content-signals">Crawl rejected by Content Signals</h3>
<p>If your crawl request returns a <code>400 Bad Request</code> with the message <code>Crawl disallowed by Content-Signal directive (purpose or use level)</code>, the target site's <code>robots.txt</code> includes a <code>Content-Signal</code> directive that disallows one or more of your declared <code>crawlPurposes</code>, or a <code>use</code> directive that is more restrictive than your declared <code>contentUse</code> level. To resolve this, check the site's <code>robots.txt</code> for <code>Content-Signal:</code> entries:</p>
<ul>
<li>If the site sets a purpose to <code>no</code>, set <code>crawlPurposes</code> to only the purposes you need. For example, if the site sets <code>ai-train=no</code> and you only need search indexing, use <code>&quot;crawlPurposes&quot;: [&quot;search&quot;]</code>.</li>
<li>If the site sets a <code>use</code> level, set <code>contentUse</code> to a level at or below it. For example, if the site sets <code>use=reference</code>, use <code>&quot;contentUse&quot;: &quot;reference&quot;</code>.</li>
</ul>
<p>Refer to <a href="#content-signals">Content Signals</a> for details.</p>
<h3 id="crawl-job-takes-too-long">Crawl job takes too long</h3>
<p>If a crawl job remains in <code>running</code> status for an extended period:</p>
<ul>
<li><strong>Slow page loads</strong> — Pages with heavy JavaScript take longer to render. Use <code>render: false</code> if the content you need is in the initial HTML.</li>
<li><strong>Rate limiting</strong> — The crawler enforces a per-domain rate limit to avoid overwhelming origin servers. If a site specifies a <code>crawl-delay</code> in its <code>robots.txt</code>, the crawler respects it. Otherwise, the crawler uses a default delay of 0.5 seconds between requests to the same domain. If you run multiple crawl jobs targeting the same domain, they share the same per-domain rate limit, which can cause all jobs to take longer than if each ran individually.</li>
<li><strong>Unnecessary resources</strong> — Block resources that are not needed for content extraction using <code>rejectResourceTypes</code> (for example, <code>image</code>, <code>media</code>, <code>font</code>).</li>
</ul>
<h3 id="crawl-job-cancelled-due-to-limits">Crawl job cancelled due to limits</h3>
<p>A <code>cancelled_due_to_limits</code> status means your account hit its browser time limit. <a href="/browser-run/limits/#workers-free">Workers Free plan</a> accounts are capped at 10 minutes of browser use per day. To resolve this:</p>
<ul>
<li><a href="/workers/platform/pricing/">Upgrade to a Workers Paid plan</a> for higher <a href="/browser-run/limits/#workers-paid">limits</a>.</li>
<li>Use <code>render: false</code> for static content to avoid consuming browser time.</li>
<li>Increase <code>maxAge</code> to use cached results where possible.</li>
<li>Reduce the <code>limit</code> parameter.</li>
</ul>
<h3 id="json-extraction-errors">JSON extraction errors</h3>
<p>If the <code>json</code> format returns null or empty results:</p>
<ul>
<li><strong>Provide a clear prompt</strong> — Be specific about what data to extract and where it appears on the page (for example, &quot;Extract the product name, price, and description from the main product section&quot;).</li>
<li><strong>Define a response schema</strong> — Use <code>response_format</code> with a JSON schema to enforce the expected output structure.</li>
<li><strong>Use a custom model</strong> — If the default <a href="/workers-ai/">Workers AI</a> model does not produce the desired results, use the <code>custom_ai</code> parameter to specify a different model. Refer to <a href="/browser-run/quick-actions/json-endpoint/#using-a-custom-model-byo-api-key">Using a custom model (BYO API Key)</a> for details.</li>
</ul>
<p>If you have questions or encounter other errors, refer to the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
<h2 id="troubleshooting-1">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
