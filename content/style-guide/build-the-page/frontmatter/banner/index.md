---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/
  description: How to display a banner at the top of the page and when to use it.
  full_title: Banner · Cloudflare Style Guide
  head_html: <title>Banner · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="How to display a banner at the top of the page and when to use it."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/index.md"><meta property="og:title" content="Banner · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How to display a banner at the top of the page and when to use it."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/#page","headline":"Banner \u00b7 Cloudflare Style Guide","description":"How to display a banner at the top of the page and when to use it.","url":"https://developers.cloudflare.com/style-guide/build-the-page/frontmatter/banner/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/frontmatter/banner/
  schema: 1
---
<p>One of the fields you can add to the <a href="/style-guide/build-the-page/frontmatter/">Frontmatter</a> is <code>banner</code>. It displays a prominent section at the top of the page and supports the use of HTML for links and formatting.</p>
<p>Only use it to alert about disruptive situations and take note to remove it when applicable.</p>
<h2 id="example">Example</h2>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Do &lt;strong&gt;not&lt;/strong&gt; use banners in the &lt;a href=&quot;/style-guide/build-the-page/frontmatter/&quot;&gt;Frontmatter&lt;/a&gt; unless a change will cause customer application to break.&#10;&#45;--&#10;</code></pre>
<h2 id="styles-types">Styles / Types</h2>
<h3 id="note">Note</h3>
<p>The note banner is used to alert about important information.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Ensure you read this!&#10;  type: note&#10;&#45;--&#10;</code></pre>
<h3 id="tip">Tip</h3>
<p>The tip banner is used to alert about important suggestions.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Consider this alternative!&#10;  type: tip&#10;&#45;--&#10;</code></pre>
<h3 id="caution">Caution</h3>
<p>The caution banner is used to warn readers of upcoming disruptive changes.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: This is deprecated and will break on &lt;strong&gt;1970-01-01&lt;/strong&gt;!&#10;  type: caution&#10;&#45;--&#10;</code></pre>
<h3 id="danger">Danger</h3>
<p>The danger banner is used to alert about errors.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: This has been removed!&#10;  type: danger&#10;&#45;--&#10;</code></pre>
<h3 id="default">Default</h3>
<p>The default banner is used in all other circumstances.</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;title: Banner&#10;description: How to display a banner at the top of the page and when to use it.&#10;banner:&#10;  content: Do &lt;strong&gt;not&lt;/strong&gt; use banners in the &lt;a href=&quot;/style-guide/build-the-page/frontmatter/&quot;&gt;Frontmatter&lt;/a&gt; unless a change will cause customer application to break.&#10;&#45;--&#10;</code></pre>
