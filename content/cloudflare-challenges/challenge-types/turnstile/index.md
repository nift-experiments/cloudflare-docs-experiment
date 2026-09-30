---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/
  description: Embed a CAPTCHA-alternative widget that verifies visitors without interrupting their experience.
  full_title: Turnstile · Cloudflare challenges docs
  head_html: <title>Turnstile · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="Embed a CAPTCHA-alternative widget that verifies visitors without interrupting their experience."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/index.md"><meta property="og:title" content="Turnstile · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Embed a CAPTCHA-alternative widget that verifies visitors without interrupting their experience."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Challenges"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/#page","headline":"Turnstile \u00b7 Cloudflare challenges docs","description":"Embed a CAPTCHA-alternative widget that verifies visitors without interrupting their experience.","url":"https://developers.cloudflare.com/cloudflare-challenges/challenge-types/turnstile/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/challenge-types/turnstile/
  schema: 1
---
<p><a href="/turnstile/">Turnstile</a> is Cloudflare's CAPTCHA-alternative solution. You can embed Turnstile as a widget on your website or application, where it runs a client-side challenge directly in the background of the visitor's browser.</p>
<p>Turnstile differs from Challenges Pages in that the challenge does not pause the request or interrupt the user's experience. Since the widget is embedded onto the webpage and only runs on a specific part of the HTML, the visitor will have already arrived at the destination URL and is viewing the page when they encounter a Turnstile widget. Instead of blocking the visitor from accessing the entire website, the Turnstile widget prevents the visitor from certain actions such as completing login or sign up forms, and more, until the widget is solved.</p>
<p>In most cases, nothing further is required from the visitor. However, if necessary, Turnstile may display a simple checkbox that the visitor must click to proceed.</p>
<p>After the challenge passes, Turnstile issues a clearance token to the visitor that must be validated via the <a href="/turnstile/get-started/server-side-validation/">Siteverify API</a> before completing a sensitive action like login, sign up, or other form submissions.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4035.md")
</aside>
<h2 id="widget-types">Widget types</h2>
<p>While there are three types of widgets that you can choose to implement on your website or application, the challenge logic behind them remains the same.</p>
<ul>
<li>
<p><strong>Managed (recommended)</strong>: Functions similar to a Managed Challenge Page. It selects a challenge based on the signals gathered from the visitor's browser and presents an interaction only if it detects potentially automated traffic.</p>
</li>
<li>
<p><strong>Non-Interactive</strong>: The widget is displayed, but the visitor does not need to interact with it to verify their identity.</p>
</li>
<li>
<p><strong>Invisible</strong>: The widget is completely invisible to the visitor, but the challenge still runs in the background.</p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="link-to-cloudflare-s-turnstile-privacy-policy">Link to Cloudflare's Turnstile Privacy Policy</h3>
@markup("md", "content/.markup/bodies/4034.md")
</aside>
<h2 id="implementation">Implementation</h2>
<p>When you create a widget for your website or application via the Cloudflare dashboard, you will receive a sitekey.</p>
<p>The sitekey is used with <a href="/turnstile/get-started/client-side-rendering/#implicitly-render-the-turnstile-widget">client-side rendering</a> by adding it to the <code>&lt;div&gt; </code> container placeholder. You will then place that <code>&lt;div&gt; </code> code snippet where you want to add the widget to your site page or form.</p>
<h2 id="get-started">Get started</h2>
<p>Refer to the <a href="/turnstile/get-started/">Turnstile documentation</a> for guidance on implementing a widget to your website or application.</p>
