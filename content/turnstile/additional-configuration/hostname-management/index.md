<p>Hostname management controls where your Turnstile widgets can be used by specifying which domains are authorized to load and execute your widgets. This security measure prevents unauthorized use of your widgets on domains that you do not control.</p>
<p>You can associate hostnames with your widget to control where it can be used via Hostname Management. Managing your hostnames ensures that Turnstile works seamlessly with your setup, whether you add standalone hostnames or leverage zones registered to your Cloudflare account.</p>
<hr />
<h2 id="hostname-requirements">Hostname requirements</h2>
<h3 id="standard-configuration">Standard configuration</h3>
<p>By default, every widget requires at least one hostname to be configured. You cannot create a widget without specifying at least one authorized hostname.</p>
<h3 id="hostname-format-requirements">Hostname format requirements</h3>
<p>When adding hostnames, follow these requirements:</p>
<ul>
<li>The hostname must be fully qualified domain names (FQDNs): <code>example.com</code> or <code>subdomain.example.com</code></li>
<li>Wildcard characters (such as <code>*</code>) are not supported in the hostname field. However, adding a hostname automatically authorizes all of its subdomains.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="invalid-formats">Invalid formats</h3>
@markup("md", "content/.markup/bodies/15034.md")
</aside>
<h3 id="subdomain-behavior">Subdomain behavior</h3>
<p>When you add a hostname, the widget will work on that exact hostname and all of its subdomains. This means adding a root domain covers all subdomains beneath it, while adding a specific subdomain restricts the widget to only that subdomain and its children.</p>
<h4 id="example-root-domain">Example: Root domain</h4>
<p>Adding <code>example.com</code> as a hostname will allow the widget to work on:</p>
<ul>
<li><code>example.com</code></li>
<li><code>www.example.com</code></li>
<li><code>shop.example.com</code></li>
<li><code>any.sub.example.com</code></li>
</ul>
<h4 id="example-specific-subdomain">Example: Specific subdomain</h4>
<p>Adding <code>www.example.com</code> as a hostname provides more restrictive control. The widget will work on:</p>
<ul>
<li><code>www.example.com</code></li>
<li><code>abc.www.example.com</code> (subdomains of the specified hostname)</li>
</ul>
<p>However, it will <strong>not</strong> work on:</p>
<ul>
<li><code>example.com</code> (parent domain)</li>
<li><code>dash.example.com</code> (sibling subdomain)</li>
<li><code>cloudflare.com</code> (unrelated domain)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15033.md")
</aside>
<h2 id="add-hostnames">Add hostnames</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15041.md")
</div></div>
<hr />
<h2 id="limitations">Limitations</h2>
<p>Free users are entitled to a maximum of 10 hostnames per widget.</p>
<p>Enterprise customers can have up to 200 hostnames per widget.</p>
