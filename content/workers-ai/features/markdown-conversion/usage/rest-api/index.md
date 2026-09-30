<p>You can also use the Markdown Conversion REST API to convert your documents into Markdown.</p>
<h2 id="prerequisite-get-workers-ai-api-token">Prerequisite: Get Workers AI API token</h2>
<p>To use the Markdown Conversion service via the REST API, you need an API token with permissions for the <a href="/workers-ai/">Workers AI</a> REST API. Refer to <a href="/workers-ai/get-started/rest-api/">Get started with the Workers AI REST API</a> for instructions on obtaining an API token with the correct permissions.</p>
<h2 id="transform">Transform</h2>
<p>This endpoint lets you convert any file given to us into markdown.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &quot;files=@cat.jpeg&quot; \&#10;  &#45;F &quot;files=@somatosensory.pdf&quot; \&#10;  &#45;F &#x27;conversionOptions={ ... }&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15833.md")
</aside>
<h3 id="parameters">Parameters</h3>
<p><code>files</code> <span class="nb-type">File[]</span> <span class="nb-metainfo">required</span></p>
<p>The files you want to convert.</p>
<p><code>conversionOptions</code> <span class="nb-type">ConversionOptions</span> <span class="nb-metainfo">optional</span></p>
<p>Options that allow you to control how your files are converted. Refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a> for further details.</p>
<h3 id="response">Response</h3>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;...&quot;,&#10;			&quot;name&quot;: &quot;good.html&quot;,&#10;			&quot;mimeType&quot;: &quot;text/html&quot;,&#10;			&quot;format&quot;: &quot;markdown&quot;,&#10;			&quot;tokens&quot;: 49,&#10;			&quot;data&quot;: &quot;# Image Embedded with a Data URI\n\nThis _image_ is directly encoded in the HTML:\n\n\n\nAn image description\n\n \n\nIt&#x27;s a tiny 5x5 pixel PNG, scaled up to 50x50px.\n\n&quot;&#10;		},&#10;		{&#10;			&quot;id&quot;: &quot;...&quot;,&#10;			&quot;name&quot;: &quot;bad.pdf&quot;,&#10;			&quot;mimeType&quot;: &quot;application/pdf&quot;,&#10;			&quot;format&quot;: &quot;error&quot;,&#10;			&quot;error&quot;: &quot;Some error that prevented this image from being converted&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="supported">Supported</h2>
<p>This endpoint lets you programmatically retrieve the full set of rich formats that are supported for conversion.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown/supported \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15832.md")
</aside>
<h3 id="response-1">Response</h3>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;extension&quot;: &quot;.html&quot;,&#10;      &quot;mimeType&quot;: &quot;text/html&quot;&#10;    },&#10;    {&#10;      &quot;extension&quot;: &quot;.pdf&quot;,&#10;      &quot;mimeType&quot;: &quot;application/pdf&quot;&#10;    },&#10;    ...&#10;  ]&#10;}&#10;</code></pre>
