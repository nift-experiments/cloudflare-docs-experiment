---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/
  description: Submit Turnstile feedback reports for false positive challenges.
  full_title: Feedback reports · Cloudflare Turnstile docs
  head_html: <title>Feedback reports · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Submit Turnstile feedback reports for false positive challenges."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/index.md"><meta property="og:title" content="Feedback reports · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Submit Turnstile feedback reports for false positive challenges."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Turnstile"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/#page","headline":"Feedback reports \u00b7 Cloudflare Turnstile docs","description":"Submit Turnstile feedback reports for false positive challenges.","url":"https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /turnstile/troubleshooting/feedback-reports/
  schema: 1
---
<p>When Cloudflare detects that a challenge has failed or the user cannot be verified on a page with Turnstile, the user will encounter an <a href="/turnstile/concepts/widget/#error-states">error</a> on the widget and may be asked to send feedback on the issue that they have encountered by choosing one of the options listed.</p>
<p>When debugging or submitting a feedback report for an unresolved issue, you must provide the Ray ID (a request identifier displayed on the challenge page) or QR code associated with the challenge. These identifiers are essential for Cloudflare Support to trace the specific event.</p>
<p>To obtain these identifiers:</p>
<ol>
<li>Ray ID: Find the Ray ID displayed at the end of the Challenge Page. The RayID is collected by the feedback report.</li>
<li>QR Code: Click the success, failure, or spinner logo on the Turnstile widget four times. This action will reveal the unique QR code for that challenge instance.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14995.md")
</aside>
<p>Available options include:</p>
<ul>
<li>The widget always fails</li>
<li>The widget sometimes fails</li>
<li>The widget is too slow</li>
<li>The widget keeps looping</li>
<li>Other</li>
</ul>
<p>Users can provide additional data in the text field and then select <strong>Submit</strong>.</p>
