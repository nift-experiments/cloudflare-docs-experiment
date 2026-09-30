<p>When a browser requests a page, the origin server takes time to prepare the full response. Early Hints uses this wait time to send the browser a preliminary <code>103</code> response containing <code>Link</code> headers that tell the browser which assets it will need. The browser can start loading those assets before the full response arrives, which speeds up page loads.</p>
<p>Early Hints is defined in <a href="https://httpwg.org/specs/rfc8297.html">RFC 8297</a> as a new HTTP status code (<code>103 Early Hints</code>). Cloudflare caches and serves these <code>103</code> responses with <code>Link</code> headers from your HTML pages, reducing user-perceived latency.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3850.md")
</aside>
<p>For more information about Early Hints, refer to the <a href="https://blog.cloudflare.com/early-hints">Cloudflare</a> and <a href="https://developer.chrome.com/en/blog/early-hints/">Google Chrome</a> blogs.</p>
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
<h2 id="enable-early-hints">Enable Early Hints</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Speed</strong> &gt; <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Content Optimization</strong> tab.</li>
<li>For <strong>Early Hints</strong>, toggle the switch to <strong>On</strong>.</li>
</ol>
<h2 id="generate-early-hints">Generate Early Hints</h2>
<p>Early Hints are only generated and cached:</p>
<ul>
<li>For URIs with <code>.html</code>, <code>.htm</code>, or <code>.php</code> file extensions, or no file extension</li>
<li>On 200, 301, or 302 response return codes</li>
<li>When the response contains <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link">link headers</a> with preconnect or preload rel types, such as <code>Link: &lt;/img/preloaded.png&gt;; rel=preload</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3849.md")
</aside>
<h2 id="emit-early-hints">Emit Early Hints</h2>
<p>Cloudflare will asynchronously look up and emit a cached 103 Early Hints response ahead of a main response.</p>
<p>Currently, only certain browser versions will take action to preload or preconnect on receiving Early Hints, such as Google Chrome M94 and higher. Instructions for running WebPageTest to experiment with compatible client browsers can be found in the <a href="https://blog.cloudflare.com/early-hints/#testing-early-hints-with-web-page-test">blog post</a>.</p>
<p>Additionally, keep the following in mind:</p>
<ul>
<li>Early Hints responses may be emitted before reaching the origin server or Worker. When Early Hints is enabled and pages on your site require authentication, unauthenticated visitors may receive a 103 response. The 103 response would contain cached Link headers and be sent before a 403 Forbidden response from your origin.</li>
<li>Early Hints may be emitted less frequently on requests where the content is cacheable. Cloudflare CDN is more likely to retrieve a response header before the asynchronous Early Hints lookup finishes if the response has been cached. Cloudflare will not send a 103 response if the main response header is already available.</li>
<li>Cloudflare currently disables Early Hints on some User-Agents, for example, select search crawler bots that show incompatibility with 1xx responses.</li>
<li>You may see an influx of <code>504</code> responses with <code>ClientRequestSource: earlyHintsCache</code> in Cloudflare Logs when Early Hints is enabled, which is expected and benign. Requests with this source are internal subrequests for cached Early Hints; they are neither end user requests, nor do they reach your origin. Their response status only indicates whether there are cached Early Hints for the request URI (<code>200</code> on cache HIT, <code>504</code> on cache MISS). These requests are already filtered out in other views, such as Cache Analytics. To filter them out of Log Explorer, use <code>ClientRequestSource != &quot;earlyHintsCache&quot;</code>. To filter using the GraphQL API, refer to <a href="/analytics/graphql-api/features/filtering/#filter-end-users">Filter end users</a>.</li>
</ul>
