<h2 id="create-a-function">Create a function</h2>
<p>This tutorial creates a custom Google Sheets function that queries Cloudflare's 1.1.1.1 DNS resolver using DNS over HTTPS (DoH) — a protocol that encrypts DNS lookups over HTTPS. Once set up, you can type a formula like <code>=NSLookup(&quot;A&quot;, &quot;example.com&quot;)</code> in any cell to retrieve DNS records without leaving your spreadsheet. This is useful for bulk domain audits, migration planning, or monitoring DNS changes across many domains at once.</p>
<p>To get started, open your Google Sheet and create a <a href="https://developers.google.com/apps-script/guides/sheets/functions">custom function in Google Apps Script</a> with the following code:</p>
<pre><code class="language-js">function NSLookup(type, domain, useCache = false, minCacheTTL = 30) {&#10;	// --- Parameter validation ---&#10;	if (typeof type == &quot;undefined&quot;) {&#10;		throw new Error(&quot;Missing parameter 1 dns type&quot;);&#10;	}&#10;&#10;	if (typeof domain == &quot;undefined&quot;) {&#10;		throw new Error(&quot;Missing parameter 2 domain name&quot;);&#10;	}&#10;&#10;	if (typeof useCache != &quot;boolean&quot;) {&#10;		throw new Error(&quot;Only boolean values allowed in 3 use cache&quot;);&#10;	}&#10;&#10;	if (typeof minCacheTTL != &quot;number&quot;) {&#10;		throw new Error(&quot;Only numeric values allowed in 4 min cache ttl&quot;);&#10;	}&#10;&#10;	type = type.toUpperCase();&#10;	domain = domain.toLowerCase();&#10;&#10;	// --- Optional caching layer (uses Google Apps Script CacheService) ---&#10;	let cache = null;&#10;	if (useCache) {&#10;		// Cache key and hash&#10;		cacheKey = domain + &quot;@&quot; + type;&#10;		cacheHash = Utilities.base64Encode(cacheKey);&#10;		cacheBinKey = &quot;nslookup-result-&quot; + cacheHash;&#10;&#10;		cache = CacheService.getScriptCache();&#10;		const cachedResult = cache.get(cacheBinKey);&#10;		if (cachedResult != null) {&#10;			return cachedResult;&#10;		}&#10;	}&#10;&#10;	// --- DNS-over-HTTPS query to Cloudflare&#x27;s 1.1.1.1 resolver ---&#10;	const url =&#10;		&quot;https://cloudflare-dns.com/dns-query?name=&quot; +&#10;		encodeURIComponent(domain) +&#10;		&quot;&amp;type=&quot; +&#10;		encodeURIComponent(type);&#10;	const options = {&#10;		muteHttpExceptions: true,&#10;		headers: {&#10;			accept: &quot;application/dns-json&quot;,&#10;		},&#10;	};&#10;&#10;	const result = UrlFetchApp.fetch(url, options);&#10;	const rc = result.getResponseCode();&#10;	const resultText = result.getContentText();&#10;&#10;	if (rc !== 200) {&#10;		throw new Error(rc);&#10;	}&#10;&#10;	// --- Standard DNS response codes ---&#10;	const errors = [&#10;		{ name: &quot;NoError&quot;, description: &quot;No Error&quot; }, // 0&#10;		{ name: &quot;FormErr&quot;, description: &quot;Format Error&quot; }, // 1&#10;		{ name: &quot;ServFail&quot;, description: &quot;Server Failure&quot; }, // 2&#10;		{ name: &quot;NXDomain&quot;, description: &quot;Non-Existent Domain&quot; }, // 3&#10;		{ name: &quot;NotImp&quot;, description: &quot;Not Implemented&quot; }, // 4&#10;		{ name: &quot;Refused&quot;, description: &quot;Query Refused&quot; }, // 5&#10;		{ name: &quot;YXDomain&quot;, description: &quot;Name Exists when it should not&quot; }, // 6&#10;		{ name: &quot;YXRRSet&quot;, description: &quot;RR Set Exists when it should not&quot; }, // 7&#10;		{ name: &quot;NXRRSet&quot;, description: &quot;RR Set that should exist does not&quot; }, // 8&#10;		{ name: &quot;NotAuth&quot;, description: &quot;Not Authorized&quot; }, // 9&#10;	];&#10;&#10;	const response = JSON.parse(resultText);&#10;&#10;	if (response.Status !== 0) {&#10;		return errors[response.Status].name;&#10;	}&#10;&#10;	// --- Extract answer records and determine cache TTL ---&#10;	const outputData = [];&#10;	let cacheTTL = 0;&#10;&#10;	for (const i in response.Answer) {&#10;		outputData.push(response.Answer[i].data);&#10;		const ttl = response.Answer[i].TTL;&#10;		cacheTTL = Math.min(cacheTTL || ttl, ttl);&#10;	}&#10;&#10;	const outputString = outputData.join(&quot;,&quot;);&#10;&#10;	if (useCache) {&#10;		cache.put(cacheBinKey, outputString, Math.max(cacheTTL, minCacheTTL));&#10;	}&#10;&#10;	return outputString;&#10;}&#10;</code></pre>
<h2 id="using-1-1-1-1">Using 1.1.1.1</h2>
<p>When you call the <code>NSLookup</code> function with a record type and a domain, the cell displays the corresponding DNS record value — the data (such as an IP address) that DNS returns for that domain and record type.</p>
<p>The full function signature is:</p>
<p><code>=NSLookup(type, domain, useCache, minCacheTTL)</code></p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>type</code></td>
<td>Yes</td>
<td>—</td>
<td>DNS record type to query (for example, <code>A</code>, <code>AAAA</code>, <code>MX</code>).</td>
</tr>
<tr>
<td><code>domain</code></td>
<td>Yes</td>
<td>—</td>
<td>The domain name to look up.</td>
</tr>
<tr>
<td><code>useCache</code></td>
<td>No</td>
<td><code>false</code></td>
<td>Set to <code>true</code> to cache results using Google Apps Script's CacheService, which reduces repeated DNS lookups in large spreadsheets.</td>
</tr>
<tr>
<td><code>minCacheTTL</code></td>
<td>No</td>
<td><code>30</code></td>
<td>Minimum cache duration in seconds. The actual TTL is the higher of this value or the TTL returned by the DNS response.</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>Supported DNS record types</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1820.md")
</div></details>
<p>For example, if cell <code>B1</code> contains <code>A</code> (the record type) and <code>B2</code> contains <code>example.com</code> (the domain), typing the following formula in another cell:</p>
<pre><code class="language-txt">=NSLookup(B1, B2)&#10;</code></pre>
<p>Depending on your regional settings, you may need to use a semicolon as the argument separator:</p>
<pre><code class="language-txt">=NSLookup(B1; B2)&#10;</code></pre>
<div class="medium-img">
<p><img src="/assets/upstream/images/1.1.1.1/google-sheet-function.png" alt="Google Sheets cell containing the NSLookup formula" /></p>
</div>
<br />
<p>Returns the <code>A</code> record for that domain:</p>
<pre><code class="language-txt">198.41.214.162, 198.41.215.162&#10;</code></pre>
<div class="medium-img">
<p><img src="/assets/upstream/images/1.1.1.1/google-sheet-result.png" alt="Google Sheets cell displaying the DNS lookup result" /></p>
</div>
