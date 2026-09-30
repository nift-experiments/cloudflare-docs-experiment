<p>Most subdomains serve a specific purpose within the overall context of your website. For example, <code>blog.example.com</code> might be your blog, <code>support.example.com</code> could be your customer help portal, and <code>store.example.com</code> would be your e-commerce site.</p>
<p>Even if you do not require specific subdomains, you might want to set up at least a subdomain record on <code>www</code>. It will usually point to the same content as what you have on the apex domain (<code>example.com</code>) or use a <a href="/fundamentals/manage-domains/manage-subdomains/#redirect-a-subdomain-to-the-apex-domain">redirect</a>. Having a subdomain DNS record on <code>www</code> helps guarantee that a visitor who types <code>www.</code> in front of your domain address can still find your website or application.</p>
<h2 id="subdomain-records">Subdomain records</h2>
<p>To host content on a subdomain of your domain, first ensure that your <a href="/fundamentals/manage-domains/#host-your-domain">hosting provider</a> can serve content for the given hostname (<code>&lt;subdomain&gt;.example.com</code>).</p>
<p>Then, you would create a corresponding <a href="/dns/manage-dns-records/reference/dns-record-types/#ip-address-resolution">IP address resolution record</a> (<code>A</code>, <code>AAAA</code>, or <code>CNAME</code>), specifying the label for your subdomain (<code>blog</code>, <code>www</code>, or <code>store</code>, for example) as the record <strong>Name</strong>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7836.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7841.md")
</div></div>
<h2 id="subdomain-redirects">Subdomain redirects</h2>
<p>For more guidance on redirecting a subdomain — either to your main domain or another location — refer to <a href="/fundamentals/manage-domains/manage-subdomains/#set-up-redirects">Set up subdomain redirects</a>.</p>
<h2 id="ssl-tls-for-subdomains">SSL/TLS for subdomains</h2>
<p>While DNS is what communicates where your website or application can be reached, SSL/TLS is what enables websites and applications to establish connections in a secure way.</p>
<p>If your subdomains are not correctly covered by an SSL/TLS certificate, your visitors will find a warning on their browser stating that your website or application is not secure.</p>
<p>If your main domain is using Cloudflare's <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificate</a>, that certificate also covers all first-level subdomains (<code>blog.example.com</code>).</p>
<p>For deeper subdomains (<code>dev.blog.example.com</code>), use a <a href="/ssl/edge-certificates/universal-ssl/limitations/#full-setup">different type of certificate</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="proxy-status">Proxy status</h3>
@markup("md", "content/.markup/bodies/7835.md")
</aside>
<h2 id="customize-subdomain-behavior">Customize subdomain behavior</h2>
<p>If you want to customize Cloudflare settings for individual subdomains, your approach will vary depending on your plan.</p>
<p>Enterprise customers can set up custom settings and access for a specific subdomain within Cloudflare with <a href="/dns/zone-setups/subdomain-setup/">Subdomain support</a>.</p>
<p>All other customers can set up subdomain-specific <a href="/rules/configuration-rules/">Configuration Rules</a> or <a href="/rules/page-rules/">Page Rules</a> to alter Cloudflare settings.</p>
<p>If you want a subdomain's DNS settings managed totally outside of Cloudflare — meaning this subdomain can be managed by individuals without access to your Cloudflare account — refer to <a href="/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/">Delegating subdomains outside of Cloudflare</a>.</p>
