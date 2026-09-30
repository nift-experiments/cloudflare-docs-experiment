---
cp9:
  canonical: https://developers.cloudflare.com/speed/observatory/faq/
  description: Find answers to common questions about Cloudflare Observatory.
  full_title: FAQ · Cloudflare Speed docs
  head_html: <title>FAQ · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Find answers to common questions about Cloudflare Observatory."><link rel="canonical" href="https://developers.cloudflare.com/speed/observatory/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/observatory/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Find answers to common questions about Cloudflare Observatory."><meta property="og:url" content="https://developers.cloudflare.com/speed/observatory/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/observatory/faq/#page","headline":"FAQ \u00b7 Cloudflare Speed docs","description":"Find answers to common questions about Cloudflare Observatory.","url":"https://developers.cloudflare.com/speed/observatory/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/observatory/faq/
  schema: 1
---
<p>Below you will find answers to our most commonly asked questions. If you cannot find the answer you are looking for, refer to the <a href="https://community.cloudflare.com/c/website-application-performance/88">community page</a> to explore more resources.</p>
<h2 id="how-long-does-it-take-for-a-test-to-load">How long does it take for a test to load?</h2>
<p>It can vary from about 25 seconds to over a minute. If you leave your speed tab open, your test is still going to run. You can leave and return and still see your test results.</p>
<h2 id="are-query-parameters-or-anchors-supported-in-tested-urls">Are query parameters or anchors supported in tested URLs?</h2>
<p>No. At the moment, any query parameter or anchor appended to the tested URL are dropped.</p>
<p>For example, using the <code>https://example.com/blog/?utm_medium=social#title</code> URL, the Observatory will discard the <code>?utm_medium=social</code> query parameter as well as the <code>#title</code> anchor. The tested URL will actually be <code>https://example.com/blog/</code>.</p>
<h2 id="i-get-a-403-response-when-rerunning-the-website-analysis">I get a <code>403</code> response when rerunning the website analysis?</h2>
<p>Check your WAF custom rules to make sure that you are not blocking traffic from Observatory to request your site.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13904.md")
</aside>
<h2 id="why-might-users-not-see-any-real-user-monitoring-rum-data-on-the-map-in-observatory">Why might users not see any Real User Monitoring (RUM) data on the map in Observatory?</h2>
<p>There are several reasons why users might not see any Real User Monitoring (RUM) data on the map in Observatory:</p>
<ul>
<li>
<p>Time Required for RUM Data Population: Populating the RUM database takes some time. It means that newly enabled RUM might not have immediate data available, and users may need to wait for some time before RUM data starts appearing on the map.</p>
</li>
<li>
<p>Progressive Sampling: RUM data is progressively sampled, which means that not all requests are captured. Some requests may pass through the sampling period, resulting in incomplete or missing data points on the map.</p>
</li>
<li>
<p>Adblockers Impact on RUM Data: RUM data collection relies on third-party JavaScript executing on the real-user browser. However, adblockers or similar browser extensions can block this script, preventing the collection of RUM data, and thereby affecting the completeness of the analytics presented on the map.</p>
</li>
<li>
<p>The RUM feature needs to be enabled and configured in your environment. If it has not been turned on, or if configuration is incomplete, RUM data may not appear.</p>
</li>
</ul>
<h2 id="what-are-the-potential-reasons-for-discrepancies-between-rum-analytics-and-traffic-analytics-in-observatory">What are the potential reasons for discrepancies between RUM analytics and traffic analytics in Observatory?</h2>
<p>Differences between Real User Monitoring (RUM) analytics and traffic analytics in Observatory can occur due to the following reasons:</p>
<ul>
<li>
<p>Adblockers Impact on RUM Data: Similar to the previous point, RUM data collection can be thwarted by adblockers, leading to missed data. Since traffic analytics typically rely on server-side data collection, they may not be as affected by adblockers as RUM.</p>
</li>
<li>
<p>Progressive Sampling in RUM: RUM data is collected through progressive sampling, which means that not all user requests are captured. This sampling method could result in slight variations in analytics when compared to traditional traffic analytics that record every server request.</p>
</li>
</ul>
<h2 id="how-do-i-disable-real-user-monitoring-rum-if-it-has-been-enabled-from-the-observatory-test-result-page">How do I disable Real User Monitoring (RUM) if it has been enabled from the Observatory test result page?</h2>
<p>Enabling RUM creates a Web Analytics configuration entry for the hostname at the account level.</p>
<p>If you wish to disable RUM, follow these steps:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Manage Site</strong> for the hostname for which you wish to disable RUM.</li>
<li>Select <strong>Delete</strong>.</li>
</ol>
