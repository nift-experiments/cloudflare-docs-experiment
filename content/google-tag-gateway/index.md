---
cp9:
  canonical: https://developers.cloudflare.com/google-tag-gateway/
  description: Deploy Google measurement tags from your domain for improved ad signal recovery.
  full_title: Google tag gateway for advertisers · Google tag gateway for advertisers docs
  head_html: <title>Google tag gateway for advertisers · Google tag gateway for advertisers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Google measurement tags from your domain for improved ad signal recovery."><link rel="canonical" href="https://developers.cloudflare.com/google-tag-gateway/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/google-tag-gateway/index.md"><meta property="og:title" content="Google tag gateway for advertisers · Google tag gateway for advertisers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Google measurement tags from your domain for improved ad signal recovery."><meta property="og:url" content="https://developers.cloudflare.com/google-tag-gateway/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Google tag gateway for advertisers"><meta name="algolia_product_filter" content="Google tag gateway for advertisers"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Google tag gateway for advertisers"><meta name="pcx_tags" content="Google"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/google-tag-gateway/#page","headline":"Google tag gateway for advertisers \u00b7 Google tag gateway for advertisers docs","description":"Deploy Google measurement tags from your domain for improved ad signal recovery.","url":"https://developers.cloudflare.com/google-tag-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Google"]}</script>
  markdown: true
  noindex: false
  route: /google-tag-gateway/
  schema: 1
---
<p>Google tag gateway for advertisers allows website owners using Cloudflare as a CDN to get the most out of ad measurement tools with just a few clicks. It allows you to deploy Google scripts using your own domain, enhancing data privacy and improving signal measurement recovery. Unlike standard setups where tags are requested from a Google domain, Google tag gateway for advertisers loads the tag from your domain and sends measurement events to your domain, where they are forwarded to Google.</p>
<p>Learn more about why we built it and how it works in our <a href="https://blog.cloudflare.com/google-tag-gateway-for-advertisers/">blog post</a>.</p>
<h2 id="pricing">Pricing</h2>
<p>Google tag gateway for advertisers is free to use. Requests routed through the gateway do not count toward usage or billing for other Cloudflare products such as <a href="/cache/">CDN</a>, <a href="/waf/">WAF</a>, or <a href="/bots/">Bot Management</a>.</p>
<h2 id="get-started">Get started</h2>
<p>Site owners can enable this feature in one of two ways: through the Google tag console, or through the <a href="https://dash.cloudflare.com/?to=/:account/tag-management/google-tag-gateway">Cloudflare dashboard</a>.</p>
<h3 id="configure-in-google-tag-manager">Configure in Google Tag Manager</h3>
The fastest way to set up Google tag gateway for advertisers is in Google Tag Manager. [Follow the steps in Google's Help Center](https://support.google.com/analytics/answer/16061641).
<h3 id="configure-in-the-cloudflare-dashboard">Configure in the Cloudflare dashboard</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/997.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Google Tag Gateway</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your domain.</li>
<li>Enable the toggle for <strong>Turn on and configure Google tag gateway</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/google-tag-gateway/google-tag-configuration.png" alt="Google tag gateway for advertisers configuration" /></p>
<ol start="4">
<li>Add your Google tag ID and the path on your website reserved for the Google tag.
The <a href="https://support.google.com/analytics/answer/9539598?hl=en">Google tag ID</a> can be found in the Google Tag Experience dashboard. The measurement path is an unused path on your site that will load Google Tag Manager and all subsequent measurement requests.</li>
</ol>
<p><img src="/assets/upstream/images/google-tag-gateway/google-tag-id-path.png" alt="Add to ID and path" /></p>
<ol start="5">
<li>Once you click <strong>Save</strong>, Google tag gateway for advertisers will be enabled on your zone. If you already have a GTM script on your website, this First Party Tag will override the existing script.</li>
</ol>
<p>Now that you have authenticated into your Cloudflare account and configured GTM in first-party mode, your Google Tags will be loaded using <code>https://your-domain/measurement-path/...</code>and subsequent measurement requests will be served by Cloudflare.</p>
<h2 id="zone-level-configuration">Zone-level configuration</h2>
<p>Google tag gateway for advertisers is configured at the zone level. When you enable it for a zone (for example, <code>example.com</code>), it applies to all hostnames and subdomains within that zone, including custom hostnames. Currently, it is not possible to enable or disable the feature for individual subdomains independently. <a href="/rules/configuration-rules/">Configuration Rules</a> cannot be used to control or disable the tag injection on specific subdomains.</p>
<h3 id="handle-subdomain-specific-logic-with-triggers">Handle subdomain-specific logic with triggers</h3>
<p>If you need different tag behavior for specific subdomains (for example, only firing certain tags on <code>shop.example.com</code>), you can use <a href="https://support.google.com/tagmanager/answer/7679316">Google Tag Manager triggers</a> to control when tags fire. For example, you can create a trigger condition like <strong>Page Hostname</strong> equals <code>shop.example.com</code> to restrict a tag to a specific subdomain.</p>
<p>This approach lets you maintain a single zone-wide Google tag gateway configuration while still customizing tag behavior per subdomain.</p>
<h2 id="related-resources">Related resources</h2>
- [Google Developer Docs: Set up Google tag gateway for advertisers](https://developers.google.com/tag-platform/tag-manager/gateway/setup-guide?setup=auto)
- [Google Help Center: Set up Google tag gateway for advertisers in the Google tag with Cloudflare](https://support.google.com/tagmanager/answer/16061406)
- [Google Help Center: Set up Google tag gateway for advertisers in Google Tag Manager with Cloudflare](https://support.google.com/analytics/answer/16061641)
