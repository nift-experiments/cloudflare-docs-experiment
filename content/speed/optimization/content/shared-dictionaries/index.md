<p>Shared dictionaries (<a href="https://datatracker.ietf.org/doc/rfc9842/">RFC 9842</a>) let your origin compress a response against a copy of the same — or a different — resource that the visitor's browser already has cached. Only the difference between the two resources travels over the wire.</p>
<p>This is most effective for versioned assets that change incrementally between deploys, such as JavaScript bundles, CSS files, and framework chunks. After a deploy, returning visitors can receive the new asset as a small delta against the version they already have, instead of redownloading the full file.</p>
<p>Cloudflare supports shared dictionaries in <strong>passthrough</strong> mode: your origin manages dictionaries and produces delta-compressed responses. Cloudflare forwards the dictionary headers and <code>dcb</code>/<code>dcz</code> content encodings without modifying or recompressing them, and varies the cache so each delta-compressed variant is stored separately.</p>
<p>For background on the other compression algorithms Cloudflare supports, refer to <a href="/speed/optimization/content/compression/">Content compression</a>.</p>
<hr />
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
<td>Yes (beta)</td>
<td>Yes (beta)</td>
<td>Yes (beta)</td>
<td>Yes (beta)</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="requirements">Requirements</h2>
<p>Shared dictionaries work when all of the following are true:</p>
<ul>
<li>The visitor's browser supports <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport">compression dictionary transport</a>. Today, this is Chrome 130 or later, Edge 130 or later, or another Chromium browser at the same version.</li>
<li>The browser request includes <code>dcb</code> or <code>dcz</code> in <code>Accept-Encoding</code> and an <code>Available-Dictionary</code> header.</li>
<li>Your origin returns a delta-compressed response with <code>Content-Encoding: dcb</code> or <code>dcz</code> and a <code>Vary</code> header that includes <code>Accept-Encoding, Available-Dictionary</code>.</li>
<li>The dictionary, the delta response, and the request are served over HTTPS from the same origin. Per <a href="https://www.rfc-editor.org/rfc/rfc9842.html#section-8">RFC 9842, Section 8</a>, compression dictionary transport is HTTPS-only.</li>
</ul>
<hr />
<h2 id="how-shared-dictionaries-work">How shared dictionaries work</h2>
<p>The protocol uses two new request and response headers and two new content encodings:</p>
<table>
<thead>
<tr>
<th>Header</th>
<th>Direction</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Use-As-Dictionary</code></td>
<td>Origin → browser</td>
<td>Marks a response as usable as a dictionary for future requests matching the supplied <code>match</code> value.</td>
</tr>
<tr>
<td><code>Available-Dictionary</code></td>
<td>Browser → origin</td>
<td>Advertises the SHA-256 hash of a dictionary the browser already has for the request URL.</td>
</tr>
<tr>
<td><code>Content-Encoding: dcb</code> or <code>dcz</code></td>
<td>Origin → browser</td>
<td>Delta-compressed against the advertised dictionary, using Brotli (<code>dcb</code>) or Zstandard (<code>dcz</code>).</td>
</tr>
</tbody>
</table>
<p>The first response for a versioned asset includes <code>Use-As-Dictionary</code>, and the browser stores the response. On subsequent requests for assets matching the pattern, the browser sends <code>Available-Dictionary: :&lt;sha256&gt;:</code> and adds <code>dcb, dcz</code> to <code>Accept-Encoding</code>. Your origin compresses the new asset against the dictionary and returns it with <code>Content-Encoding: dcb</code> or <code>dcz</code>. The browser uses its stored copy to reconstruct the full response.</p>
<p>The <code>match</code> value in <code>Use-As-Dictionary</code> is a <a href="https://urlpattern.spec.whatwg.org/">WHATWG URL Pattern</a>, not a regular expression. Match patterns operate on the percent-encoded URL path and are scoped to the same origin as the dictionary.</p>
<p>The <code>Available-Dictionary</code> value is a <a href="https://www.rfc-editor.org/rfc/rfc9651">Structured Field</a> byte sequence: the base64-encoded SHA-256 hash wrapped in colons (for example, <code>:pZGm1Av0IEBKARczz7exkNYsZb8LzaMrV7J32a2fFG4=:</code>). The colons are part of the syntax.</p>
<hr />
<h2 id="enable-shared-dictionaries">Enable shared dictionaries</h2>
<p>Enabling shared dictionaries is a two-part task:</p>
<ol>
<li>Turn on passthrough for your zone in Cloudflare. This tells Cloudflare to forward dictionary headers and vary cache entries correctly.</li>
<li>Update your origin server to mark assets as dictionaries and return delta-compressed responses against them.</li>
</ol>
<p>The work of creating dictionaries and compressing new responses against them happens at your origin, not at Cloudflare.</p>
<h3 id="1-enable-passthrough-in-cloudflare"><ol>
<li>Enable passthrough in Cloudflare</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13934.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13930.md")
</aside>
<h3 id="2-mark-assets-as-dictionaries-at-your-origin"><ol start="2">
<li>Mark assets as dictionaries at your origin</li>
</ol></h3>
<p>For each versioned asset you want to use as a dictionary, include a <code>Use-As-Dictionary</code> header on the first response:</p>
<pre><code class="language-txt">Use-As-Dictionary: match=&quot;/static/app-*.js&quot;, type=&quot;raw&quot;&#10;Cache-Control: public, max-age=31536000, immutable&#10;Content-Encoding: br&#10;</code></pre>
<p>The <code>match</code> value tells the browser which future request URLs should advertise this dictionary. It is a WHATWG URL Pattern, does not support regular expressions, and must resolve to the same origin as the dictionary.</p>
<h3 id="3-compress-new-versions-against-the-advertised-dictionary"><ol start="3">
<li>Compress new versions against the advertised dictionary</li>
</ol></h3>
<p>When a request arrives with an <code>Available-Dictionary</code> header, look up the dictionary by its SHA-256 hash. If you have it, compress the response against it and return:</p>
<pre><code class="language-txt">Content-Encoding: dcz&#10;Vary: Accept-Encoding, Available-Dictionary&#10;Cache-Control: public, max-age=31536000, immutable&#10;</code></pre>
<p><a href="https://www.rfc-editor.org/rfc/rfc9842.html#section-6.2">RFC 9842, Section 6.2</a> requires the <code>Vary: Accept-Encoding, Available-Dictionary</code> response header so that browser caches do not serve the wrong variant. Cloudflare's cache also varies on these headers when passthrough is on.</p>
<h3 id="4-fall-back-when-no-dictionary-is-available"><ol start="4">
<li>Fall back when no dictionary is available</li>
</ol></h3>
<p>When the browser does not advertise <code>Available-Dictionary</code>, the hash does not match a dictionary you have, or the browser does not advertise <code>dcb</code>/<code>dcz</code>, return the response with normal Brotli, Zstandard, or Gzip compression.</p>
<h3 id="implementation-options">Implementation options</h3>
<p>Cloudflare does not prescribe a specific origin implementation. Common starting points include:</p>
<ul>
<li><strong>A reverse proxy.</strong> Configure NGINX, Caddy, or a similar proxy to attach <code>Use-As-Dictionary</code> headers and produce delta responses with a sidecar process.</li>
<li><strong>Native support in your application server.</strong> Extend your existing compression middleware to read <code>Available-Dictionary</code> and emit <code>dcb</code> or <code>dcz</code>.</li>
</ul>
<hr />
<h2 id="test-shared-dictionaries">Test shared dictionaries</h2>
<p>To confirm a request is using a shared dictionary, request the asset twice. The second request advertises the dictionary you received in the first response.</p>
<pre><code class="language-sh">&#35; Prime the dictionary.&#10;curl -sI -H &quot;Accept-Encoding: br, gzip, zstd, dcb, dcz&quot; \&#10;  https://example.com/static/app.v1.js&#10;&#10;&#35; Request the next version, advertising the dictionary you just received.&#10;&#35; Replace &lt;hash&gt; with the base64-encoded SHA-256 of the first response.&#10;&#35; The surrounding colons are part of the Structured Field syntax&#10;&#35; and are required by RFC 9842, Section 2.2.&#10;curl -sI -H &quot;Accept-Encoding: br, gzip, zstd, dcb, dcz&quot; \&#10;  &#45;H &quot;Available-Dictionary: :&lt;hash&gt;:&quot; \&#10;  https://example.com/static/app.v2.js&#10;</code></pre>
<p>The second response should include <code>Content-Encoding: dcz</code> (or <code>dcb</code>), <code>Vary: Accept-Encoding, Available-Dictionary</code>, and a <code>Content-Length</code> significantly smaller than a non-delta response.</p>
<p>You can also use <a href="https://canicompress.com/">canicompress.com</a> to confirm your browser supports shared dictionaries and to inspect a working delta-compressed response.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>Origin-side work is required.</strong> In passthrough mode, Cloudflare does not generate dictionaries or compute deltas. If your origin does not produce <code>dcb</code>/<code>dcz</code> responses, no compression savings occur.</li>
<li><strong>Body-modifying features are incompatible.</strong> Cloudflare features that rewrite response bodies do not work on delta-compressed responses. Turn these features off on dictionary-compressed paths, or set <code>cache-control: no-transform</code> on the origin response. For details, refer to <a href="/speed/optimization/content/compression/">Content compression</a>.</li>
<li><strong>Browser support is partial.</strong> Visitors on browsers that do not request <code>dcb</code> or <code>dcz</code> continue to receive Brotli, Zstandard, or Gzip per your existing <a href="/rules/compression-rules/">Compression Rules</a> and <a href="/speed/optimization/content/compression/">default compression behavior</a>.</li>
<li><strong>Same-origin only.</strong> Per <a href="https://www.rfc-editor.org/rfc/rfc9842.html#section-9.3.1">RFC 9842, Section 9.3.1</a>, dictionaries are scoped to the response origin. Cross-origin dictionary use is not supported.</li>
</ul>
