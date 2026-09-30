---
cp9:
  canonical: https://developers.cloudflare.com/email-service/concepts/email-authentication/
  description: SPF, DKIM, and DMARC authentication for secure and deliverable email sending with Email Service.
  full_title: Email authentication · Cloudflare Email Service docs
  head_html: <title>Email authentication · Cloudflare Email Service docs</title><meta name="generator" content="Nift"><meta name="description" content="SPF, DKIM, and DMARC authentication for secure and deliverable email sending with Email Service."><link rel="canonical" href="https://developers.cloudflare.com/email-service/concepts/email-authentication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-service/concepts/email-authentication/index.md"><meta property="og:title" content="Email authentication · Cloudflare Email Service docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="SPF, DKIM, and DMARC authentication for secure and deliverable email sending with Email Service."><meta property="og:url" content="https://developers.cloudflare.com/email-service/concepts/email-authentication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email Service"><meta name="algolia_product_filter" content="Email Service"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email Service"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/email-service/concepts/email-authentication/#page","headline":"Email authentication \u00b7 Cloudflare Email Service docs","description":"SPF, DKIM, and DMARC authentication for secure and deliverable email sending with Email Service.","url":"https://developers.cloudflare.com/email-service/concepts/email-authentication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /email-service/concepts/email-authentication/
  schema: 1
---
<p class="article-summary">Learn about SPF, DKIM, and DMARC for secure and deliverable email sending.</p>
<p>Email authentication verifies sender identity and improves deliverability. <strong>Cloudflare Email Service handles authentication automatically</strong>, but understanding these concepts helps troubleshoot issues.</p>
<h2 id="spf-sender-policy-framework">SPF (Sender Policy Framework)</h2>
<p>SPF ensures that no one else can send emails with your domain by authorizing which mail servers are allowed to send on your behalf.</p>
<p>Email Service configures separate SPF records for sending and routing:</p>
<ul>
<li><strong>Email Sending</strong> SPF record on <code>cf-bounce.yourdomain.com</code>:</li>
</ul>
<pre tabindex="0"><code class="language-txt">TXT cf-bounce.yourdomain.com &quot;v=spf1 include:_spf.mx.cloudflare.net ~all&quot;&#10;</code></pre>
<ul>
<li><strong>Email Routing</strong> SPF record on the root domain:</li>
</ul>
<pre tabindex="0"><code class="language-txt">TXT yourdomain.com &quot;v=spf1 include:_spf.mx.cloudflare.net ~all&quot;&#10;</code></pre>
<p>SPF works by:</p>
<ol>
<li>Publishing authorized IP addresses in DNS</li>
<li>Recipient servers checking your SPF record</li>
<li>Comparing the sending IP against authorized IPs</li>
<li>Passing or failing based on the result</li>
</ol>
<h2 id="dkim-domainkeys-identified-mail">DKIM (DomainKeys Identified Mail)</h2>
<p>DKIM ensures that emails have not been tampered during transit by cryptographically signing them with your domain's private key.</p>
<p><strong>How DKIM works:</strong></p>
<ol>
<li>Email headers and body are signed with a private key</li>
<li>DKIM-Signature header is added to the email</li>
<li>Public key is published in DNS</li>
<li>Recipients use the public key to verify the signature</li>
</ol>
<p>Email Service uses separate DKIM selectors for sending and routing:</p>
<ul>
<li><strong>Email Sending</strong>: <code>cf-bounce._domainkey.yourdomain.com</code></li>
<li><strong>Email Routing</strong>: <code>cf2024-1._domainkey.yourdomain.com</code></li>
</ul>
<p>Cloudflare automatically generates and manages DKIM keys. You add the provided DNS records from the dashboard.</p>
<h2 id="dmarc-domain-based-message-authentication-reporting-conformance">DMARC (Domain-based Message Authentication, Reporting &amp; Conformance)</h2>
<p>DMARC ensures that emails claiming to be from your domain actually pass SPF and DKIM checks, telling recipients what to do with emails that fail authentication.</p>
<p><strong>DMARC record example:</strong></p>
<pre tabindex="0"><code class="language-txt">TXT _dmarc.yourdomain.com &quot;v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8641.md")
</aside>
<p><strong>DMARC policies:</strong></p>
<ul>
<li><code>p=none</code> - Monitor only (recommended to start)</li>
<li><code>p=quarantine</code> - Quarantine suspicious emails</li>
<li><code>p=reject</code> - Reject unauthenticated emails</li>
</ul>
<p><strong>Deployment strategy:</strong></p>
<ol>
<li>Start with <code>p=none</code> to monitor authentication</li>
<li>Gradually increase to <code>p=quarantine</code></li>
<li>Finally implement <code>p=reject</code> after confirming legitimate mail authenticates</li>
</ol>
<h2 id="key-benefits">Key benefits</h2>
<p>Email authentication provides:</p>
<ul>
<li><strong>Deliverability</strong>: Improves inbox placement</li>
<li><strong>Security</strong>: Protects your domain from spoofing</li>
<li><strong>Reputation</strong>: Maintains good sender reputation with ISPs</li>
</ul>
<p>Cloudflare Email Service handles authentication automatically, but you need to configure the DNS records for SPF, DKIM, and DMARC as provided in your dashboard. Email Sending and Email Routing use separate DNS records -- refer to <a href="/email-service/configuration/domains/">Domain configuration</a> for the full details.</p>
