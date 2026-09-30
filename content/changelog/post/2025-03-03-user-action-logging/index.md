---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/
  description: New updates and improvements at Cloudflare.
  full_title: Gain visibility into user actions in Zero Trust Browser Isolation sessions · Changelog
  head_html: <title>Gain visibility into user actions in Zero Trust Browser Isolation sessions · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Gain visibility into user actions in Zero Trust Browser Isolation sessions · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/#page","headline":"Gain visibility into user actions in Zero Trust Browser Isolation sessions \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-03-03-user-action-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-03-03-user-action-logging/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 4, 2025</time><h2 id="post-title">Gain visibility into user actions in Zero Trust Browser Isolation sessions</h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>We're excited to announce that new logging capabilities for <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> through <a href="/logs/logpush/logpush-job/datasets/account/">Logpush</a> are available in Beta starting today!</p>
<p>With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;AccountID&quot;: &quot;$ACCOUNT_ID&quot;,&#10;	&quot;Decision&quot;: &quot;block&quot;,&#10;	&quot;DomainName&quot;: &quot;www.example.com&quot;,&#10;	&quot;Timestamp&quot;: &quot;2025-02-27T23:15:06Z&quot;,&#10;	&quot;Type&quot;: &quot;copy&quot;,&#10;	&quot;UserID&quot;: &quot;$USER_ID&quot;&#10;}&#10;</code></pre>
<p>User Actions available:</p>
<ul>
<li><strong>Copy &amp; Paste</strong></li>
<li><strong>Downloads &amp; Uploads</strong></li>
<li><strong>Printing</strong></li>
</ul>
<p>Learn more about how to get started with Logpush in our <a href="/logs/logpush/">documentation</a>.</p>
</div></article></div>
