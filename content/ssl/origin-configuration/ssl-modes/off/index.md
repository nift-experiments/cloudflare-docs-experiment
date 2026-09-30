<p>Setting your encryption mode to <strong>Off (not recommended)</strong> redirects any HTTPS request to plaintext HTTP.</p>
<pre><code class="language-mermaid">    flowchart LR&#10;        accTitle: No SSL/TLS Encryption&#10;        accDescr: With an encryption mode of Off, your application does not encrypt traffic between the visitor and Cloudflare or between Cloudflare and your server.&#10;        A[Visitor] &lt;--Unencrypted--&gt; B((Cloudflare))&lt;--Unencrypted--&gt; C[(Origin server)]&#10;</code></pre>
<h2 id="use-when">Use when</h2>
<p>Cloudflare does not recommend setting your encryption mode to <strong>Off</strong>.</p>
<h2 id="required-setup">Required setup</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14252.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>When you set your encryption mode to <strong>Off</strong>, your application:</p>
<ul>
<li>Leaves your visitors and your application <a href="https://www.cloudflare.com/learning/ssl/why-use-https/">vulnerable to attacks</a>.</li>
<li>Will be marked as &quot;not secure&quot; by Chrome and other browsers, reducing visitor trust.</li>
<li>Will be penalized in <a href="https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html">SEO rankings</a>.</li>
</ul>
<h3 id="incompatible-settings">Incompatible settings</h3>
<p>When you set your SSL/TLS encryption mode to <strong>Off</strong>, you will not see the options for <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a> or <a href="/network/onion-routing/"><strong>Onion Routing</strong></a>.</p>
<p><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pull</a> does not work when your <a href="/ssl/origin-configuration/ssl-modes/"><strong>SSL/TLS encryption mode</strong></a> is set to <strong>Off</strong> or <strong>Flexible</strong>.
<br /></p>
