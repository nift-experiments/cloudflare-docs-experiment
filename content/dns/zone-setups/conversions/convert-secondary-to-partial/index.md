---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/
  description: If you initially set up incoming zone transfers (Cloudflare as secondary), you can later convert your zone to use a partial setup.
  full_title: Convert secondary setup to partial setup · Cloudflare DNS docs
  head_html: <title>Convert secondary setup to partial setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="If you initially set up incoming zone transfers (Cloudflare as secondary), you can later convert your zone to use a partial setup."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/index.md"><meta property="og:title" content="Convert secondary setup to partial setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="If you initially set up incoming zone transfers (Cloudflare as secondary), you can later convert your zone to use a partial setup."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/#page","headline":"Convert secondary setup to partial setup \u00b7 Cloudflare DNS docs","description":"If you initially set up incoming zone transfers (Cloudflare as secondary), you can later convert your zone to use a partial setup.","url":"https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/conversions/convert-secondary-to-partial/
  schema: 1
---
<p>If you initially set up <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">incoming zone transfers (Cloudflare as secondary)</a>, you can later convert your zone to use a <span class="nb-glossary-tooltip" title="CNAME setup">CNAME setup (partial)</span>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-setup">Subdomain setup</h3>
@markup("md", "content/.markup/bodies/7963.md")
</aside>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-dns-conversion-subdomain-setup-callout-mdx-1">Meaning you have one or more subdomains (`sub.example.com`) added to Cloudflare as their own zone, separate from your apex domain (`example.com`).</li></ol></section>
<p>Follow the steps below to achieve this conversion.</p>
<h2 id="1-stop-transferring-the-zone"><ol>
<li>Stop transferring the zone</li>
</ol></h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>DNS Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>DNS Zone Transfers</strong>, and select <strong>Manage linked peers</strong>.</li>
<li>Unlink the peer and select <strong>Save</strong>.</li>
</ol>
<p>At this point, your zone will be read-only.</p>
<h2 id="2-configure-your-authoritative-dns-provider"><ol start="2">
<li>Configure your authoritative DNS provider</li>
</ol></h2>
<ol>
<li>
<p>(Optional) If you are also migrating to a new authoritative DNS provider, export a zone file from the previous provider and import it into the new one.</p>
</li>
<li>
<p>At your authoritative DNS provider, create <code>CNAME</code> records pointing to <code>{your-hostname}.cdn.cloudflare.net</code> for every hostname you wish to proxy through Cloudflare.</p>
<details class="nb-details"><summary>Example CNAME record at authoritative DNS provider</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/7965.md")
</div></details>
<ol start="3">
<li>At your authoritative DNS provider, remove any previously existing <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> records referencing the hostnames you want to proxy through Cloudflare. For these hostnames, leave only the records pointing to <code>{your-hostname}.cdn.cloudflare.net</code>.</li>
</ol>
<h2 id="3-convert-your-cloudflare-zone"><ol start="3">
<li>Convert your Cloudflare zone</li>
</ol></h2>
<ol>
<li>
<p>Back at your Cloudflare zone, confirm that you have all the <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> needed for the hostnames you pointed to <code>{your-hostname}.cdn.cloudflare.net</code> in the previous step. You can also delete any DNS records that have a different type, as they will no longer resolve once you convert your zone to a CNAME setup (partial).</p>
</li>
<li>
<p>Use the <a href="/api/resources/zones/methods/edit/">Edit Zone endpoint</a> with <code>type</code> set to <code>partial</code> to convert the zone type. Existing DNS records will not be affected.</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page, get the <strong>Verification TXT Record</strong> and add it at your authoritative DNS provider.</p>
<details class="nb-details"><summary>Example verification record</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/7966.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7962.md")
</aside>
<h2 id="4-update-nameservers"><ol start="4">
<li>Update nameservers</li>
</ol></h2>
<p>At your domain registrar (or parent zone), <a href="/dns/nameservers/update-nameservers/">update the nameservers</a>. In a CNAME setup (partial), only the nameservers of your external DNS provider should be listed.</p>
<pre tabindex="0"><code>- Remove any `secondary.cloudflare.com` nameservers if you used to have them.&#10;- If you are also migrating to a new authoritative DNS provider, add your new nameservers.&#10;</code></pre>
