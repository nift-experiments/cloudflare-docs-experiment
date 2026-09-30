<p>When you add a domain to Cloudflare, you may also need to create or review the DNS record on your zone apex. Zone apex refers to the domain (<code>example.com</code>) or subdomain (<code>blog.example.com</code>) that you are <a href="/dns/concepts/#zone">adding to Cloudflare</a>.</p>
<p>Usually, the zone apex record makes your domain accessible by visitors. In this case, the necessary record type (<a href="/dns/manage-dns-records/reference/dns-record-types/#ip-address-resolution">A, AAAA, or CNAME</a>) and its content will depend on the provider that <a href="/fundamentals/manage-domains/#host-your-domain">hosts</a> your website or application. If you are using Cloudflare Pages, refer to <a href="/pages/configuration/custom-domains/">Custom domains</a>. If you are using other providers, look for their guidance on how to connect domains managed on external DNS services.</p>
<h3 id="aname-or-alias">ANAME or ALIAS</h3>
<p>ANAME or ALIAS are DNS records used by specific DNS providers. If your previous provider was using ANAME or ALIAS, you can recreate these records on Cloudflare as CNAME records. Cloudflare's <a href="/dns/cname-flattening/">CNAME flattening</a><sup><a href="#footnote-dns-aname-alias-callout-mdx-1">1</a></sup> allows you to create CNAME records at your <a href="/dns/concepts/#zone-apex">zone apex</a>, removing the need for those other record types.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-aname-alias-callout-mdx-1">A process in which Cloudflare returns an IP address instead of the target hostname that a CNAME record points to.</li></ol></section>
<h2 id="zone-apex-record">Zone apex record</h2>
<p>To create a zone apex record, use <code>@</code> for the record <strong>Name</strong>, as in the following example.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7829.md")
</div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7834.md")
</div></div>
<h2 id="domain-redirects">Domain redirects</h2>
<p>Once you create a domain, you may want to route that traffic to other places.</p>
<p>For more guidance, refer to <a href="/fundamentals/manage-domains/manage-subdomains/#redirect-the-apex-domain-to-a-subdomain">Redirect domain to subdomain</a> or <a href="/fundamentals/manage-domains/redirect-domain/">Redirect one domain to another</a>.</p>
<h2 id="get-free-ssl-certificates">Get free SSL certificates</h2>
<p>While DNS is what communicates where your website or application can be reached, SSL/TLS is what enables websites and applications to establish connections in a secure way.</p>
<p>If your domain is not correctly covered by an SSL/TLS certificate, your visitors will find a warning on their browser stating that your website or application is not secure.</p>
<p>Cloudflare offers free, unshared, publicly trusted <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificates</a> to all Cloudflare domains.</p>
