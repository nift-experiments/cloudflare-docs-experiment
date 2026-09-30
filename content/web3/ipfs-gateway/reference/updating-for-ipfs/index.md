---
cp9:
  canonical: https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/
  description: Host your website on IPFS and serve it through Cloudflare.
  full_title: Using IPFS with your website · Cloudflare Web3 docs
  head_html: <title>Using IPFS with your website · Cloudflare Web3 docs</title><meta name="generator" content="Nift"><meta name="description" content="Host your website on IPFS and serve it through Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/index.md"><meta property="og:title" content="Using IPFS with your website · Cloudflare Web3 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Host your website on IPFS and serve it through Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Web3"><meta name="algolia_product_filter" content="Web3"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Web3"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/#page","headline":"Using IPFS with your website \u00b7 Cloudflare Web3 docs","description":"Host your website on IPFS and serve it through Cloudflare.","url":"https://developers.cloudflare.com/web3/ipfs-gateway/reference/updating-for-ipfs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web3/ipfs-gateway/reference/updating-for-ipfs/
  schema: 1
---
<p>Though it is not required, it is strongly recommended that websites hosted on IPFS use only relative links, unless linking to a different domain. This is because data can be accessed in many different (but ultimately equivalent) ways:</p>
<ul>
<li>From your custom domain: <code>https://ipfs.tech/index.html</code></li>
<li>From a gateway: <code>https://cloudflare-ipfs.com/ipns/ipfs.tech/index.html</code></li>
<li>By immutable hash: <code>https://cloudflare-ipfs.com/ipfs/QmNksJqvwHzNtAtYZVqFZFfdCVciY4ojTU2oFZQSFG9U7B/index.html</code></li>
</ul>
<p>Using only relative links within a web application supports all of these at once, and gives the most flexibility to the user. The exact method for switching to relative links, if you do not use them already, depends on the framework you use.</p>
<h2 id="angular-react-vue">Angular, React, Vue</h2>
<p>These popular JavaScript frameworks are covered in a <a href="https://medium.com/pinata/how-to-easily-host-a-website-on-ipfs-9d842b5d6a01">blog post</a> from <a href="https://pinata.cloud/">Pinata</a>. They are fixed with minor config changes.</p>
<h2 id="gatsby">Gatsby</h2>
<p>Gatsby is a JavaScript framework based on React. There is a <a href="https://www.gatsbyjs.org/packages/gatsby-plugin-ipfs/">plugin</a> for it that ensures links are relative.</p>
<h2 id="jekyll">Jekyll</h2>
<p>Add a file <code>_includes/base.html</code> with the contents:</p>
<pre tabindex="0"><code>{% assign base = &#x27;&#x27; %}&#10;{% assign depth = page.url | split: &#x27;/&#x27; | size | minus: 1 %}&#10;{% if    depth &lt;= 1 %}{% assign base = &#x27;.&#x27; %}&#10;{% elsif depth == 2 %}{% assign base = &#x27;..&#x27; %}&#10;{% elsif depth == 3 %}{% assign base = &#x27;../..&#x27; %}&#10;{% elsif depth == 4 %}{% assign base = &#x27;../../..&#x27; %}{% endif %}&#10;</code></pre>
<p>This snippet computes the relative path back to the root of the website from the current page. Update any pages that need to link to the root by adding this at the top:</p>
<pre tabindex="0"><code>{%- include base.html -%}&#10;</code></pre>
<p>This snippet also prefixing any links with <code>{{base}}</code>. So for example, we would change
<code>href=&quot;/css/main.css&quot;</code> to be <code>href=&quot;{{base}}/css/main.css&quot;</code></p>
<h2 id="generic">Generic</h2>
<p>For other frameworks, or if a framework was not used, there's a script called <a href="https://github.com/tmcw/make-relative">make-relative</a> that will parse the HTML of a website and automatically rewrite links and images to be relative.</p>
