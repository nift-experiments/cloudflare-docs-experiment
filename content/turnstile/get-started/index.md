---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/get-started/
  description: Set up Turnstile to verify visitors without a traditional CAPTCHA.
  full_title: Get started · Cloudflare Turnstile docs
  head_html: <title>Get started · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Turnstile to verify visitors without a traditional CAPTCHA."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Turnstile to verify visitors without a traditional CAPTCHA."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Forms"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/get-started/#page","headline":"Get started \u00b7 Cloudflare Turnstile docs","description":"Set up Turnstile to verify visitors without a traditional CAPTCHA.","url":"https://developers.cloudflare.com/turnstile/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Forms"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/get-started/
  schema: 1
---
<p>Turnstile protects your website forms from bots. It works in two steps: a JavaScript widget runs challenges in the visitor's browser and produces a token, then your server sends that token to Cloudflare to confirm it is valid. This guide covers how to set up both steps.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, you must have:</p>
<ul>
<li><a href="/fundamentals/account/create-account/">A Cloudflare account</a></li>
<li>A website or web application to protect</li>
<li>Basic knowledge of HTML and your preferred server-side language</li>
</ul>
<hr />
<h2 id="process">Process</h2>
<p>A Turnstile widget is an instance of Turnstile embedded on your webpage. Each widget has a <span class="nb-glossary-tooltip" title="sitekey">sitekey</span> (a public identifier you place in your HTML) and a <span class="nb-glossary-tooltip" title="secret key">secret key</span> (a private credential your server uses to validate tokens).</p>
<p>Each widget gets its own unique sitekey and secret key pair, and options for configurations.</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sitekey</td>
<td>Public key used to invoke the Turnstile widget on your site.</td>
</tr>
<tr>
<td>Secret key</td>
<td>Private key used for server-side token validation.</td>
</tr>
<tr>
<td>Configurations</td>
<td>Mode, hostnames, appearance settings, and other options.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15018.md")
</aside>
<p>Implementing Turnstile involves two essential components that work together:</p>
<ol>
<li>
<p>Client-side: <a href="/turnstile/get-started/client-side-rendering/">Embed the widget</a></p>
<p>Add the Turnstile widget to your webpage to challenge visitors and generate tokens. A token is a string (up to 2,048 characters) generated when the visitor completes a challenge.</p>
</li>
<li>
<p>Server-side: <a href="/turnstile/get-started/server-side-validation/">Validate the token</a></p>
<p>Send tokens to Cloudflare's <a href="/turnstile/get-started/server-side-validation/">Siteverify API</a> — the endpoint for validating Turnstile tokens — to confirm they are authentic and have not been tampered with.</p>
</li>
</ol>
<p>Turnstile is designed to be an independent service. You can use Turnstile on any website, regardless of whether it is proxied through the Cloudflare network. This allows for flexible deployment across multi-cloud environments, on-premises infrastructure, or sites using other CDNs. The client-side widget and server-side validation steps are completely self-contained.</p>
<p>Refer to <a href="#implementation">Implementation</a> below for guidance on how to implement Turnstile on your website.</p>
<hr />
<h2 id="implementation">Implementation</h2>
<p>Follow the steps below to implement Turnstile.</p>
<h3 id="1-create-your-widget"><ol>
<li>Create your widget</li>
</ol></h3>
<p>First, you must create a Turnstile widget to get your sitekey and secret key.</p>
<p>Select your preferred implementation method:</p>
<p><a class="nb-link-button" href="/turnstile/get-started/widget-management/dashboard/">Cloudflare dashboard</a></p>
<p><a class="nb-link-button" href="/turnstile/get-started/widget-management/api/">API</a></p>
<p><a class="nb-link-button" href="/turnstile/get-started/widget-management/terraform/">Terraform</a></p>
<h3 id="2-embed-the-widget"><ol start="2">
<li>Embed the widget</li>
</ol></h3>
<p>Add the Turnstile widget to your webpage forms and applications.</p>
<p>Refer to <a href="/turnstile/get-started/client-side-rendering/">Embed the widget</a> to learn more about implicit and explicit rendering methods.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="testing">Testing</h3>
@markup("md", "content/.markup/bodies/15017.md")
</aside>
<h3 id="3-validate-tokens"><ol start="3">
<li>Validate tokens</li>
</ol></h3>
<p>Implement server-side validation to verify the tokens generated by your widgets.</p>
<p>Refer to <a href="/turnstile/get-started/server-side-validation/">Validate the token</a> to secure your implementation with proper token verification.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="testing-1">Testing</h3>
@markup("md", "content/.markup/bodies/15016.md")
</aside>
<h2 id="additional-implementation-options">Additional implementation options</h2>
<h3 id="mobile-configuration">Mobile configuration</h3>
<p>Special considerations are necessary for mobile applications and WebView implementations.</p>
<p>Refer to <a href="/turnstile/get-started/mobile-implementation/">Mobile implementation</a> for more information on mobile application integration.</p>
<h3 id="migration-from-other-captchas">Migration from other CAPTCHAs</h3>
<p>If you are currently using reCAPTCHA, hCaptcha, or another CAPTCHA service, Turnstile can be a drop-in replacement. You can copy and paste our script wherever you have deployed the existing script today.</p>
<p>Refer to <a href="/turnstile/migration/">Migration</a> for step-by-step migration guidance from other CAPTCHA services.</p>
<hr />
<h2 id="security-requirements">Security requirements</h2>
<ul>
<li>
<p>Server-side validation is mandatory. It is critical to enforce Turnstile tokens with the Siteverify API. The Turnstile token could be invalid, expired, or already redeemed. Not verifying the token will leave major vulnerabilities in your implementation. You must call Siteverify to complete your Turnstile configuration. Otherwise, it is incomplete and will result in zeroes for token validation when viewing your metrics in <a href="/turnstile/turnstile-analytics/">Turnstile Analytics</a>.</p>
</li>
<li>
<p>Tokens expire after 300 seconds (5 minutes). Each token can only be validated once. Expired or used tokens must be replaced with fresh challenges.</p>
</li>
</ul>
<hr />
<h2 id="best-practices">Best practices</h2>
<h3 id="security">Security</h3>
<ul>
<li>Protect your secret keys. Never expose secret keys in client-side code.</li>
<li>Rotate your keys regularly. Use API or dashboard to rotate secret keys periodically.</li>
<li>Restrict your hostnames. Only allow widgets on domains that you control.</li>
<li>Monitor the usage. Use analytics to detect unusual patterns.</li>
</ul>
<h3 id="operational">Operational</h3>
<ul>
<li>Use descriptive names. Name widgets based on their purpose, such as &quot;Login Form&quot; or &quot;Contact Page&quot;.</li>
<li>Separate your environments. Use different widgets for development, staging, and production.</li>
<li>Keep track of which widgets are used at which locations.</li>
<li>Store your widget configurations in version control when using Terraform.</li>
</ul>
