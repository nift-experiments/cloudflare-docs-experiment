---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/migration/recaptcha/
  description: Migrate from Google reCAPTCHA to Cloudflare Turnstile.
  full_title: Migrate from reCAPTCHA · Cloudflare Turnstile docs
  head_html: <title>Migrate from reCAPTCHA · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from Google reCAPTCHA to Cloudflare Turnstile."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/migration/recaptcha/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/migration/recaptcha/index.md"><meta property="og:title" content="Migrate from reCAPTCHA · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from Google reCAPTCHA to Cloudflare Turnstile."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/migration/recaptcha/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Migration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/migration/recaptcha/#page","headline":"Migrate from reCAPTCHA \u00b7 Cloudflare Turnstile docs","description":"Migrate from Google reCAPTCHA to Cloudflare Turnstile.","url":"https://developers.cloudflare.com/turnstile/migration/recaptcha/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Migration"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/migration/recaptcha/
  schema: 1
---
<p>If you are using reCAPTCHA today, you can switch seamlessly to Cloudflare Turnstile by following the step-by-step guide below to assist with the upgrade process.</p>
<p>To complete the migration, you must obtain the <a href="/turnstile/get-started/widget-management/">sitekey and secret key</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15001.md")
</aside>
<h2 id="client-side-integration">Client-side integration</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15002.md")
</div>
<h2 id="server-side-integration">Server-side integration</h2>
<p>Update the server-side integration by replacing the Siteverify URL.</p>
<p>Replace <code>https://www.google.com/recaptcha/api/siteverify</code> with the following:</p>
<pre tabindex="0"><code class="language-txt">https://challenges.cloudflare.com/turnstile/v0/siteverify&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="differences-to-recaptcha-s-siteverify">Differences to reCAPTCHA's Siteverify</h3>
@markup("md", "content/.markup/bodies/14998.md")
</aside>
