---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/embeds/
  description: Embed third-party widgets like chat and support tools with Zaraz.
  full_title: Embeds · Cloudflare Zaraz docs
  head_html: <title>Embeds · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Embed third-party widgets like chat and support tools with Zaraz."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/embeds/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/embeds/index.md"><meta property="og:title" content="Embeds · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Embed third-party widgets like chat and support tools with Zaraz."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/embeds/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/embeds/#page","headline":"Embeds \u00b7 Cloudflare Zaraz docs","description":"Embed third-party widgets like chat and support tools with Zaraz.","url":"https://developers.cloudflare.com/zaraz/embeds/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/embeds/
  schema: 1
---
<p>Embeds are tools for incorporating external content, like social media posts, directly onto webpages, enhancing user engagement without compromising site performance and security.</p>
<p>Cloudflare Zaraz introduces server-side rendering for embeds, avoiding third-party JavaScript to improve security, privacy, and page speed. This method processes content on the server side, removing the need for direct communication between the user's browser and third-party servers.</p>
<p>To add an Embed to Your Website:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag Setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Tools Configuration**.
3. Click "add new tool" and activate the desired tools on your Cloudflare Zaraz dashboard.
4. Add a placeholder in your HTML, specifying the necessary attributes. For a generic embed, the snippet looks like this:
<pre tabindex="0"><code class="language-html">&lt;componentName-embedName attribute=&quot;value&quot;&gt;&lt;/componentName-embedName&gt;&#10;</code></pre>
<p>Replace <code>componentName</code>, <code>embedName</code> and <code>attribute=&quot;value&quot;</code> with the specific Managed Component requirements. Zaraz automatically detects placeholders and replaces them with the content in a secure and efficient way.</p>
<h2 id="examples">Examples</h2>
<h3 id="x-twitter-embed">X (Twitter) embed</h3>
<pre tabindex="0"><code class="language-html">&lt;twitter-post tweet-id=&quot;12345&quot;&gt;&lt;/twitter-post&gt;&#10;</code></pre>
<p>Replace <code>tweet-id</code> with the actual tweet ID for the content you wish to embed.</p>
<h3 id="instagram-embed">Instagram embed</h3>
<pre tabindex="0"><code class="language-html">&lt;instagram-post post-url=&quot;https://www.instagram.com/p/ABC/&quot; captions=&quot;true&quot;&gt;&lt;/instagram-post&gt;&#10;</code></pre>
<p>Replace <code>post-url</code> with the actual URL for the content you wish to embed. To include posts captions set captions attribute to <code>true</code>.</p>
