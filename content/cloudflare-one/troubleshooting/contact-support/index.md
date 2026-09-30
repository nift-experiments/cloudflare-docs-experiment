---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/
  description: Contact Cloudflare Support in Zero Trust.
  full_title: Contact Cloudflare Support · Cloudflare One docs
  head_html: <title>Contact Cloudflare Support · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Contact Cloudflare Support in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/index.md"><meta property="og:title" content="Contact Cloudflare Support · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Contact Cloudflare Support in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/#page","headline":"Contact Cloudflare Support \u00b7 Cloudflare One docs","description":"Contact Cloudflare Support in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/troubleshooting/contact-support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/troubleshooting/contact-support/
  schema: 1
---
<p>If you cannot resolve an issue using our troubleshooting guides, you can <a href="/support/contacting-cloudflare-support/">open a support case</a>.</p>
<p>To help us investigate your issue quickly, please collect and provide the following information when you contact Cloudflare Support.</p>
<h2 id="1-gather-general-information"><ol>
<li>Gather general information</li>
</ol></h2>
<p>For all issues, please include:</p>
<ul>
<li><strong>Timestamp (UTC)</strong>: The exact time the issue occurred.</li>
<li><strong>Detailed description</strong>: A clear description of the problem and the steps to reproduce it.</li>
<li><strong>Actual vs. Expected</strong>: What happened versus what you expected to happen.</li>
<li><strong>Problem frequency</strong>: How often does the issue occur?</li>
<li><strong>Screenshots</strong>: Any relevant screenshots or videos of the error.</li>
<li><strong>Example URLs</strong>: Specific URLs where the issue is occurring.</li>
</ul>
<h2 id="2-collect-product-diagnostics"><ol start="2">
<li>Collect product diagnostics</li>
</ol></h2>
<p>Depending on the product, providing diagnostic files is critical for a technical investigation.</p>
<h3 id="cloudflare-one-client-warp">Cloudflare One Client (WARP)</h3>
If the issue involves the Cloudflare One Client, run the `warp-diag` command on the affected device and attach the resulting `.zip` file to your case. For more information, refer to [Diagnostic logs](/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/).
<h3 id="cloudflare-tunnel">Cloudflare Tunnel</h3>
If the issue involves Cloudflare Tunnel, run the `cloudflared tunnel diag` command and provide the generated report. For more information, refer to [Tunnel diagnostic logs](/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/).
<h3 id="access-and-gateway">Access and Gateway</h3>
For issues related to authentication loops, blocked websites, or policy enforcement:
<ul>
<li><strong>HAR file</strong>: Provide a <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#generate-a-har-file">HAR file</a> captured while reproducing the issue.</li>
<li><strong>Ray ID</strong>: If you see a Cloudflare error page, provide the <strong>Ray ID</strong> displayed at the bottom of the page.</li>
<li><strong>Identity Provider logs</strong>: Relevant logs from your identity provider (IdP) if the issue involves login failures.</li>
<li><strong>Request ID</strong>: For Gateway issues, you can find the <code>request_id</code> (HTTP logs) or <code>query_id</code> (DNS logs) in your <a href="/cloudflare-one/traffic-policies/troubleshooting/">Gateway logs</a>.</li>
</ul>
<h3 id="digital-experience-monitoring-dex">Digital Experience Monitoring (DEX)</h3>
For issues with DEX tests or device monitoring, provide a [remote capture](/cloudflare-one/insights/dex/diagnostics/client-packet-capture/) from the Zero Trust dashboard.
<hr />
<p>For more information, refer to <a href="/support/contacting-cloudflare-support/">Contacting Cloudflare Support</a>.</p>
