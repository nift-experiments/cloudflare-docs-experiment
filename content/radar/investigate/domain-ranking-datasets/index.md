<p>Cloudflare regularly generates a domain ranking based on DNS queries to <a href="/1.1.1.1/">1.1.1.1</a>,  Cloudflare's public DNS resolver.  Refer to the <a href="https://blog.cloudflare.com/radar-domain-rankings/">blog post</a> for a deep dive. In short, Cloudflare generates two types of listings:</p>
<ul>
<li>An ordered list of the top 100 most popular domains globally and per country. This includes the last 24 hours and is updated daily.</li>
<li>An unordered global most popular domains dataset, divided into buckets of the following number of domains: 200, 500, 1,000, 2,000, 5,000, 10,000, 20,000, 50,000, 100,000, 200,000, 500,000, 1,000,000. It includes the last seven days and is updated weekly.</li>
</ul>
<h2 id="list-of-endpoints">List of endpoints</h2>
<h3 id="top">Top</h3>
<h4 id="example-get-the-current-ordered-top-domains-in-the-cloudflare-ranking">Example: Get the current ordered top domains in the Cloudflare ranking</h4>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/ranking/top?name=top&amp;limit=5&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;top_0&quot;: [&#10;			{&#10;				&quot;rank&quot;: 1,&#10;				&quot;domain&quot;: &quot;google.com&quot;&#10;			},&#10;			{&#10;				&quot;rank&quot;: 2,&#10;				&quot;domain&quot;: &quot;googleapis.com&quot;&#10;			},&#10;			{&#10;				&quot;rank&quot;: 3,&#10;				&quot;domain&quot;: &quot;facebook.com&quot;&#10;			},&#10;			{&#10;				&quot;rank&quot;: 4,&#10;				&quot;domain&quot;: &quot;gstatic.com&quot;&#10;			},&#10;			{&#10;				&quot;rank&quot;: 5,&#10;				&quot;domain&quot;: &quot;apple.com&quot;&#10;			}&#10;    ]&#10;  },&#10;	&quot;meta&quot;: {&#10;		// ...&#10;	}&#10;}&#10;</code></pre>
<p>For more information refer to <a href="/api/resources/radar/subresources/ranking/methods/top/">Get top domains</a>.</p>
<h4 id="example-download-top-x-ranking-bucket-file">Example: Download top <code>x</code> ranking bucket file</h4>
<p>As mentioned in the <a href="https://blog.cloudflare.com/radar-domain-rankings/">blog post</a>, Cloudflare provides an ordered rank
for the top 100 domains, but for the remainder it only provides ranking buckets — like top 200 thousand, top one million,
etc.. These are available through Cloudflare's <a href="/api/resources/radar/subresources/datasets/methods/list/">datasets endpoints</a>.</p>
<p>In the following example we will request the last available domain ranking buckets:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/datasets?limit=10&amp;datasetType=RANKING_BUCKET&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;		&quot;datasets&quot;: [&#10;			{&#10;				&quot;id&quot;: 213,&#10;				&quot;title&quot;: &quot;Top 1000000 ranking domains&quot;,&#10;				&quot;description&quot;: &quot;Unordered top 1000000 from 2023-01-02 to 2023-01-09&quot;,&#10;				&quot;type&quot;: &quot;RANKING_BUCKET&quot;,&#10;				&quot;tags&quot;: [&#10;					&quot;GLOBAL&quot;,&#10;					&quot;top_1000000&quot;&#10;				],&#10;				&quot;meta&quot;: {&#10;					&quot;top&quot;: 1000000&#10;				},&#10;				&quot;alias&quot;: &quot;ranking_top_1000000&quot;&#10;			},&#10;			// ...&#10;		]&#10;	}&#10;}&#10;</code></pre>
<p>If you are interested in a specific top (like the top one million), go through the <code>meta.top</code> property. After finding the top you are looking for, get its <code>id</code> to fetch the dataset using the <a href="/api/resources/radar/subresources/datasets/methods/download/"><code>GET dataset download url</code></a> endpoint.</p>
<p>Then you can request a download url:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/datasets/download&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;datasetId&quot;: 213&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;		&quot;dataset&quot;: {&#10;			&quot;url&quot;: &quot;https://example.com/download&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="example-get-the-last-top-x-ranking-bucket">Example: Get the last top <code>x</code> ranking bucket</h4>
<p>This endpoint allows you to directly request the latest top x bucket available (optionally at a given date)
<a href="/api/resources/radar/subresources/datasets/methods/get/">Get dataset stream</a> endpoint.</p>
<p>The dataset alias can be retrieved from the <a href="/api/resources/radar/subresources/datasets/methods/list/">Get datasets</a> endpoint
as the example above.</p>
<p>This stream endpoint is only available for datasets generated after 2023-01-08.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/datasets/ranking_top_1000&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-csv">domain&#10;1rx.io&#10;2mdn.net&#10;360yield.com&#10;3lift.com&#10;a-msedge.net&#10;a2z.com&#10;...&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Refer to <a href="/radar/investigate/outages/">Investigate outages</a> to get data from outages occurring around the world.</p>
