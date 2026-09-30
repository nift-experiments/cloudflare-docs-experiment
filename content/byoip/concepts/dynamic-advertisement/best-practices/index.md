---
cp9:
  canonical: https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/
  description: Best practices for managing dynamic IP prefix advertisement.
  full_title: Best practices for dynamic advertisement · Cloudflare BYOIP docs
  head_html: <title>Best practices for dynamic advertisement · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Best practices for managing dynamic IP prefix advertisement."><link rel="canonical" href="https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/index.md"><meta property="og:title" content="Best practices for dynamic advertisement · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Best practices for managing dynamic IP prefix advertisement."><meta property="og:url" content="https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="BYOIP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/#page","headline":"Best practices for dynamic advertisement \u00b7 Cloudflare BYOIP docs","description":"Best practices for managing dynamic IP prefix advertisement.","url":"https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /byoip/concepts/dynamic-advertisement/best-practices/
  schema: 1
---
<h2 id="prerequisites">Prerequisites</h2>
<p>To prevent issues and simplify the advertisement process during an attack scenario, complete the following tasks.</p>
<ul>
<li>
<p>Assign appropriate user roles. Ensure that users assigned to manage the status of IP prefix advertisement have the <strong>Administrator</strong> or <strong>Super Administrator</strong> role in your Cloudflare account. For more information, refer to <a href="/fundamentals/manage-members/">Setting up Multi-user accounts on Cloudflare</a>.</p>
</li>
<li>
<p>Get a list of the prefix IDs that you want to manage. Maintain a list of Cloudflare prefix IDs to simplify dynamic advertisement management and operations. You can <a href="#obtain-prefix-ids">obtain prefix IDs</a> via the Cloudflare dashboard or use the <a href="/api/resources/addressing/subresources/prefixes/methods/list/">list prefixes</a> operation in the Cloudflare API. Refer to these prefix IDs when managing prefix advertisement.</p>
</li>
</ul>
<h2 id="enable-prefix-advertisement">Enable prefix advertisement</h2>
<p>You can avoid latency and the possibility of dropped routes by enabling prefix advertisement from Cloudflare before you withdraw the advertisement from your data center.</p>
<ol>
<li>Refer to <a href="#configure-dynamic-advertisement">configure dynamic advertisement</a>. This operation requires your account ID, prefix IDs, and API key.</li>
<li>Verify the advertisement using a looking glass of your choice, such as <a href="https://lg.he.net/">Hurricane Electric Internet Services</a>. Use the Cloudflare ASN (<code>13335</code>) to track the advertisement route.</li>
<li>Remove the prefix advertisement that originates from your data center.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3793.md")
</aside>
<p>Enablement takes approximately five to seven minutes.</p>
<h2 id="disable-or-withdraw-prefix-advertisement">Disable or withdraw prefix advertisement</h2>
<ol>
<li>Add the prefix advertisement to your data center.</li>
<li>(Optional) Verify the advertisement using a looking glass of your choice, such as <a href="https://lg.he.net/">Hurricane Electric Internet Services</a>.</li>
<li>Refer to <a href="#configure-dynamic-advertisement">configure dynamic advertisement</a>. This operation requires your account ID, prefix IDs, and API key.</li>
</ol>
<p>Disablement takes approximately 15 minutes.</p>
<h2 id="configure-dynamic-advertisement">Configure dynamic advertisement</h2>
<h3 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h3>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>IP Addresses</strong> &gt; <strong>BYOIP Prefixes</strong>.</li>
<li>Select <strong>Edit</strong> at the end of the entry.</li>
<li>From <strong>Edit IP Prefixes</strong>, select <strong>Advertised</strong> or <strong>Withdrawn</strong> under <strong>Status</strong>.</li>
<li>Select <strong>Save</strong> to commit your changes.</li>
</ol>
<p>After saving your changes, it takes between two to seven minutes to enable advertisement and approximately 15 minutes to disable or withdraw advertisement.</p>
<h3 id="via-the-api">Via the API</h3>
<p>To configure prefix advertisement with the Cloudflare API, use the <a href="/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/">IP Address Management and Dynamic Advertisement</a> API.</p>
<p>Most dynamic advertisement operations require that you supply the Cloudflare ID for any prefix you want to access with the Cloudflare API. The following section outlines how to obtain prefix IDs.</p>
<h2 id="obtain-prefix-ids">Obtain prefix IDs</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3796.md")
</div></div>
