---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/logpush/
  description: '2026-04-14'
  full_title: logpush changelog | Cloudflare Docs
  head_html: <title>logpush changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-14"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/logpush/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="logpush changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-14"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/logpush/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/logpush/#page","headline":"logpush changelog | Cloudflare Docs","description":"2026-04-14","url":"https://developers.cloudflare.com/changelog/product/logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/logpush/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="logpush-to-bigquery-cloudflare-dashboard-support"><a href="/changelog/post/2026-04-14-bigquery-dashboard-support/">Logpush to BigQuery — Cloudflare dashboard support</a></h2>
<p><em>2026-04-14</em></p>
<p>You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.</p>
<p>Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the <strong>Logpush</strong> page in the Cloudflare dashboard by selecting <strong>Google BigQuery</strong> as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Enable Logpush to Google BigQuery</a>.</p>


<h2 id="logpush-more-granular-timestamps"><a href="/changelog/post/2026-03-25-logpush-granular-timestamps/">Logpush — More granular timestamps</a></h2>
<p><em>2026-03-25</em></p>
<p>Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>To use the new formats, set <code>timestamp_format</code> in your Logpush job's <code>output_options</code>:</p>
<ul>
<li><code>rfc3339ms</code> — <code>2024-02-17T23:52:01.123Z</code></li>
<li><code>rfc3339ns</code> — <code>2024-02-17T23:52:01.123456789Z</code></li>
</ul>
<p>Default timestamp formats apply unless explicitly set. The dashboard defaults to <code>rfc3339</code> and the API defaults to <code>unixnano</code>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/log-output-options/">Log output options</a> documentation.</p>



