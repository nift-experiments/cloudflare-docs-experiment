---
cp9:
  canonical: https://developers.cloudflare.com/email-service/configuration/mta-sts/
  description: Enable MTA Strict Transport Security for your Email Service domain to protect against downgrade attacks.
  full_title: Configure MTA-STS · Cloudflare Email Service docs
  head_html: <title>Configure MTA-STS · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable MTA Strict Transport Security for your Email Service domain to protect against downgrade attacks."><link rel="canonical" href="https://developers.cloudflare.com/email-service/configuration/mta-sts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/configuration/mta-sts/index.md"><meta property="og:title" content="Configure MTA-STS · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable MTA Strict Transport Security for your Email Service domain to protect against downgrade attacks."><meta property="og:url" content="https://developers.cloudflare.com/email-service/configuration/mta-sts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/configuration/mta-sts/#page","headline":"Configure MTA-STS \u00b7 Cloudflare Email Service docs","description":"Enable MTA Strict Transport Security for your Email Service domain to protect against downgrade attacks.","url":"https://developers.cloudflare.com/email-service/configuration/mta-sts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/configuration/mta-sts/
  schema: 1
---
<p>MTA Strict Transport Security (<a href="https://datatracker.ietf.org/doc/html/rfc8461">MTA-STS</a>) was introduced by email service providers including Microsoft, Google and Yahoo as a solution to protect against downgrade and man-in-the-middle attacks in SMTP sessions, as well as solving the lack of security-first communication standards in email.</p>
<p>Suppose that <code>example.com</code> is your domain and uses Email Service. Here is how you can enable MTA-STS for it.</p>
<h2 id="add-the-mta-sts-dns-record">Add the <code>_mta-sts</code> DNS record</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Create a new CNAME record with the name <code>_mta-sts</code> that points to Cloudflare's record <code>_mta-sts.mx.cloudflare.net</code>. Make sure to disable the proxy mode.</li>
</ol>
<p><img src="/assets/upstream/images/email-service/mta-sts-record.png" alt="MTA-STS CNAME record" /></p>
<ol start="3">
<li>Confirm that the record was created:</li>
</ol>
<pre tabindex="0"><code class="language-sh">dig txt _mta-sts.example.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">_mta-sts.example.com. 300 IN  CNAME _mta-sts.mx.cloudflare.net.&#10;_mta-sts.mx.cloudflare.net. 300 IN  TXT &quot;v=STSv1; id=20230615T153000;&quot;&#10;</code></pre>
<p>This tells the other end client that is trying to connect to us that we support MTA-STS.</p>
<h2 id="serve-the-policy-file">Serve the policy file</h2>
<p>Next you need an HTTPS endpoint at <code>mta-sts.example.com</code> to serve your policy file. This file defines the mail servers in the domain that use MTA-STS. The reason why HTTPS is used here instead of DNS is because not everyone uses DNSSEC yet, so we want to avoid another MITM attack vector.</p>
<p>To do this you need to deploy a Worker that allows email clients to pull Cloudflare's Email Service policy file using the &quot;well-known&quot; URI convention.</p>
<ol>
<li>
<p>Deploy the MTA-STS proxy Worker to your account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/mta-sts-proxy"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This Worker proxies <code>https://mta-sts.mx.cloudflare.net/.well-known/mta-sts.txt</code> to your own domain.</p>
</li>
<li>
<p>After deploying it, go to the Worker configuration, then <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong> &gt; <strong>+Add</strong>. Type the subdomain <code>mta-sts.example.com</code>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-service/mta-sts-domain.png" alt="MTA-STS Worker Custom Domain" /></p>
<p>You can then confirm that your policy file is working with the following:</p>
<pre tabindex="0"><code class="language-sh">curl https://mta-sts.example.com/.well-known/mta-sts.txt&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">version: STSv1&#10;mode: enforce&#10;mx: *.mx.cloudflare.net&#10;max_age: 86400&#10;</code></pre>
<p>This says that you domain <code>example.com</code> enforces MTA-STS. Capable email clients will only deliver email to this domain over a secure connection to the specified MX servers. If no secure connection can be established the email will not be delivered.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="test-before-enforcing">Test before enforcing</h3>
@markup("md", "content/.markup/bodies/8616.md")
</aside>
<p>Email Service also supports MTA-STS upstream, which greatly improves security when forwarding your emails to service providers like Gmail, Microsoft, and others.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/concepts/email-authentication/">Email authentication</a> — SPF, DKIM, and DMARC reference.</li>
<li><a href="/email-service/reference/postmaster/">Postmaster</a> — TLS, ARC, and SMTP details for postmasters.</li>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — review your domain's DNS records.</li>
</ul>
