<h2 id="simple-explanation">Simple explanation</h2>
<p>When visitors request content from your domain, Cloudflare first attempts to serve content from the cache. If this attempt fails, Cloudflare sends a request — or an <code>origin pull</code> — back to your origin web server to get the content.</p>
<p>Authenticated Origin Pulls makes sure that all of these <code>origin pulls</code> come from Cloudflare. Put another way, Authenticated Origin Pulls ensures that any HTTPS requests outside of Cloudflare will not receive a response from your origin.</p>
<p>This block also applies for requests to <a href="/dns/proxy-status/#dns-only-records">unproxied DNS records</a> in Cloudflare.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14284.md")
</aside>
<h2 id="detailed-explanation">Detailed explanation</h2>
<p>Cloudflare enforces authenticated origin pulls by adding an extra layer of TLS client certificate authentication when establishing a connection between Cloudflare and the origin web server.</p>
<p>For more details, refer to the <a href="https://blog.cloudflare.com/protecting-the-origin-with-tls-authenticated-origin-pulls/">introductory blog post</a>.</p>
<hr />
<h3 id="types-of-handshakes">Types of handshakes</h3>
<p>For more details, refer to <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">What is a TLS handshake?</a>.</p>
<p><strong>Standard TLS handshake</strong></p>
<p><img src="/assets/upstream/images/ssl/client-auth-tls-standard.png" alt="Diagram showing the Standard TLS handshake" /></p>
<p><strong>Client authenticated TLS handshake</strong></p>
<p><img src="/assets/upstream/images/ssl/client-auth-tls-handshake.png" alt="Diagram showing the client authenticated TLS handshake" /></p>
<h3 id="comparison-diagrams">Comparison diagrams</h3>
<p>Without Authenticated Origin Pulls, Cloudflare performs standard TLS handshakes between a client device and Cloudflare and Cloudflare and your origin.
This is true even if you have <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong></a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong></a> encryption modes enabled.</p>
<pre><code class="language-mermaid">    flowchart TD&#10;      accTitle: Connection diagram without Authenticated Origin Pulls&#10;      A[End user query for &lt;code&gt;example.com&lt;/code&gt;] --Standard TLS Handshake--&gt; B[Cloudflare network]&#10;      B --Standard TLS Handshake--&gt; C[Origin server]&#10;      D[External device] --Standard TLS Handshake ----&gt; C&#10;</code></pre>
<br />
<p>This lack of authentication means that - even if your origin is <a href="/fundamentals/concepts/how-cloudflare-works/">protected behind Cloudflare</a> - attackers with your origin's IP address will still receive a response from your origin for HTTPS requests.</p>
<p>With Authenticated Origin Pulls, Cloudflare performs standard TLS handshakes between a client device and Cloudflare, but a client-authenticated TLS handshake between Cloudflare and your origin.</p>
<pre><code class="language-mermaid">    flowchart TD&#10;      accTitle: Connection diagram with Authenticated Origin Pulls&#10;      A[End user query for &lt;code&gt;example.com&lt;/code&gt;] --Standard TLS Handshake--&gt; B[Cloudflare network]&#10;      B --Client authenticated TLS Handshake--&gt; C[Origin server]&#10;      D[External device] --Standard TLS Handshake -----x C&#10;</code></pre>
<br />
<p>This additional layer of authentication ensures that any HTTPS requests outside of Cloudflare will not receive a response from your origin.</p>
