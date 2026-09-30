---
cp9:
  canonical: https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/
  description: How APO handles query parameters, UTMs, and cookies in cached responses.
  full_title: Query parameters and cached responses · Cloudflare Automatic Platform Optimization docs
  head_html: <title>Query parameters and cached responses · Cloudflare Automatic Platform Optimization docs</title><meta name="generator" content="Nift"><meta name="description" content="How APO handles query parameters, UTMs, and cookies in cached responses."><link rel="canonical" href="https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/index.md"><meta property="og:title" content="Query parameters and cached responses · Cloudflare Automatic Platform Optimization docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How APO handles query parameters, UTMs, and cookies in cached responses."><meta property="og:url" content="https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Automatic Platform Optimization"><meta name="algolia_product_filter" content="Automatic Platform Optimization"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Automatic Platform Optimization"><meta name="pcx_tags" content="Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/#page","headline":"Query parameters and cached responses \u00b7 Cloudflare Automatic Platform Optimization docs","description":"How APO handles query parameters, UTMs, and cookies in cached responses.","url":"https://developers.cloudflare.com/automatic-platform-optimization/reference/query-parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies"]}</script>
  markdown: true
  noindex: false
  route: /automatic-platform-optimization/reference/query-parameters/
  schema: 1
---
<p>Query parameters often signal the presence of dynamic content. As a result, if there are query parameters in the URL, APO bypasses the cache and attempts to get a new version of the page from the origin by default. Because query parameters are also often used for marketing attribution, like UTMs, quick loading times are especially important for users.</p>
<p>To add a query parameter to our allowlist, <a href="https://community.cloudflare.com/">create a post in the community</a> for consideration.</p>
<p>APO serves cached content as long as the query parameters in the URL are one of the following:</p>
<ul>
<li><code>ref</code></li>
<li><code>utm_source</code></li>
<li><code>utm_medium</code></li>
<li><code>utm_campaign</code></li>
<li><code>utm_term</code></li>
<li><code>utm_content</code></li>
<li><code>utm_expid</code></li>
<li><code>fbclid</code></li>
<li><code>fb_action_ids</code></li>
<li><code>fb_action_types</code></li>
<li><code>fb_source</code></li>
<li><code>mc_cid</code></li>
<li><code>mc_eid</code></li>
<li><code>gclid</code></li>
<li><code>dclid</code></li>
<li><code>_ga</code></li>
<li><code>campaignid</code></li>
<li><code>adgroupid</code></li>
<li><code>_ke</code></li>
<li><code>cn-reloaded</code></li>
<li><code>age-verified</code></li>
<li><code>ao_noptimize</code></li>
<li><code>usqp</code></li>
<li><code>mkt_tok</code></li>
<li><code>epik</code></li>
<li><code>ck_subscriber_id</code></li>
</ul>
<h2 id="cookies-prefixes-that-always-bypass-cache">Cookies prefixes that always bypass cache</h2>
<ul>
<li><code>wp-</code></li>
<li><code>wordpress</code></li>
<li><code>comment_</code></li>
<li><code>woocommerce_</code></li>
<li><code>xf_</code></li>
<li><code>edd_</code></li>
<li><code>jetpack</code></li>
<li><code>yith_wcwl_session_</code></li>
<li><code>yith_wrvp_</code></li>
<li><code>wpsc_</code></li>
<li><code>ecwid</code></li>
<li><code>ec_</code></li>
<li><code>bookly_</code></li>
<li><code>bookly</code></li>
</ul>
