---
cp9:
  canonical: https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/
  description: Configure MX, SPF, DKIM, and DMARC records for email.
  full_title: Set up email records · Cloudflare DNS docs
  head_html: <title>Set up email records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure MX, SPF, DKIM, and DMARC records for email."><link rel="canonical" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/index.md"><meta property="og:title" content="Set up email records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure MX, SPF, DKIM, and DMARC records for email."><meta property="og:url" content="https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/#page","headline":"Set up email records \u00b7 Cloudflare DNS docs","description":"Configure MX, SPF, DKIM, and DMARC records for email.","url":"https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/manage-dns-records/how-to/email-records/
  schema: 1
---
<p>There are three reasons to set up email records for your domain:</p>
<ul>
<li>To make sure your domain can <a href="#receive-email">receive email</a>.</li>
<li>To make sure your domain can <a href="#send-and-receive-email">send and receive email</a>.</li>
<li>To prevent other email senders from <a href="#prevent-domain-spoofing">spoofing your domain</a>.</li>
</ul>
<p>The exact values for your DNS mail records depend on your email provider. If you have issues, review the <a href="/dns/troubleshooting/email-issues/">Troubleshooting</a> and contact your email service provider to confirm your DNS records are correct.</p>
<hr />
<h2 id="receive-email">Receive email</h2>
<p>If you only need to <strong>receive</strong> emails, Cloudflare offers <a href="/email-service/">Email Routing</a> for free email forwarding to custom email addresses.</p>
<h2 id="send-and-receive-email">Send and receive email</h2>
<p>To <strong>send and receive</strong> emails from your domain, you need an SMTP provider. Then, create two DNS records within Cloudflare, following the steps below:</p>
<ol>
<li>
<p>Get the IP address and MX record details from your SMTP provider (<a href="/dns/manage-dns-records/reference/vendor-specific-records/">vendor-specific guidelines</a>).</p>
</li>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-dns-records/">Add an <code>A</code> or <code>AAAA</code> record</a> for your mail subdomain that points to the IP address of your mail server.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>IPv4 address</strong></th>
<th><strong>Proxy status</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td><code>mail</code></td>
<td><code>192.0.2.1</code></td>
<td>DNS only</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code> &lt;details&gt;&#10;&#10;  &lt;summary&gt;API example&lt;/summary&gt;&#10;</code></pre>
<div>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;A&quot;,&#10;  &quot;name&quot;: &quot;mail.example.com&quot;,&#10;  &quot;content&quot;: &quot;192.0.2.1&quot;,&#10;  &quot;ttl&quot;: 3600,&#10;  &quot;proxied&quot;: false&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;    &quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;    &quot;zone_name&quot;: &quot;example.com&quot;,&#10;    &quot;name&quot;: &quot;mail.example.com&quot;,&#10;    &quot;type&quot;: &quot;A&quot;,&#10;    &quot;content&quot;: &quot;192.0.2.1&quot;,&#10;    &quot;proxiable&quot;: true,&#10;    &quot;proxied&quot;: false,&#10;    &quot;ttl&quot;: 3600,&#10;    &quot;locked&quot;: false,&#10;    &quot;meta&quot;: {&#10;      &quot;source&quot;: &quot;primary&quot;&#10;    },&#10;    &quot;comment&quot;: null,&#10;    &quot;tags&quot;: [],&#10;    &quot;created_on&quot;: &quot;2023-01-17T20:37:05.368097Z&quot;,&#10;    &quot;modified_on&quot;: &quot;2023-01-17T20:37:05.368097Z&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
</div>
<pre tabindex="0"><code>  &lt;/details&gt;&#10;</code></pre>
<ol start="3">
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/">Add an <code>MX</code> record</a> that points to that subdomain.</li>
</ol>
<table>
<thead>
<tr>
<th><strong>Type</strong></th>
<th><strong>Name</strong></th>
<th><strong>Mail server</strong></th>
<th><strong>TTL</strong></th>
<th><strong>Priority</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>MX</td>
<td><code>@</code></td>
<td><code>mail.example.com</code></td>
<td>Auto</td>
<td>5</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code>  &lt;details&gt;&#10;&#10;  &lt;summary&gt;API example&lt;/summary&gt;&#10;</code></pre>
<div>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;MX&quot;,&#10;  &quot;name&quot;: &quot;example.com&quot;,&#10;  &quot;content&quot;: &quot;mail.example.com&quot;,&#10;  &quot;priority&quot;: 5,&#10;  &quot;ttl&quot;: 3600&#10;}&#x27;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;    &quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;    &quot;zone_name&quot;: &quot;example.com&quot;,&#10;    &quot;name&quot;: &quot;example.com&quot;,&#10;    &quot;type&quot;: &quot;MX&quot;,&#10;    &quot;content&quot;: &quot;mail.example.com&quot;,&#10;    &quot;priority&quot;: 5,&#10;    &quot;proxiable&quot;: false,&#10;    &quot;proxied&quot;: false,&#10;    &quot;ttl&quot;: 3600,&#10;    &quot;locked&quot;: false,&#10;    &quot;meta&quot;: {&#10;      &quot;source&quot;: &quot;primary&quot;&#10;    },&#10;    &quot;comment&quot;: null,&#10;    &quot;tags&quot;: [],&#10;    &quot;created_on&quot;: &quot;2023-01-17T20:54:23.660869Z&quot;,&#10;    &quot;modified_on&quot;: &quot;2023-01-17T20:54:23.660869Z&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
</div>
<pre tabindex="0"><code>  &lt;/details&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7828.md")
</aside>
<hr />
<h2 id="prevent-domain-spoofing">Prevent domain spoofing</h2>
<p>Without email authentication records, anyone can send email that appears to come from your domain — a technique known as domain spoofing. To prevent this, you add DNS TXT records (text-based entries in your domain's DNS settings) that allow receiving mail servers to verify whether an email actually came from you:</p>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">Sender Policy Framework (SPF)</a>: Lists the IP addresses and domains authorized to send email on behalf of your domain.</li>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DomainKeys Identified Mail (DKIM)</a>: Authenticates the sender's domain and verifies that email content was not altered in transit, using a cryptographic signature.</li>
<li><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">Domain-based Message Authentication Reporting and Conformance (DMARC)</a>: Tells receiving servers what to do when SPF or DKIM checks fail (for example, reject or quarantine the email), and sends you aggregate reports about your email traffic.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7827.md")
</aside>
<h3 id="configure-email-security-records">Configure email security records</h3>
<p>Refer to <a href="/dmarc-management/security-records/">Security records</a> to learn how to set up your email security records.</p>
<h2 id="proxy-smtp-traffic">Proxy SMTP traffic</h2>
<p>By default, Cloudflare does not proxy email traffic on port 25 (SMTP). You can only proxy outgoing email if you have <a href="/spectrum/">Spectrum</a> configured for <a href="/spectrum/reference/configuration-options/#smtp">SMTP</a>.</p>
