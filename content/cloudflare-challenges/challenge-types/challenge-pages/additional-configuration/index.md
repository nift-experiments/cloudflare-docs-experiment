---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/
  description: Customize challenge pages with multi-language support, branding, and text options.
  full_title: Additional configuration · Cloudflare challenges docs
  head_html: <title>Additional configuration · Cloudflare challenges docs</title><meta name="generator" content="Nift"><meta name="description" content="Customize challenge pages with multi-language support, branding, and text options."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/index.md"><meta property="og:title" content="Additional configuration · Cloudflare challenges docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Customize challenge pages with multi-language support, branding, and text options."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Challenges"><meta name="algolia_product_filter" content="Challenges"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Challenges"><meta name="pcx_tags" content="CSP,Headers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/#page","headline":"Additional configuration \u00b7 Cloudflare challenges docs","description":"Customize challenge pages with multi-language support, branding, and text options.","url":"https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["CSP","Headers"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-challenges/challenge-types/challenge-pages/additional-configuration/
  schema: 1
---
<h2 id="multi-language-support">Multi-language support</h2>
<p>Refer to <a href="/cloudflare-challenges/reference/supported-languages/">supported languages</a> for more information.</p>
<hr />
<h2 id="favicon-customization">Favicon customization</h2>
<p>Cloudflare Challenges take the favicon of your website using <code>GET /favicon.ico</code> and displays it on the Challenge Page.</p>
<p>You can customize your favicon by using the HTML snippet below.</p>
<pre tabindex="0"><code class="language-html">&lt;link rel=&quot;shortcut icon&quot; href=&quot;&lt;FAVICON_LINK&gt;&quot; /&gt;&#10;</code></pre>
<hr />
<h2 id="custom-content-security-policy-csp-and-error-pages">Custom Content Security Policy (CSP) and error pages</h2>
<p>A Content Security Policy (CSP) controls which scripts and resources a browser is allowed to load on a page. Challenge pages depend on specific Cloudflare scripts, so custom CSP configurations can prevent challenges from working.</p>
<p>You cannot set your own CSP or Referer-Policy on challenge pages using <code>&lt;meta&gt;</code> tags or <a href="/rules/transform/">Transform Rules</a>. Origin response headers can still be modified in a challenge page context, but doing so may cause the challenge to break.</p>
<p>If you have a <a href="/rules/transform/">Transform Rule</a> that modifies HTTP response headers across your website (for example, adding custom CSP headers), the rule will interfere with challenge pages and cause them to fail.</p>
<p>To prevent this, modify your Transform Rule expression to exclude challenge page responses. Add the following condition to the beginning of your expression:</p>
<pre tabindex="0"><code class="language-txt">not cf.response.error_type in {&quot;managed_challenge&quot; &quot;iuam&quot; &quot;legacy_challenge&quot; &quot;country_challenge&quot;}&#10;</code></pre>
<p>This expression skips your header modifications when Cloudflare serves a challenge page, so the challenge scripts load correctly.</p>
<hr />
<h2 id="custom-challenge-pages">Custom Challenge Pages</h2>
<p>Before defining a custom Challenge Page in your Cloudflare account, you will need to design and code that page. It can be hosted on your own web server or using a Cloudflare product like <a href="/rules/snippets/">Snippets</a>.</p>
<p>Refer to <a href="/rules/custom-errors/edit-error-pages/#1-design-your-custom-error-page">Design your custom error page</a> for more information.</p>
<h3 id="how-it-works">How it works</h3>
<p>When you configure a custom challenge page, Cloudflare fetches your uploaded HTML template and replaces the <code>::CF_WIDGET_BOX::</code> placeholder with the challenge script.</p>
<h3 id="placeholder-tokens">Placeholder tokens</h3>
<p>The custom error token provides diagnostic information or specific functionality that appears on the error page. Refer to <a href="/rules/custom-errors/reference/error-tokens/">Error tokens</a> for more details.</p>
<ul>
<li><code>::CF_WIDGET_BOX::</code></li>
<li><code>::CAPTCHA_BOX::</code></li>
<li><code>::IM_UNDER_ATTACK_BOX::</code></li>
<li><code>::CLIENT_IP::</code></li>
<li><code>::RAY_ID::</code></li>
<li><code>::GEO::</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4051.md")
</aside>
<h3 id="requirements">Requirements</h3>
<ol>
<li><code>::CF_WIDGET_BOX::</code> must appear exactly once in the body. This is where the challenge script is injected.</li>
<li><code>&lt;head&gt;</code> tag must be present.</li>
<li>Cloudflare will set <code>cTplC: 1</code> in the browser's <code>window._cf_chl_opt</code> when a custom template is in use. Do not add your own <code>window._cf_chl_opt</code>. Any existing definition will cause conflicts.</li>
<li>Do not block <code>/cdn-cgi/challenge-platform/</code> paths via Content Security Policy (CSP). Challenges will not work correctly with this kind of block in place.</li>
<li>The page is served for all three challenge types (managed, interactive, non-interactive) if you use <code>::CF_WIDGET_BOX::</code>.</li>
</ol>
<h3 id="templates">Templates</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4054.md")
</div></div>
