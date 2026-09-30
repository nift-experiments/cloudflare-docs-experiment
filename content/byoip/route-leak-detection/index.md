---
cp9:
  canonical: https://developers.cloudflare.com/byoip/route-leak-detection/
  description: Detect unauthorized advertisement of your IP prefixes.
  full_title: Route Leak Detection · Cloudflare BYOIP docs
  head_html: <title>Route Leak Detection · Cloudflare BYOIP docs</title><meta name="generator" content="Nift"><meta name="description" content="Detect unauthorized advertisement of your IP prefixes."><link rel="canonical" href="https://developers.cloudflare.com/byoip/route-leak-detection/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/byoip/route-leak-detection/index.md"><meta property="og:title" content="Route Leak Detection · Cloudflare BYOIP docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect unauthorized advertisement of your IP prefixes."><meta property="og:url" content="https://developers.cloudflare.com/byoip/route-leak-detection/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="BYOIP"><meta name="algolia_product_filter" content="BYOIP"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="BYOIP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/byoip/route-leak-detection/#page","headline":"Route Leak Detection \u00b7 Cloudflare BYOIP docs","description":"Detect unauthorized advertisement of your IP prefixes.","url":"https://developers.cloudflare.com/byoip/route-leak-detection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /byoip/route-leak-detection/
  schema: 1
---
<p>Route Leak Detection protects your routes on the Internet by notifying you when your traffic is routed somewhere it should not go, which could indicate a possible attack. Route Leak Detection also reduces the amount of time needed to mitigate leaks by providing you with timely notifications.</p>
<p>Cloudflare detects route leaks by using several sources of routing data to create a synthesis of how the Internet sees routes to BYOIP users. Cloudflare then watches these views to track any sudden changes that occur on the Internet. If the changes can be correlated to actions Cloudflare has taken, no further action is required. However, if changes have not been made, Cloudflare notifies you to inform you that your routes and users may be at risk.</p>
<h2 id="enable-route-leak-detection">Enable Route Leak Detection</h2>
<details><summary>Route Leak Detection Alert</summary><strong>Who is it for?</strong><p><a href="/byoip/">BYOIP customers</a> who want to receive a notification when their prefixes are advertised in places they should not be.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Purchase of BYOIP.</p>
<strong>What should you do if you receive one?</strong><p>Confirm your traffic is healthy. Reach out to your transit providers to ensure you are behaving as expected and ask them to follow up with any providers accepting the unauthorized routes.</p>
</details>
<p>You must be a user who has brought your own IP address to Cloudflare, which includes Magic Transit, Spectrum, and WAF users. Only prefixes advertised by Cloudflare qualify for Route Leak Detection.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong>.</li>
<li>Locate <strong>Route Leak Detection</strong> from the list &gt; <strong>Select</strong>.</li>
<li>Enter a name and description for the notification.</li>
<li>Enter one or more email addresses to receive the notifications.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
