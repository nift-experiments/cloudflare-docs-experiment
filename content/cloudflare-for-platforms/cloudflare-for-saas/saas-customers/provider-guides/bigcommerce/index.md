---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/
  description: Learn how to configure your Enterprise zone with BigCommerce.
  full_title: BigCommerce · Cloudflare for Platforms docs
  head_html: <title>BigCommerce · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to configure your Enterprise zone with BigCommerce."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/index.md"><meta property="og:title" content="BigCommerce · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to configure your Enterprise zone with BigCommerce."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/#page","headline":"BigCommerce \u00b7 Cloudflare for Platforms docs","description":"Learn how to configure your Enterprise zone with BigCommerce.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/
  schema: 1
---
<p>Cloudflare partners with BigCommerce to provide BigCommerce customers’ websites with Cloudflare’s performance and security benefits.</p>
<p>If you use BigCommerce and also have a Cloudflare plan, you can use your own Cloudflare zone to proxy web traffic to your zone first, then BigCommerce's (the SaaS Provider) zone second. This configuration option is called <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">O2O</a>.</p>
<h2 id="benefits">Benefits</h2>
<p>O2O's benefits include applying your own Cloudflare zone's services and settings — such as <a href="/waf/">WAF</a>, <a href="/bots/plans/bm-subscription/">Bot Management</a>, <a href="/waiting-room/">Waiting Room</a>, and more — on the traffic destined for your BigCommerce environment.</p>
<h2 id="how-it-works">How it works</h2>
<p>For more details about how O2O is different than other Cloudflare setups, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/">How O2O works</a>.</p>
<h2 id="enable">Enable</h2>
<p>BigCommerce customers can enable O2O on any Cloudflare zone plan.</p>
<p>To enable O2O on your account, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create</a> a <code>CNAME</code> DNS record.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Name</th>
<th>Target</th>
<th>Proxy status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CNAME</code></td>
<td><code>&lt;YOUR_HOSTNAME&gt;</code></td>
<td><code>shops.mybigcommerce.com</code></td>
<td>Proxied</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4128.md")
</aside>
<h2 id="product-compatibility">Product compatibility</h2>
<p>When a hostname within your Cloudflare zone has O2O enabled, you assume additional responsibility for the traffic on that hostname because you can now configure various Cloudflare products to affect that traffic. Some of the Cloudflare products compatible with O2O are:</p>
<ul>
<li><a href="/cache/">Caching</a></li>
<li><a href="/workers/">Workers</a></li>
<li><a href="/rules/">Rules</a></li>
</ul>
<p>For a full list of compatible products and potential limitations, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/">Product compatibility</a>.</p>
<h2 id="zone-hold">Zone hold</h2>
<p>If your own Cloudflare zone is on the Enterprise plan, you have access to the <a href="/fundamentals/account/account-security/zone-holds/">zone hold feature</a>, which is a toggle that prevents your domain name from being created as a zone in a different Cloudflare account. Additionally, if the zone hold is enabled, it prevents the activation of custom hostnames onboarded to BigCommerce. BigCommerce would receive the following error message for your custom hostname: <code>The hostname is associated with a held zone. Please contact the owner of this domain to have the hold removed.</code></p>
<p>To successfully activate the custom hostname on BigCommerce, the owner of the zone needs to <a href="/fundamentals/account/account-security/zone-holds/#release-zone-holds">temporarily release the hold</a>. If you are only onboarding a subdomain as a custom hostname to BigCommerce, only the subfeature titled <strong>Also prevent Subdomains</strong> needs to be temporarily disabled.</p>
<p>Once the zone hold is temporarily disabled, follow BigCommerce's instructions to refresh the custom hostname and it should activate.</p>
<h2 id="additional-support">Additional support</h2>
<p>If you are a BigCommerce customer and have set up your own Cloudflare zone with O2O enabled on specific hostnames, contact your Cloudflare Account Team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> for help resolving issues in your own zone.</p>
<p>Cloudflare will consult BigCommerce if there are technical issues that Cloudflare cannot resolve.</p>
