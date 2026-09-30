---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/
  description: New updates and improvements at Cloudflare.
  full_title: Exchange user risk scores with Okta · Changelog
  head_html: <title>Exchange user risk scores with Okta · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Exchange user risk scores with Okta · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/#page","headline":"Exchange user risk scores with Okta \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-06-17-okta-risk-exchange/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-06-17-okta-risk-exchange/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 17, 2024</time><h2 id="post-title">Exchange user risk scores with Okta</h2>
<div class="changelog-badges"><span>risk-score</span></div><div class="changelog-body"><p>Beyond the controls in <a href="/cloudflare-one/">Zero Trust</a>, you can now <a href="/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta">exchange user risk scores</a> with Okta to inform SSO-level policies.</p>
<p>First, configure Cloudflare One to send user risk scores to Okta.</p>
<ol>
<li>Set up the <a href="/cloudflare-one/integrations/identity-providers/okta/">Okta SSO integration</a>.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>In <strong>Your identity providers</strong>, locate your Okta integration and select <strong>Edit</strong>.</li>
<li>Turn on <strong>Send risk score to Okta</strong>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Upon saving, Cloudflare One will display the well-known URL for your organization. Copy the value.</li>
</ol>
<p>Next, configure Okta to receive your risk scores.</p>
<ol>
<li>On your Okta admin dashboard, go to <strong>Security</strong> &gt; <strong>Device Integrations</strong>.</li>
<li>Go to <strong>Receive shared signals</strong>, then select <strong>Create stream</strong>.</li>
<li>Name your integration. In <strong>Set up integration with</strong>, choose <em>Well-known URL</em>.</li>
<li>In <strong>Well-known URL</strong>, enter the well-known URL value provided by Cloudflare One.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
</div></article></div>
