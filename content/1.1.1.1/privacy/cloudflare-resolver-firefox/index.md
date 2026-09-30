---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/privacy/cloudflare-resolver-firefox/
  description: How 1.1.1.1 works as the trusted resolver for Firefox.
  full_title: Cloudflare Resolver for Firefox · Cloudflare 1.1.1.1 docs
  head_html: <title>Cloudflare Resolver for Firefox · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="How 1.1.1.1 works as the trusted resolver for Firefox."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/privacy/cloudflare-resolver-firefox/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/privacy/cloudflare-resolver-firefox/index.md"><meta property="og:title" content="Cloudflare Resolver for Firefox · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How 1.1.1.1 works as the trusted resolver for Firefox."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/privacy/cloudflare-resolver-firefox/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="Privacy"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/privacy/cloudflare-resolver-firefox/#page","headline":"Cloudflare Resolver for Firefox \u00b7 Cloudflare 1.1.1.1 docs","description":"How 1.1.1.1 works as the trusted resolver for Firefox.","url":"https://developers.cloudflare.com/1.1.1.1/privacy/cloudflare-resolver-firefox/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/privacy/cloudflare-resolver-firefox/
  schema: 1
---
<h2 id="frequently-asked-questions-about-the-cloudflare-resolver-for-firefox">Frequently asked questions about the Cloudflare resolver for Firefox</h2>
<h3 id="what-is-the-cloudflare-resolver-for-firefox">What is the Cloudflare resolver for Firefox?</h3>
<p>Every time you type a web address, such as <a href="http://www.mozilla.org">www.mozilla.org</a> or <a href="http://www.firefox.com">www.firefox.com</a>, into a web browser, the web browser sends a query to a DNS resolver. If DNS is like the card catalog of the Internet, then a DNS resolver is like a helpful librarian that knows how to use the information from that catalog to track down the exact location of a website. Whenever a resolver receives your query it looks up the IP address associated with the web address that you entered and relays that information to your web browser. “DNS resolution” as this process is referred to, is a crucial component of your Internet experience because without it your web browser would be unable to communicate with the servers that host your favorite websites, since communication requires knowing the IP addresses of those websites.</p>
<p>For most Internet users, the DNS resolver that they use is either the one that comes with the operating system running on their machines or the one that is set by their network provider. In some cases, these resolvers leave a lot to be desired because of their susceptibility to unwanted spying and other security threats.</p>
<p>To address this, Mozilla has partnered with Cloudflare to provide DNS resolution directly from within the Firefox browser using the Cloudflare resolver for Firefox. When this feature is active, Firefox sends DNS queries over a secure channel to the Cloudflare resolver for Firefox rather than to an unknown DNS resolver, significantly decreasing the odds of unwanted spying or man-in-the-middle attacks.</p>
<h3 id="what-information-does-the-cloudflare-resolver-for-firefox-collect">What information does the Cloudflare resolver for Firefox collect?</h3>
<p>Any data Cloudflare handles as a result of its resolver for Firefox is as a data processor acting pursuant to Mozilla's data processing instructions. The data Cloudflare collects and processes pursuant to its agreement with Mozilla is not covered by the <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare Privacy Policy</a>. As part of its agreement with Mozilla, Cloudflare has agreed to collect only a limited amount of data about the DNS requests sent to the Cloudflare resolver for Firefox via the Firefox browser. Cloudflare will collect only the following information from Firefox users:</p>
<ul>
<li>date</li>
<li>dateTime</li>
<li>srcAsNum</li>
<li>srcIPVersion</li>
<li>dstIPVersion</li>
<li>dstIPv6</li>
<li>dstIPv4</li>
<li>dstPort</li>
<li>protocol</li>
<li>queryName</li>
<li>queryType</li>
<li>queryClass</li>
<li>queryRd</li>
<li>queryDo</li>
<li>querySize</li>
<li>queryEdns</li>
<li>ednsVersion</li>
<li>ednsPayload</li>
<li>ednsNsid</li>
<li>responseType</li>
<li>responseCode</li>
<li>responseSize</li>
<li>responseCount</li>
<li>responseTimeMs</li>
<li>responseCached</li>
<li>responseMinTTL</li>
<li>answerData type</li>
<li>answerData</li>
<li>validationState</li>
<li>coloID (unique Cloudflare data center ID)</li>
<li>metalId (unique Cloudflare data center ID)</li>
</ul>
<p>All of the above information is stored in temporary logs and then permanently deleted within 24 hours of Cloudflare's receipt of such information. In addition, Cloudflare stores the following in permanent logs:</p>
<ul>
<li>Total number of requests processed by each Cloudflare data center.</li>
<li>Aggregate list of all domain names requested.</li>
<li>Samples of domain names queried along with the times of such queries.</li>
</ul>
<p>Information stored in permanent logs is anonymized and may be held indefinitely by Cloudflare for internal research and development purposes.</p>
<h3 id="what-is-the-cloudflare-promise">What is the Cloudflare promise?</h3>
<p>Cloudflare commits to using the information collected from the Cloudflare resolver for Firefox solely to improve the performance of the Cloudflare resolver for Firefox and to assist in debugging efforts if an issue arises. In addition to limiting collection and use of data, Cloudflare promises:</p>
<ul>
<li>
<p>Cloudflare will not retain or sell or transfer to any third party (except as may be required by law) any personal information, IP addresses, or other user identifiers from the DNS queries sent from the Firefox browser to the Cloudflare resolver for Firefox.</p>
</li>
<li>
<p>Cloudflare will not combine the data that it collects from such queries with any other Cloudflare or third-party data in any way that can be used to identify individual end users.</p>
</li>
<li>
<p>Cloudflare will not sell, license, sublicense, or grant any rights to your data to any other person or entity without Mozilla's explicit written permission.</p>
</li>
</ul>
<h3 id="what-about-government-requests-for-content-blocking">What about government requests for content blocking?</h3>
<p>Cloudflare does not block or filter content through the Cloudflare resolver for Firefox. As part of its agreement with Mozilla, Cloudflare provides only direct DNS resolution. If Cloudflare were to receive written requests from law enforcement and government agencies to block access to domains or content through the Cloudflare resolver for Firefox, Cloudflare would, in consultation with Mozilla, exhaust its legal remedies before complying with such a request. We also commit to documenting any government request to block access in our semi-annual transparency report, unless legally prohibited from doing so.</p>
