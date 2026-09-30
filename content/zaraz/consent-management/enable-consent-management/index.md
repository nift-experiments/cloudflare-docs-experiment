---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/consent-management/enable-consent-management/
  description: Enable and configure Zaraz Consent Management.
  full_title: Enable the Consent Management platform (CMP) · Cloudflare Zaraz docs
  head_html: <title>Enable the Consent Management platform (CMP) · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable and configure Zaraz Consent Management."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/consent-management/enable-consent-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/consent-management/enable-consent-management/index.md"><meta property="og:title" content="Enable the Consent Management platform (CMP) · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable and configure Zaraz Consent Management."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/consent-management/enable-consent-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/consent-management/enable-consent-management/#page","headline":"Enable the Consent Management platform (CMP) \u00b7 Cloudflare Zaraz docs","description":"Enable and configure Zaraz Consent Management.","url":"https://developers.cloudflare.com/zaraz/consent-management/enable-consent-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/consent-management/enable-consent-management/
  schema: 1
---
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Consent</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Turn on **Enable Consent Management**.
3. In **Consent modal text** fill in any legal information required in your country. Use HTML code to format your information as you would in any other HTML editor.
4. Under **Purposes**, select **Add new Purpose**. Give your new purpose a name and a description. Purposes are the reasons for using third-party tools in your website.
5. In **Assign purpose to tools**, match tools to purposes by selecting one of the purposes previously created from the drop-down menu. Do this for all your tools.
6. Select **Save**.
<p>Your Consent Management platform is ready. Your website should now display a modal asking for consent for the tools you have configured.</p>
<h2 id="adding-different-languages">Adding different languages</h2>
<p>In your Zaraz consent settings, you can add your consent modal text and purposes in various languages.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Consent</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select a default language of your choice. The default setting is English.
3. In **Consent modal text** and **Purposes**, you can select different languages and add translations.
<h2 id="overriding-the-consent-modal-language">Overriding the consent modal language</h2>
<p>By default, the Zaraz Consent Management Platform will try to match the language of the consent modal with the language requested by the browser, using the <code>Accept-Language</code> HTTP header.
If, for any reason, you would like to force the consent modal language to a specific one, you can use the <code>zaraz.set</code> Web API to define the default <code>__zarazConsentLanguage</code> value.</p>
<p>Below is an example that forces the language shown to be American English.</p>
<pre tabindex="0"><code class="language-html">&lt;script&gt;&#10;  zaraz.set(&#x27;__zarazConsentLanguage&#x27;, &#x27;en-US&#x27;)&#10;&lt;/script&gt;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>If the default consent modal does not suit your website's design, you can use the <a href="/zaraz/consent-management/custom-css/">Custom CSS tool</a> to add your own custom design.</p>
