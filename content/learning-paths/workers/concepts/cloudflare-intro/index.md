---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/
  description: Learn about Cloudflare's network and products.
  full_title: Introduction to Cloudflare · Cloudflare Learning Paths
  head_html: <title>Introduction to Cloudflare · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about Cloudflare&#x27;s network and products."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/index.md"><meta property="og:title" content="Introduction to Cloudflare · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about Cloudflare&#x27;s network and products."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/#page","headline":"Introduction to Cloudflare \u00b7 Cloudflare Learning Paths","description":"Learn about Cloudflare's network and products.","url":"https://developers.cloudflare.com/learning-paths/workers/concepts/cloudflare-intro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/workers/concepts/cloudflare-intro/
  schema: 1
---
<p><a href="https://www.cloudflare.com/learning/what-is-cloudflare/">Cloudflare</a> is a global network of <a href="https://www.cloudflare.com/learning/cdn/glossary/edge-server/">servers</a>. It is one of the largest <a href="https://www.cloudflare.com/network/">networks</a> on the Internet.</p>
<p>Cloudflare's product offering is composed of <a href="https://www.cloudflare.com/zero-trust/">SASE and SSE services</a>, <a href="https://www.cloudflare.com/application-services/">application</a> and <a href="https://www.cloudflare.com/network-services/">infrastructure services</a>, and <a href="https://www.cloudflare.com/developer-platform/solutions/">Developer Platform</a>.</p>
<p>Cloudflare's products offer something to developers, private and public organizations, businesses, governments, and individual consumers.</p>
<h2 id="cloudflare-developer-platform">Cloudflare Developer Platform</h2>
<p>The <a href="https://www.cloudflare.com/developer-platform/products/">Cloudflare Developer Platform</a> includes <a href="/workers/">Cloudflare Workers</a>, which allows you to deploy serverless code instantly across the globe. You will learn more about <a href="/learning-paths/workers/devplat/">the Developer Platform in this module</a>.</p>
<h2 id="built-on-cloudflare">Built on Cloudflare</h2>
<p>If your application is built on Cloudflare, then Cloudflare would act as the origin server of your application.</p>
<p>An example tech stack for an application built on Cloudflare would look like:</p>
<ul>
<li><a href="/registrar/">Domain Registrar</a> to buy a new domain.</li>
<li><a href="/pages/">Cloudflare Pages</a> to configure and deploy a front-end site.</li>
<li><a href="/workers/">Cloudflare Workers</a> or <a href="/pages/functions/">Pages Functions</a> (which are Workers under the hood) to add dynamic functionality to your site.</li>
<li><a href="/workers/platform/storage-options/">Storage resources</a> to persist different types of data.</li>
<li><a href="https://www.cloudflare.com/application-services/products/#security-services">Application security (DDoS protection, WAF, and more)</a> to secure your site.</li>
<li><a href="https://www.cloudflare.com/application-services/products/#performance-services">Application performance (CDN, Load Balancing, and more)</a> to customize and enhance your site's performance.</li>
<li><a href="/use-cases/ai/">AI</a> to run machine learning models.</li>
</ul>
<p>And more depending on your use case.</p>
<h2 id="built-with-cloudflare">Built with Cloudflare</h2>
<p>When you add your application to Cloudflare, Cloudflare's global network of servers will sit in between requests to your application and your application's <a href="https://www.cloudflare.com/learning/cdn/glossary/origin-server/">origin server</a>.</p>
<p><img src="/assets/upstream/images/fundamentals/get-started/website-with-cloudflare.svg" alt="Cloudflare sits in between requests and your origin server." /></p>
<p>After you add your application to <a href="/fundamentals/concepts/how-cloudflare-works/">Cloudflare</a>, you can:</p>
<ul>
<li>Use Workers to augment the application by deploying code.</li>
<li>Add storage resources available on the Developer Platform.</li>
<li>Enhance your application's performance by speeding up content delivery and user experience (<a href="https://www.cloudflare.com/learning/cdn/what-is-a-cdn/">CDN</a>).</li>
<li>Protect your website from malicious activity (<a href="https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/">DDoS</a> by configuring the <a href="https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/">Web Application Firewall</a>).</li>
<li>Route traffic (<a href="/load-balancing/">Load balancing</a>, <a href="/waiting-room/">Waiting Room</a>).</li>
</ul>
<p>And more depending on your use case.</p>
<h2 id="summary">Summary</h2>
<p>By reading this page, you have:</p>
<ul>
<li>Learned the scale of Cloudflare's global network.</li>
<li>Explored the product offering to know what Cloudflare can offer for users like you.</li>
<li>Reviewed how you can build your applications with Cloudflare and Cloudflare Workers.</li>
</ul>
<p>In the next section, you will be introduced to the fundamentals of serverless computing, the concept behind Cloudflare Workers.</p>
