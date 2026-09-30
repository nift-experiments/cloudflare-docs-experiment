---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/support/
  description: '2026-08-11'
  full_title: support changelog | Cloudflare Docs
  head_html: <title>support changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-11"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/support/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="support changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-11"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/support/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/support/#page","headline":"support changelog | Cloudflare Docs","description":"2026-08-11","url":"https://developers.cloudflare.com/changelog/product/support/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/support/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-cloudflare-status-page"><a href="/changelog/post/2026-08-11-new-status-page/">New Cloudflare Status page</a></h2>
<p><em>2026-08-11</em></p>
<p>The Cloudflare Status page at <a href="https://www.cloudflarestatus.com/">www.cloudflarestatus.com</a> has been rebuilt. It is available at the same address, and every previously documented <a href="https://www.cloudflarestatus.com/api">Status API</a> endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.</p>
<h4 id="2026-08-11-new-status-page-notifications-that-fire-even-when-cloudflare-is-down">Notifications that fire even when Cloudflare is down</h4>
<p>The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.</p>
<p>The <strong>Maintenance Notification</strong> and <strong>Incident Alerts</strong> in <a href="/notifications/">Cloudflare Notifications</a> remain supported, and deliver to the destinations already configured on your account.</p>
<h4 id="2026-08-11-new-status-page-markdown-for-ai-agents">Markdown for AI agents</h4>
<p>Every page on the status page returns Markdown when requested with an <code>Accept: text/markdown</code> header, so agents can read the current status without parsing HTML:</p>
<pre tabindex="0"><code class="language-sh">curl -H &quot;Accept: text/markdown&quot; https://www.cloudflarestatus.com/locations&#10;</code></pre>
<h4 id="2026-08-11-new-status-page-separate-feeds-for-incidents-and-maintenance">Separate feeds for incidents and maintenance</h4>
<p>Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:</p>
<pre tabindex="0"><code class="language-txt">https://www.cloudflarestatus.com/api/v3/incidents.rss&#10;https://www.cloudflarestatus.com/api/v3/incidents.atom&#10;https://www.cloudflarestatus.com/api/v3/maintenance.rss&#10;https://www.cloudflarestatus.com/api/v3/maintenance.atom&#10;</code></pre>
<p>For more information, refer to <a href="/support/cloudflare-status/">Cloudflare Status</a>.</p>


<h2 id="direct-access-to-support-from-the-dashboard"><a href="/changelog/post/2026-04-28-direct-support-navigation/">Direct access to Support from the dashboard</a></h2>
<p><em>2026-04-28</em></p>
<h4 id="2026-04-28-direct-support-navigation-direct-access-to-support-from-the-dashboard">Direct access to Support from the dashboard</h4>
<p>The <strong>Support</strong> button in the dashboard global navigation header now takes you directly to the <a href="https://support.cloudflare.com">Cloudflare Support Portal</a>, eliminating the previous dropdown menu.</p>
<p>This change ensures that when you need help, you spend less time navigating the UI and more time getting the answers you need.</p>
<h4 id="2026-04-28-direct-support-navigation-what-changed">What changed?</h4>
<ul>
<li><strong>Previous behavior</strong>: Selecting <strong>? Support</strong> opened a dropdown menu with various links (Help Center, Cloudflare Community, etc.).</li>
<li><strong>New behavior</strong>: Selecting <strong>Support</strong> immediately redirects your current tab to the Support Portal.</li>
</ul>
<p>To learn more about the resources available to you, refer to the <a href="https://developers.cloudflare.com/support/contacting-cloudflare-support/">Cloudflare Support documentation</a>.</p>


<h2 id="redesigned-support-portal-for-faster-personalized-help"><a href="/changelog/post/2026-04-06-redesigned-support-portal/">Redesigned Support Portal for faster, personalized help</a></h2>
<p><em>2026-04-07</em></p>
<h4 id="2026-04-06-redesigned-support-portal-redesigned-get-help-portal-for-faster-personalized-help">Redesigned &quot;Get Help&quot; Portal for faster, personalized help</h4>
<p>Cloudflare has officially launched a redesigned &quot;Get Help&quot; Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.</p>
<p>The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as &quot;Ask AI&quot;, &quot;Chat with a human&quot;, or &quot;Community&quot; — without the manual triage.</p>
<h4 id="2026-04-06-redesigned-support-portal-what-s-new">What's New</h4>
<ul>
<li><strong>One Page, Clear Choices</strong>: No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.</li>
<li><strong>A Radically Simpler Support Form</strong>: We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.</li>
<li><strong>AI-Driven Triage</strong>: Using <a href="https://developers.cloudflare.com/workers-ai/">Cloudflare Workers AI</a> and <a href="https://developers.cloudflare.com/vectorize/">Vectorize</a>, the portal now automatically generates case subjects and predicts product categories.</li>
</ul>
<h4 id="2026-04-06-redesigned-support-portal-moving-complexity-to-the-backend">Moving complexity to the backend</h4>
<p>Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.</p>
<p>By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.</p>
<p>To learn more, refer to the <a href="/support/contacting-cloudflare-support/">Support documentation</a> or select <strong>Get Help</strong> directly in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a>.</p>



