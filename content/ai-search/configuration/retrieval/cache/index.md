<p>Similarity-based caching in AI Search lets you serve responses from Cloudflare's cache for queries that are similar to previous requests, rather than creating new, unique responses for every request. This speeds up response times and cuts costs by reusing answers for questions that are close in meaning.</p>
<h2 id="how-it-works">How it works</h2>
<p>Unlike with basic caching, which creates a new response with every request, this is what happens when a request is received using similarity-based caching:</p>
<ol>
<li>AI Search checks if a <em>similar</em> prompt (based on your chosen threshold) has been answered before.</li>
<li>If a match is found, it returns the cached response instantly.</li>
<li>If no match is found, it generates a new response and caches it.</li>
</ol>
<p>To see if a response came from the cache, check the <code>cf-aig-cache-status</code> header: <code>HIT</code> for cached and <code>MISS</code> for new.</p>
<h2 id="what-to-consider-when-using-similarity-cache">What to consider when using similarity cache</h2>
<p>Consider these behaviors when using similarity caching:</p>
<ul>
<li><strong>Volatile Cache</strong>: If two similar requests hit at the same time, the first might not cache in time for the second to use it, resulting in a <code>MISS</code>.</li>
<li><strong>Configurable duration</strong>: Cached responses expire based on the instance's <code>cache_ttl</code> setting. The default is 48 hours.</li>
<li><strong>Data Dependency</strong>: Cached responses are tied to specific document chunks. If those chunks change or get deleted, the cache clears to keep answers fresh.</li>
</ul>
<h2 id="how-similarity-matching-works">How similarity matching works</h2>
<p>AI Search's similarity cache uses <strong>MinHash and Locality-Sensitive Hashing (LSH)</strong> to find and reuse responses for prompts that are worded similarly.</p>
<p>Here's how it works when a new prompt comes in:</p>
<ol>
<li>The prompt is split into small overlapping chunks of words (called shingles), like &quot;what's the&quot; or &quot;the weather.&quot;</li>
<li>These shingles are turned into a &quot;fingerprint&quot; using MinHash. The more overlap two prompts have, the more similar their fingerprints will be.</li>
<li>Fingerprints are placed into LSH buckets, which help AI Search quickly find similar prompts without comparing every single one.</li>
<li>If a past prompt in the same bucket is similar enough (based on your configured threshold), AI Search reuses its cached response.</li>
</ol>
<h2 id="choose-a-threshold">Choose a threshold</h2>
<p>The similarity threshold decides how close two prompts need to be to reuse a cached response. You can set the threshold at the instance level or override it per request.</p>
<table>
<thead>
<tr>
<th>Threshold</th>
<th>API value</th>
<th>Description</th>
<th>Example match</th>
</tr>
</thead>
<tbody>
<tr>
<td>Exact</td>
<td><code>super_strict_match</code></td>
<td>Near-identical matches only</td>
<td>&quot;What's the weather like today?&quot; matches with &quot;What is the weather like today?&quot;</td>
</tr>
<tr>
<td>Strong</td>
<td><code>close_enough</code> (default)</td>
<td>High semantic similarity</td>
<td>&quot;What's the weather like today?&quot; matches with &quot;How's the weather today?&quot;</td>
</tr>
<tr>
<td>Broad</td>
<td><code>flexible_friend</code></td>
<td>Moderate match, more hits</td>
<td>&quot;What's the weather like today?&quot; matches with &quot;Tell me today's weather&quot;</td>
</tr>
<tr>
<td>Loose</td>
<td><code>anything_goes</code></td>
<td>Low similarity, max reuse</td>
<td>&quot;What's the weather like today?&quot; matches with &quot;Give me the forecast&quot;</td>
</tr>
</tbody>
</table>
<h2 id="set-cache-duration">Set cache duration</h2>
<p>Set <code>cache_ttl</code> when creating or updating an instance to control how long the instance retains cached responses. Allowed values are:</p>
<table>
<thead>
<tr>
<th>Duration</th>
<th>API value</th>
</tr>
</thead>
<tbody>
<tr>
<td>10 minutes</td>
<td><code>600</code></td>
</tr>
<tr>
<td>30 minutes</td>
<td><code>1800</code></td>
</tr>
<tr>
<td>1 hour</td>
<td><code>3600</code></td>
</tr>
<tr>
<td>2 hours</td>
<td><code>7200</code></td>
</tr>
<tr>
<td>6 hours</td>
<td><code>21600</code></td>
</tr>
<tr>
<td>12 hours</td>
<td><code>43200</code></td>
</tr>
<tr>
<td>24 hours</td>
<td><code>86400</code></td>
</tr>
<tr>
<td>48 hours</td>
<td><code>172800</code></td>
</tr>
<tr>
<td>72 hours</td>
<td><code>259200</code></td>
</tr>
<tr>
<td>6 days</td>
<td><code>518400</code></td>
</tr>
</tbody>
</table>
<h2 id="purge-cached-responses">Purge cached responses</h2>
<p>To clear all cached responses for an instance immediately, use the purge cache operation:</p>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/namespaces/default/instances/$INSTANCE_NAME/purge_cache&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Purging the cache rotates the instance's internal cache key, so new queries do not reuse previous cached responses.</p>
<p>You can also purge cached responses from the instance settings page in the Cloudflare dashboard.</p>
<h2 id="per-request-cache-override">Per-request cache override</h2>
<p>You can override the instance-level cache setting on a per-request basis using the <code>cache</code> parameter in <code>ai_search_options</code>:</p>
<pre><code class="language-ts">const instance = env.AI_SEARCH.get(&quot;my-instance&quot;);&#10;&#10;const results = await instance.search({&#10;	messages: [{ role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot; }],&#10;	ai_search_options: {&#10;		cache: {&#10;			enabled: true,&#10;			cache_threshold: &quot;flexible_friend&quot;,&#10;		},&#10;	},&#10;});&#10;</code></pre>
