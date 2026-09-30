---
cp9:
  canonical: https://developers.cloudflare.com/dns/faq/
  description: Find answers to common questions about Cloudflare's authoritative DNS.
  full_title: FAQ · Cloudflare DNS docs
  head_html: <title>FAQ · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Find answers to common questions about Cloudflare&#x27;s authoritative DNS."><link rel="canonical" href="https://developers.cloudflare.com/dns/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Find answers to common questions about Cloudflare&#x27;s authoritative DNS."><meta property="og:url" content="https://developers.cloudflare.com/dns/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/faq/#page","headline":"FAQ \u00b7 Cloudflare DNS docs","description":"Find answers to common questions about Cloudflare's authoritative DNS.","url":"https://developers.cloudflare.com/dns/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/faq/
  schema: 1
---
<p>The sections below cover frequently asked questions about Cloudflare authoritative DNS. For DNS Firewall, refer to <a href="/dns/dns-firewall/faq/">DNS Firewall FAQ</a>.</p>
<hr />
<h2 id="cloudflare-offerings">Cloudflare offerings</h2>
<h3 id="is-cloudflare-a-free-dns-domain-nameserver-provider">Is Cloudflare a free DNS (domain nameserver) provider?</h3>
<p>Yes. Cloudflare offers <a href="https://www.cloudflare.com/dns">free DNS services</a> to customers on all plans. Note that:</p>
<ul>
<li>You do not need to change your hosting provider to use Cloudflare.</li>
<li>You do not need to move away from your registrar. The only change you make with your registrar is to point the authoritative nameservers to the Cloudflare nameservers.</li>
</ul>
<h3 id="does-cloudflare-charge-for-or-limit-dns-queries">Does Cloudflare charge for or limit DNS queries?</h3>
<p>Cloudflare never limits or caps DNS queries, but the pricing depends on your plan level.</p>
<p>For customers on Free, Pro, or Business plans, Cloudflare does not charge for DNS queries. For customers on Enterprise plans, Cloudflare uses the number of monthly DNS queries as a pricing input to generate a custom quote.</p>
<h3 id="does-cloudflare-offer-domain-masking">Does Cloudflare offer domain masking?</h3>
<p>No. Cloudflare does not offer domain masking or DNS redirect services (your hosting provider might). However, we do offer URL forwarding through <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>.</p>
<h3 id="can-subdomains-be-added-directly-to-cloudflare">Can subdomains be added directly to Cloudflare?</h3>
<p>Yes. Enterprise customers can add subdomains directly to Cloudflare via <a href="/dns/zone-setups/subdomain-setup/">subdomain support</a>.</p>
<h3 id="does-cloudflare-support-edns0-extension-mechanisms-for-dns">Does Cloudflare support EDNS0 (extension mechanisms for DNS)?</h3>
<p>Yes, EDNS0 is a building block for modern DNS implementations and is enabled for all Cloudflare customers. EDNS0 adds support for signaling if the DNS Resolver (recursive DNS provider) supports larger message sizes and DNSSEC.</p>
<p>EDNS0 is the first approved set of mechanisms for <a href="http://en.wikipedia.org/wiki/Extension_mechanisms_for_DNS">DNS extensions</a>, originally published as <a href="https://www.rfc-editor.org/rfc/rfc2671.html">RFC 2671</a>.</p>
<hr />
<h2 id="nameservers">Nameservers</h2>
<h3 id="where-can-i-find-my-cloudflare-nameservers">Where can I find my Cloudflare nameservers?</h3>
<p>On the <strong>DNS Records</strong> page, locate the <strong>Cloudflare Nameservers</strong> card.</p>
<div class="nb-dash-button"></div>
<p>Also, the IP address associated with a specific Cloudflare nameserver can be retrieved via a dig command or a third-party DNS lookup tool hosted online such as <a href="https://www.whatsmydns.net/">whatsmydns.net</a>:</p>
<pre tabindex="0"><code class="language-sh">dig kate.ns.cloudflare.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">kate.ns.cloudflare.com.    68675    IN    A    173.245.58.124.&#10;</code></pre>
<p>To verify that your domain's parent zone is publishing the Cloudflare nameservers assigned to you (for example, when your zone is stuck in <strong>Pending Nameserver Update</strong> status), refer to <a href="/dns/zone-setups/troubleshooting/pending-nameservers/">Zone stuck in Pending Nameserver Update</a>.</p>
<h3 id="where-do-i-change-my-nameservers-to-point-to-cloudflare">Where do I change my nameservers to point to Cloudflare?</h3>
<p>Make the change at your registrar, which is where you registered your domain. This may or may not be your hosting provider - refer to <a href="/dns/nameservers/update-nameservers/">Update nameservers</a> for further context.</p>
<p>If you do not know who your registrar is for the domain, a WHOIS search can help. You can use <a href="https://lookup.icann.org/">ICANN Lookup</a>, for example.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1125.md")
</aside>
<p>Once you identify your registrar, follow their instructions.</p>
<details class="nb-details"><summary>Provider-specific instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1126.md")
</div></details>
<h3 id="why-have-i-received-an-email-mydomain-stopped-using-cloudflare-s-nameservers">Why have I received an email: (mydomain) stopped using Cloudflare's nameservers?</h3>
<p>For domains where Cloudflare hosts the DNS, Cloudflare continuously checks whether the domain uses Cloudflare's nameservers for DNS resolution. If Cloudflare's nameservers are not used, the <a href="/dns/zone-setups/reference/domain-status/">domain status</a> is updated from <strong>Active</strong> to <strong>Moved</strong> and an email is sent to the customer.</p>
<p>This is important because, if a domain is in a <strong>Moved</strong> state for a <a href="/dns/zone-setups/reference/domain-status/">long enough period of time</a>, it will be deleted from Cloudflare.</p>
<p>To recover a deleted domain, <a href="/fundamentals/manage-domains/add-site/">re-add it in Cloudflare</a> just like you would for a new domain.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1124.md")
</aside>
<h3 id="why-does-my-new-zone-have-different-nameservers-than-my-other-zones">Why does my new zone have different nameservers than my other zones?</h3>
<p>Nameserver assignments happen at zone creation and <a href="/dns/nameservers/nameserver-options/#assignment-method">cannot be changed</a> afterwards, even by Cloudflare Support.</p>
<p>A newly added zone can be assigned different nameservers from your other zones for a few reasons:</p>
<ul>
<li>The same domain is (or was recently) active on another Cloudflare account.</li>
<li>The zone was previously deleted from Cloudflare and re-added.</li>
<li>A parent or child zone in the same account already uses the preferred nameservers.</li>
<li>The account uses <a href="/dns/foundation-dns/advanced-nameservers/">Foundation DNS advanced nameservers</a>, which use different sets (<code>blue</code>, <code>gold</code>, <code>orange</code>) and rotate to keep <a href="/dns/foundation-dns/advanced-nameservers/#nameservers-hosting-and-assignment">directly descending zones</a> on different nameservers.</li>
</ul>
<p>To make future zones share the same nameservers, use one of the following options depending on your plan:</p>
<ul>
<li><a href="/dns/nameservers/custom-nameservers/account-custom-nameservers/">Account custom nameservers</a> — available on Enterprise (self-serve), or on Business after <a href="/support/contacting-cloudflare-support/">contacting Cloudflare Support</a> to enable them.</li>
<li><a href="/dns/additional-options/dns-zone-defaults/">DNS zone defaults</a> with advanced nameservers or account custom nameservers — available on Enterprise.</li>
</ul>
<p>Deleting and re-adding the zone does not force a specific nameserver assignment and can produce yet another different set.</p>
<hr />
<h2 id="dns-records">DNS records</h2>
<h3 id="does-cloudflare-limit-the-number-of-dns-records-a-domain-can-have">Does Cloudflare limit the number of DNS records a domain can have?</h3>
<p>Yes. Refer to <a href="/dns/manage-dns-records/#dns-records-quota">DNS records quota</a> for current limits per plan and details on how quotas are enforced.</p>
<h3 id="how-long-does-it-take-for-a-dns-change-i-made-to-push-out">How long does it take for a DNS change I made to push out?</h3>
<p>By default, any changes or additions you make to your Cloudflare zone file will take effect globally within 5 minutes, usually much less.</p>
<p>Depending on the Time-to-Live (TTL) set on the previous <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS record</a>, old data may still remain cached until the TTL expires. Proxied records expire after 5 minutes (&quot;Automatic&quot;), but the TTL for unproxied records can be customized.</p>
<p>If changes to records with large TTLs are anticipated, it may make sense to reduce the TTL ahead of time so that the change takes effect as quickly as possible.</p>
<h3 id="why-can-t-i-make-any-queries-to-cloudflare-dns-servers">Why can't I make ANY queries to Cloudflare DNS servers?</h3>
<p><code>ANY</code> queries are special and often misunderstood. They are usually used to get all record types available on a DNS name, but what they return is just any type in the cache of recursive resolvers. This can cause confusion when they are used for debugging.</p>
<p>Because of Cloudflare's many advanced DNS features like CNAME flattening, it can be complex and even impossible to give correct answers to <code>ANY</code> queries. For example, when DNS records dynamically come and go or are stored remotely, it can be taxing or even impossible to get all the results at the same time.</p>
<p>Refer to <a href="https://blog.cloudflare.com/deprecating-dns-any-meta-query-type/">Deprecating the DNS ANY meta-query type</a> for details. The decision to block <code>ANY</code> does not affect DNS Firewall customers.</p>
<h3 id="how-do-i-add-aname-records-on-cloudflare">How do I add ANAME records on Cloudflare?</h3>
<p>ANAME or ALIAS are DNS records used by specific DNS providers. If your previous provider was using ANAME or ALIAS, you can recreate these records on Cloudflare as CNAME records. Cloudflare's <a href="/dns/cname-flattening/">CNAME flattening</a><sup><a href="#footnote-dns-aname-alias-callout-mdx-1">1</a></sup> allows you to create CNAME records at your <a href="/dns/concepts/#zone-apex">zone apex</a>, removing the need for those other record types.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-aname-alias-callout-mdx-1">A process in which Cloudflare returns an IP address instead of the target hostname that a CNAME record points to.</li></ol></section>
<h3 id="why-does-my-txt-record-show-a-double-quote-in-the-middle-of-the-value">Why does my TXT record show a double quote in the middle of the value?</h3>
<p>This is expected behavior. Per <a href="https://www.rfc-editor.org/rfc/rfc4408#section-3.1.3">RFC 4408</a> and the DNS protocol specification (<a href="https://www.rfc-editor.org/rfc/rfc1035#section-3.3.14">RFC 1035</a>), a single DNS TXT record is composed of one or more character strings, each with a maximum length of 255 characters. When the value you enter exceeds 255 characters, it must be split into multiple strings. Each string is enclosed in double quotes (<code>&quot;</code>), so the resulting record may appear to have a quote in the middle — for example, <code>&quot;first part&quot; &quot;second part&quot;</code>.</p>
<p>This splitting is required by the DNS protocol and is performed by all DNS providers, even if some do not display it in their UI or API. For all major TXT record use cases (such as SPF, DKIM, and DMARC), the receiving application will concatenate the strings back together, so the behavior of the record is not affected.</p>
<h3 id="why-are-cloudflare-s-a-or-aaaa-records-ip-addresses-for-my-domain-s-dns-responses-appearing">Why are Cloudflare's A or AAAA records / IP addresses for my domain's DNS responses appearing?</h3>
<p>For DNS records proxied to Cloudflare, Cloudflare's IP addresses are returned in DNS queries instead of your original server IP address. This allows Cloudflare to optimize, cache, and protect all requests for your website.</p>
