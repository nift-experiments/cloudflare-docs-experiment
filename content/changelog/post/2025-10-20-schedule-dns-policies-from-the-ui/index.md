---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/
  description: New updates and improvements at Cloudflare.
  full_title: Schedule DNS policies from the UI · Changelog
  head_html: <title>Schedule DNS policies from the UI · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Schedule DNS policies from the UI · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/#page","headline":"Schedule DNS policies from the UI \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 20, 2025</time><h2 id="post-title">Schedule DNS policies from the UI</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Admins can now create <a href="/cloudflare-one/traffic-policies/dns-policies/timed-policies/">scheduled DNS policies</a> directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.</p>
<ul>
<li><strong>Preset Schedules</strong>: Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.</li>
<li><strong>Custom Schedules</strong>: Define your own schedule with specific days and up to three non-overlapping time ranges per day.</li>
<li><strong>Timezone Control</strong>: Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.</li>
<li><strong>Combined with Duration</strong>: Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.</li>
</ul>
<p>You can see the flow in the demo GIF:</p>
<p><img src="/assets/upstream/images/gateway/gateway-dns-scheduled-policies-ui.gif" alt="Schedule DNS policies demo" /></p>
<p>This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.</p>
</div></article></div>
