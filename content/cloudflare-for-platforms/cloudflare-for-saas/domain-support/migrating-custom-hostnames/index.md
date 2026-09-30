---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/
  description: Learn how to move hostnames between different zones.
  full_title: Move hostnames between zones · Cloudflare for Platforms docs
  head_html: <title>Move hostnames between zones · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to move hostnames between different zones."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/index.md"><meta property="og:title" content="Move hostnames between zones · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to move hostnames between different zones."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/#page","headline":"Move hostnames between zones \u00b7 Cloudflare for Platforms docs","description":"Learn how to move hostnames between different zones.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/
  schema: 1
---
<p>As a SaaS provider, you may want, or have, multiple zones to manage hostnames. Each zone can have different configurations or origins, as well as correlate to varying products. You might shift custom hostnames between zones to enable or disable certain features. Cloudflare allows migration within the same account through the steps below:</p>
<hr />
<h2 id="cname">CNAME</h2>
<p>If your custom hostname uses a CNAME record, add the custom hostname to the new zone and <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">update your DNS record</a> to point to the new zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4101.md")
</aside>
<ol>
<li>
<p><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Add custom hostname</a> to your new zone.</p>
</li>
<li>
<p>Direct your customer to <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">change the DNS record</a> so that it points to the new zone.</p>
</li>
<li>
<p>Confirm that the custom hostname has validated in the new zone.</p>
</li>
<li>
<p>Wait for the certificate to validate automatically through Cloudflare or <a href="/ssl/edge-certificates/changing-dcv-method/methods/#perform-dcv">validate it using Domain Control Validation (DCV)</a>.</p>
</li>
<li>
<p>Remove custom hostname from the old zone.</p>
</li>
</ol>
<p>Once these steps are complete, the custom hostname's traffic will route to the second SaaS zone and will use its configuration.</p>
<h2 id="a-record">A record</h2>
<p>Through <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">Apex Proxying</a> or <a href="/byoip/">BYOIP</a>, you can migrate the custom hostname without action from your end customer.</p>
<ol>
<li>
<p>Verify with the account team that your apex proxying IPs have been assigned to both SaaS zones.</p>
</li>
<li>
<p><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Add custom hostname</a> to the new zone.</p>
</li>
<li>
<p>Confirm that the custom hostname has validated in the new zone.</p>
</li>
<li>
<p>Wait for the certificate to validate automatically through Cloudflare or <a href="/ssl/edge-certificates/changing-dcv-method/methods/#perform-dcv">validate it using DCV</a>.</p>
</li>
<li>
<p>Remove custom hostname from the old zone.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4100.md")
</aside>
<h2 id="wildcard-certificate">Wildcard certificate</h2>
<p>If you are migrating custom hostnames that rely on a Wildcard certificate, Cloudflare cannot automatically complete Domain Control Validation (DCV).</p>
<ol>
<li>
<p><a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Add custom hostname</a> to the new zone.</p>
</li>
<li>
<p>Direct your customer to <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">change the DNS record</a> so that it points to the new zone.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/changing-dcv-method/methods/#perform-dcv">Validate the certificate</a> on the new zone through DCV.</p>
</li>
</ol>
<p>The custom hostname can activate on the new zone even if the certificate is still active on the old zone. This ensures a valid certificate exists during migration. However, it is important to validate the certificate on the new zone as soon as possible.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4099.md")
</aside>
