---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/
  description: Reference for Pay Per Crawl error response codes.
  full_title: Error codes · Cloudflare AI Crawl Control docs
  head_html: <title>Error codes · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for Pay Per Crawl error response codes."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/index.md"><meta property="og:title" content="Error codes · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for Pay Per Crawl error response codes."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/#page","headline":"Error codes \u00b7 Cloudflare AI Crawl Control docs","description":"Reference for Pay Per Crawl error response codes.","url":"https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/error-codes/
  schema: 1
---
<p>Pay per crawl error responses include a <code>crawler-error</code> header with a specific error code. The following table provides a complete reference of all possible error codes:</p>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>HTTP Status</th>
<th>What to do</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CrawlerForbidden</code></td>
<td>403</td>
<td>The site owner has blocked your crawler. You cannot access this content.</td>
</tr>
<tr>
<td><code>StrongAuthRequired</code></td>
<td>400</td>
<td>Include valid Web Bot Auth headers with strong authentication in your request.</td>
</tr>
<tr>
<td><code>InvalidSignature</code></td>
<td>400</td>
<td>Include both <code>signature-input</code> and <code>signature</code> headers in your request. Refer to <a href="/bots/reference/bot-verification/web-bot-auth/">Web Bot Auth documentation</a>.</td>
</tr>
<tr>
<td><code>InvalidCrawlerPriceValue</code></td>
<td>400</td>
<td>Check that your <code>crawler-exact-price</code> or <code>crawler-max-price</code> header value is properly formatted (for example, <code>USD 0.01</code>).</td>
</tr>
<tr>
<td><code>MissingCrawlerPrice</code></td>
<td>402</td>
<td>Include either <code>crawler-exact-price</code> or <code>crawler-max-price</code> header in your request.</td>
</tr>
<tr>
<td><code>PaymentFailed</code></td>
<td>403</td>
<td>Verify your payment processing is configured correctly in Pay Per Crawl settings. Contact Cloudflare support if the issue persists.</td>
</tr>
<tr>
<td><code>InvalidCrawlerExactPrice</code></td>
<td>402</td>
<td>Update your <code>crawler-exact-price</code> to match the <code>crawler-price</code> value from the response header.</td>
</tr>
<tr>
<td><code>InvalidCrawlerMaxPrice</code></td>
<td>402</td>
<td>Increase your <code>crawler-max-price</code> to meet or exceed the <code>crawler-price</code> value from the response header.</td>
</tr>
<tr>
<td><code>ConflictingPriceHeaders</code></td>
<td>400</td>
<td>Use only one price header per request. Remove either <code>crawler-max-price</code> or <code>crawler-exact-price</code>.</td>
</tr>
<tr>
<td><code>InvalidContentPrice</code></td>
<td>502</td>
<td>The origin returned an invalid price. This is a site owner configuration issue. Try again later or contact the site owner.</td>
</tr>
<tr>
<td><code>InternalError</code></td>
<td>500</td>
<td>A server error occurred. Retry your request with exponential backoff.</td>
</tr>
</tbody>
</table>
