---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/
  description: New updates and improvements at Cloudflare.
  full_title: Get notified when your Workers builds succeed or fail · Changelog
  head_html: <title>Get notified when your Workers builds succeed or fail · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Get notified when your Workers builds succeed or fail · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/#page","headline":"Get notified when your Workers builds succeed or fail \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-11-builds-event-subscriptions/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 9, 2026</time><h2 id="post-title">Get notified when your Workers builds succeed or fail</h2>
<div class="changelog-badges"><span>workers</span><span>queues</span></div><div class="changelog-body"><p>You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using <a href="/queues/event-subscriptions/">Event Subscriptions</a>.</p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> publishes events to a <a href="/queues/">Queue</a> that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.</p>
<p>You can deploy <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template">this Worker</a> to your own Cloudflare account to send build notifications to Slack:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The template includes:</p>
<ul>
<li>Build status with Preview/Live URLs for successful deployments</li>
<li>Inline error messages for failed builds</li>
<li>Branch, commit hash, and author name</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/builds-notifications-slack.png" alt="Slack notifications showing build events" /></p>
<p>For setup instructions, refer to the <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme">template README</a> or the <a href="/queues/event-subscriptions/manage-event-subscriptions/">Event Subscriptions documentation</a>.</p>
</div></article></div>
