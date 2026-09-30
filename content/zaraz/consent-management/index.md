---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/consent-management/
  description: Manage visitor consent for third-party tools with Zaraz.
  full_title: Zaraz Consent Management platform · Cloudflare Zaraz docs
  head_html: <title>Zaraz Consent Management platform · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage visitor consent for third-party tools with Zaraz."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/consent-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/consent-management/index.md"><meta property="og:title" content="Zaraz Consent Management platform · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage visitor consent for third-party tools with Zaraz."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/consent-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Zaraz"><meta name="pcx_tags" content="Privacy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/consent-management/#page","headline":"Zaraz Consent Management platform \u00b7 Cloudflare Zaraz docs","description":"Manage visitor consent for third-party tools with Zaraz.","url":"https://developers.cloudflare.com/zaraz/consent-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy"]}</script>
  markdown: true
  noindex: false
  route: /zaraz/consent-management/
  schema: 1
---
<p>Zaraz provides a Consent Management platform (CMP) to help you address and manage required consents under the European <a href="https://gdpr-info.eu/">General Data Protection Regulation (GDPR)</a> and the <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02002L0058-20091219&amp;from=EN#tocId7">Directive on privacy and electronic communications</a>. This consent platform lets you easily create a consent modal for your website based on the tools you have configured. With Zaraz CMP, you can make sure Zaraz only loads tools under the umbrella of the specific purposes your users have agreed to.</p>
<p>The consent modal added to your website is concise and gives your users an easy way to opt-in to any purposes of data processing your tools need.</p>
<h2 id="crucial-vocabulary">Crucial vocabulary</h2>
<p>The Zaraz Consent Management platform (CMP) has a <strong>Purposes</strong> section. This is where you will have to create purposes for the third-party tools your website uses. To better understand the terms involved in dealing with personal data, refer to these definitions:</p>
<ul>
<li><strong>Purpose</strong>: The reason you are loading a given tool on your website, such as to track conversions or improve your website’s layout based on behavior tracking. One purpose can be assigned to many tools, but one tool can be assigned only to one purpose.</li>
<li><strong>Consent</strong>: An affirmative action that the user makes, required to store and access cookies (or other persistent data, like <code>LocalStorage</code>) on the users’ computer/browser.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17605.md")
</aside>
<h2 id="purposes-and-tools">Purposes and tools</h2>
<p>When you add a new tool to your website, Zaraz does not assign any purpose to it. This means that this tool will skip consent by default. Remember to check the <a href="/zaraz/consent-management/enable-consent-management/">Consent Management settings</a> every time you set up a new tool. This helps ensure you avoid a situation where your tool is triggered before the user gives consent.</p>
<p>The user’s consent preferences are stored within a first-party cookie. This cookie is a JSON file that maps the purposes’ ID to a <code>true</code>/<code>false</code>/missing value:</p>
<ul>
<li><code>true</code> value: The user gave consent.</li>
<li><code>false</code>value: The user refused consent.</li>
<li>Missing value: The user has not made a choice yet.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/17604.md")
</aside>
<h2 id="important-things-to-note">Important things to note</h2>
<ul>
<li>Purposes that have no tools assigned will not show up in the CMP modal.</li>
<li>If a tool is assigned to a purpose, it will not run unless the user gives consent for the purpose the tool is assigned for.</li>
<li>Once your website loads for a given user for the first time, all the triggers you have configured for tools that are waiting for consent are cached in the browser. Then, they will be fired when/if the user gives consent, so they are not lost.</li>
<li>If the user visits your website for the first time, the consent modal will automatically show up. This also happens if the user has previously visited your website, but in the meantime you have enabled CMP.</li>
<li>On subsequent visits, the modal will not show up. You can make the modal show up by calling the function <code>zaraz.showConsentModal()</code> — for example, by binding it to a button.</li>
</ul>
