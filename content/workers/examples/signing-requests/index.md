---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/signing-requests/
  description: Verify a signed request using the HMAC and SHA-256 algorithms or return a 403.
  full_title: Sign requests · Cloudflare Workers docs
  head_html: <title>Sign requests · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Verify a signed request using the HMAC and SHA-256 algorithms or return a 403."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/signing-requests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/signing-requests/index.md"><meta property="og:title" content="Sign requests · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Verify a signed request using the HMAC and SHA-256 algorithms or return a 403."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/signing-requests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Security,WebCrypto,JavaScript,TypeScript,Python"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/signing-requests/#page","headline":"Sign requests \u00b7 Cloudflare Workers docs","description":"Verify a signed request using the HMAC and SHA-256 algorithms or return a 403.","url":"https://developers.cloudflare.com/workers/examples/signing-requests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Security","WebCrypto","JavaScript","TypeScript","Python"]}</script>
  markdown: true
  noindex: false
  route: /workers/examples/signing-requests/
  schema: 1
---
<p class="article-summary">Verify a signed request using the HMAC and SHA-256 algorithms or return a 403.</p>
<p>If you want to get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/signing-requests"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16341.md")
</aside>
<p>You can both verify and generate signed requests from within a Worker using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Crypto/subtle">Web Crypto APIs</a>.</p>
<p>The following Worker will:</p>
<ul>
<li>
<p>For request URLs beginning with <code>/generate/</code>, replace <code>/generate/</code> with <code>/</code>, sign the resulting path with its timestamp, and return the full, signed URL in the response body.</p>
</li>
<li>
<p>For all other request URLs, verify the signed URL and allow the request through.</p>
</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16346.md")
</div></div>
<h2 id="validate-signed-requests-using-the-waf">Validate signed requests using the WAF</h2>
<p>The provided example code for signing requests is compatible with the <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> Rules language function. This means that you can verify requests signed by the Worker script using a <a href="/waf/custom-rules/use-cases/configure-token-authentication/#option-2-configure-using-custom-rules">custom rule</a>.</p>
