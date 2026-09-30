---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/
  description: Fix mixed content by rewriting HTTP URLs to HTTPS in page responses.
  full_title: Automatic HTTPS Rewrites · Cloudflare SSL/TLS docs
  head_html: <title>Automatic HTTPS Rewrites · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Fix mixed content by rewriting HTTP URLs to HTTPS in page responses."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/index.md"><meta property="og:title" content="Automatic HTTPS Rewrites · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fix mixed content by rewriting HTTP URLs to HTTPS in page responses."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/#page","headline":"Automatic HTTPS Rewrites \u00b7 Cloudflare SSL/TLS docs","description":"Fix mixed content by rewriting HTTP URLs to HTTPS in page responses.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/automatic-https-rewrites/
  schema: 1
---
<p>Automatic HTTPS Rewrites prevents end users from seeing &quot;mixed content&quot; errors by rewriting URLs from <code>http</code> to <code>https</code> for resources or links on your web site that can be served with HTTPS.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="additional-details">Additional details</h2>
<p>If your site contains links or references to HTTP URLs that are also available securely via HTTPS, Automatic HTTPS Rewrites can help. If you connect to your site over HTTPS and the lock icon is not present, or has a yellow warning triangle on it, your site may contain references to HTTP assets (“mixed content”).</p>
<p>Mixed content is often due to factors not under the website owner’s control such as embedded third-party content or complex content management systems. By rewriting URLs from “http” to “https”, Automatic HTTPS Rewrites simplifies the task of making your entire website available over HTTPS, helping to eliminate mixed content errors and ensuring that all data loaded by your website is protected from eavesdropping and tampering.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14147.md")
</aside>
<h2 id="enable-automatic-https-rewrites">Enable Automatic HTTPS Rewrites</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14150.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14146.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Before a rewrite is applied, Cloudflare checks the HTTP resources to ensure they are accessible via HTTPS. If they are not available over HTTPS, Cloudflare cannot rewrite the URL.</p>
<p>Some resources are loaded by JavaScript or CSS via HTTP when the site is loaded in a browser. You will see mixed content warnings in those situations. To determine which URLs do not have HTTPS support, Cloudflare uses data from <a href="https://www.eff.org/https-everywhere/faq#how-do-i-add-my-own-site-to-https-everywhere">EFF’s HTTPS Everywhere</a> and <a href="https://hstspreload.org">Chrome’s HSTS preload list</a>. If your zone is not on one of these lists, only active content will be rewritten. Passive content (such as images) will not be rewritten and will still cause mixed content errors.</p>
<p>If a third-party domain supports HTTPS and is not rewritten automatically, you can manually change those links to relative links or HTTPS links. Alternatively, you can ask the third-party domain owner to submit their site for inclusion in the HTTPS Everywhere rulesets, which <a href="https://github.com/EFForg/https-everywhere/">accept pull requests on GitHub</a>. For more information on how to fix mixed content errors, refer to <a href="/ssl/troubleshooting/mixed-content-errors/">Troubleshooting mixed content errors</a>.</p>
