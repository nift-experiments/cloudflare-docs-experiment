<p>Crawler Hints uses Cloudflare cache signals to tell search engines when your content has likely changed, so they crawl your site at the right time instead of guessing.</p>
<h2 id="background">Background</h2>
<p>Search engines and similar services operate massive networks of bots that crawl the Internet to identify the content most relevant to a user query. Content on the web is always changing though, and search engine crawlers must continually wander the Internet and guess how frequently they should check a site for content updates.</p>
<p>With Crawler Hints, Cloudflare can proactively tell a crawler about the best time to index or when content changes. Additionally, Crawler Hints supports <a href="https://www.indexnow.org/">IndexNow</a>, which allows websites to notify search engines whenever content on their website content is created, updated, or deleted. Crawler Hints uses cache-status <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> to determine when content has likely been updated and sends it to IndexNow's crawler. If an asset's response has an HTTP status code greater than 4xx, the Crawler hints will not report that to <a href="https://www.indexnow.org/">IndexNow</a>.</p>
<h2 id="benefits">Benefits</h2>
<p>Crawler Hints help search engines and other bot-powered services serve the freshest version of your content, which can improve search rankings.</p>
<p>Crawler Hints also reduces unnecessary crawl traffic to your origin, lowering resource consumption and improving site performance.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-crawler-hints">Enable Crawler Hints</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enable <strong>Crawler Hints</strong>.</li>
</ol>
<p>After enabling Crawler Hints, Cloudflare will begin sending hints to search engines about when they should crawl particular parts of your website.</p>
<h2 id="prevent-indexing-for-a-specific-page">Prevent indexing for a specific page</h2>
<p>When enabled, Crawler Hints is a global setting for your entire website. You can stop a specific page from being indexed by either:</p>
<ul>
<li>Having the origin server send through the header <code>X-Robots-Tag: noindex</code> on any pages that should not be indexed.</li>
<li>Including <code>&lt;meta name=&quot;robots&quot; content=&quot;noindex, nofollow&quot; /&gt;</code> in the HTML of any pages that should not be indexed.</li>
<li>Creating a <a href="/rules/transform/response-header-modification/">Response header Transform Rule</a> in Cloudflare to add the <code>X-Robots-Tag: noindex</code> header instead of doing it from the origin server.</li>
</ul>
