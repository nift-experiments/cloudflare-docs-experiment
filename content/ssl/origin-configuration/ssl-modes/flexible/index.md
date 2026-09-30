<p>Setting your encryption mode to <strong>Flexible</strong> makes your site partially secure. Cloudflare allows HTTPS connections between your visitor and Cloudflare, but all connections between Cloudflare and your origin are made through HTTP. As a result, an SSL certificate is not required on your origin.</p>
<pre><code class="language-mermaid">flowchart LR&#10;    accTitle: Flexible SSL/TLS Encryption&#10;    accDescr: With an encryption mode of Flexible, your application encrypts traffic between the visitor and Cloudflare, but not between Cloudflare and your server.&#10;    A[Visitor] &lt;--Encrypted--&gt; B((Cloudflare))&lt;--Unencrypted--&gt; C[(Origin server)]&#10;</code></pre>
<h2 id="use-when">Use when</h2>
<p>Choose this option when you cannot set up an SSL certificate on your origin or your origin does not support SSL/TLS.</p>
<h2 id="required-setup">Required setup</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Depending on your origin configuration, you may have to adjust settings to avoid <a href="/ssl/troubleshooting/mixed-content-errors/">Mixed Content errors</a> or <a href="/ssl/troubleshooting/too-many-redirects/">redirect loops</a>.</p>
<h3 id="process">Process</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14270.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14267.md")
</aside>
<p>Flexible mode is only supported for HTTPS connections on port 443 (default port). Other ports using HTTPS will fall back to <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong> mode</a>.</p>
<p>If your application contains sensitive information (personalized data, user login), use <a href="/ssl/origin-configuration/ssl-modes/full/"><strong>Full</strong></a> or <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (Strict)</strong></a> modes instead.</p>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pull</a> does not work when your <a href="/ssl/origin-configuration/ssl-modes/"><strong>SSL/TLS encryption mode</strong></a> is set to <strong>Off</strong> or <strong>Flexible</strong>.
<br /></p>
