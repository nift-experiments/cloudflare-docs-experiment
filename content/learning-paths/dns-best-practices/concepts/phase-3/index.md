---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/
  description: Execute the DNS nameserver cutover.
  full_title: 'Phase 3: Execution (Migration window) · Cloudflare Learning Paths'
  head_html: '<title>Phase 3: Execution (Migration window) · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Execute the DNS nameserver cutover."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/index.md"><meta property="og:title" content="Phase 3: Execution (Migration window) · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Execute the DNS nameserver cutover."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/#page","headline":"Phase 3: Execution (Migration window) \u00b7 Cloudflare Learning Paths","description":"Execute the DNS nameserver cutover.","url":"https://developers.cloudflare.com/learning-paths/dns-best-practices/concepts/phase-3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>'
  markdown: true
  noindex: false
  route: /learning-paths/dns-best-practices/concepts/phase-3/
  schema: 1
---
<p>Phase 3 is when you make the actual switch to Cloudflare.</p>
<h2 id="1-final-verification"><ol>
<li>Final verification</li>
</ol></h2>
<p>Complete one last check of all DNS records in your Cloudflare dashboard for accuracy and ensure your BIND servers are still operational as a fallback if needed.</p>
<h2 id="2-update-nameservers-at-your-registrar"><ol start="2">
<li>Update nameservers at your registrar</li>
</ol></h2>
<ol>
<li>Log in to your domain registrar's control panel for each domain.</li>
<li>Navigate to the section for managing nameservers.</li>
<li>Replace your current on-prem BIND nameserver entries with your Cloudflare nameservers.</li>
<li>Add the Cloudflare nameservers assigned to your domain (Cloudflare will provide at least two).</li>
<li>Save the changes.</li>
</ol>
<h2 id="3-monitor-propagation"><ol start="3">
<li>Monitor propagation</li>
</ol></h2>
<ul>
<li>
<p>DNS nameserver changes can take time to propagate globally, typically anywhere from a few minutes to 48 hours (though often much faster due to lowered TTLs).</p>
</li>
<li>
<p>Use the commands exemplified below, replacing <code>yourdomain.com</code> by your actual domain.</p>
<ul>
<li><code>dig yourdomain.com NS @8.8.8.8</code> (query Google's DNS)</li>
<li><code>dig yourdomain.com NS @1.1.1.1</code> (query Cloudflare's DNS)</li>
<li><code>whois yourdomain.com</code></li>
<li><code>dig yourdomain.com @tld.nameserver.com</code> (<code>tld.nameserver.com</code> is the nameserver of your domain's TLD. You can find this information by querying it as <code>dig com ns +short</code> where <code>.com</code> is the example.)</li>
</ul>
<p>You are looking for the Cloudflare nameservers to be reported consistently.</p>
</li>
</ul>
<h2 id="4-initial-testing"><ol start="4">
<li>Initial testing</li>
</ol></h2>
<p>Once propagation appears to be widespread, perform basic resolution tests for critical records (for example, your website's <code>A</code> record and any <code>MX</code> records, if you had them set up).</p>
<ul>
<li><code>dig yourdomain.com A +short</code></li>
<li><code>dig yourdomain.com MX +short</code></li>
</ul>
