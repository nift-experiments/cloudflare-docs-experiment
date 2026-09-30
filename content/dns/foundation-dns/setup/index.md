<p>Advanced nameservers included with <a href="/dns/foundation-dns/">Foundation DNS</a> are an opt-in configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7662.md")
</aside>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before opting in for advanced nameservers, consider the following:</p>
<ul>
<li></li>
</ul>
<p>The advantages that come with Foundation DNS <a href="/dns/foundation-dns/advanced-nameservers/">advanced nameservers</a> are currently not available for <a href="/dns/nameservers/custom-nameservers/">custom nameservers</a>. Make sure you only use one at a time.</p>
<h3 id="differences-from-standard-nameservers">Differences from standard nameservers</h3>
<p>Some behaviors are different from standard Cloudflare nameservers:</p>
<ul>
<li>Wildcard records are still supported but, with advanced nameservers, a wildcard record (<code>*.example.com</code>) will not apply to a subdomain that is an empty non-terminal. An empty non-terminal is a node in the DNS tree that has no records associated with it but has descendants that do, as exemplified below. This behavior is in compliance with <a href="https://www.rfc-editor.org/rfc/rfc4592.html">RFC 4592</a>, which defines the role of empty non-terminals in wildcard resolution.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7664.md")
</div></details>
<ul>
<li>Subdomain delegation: once a subdomain is delegated via NS records, Cloudflare will not serve any other records (such as A, TXT, or CNAME) on that subdomain from the parent zone, even if those records exist.</li>
</ul>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7666.md")
</div></details>
<h2 id="enable-on-a-zone">Enable on a zone</h2>
<p>To enable advanced nameservers on an existing zone:</p>
<ol>
<li>Opt for advanced nameservers on your zone:</li>
</ol>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7669.md")
</div></div>
<ol start="2">
<li>Update the authoritative nameservers at your registrar. This step depends on whether you are using <a href="/registrar/">Cloudflare Registrar</a>:
<ul>
<li>If you are using Cloudflare Registrar, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to have your nameservers updated.</li>
<li>If you are using a different registrar or if your zone is delegated, <a href="/dns/nameservers/update-nameservers/#specific-processes">manually update your nameservers</a>.</li>
</ul>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7661.md")
</aside>
