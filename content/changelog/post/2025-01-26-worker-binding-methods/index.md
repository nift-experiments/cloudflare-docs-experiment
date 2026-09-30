---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/
  description: New updates and improvements at Cloudflare.
  full_title: AI Gateway Introduces New Worker Binding Methods · Changelog
  head_html: <title>AI Gateway Introduces New Worker Binding Methods · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI Gateway Introduces New Worker Binding Methods · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/#page","headline":"AI Gateway Introduces New Worker Binding Methods \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-01-26-worker-binding-methods/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 30, 2025</time><h2 id="post-title">AI Gateway Introduces New Worker Binding Methods</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>We have released new <a href="/ai-gateway/usage/worker-binding-methods/">Workers bindings API methods</a>, allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.</p>
<p>To add an AI binding to your Worker, include the following in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<p><img src="/assets/upstream/images/ai-gateway/add-binding.png" alt="Add an AI binding to your Worker." /></p>
<p>With the new AI Gateway binding methods, you can now:</p>
<ul>
<li>Send feedback and update metadata with <code>patchLog</code>.</li>
<li>Retrieve detailed log information using <code>getLog</code>.</li>
<li>Execute <a href="/ai-gateway/usage/universal/">universal requests</a> to any AI Gateway provider with <code>run</code>.</li>
</ul>
<p>For example, to send feedback and update metadata using <code>patchLog</code>:</p>
<p><img src="/assets/upstream/images/ai-gateway/send-feedback.png" alt="Send feedback and update metadata using patchLog:" /></p>
</div></article></div>
