---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/
  description: Cloudflare has bot management capabilities to help identify and mitigate automated traffic to protect domains from bad bots.
  full_title: Bot management · Cloudflare Reference Architecture docs
  head_html: <title>Bot management · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare has bot management capabilities to help identify and mitigate automated traffic to protect domains from bad bots."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/index.md"><meta property="og:title" content="Bot management · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare has bot management capabilities to help identify and mitigate automated traffic to protect domains from bad bots."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/#page","headline":"Bot management \u00b7 Cloudflare Reference Architecture docs","description":"Cloudflare has bot management capabilities to help identify and mitigate automated traffic to protect domains from bad bots.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/bots/bot-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/bots/bot-management/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Cloudflare has bot management capabilities to help identify and mitigate automated traffic to protect domains from bad bots. <a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> and <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> are options available on Free and Pro/Business accounts respectively. They offer a subset of features and capabilities available for Enterprise accounts. This reference architecture diagram focuses on <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> available for Enterprise customers.</p>
<p>With <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> customers have the maximum protection, features, and capability. A <a href="https://developers.cloudflare.com/bots/concepts/bot-score/">bot score</a> is exposed for every request. Cloudflare applies a layered detection approach to Bot Management with several detection engines that cumulatively can impact the bot score. A bot score is a score from 1 to 99 that indicates the likelihood that the request came from a bot. Scores below 30 are commonly associated with bot traffic and customers can then take action on this score with <a href="https://developers.cloudflare.com/waf/custom-rules/">WAF custom rules</a> or <a href="https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties">Workers</a>. Additionally, customers can view this score along with other bot specifics like bot score source, bot detection IDs, and bot detection tags in the Bots, Security Analytics, and Events dashboards; these fields can also be seen in more detailed logs in Log Explorer or, with Log Push, logs with these respective fields can be exported to 3rd party SIEMs/Analytics platforms.</p>
<h2 id="definitions">Definitions</h2>
<ul>
<li><strong>Bot Score:</strong> A <a href="/bots/concepts/bot-tags/">bot score</a> is a score from 1 to 99 that indicates how likely that request came from a bot. A score of 1 means Cloudflare is certain the request was automated.</li>
<li><strong>Bot Score Source:</strong> Bot Score Source is the detection engine used for the bot score.</li>
<li><strong>Bot Detection ID:</strong> <a href="/bots/additional-configurations/detection-ids/">Detection IDs</a> are static rules used to detect predictable bot behavior with no overlap with human traffic. Detection IDs refer to the precise <a href="/bots/concepts/bot-detection-engines/">detection</a> used to identify a bot, which could be from heuristics, verified bot detections, or anomaly detections.</li>
<li><strong>Bot Tag:</strong> <a href="/bots/concepts/bot-tags/">Bot tags</a> provide more detail about why Cloudflare assigned a <a href="/bots/concepts/bot-score/">bot score</a> to a request.</li>
<li><strong>Verified Bots:</strong> Cloudflare maintains <a href="https://radar.cloudflare.com/traffic/verified-bots">a list of &quot;Verified&quot; good bots</a> which can be used in policies to insure good bots such as those associated with a search engine are not blocked.</li>
<li><strong>AI Bots:</strong> <a href="/bots/concepts/bot/#ai-bots">If the feature is enabled</a>, Cloudflare will detect and block verified AI bots that respect <code>robots.txt</code> and crawl rate, and do not hide their behavior from your website. The rule has also been expanded to include more signatures of AI bots that do not follow the rules.</li>
</ul>
<h2 id="cloudflare-bot-management-detection-engines">Cloudflare Bot Management Detection Engines</h2>
<ul>
<li><strong>Heuristics:</strong> Cloudflare conducts a number of heuristic checks to identify automated traffic, and requests are matched against a growing database of malicious fingerprints. The <a href="/bots/concepts/bot-score/#heuristics">Heuristics engine</a> gives automated requests a score of 1 for high-confidence detections, or a score of 29 for detections where confidence is still being assessed.</li>
<li><strong>Machine Learning (ML):</strong> The <a href="/bots/concepts/bot-score/#machine-learning">ML engine</a> accounts for the majority of all detections, human and bot. The ML model leverages Cloudflare's global network, which proxies billions of requests daily, to identify both automated and human traffic. The ML engine produces scores 2 through 99.</li>
<li><strong>Anomaly Detection (AD):</strong> The <a href="/bots/concepts/bot-score/#anomaly-detection">AD engine</a> is an optional detection engine that uses a form of unsupervised learning. Cloudflare records a baseline of a domain's traffic and uses the baseline to intelligently detect outlier requests. Cloudflare is deprecating Anomaly Detection and is not onboarding new customers onto this engine. Future behavioral detections will cover the same detection areas.</li>
<li><strong>JavaScript Detections (JSD)</strong>: The <a href="/bots/concepts/bot-score/#javascript-detections">JSD engine</a> identifies headless browsers and other malicious fingerprints. This engine performs a lightweight, invisible JavaScript injection on the client side of any request. The JSD engine either blocks, challenges, or passes requests to other engines. JSD is enabled by default but is completely optional.</li>
</ul>
<h2 id="bot-dashboards-analytics-and-logs">Bot Dashboards, Analytics, and Logs</h2>
<p>Cloudflare bot score and bot traffic analysis is available in several locations.</p>
<ul>
<li>
<p><strong>Bots dashboard:</strong>
Customers can easily see bot activity up to 30 days back and filter on bot score and other bot, traffic, and request filters. The <a href="/bots/concepts/feedback-loop/">bot feedback loop</a> allows customers to report back to Cloudflare any false positives or false negatives for further investigation.</p>
</li>
<li>
<p><strong>Security Analytics:</strong>
Security Analytics brings together all of Cloudflare's detection capabilities in one dashboard and provides a broad view of all traffic across the site. The Bots Likelihood graph and widget provide visibility and allow customers to easily view and filter based on bot score and respective categorization of Automated, Likely Automated, Human, and Likely Human.</p>
</li>
<li>
<p><strong>Events:</strong>
Events displays all events the WAF took action on. Events and logs can easily be filtered by bot score and other bot, traffic, or request criteria.</p>
</li>
<li>
<p><strong>Log Explorer:</strong>
Customers can use Log Explorer to pull additional detailed log data. Logs can easily be filtered by bot score and other bot, traffic, or request criteria.</p>
</li>
<li>
<p><strong>Log Push:</strong>
Customers can also export logs to a third party SIEM or Analytics platform. Bot score, bot score source, bot detection IDs, and bot detection tags can all be exported as part of the logs.</p>
<h2 id="bot-management-traffic-flow">Bot Management Traffic Flow</h2>
</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/bot-management/bot-management-ra-diagram.svg" alt="Figure 1: How Cloudflare identifies, scores and processes traffic from bots." title="Figure 1: How Cloudflare identifies, scores and processes traffic from bots." /></p>
<ol>
<li>Client request is sent to the closest Cloudflare Data Center via anycast ensuring low latency.</li>
<li>Cloudflare applies a layered approach for bot detection; each detection mechanism impacts the bot score assigned by Cloudflare to every request. Every request is assigned a bot score between 1-99 inclusive.</li>
<li>Once the client request has been processed by all of Cloudflare's detection engines and assigned a bot score, defined security policies will be executed, some of which may also be leveraging bot score. Various actions can be taken based on the assigned bot score including block, allow, rate limit, and one of the challenge actions.</li>
<li>Cloudflare provides analytics and insights into traffic and requests traversing the Cloudflare network. Customers can use the Bots, Security Analytics, Events, and Log Explorer dashboards to understand the overall traffic and bots activity across their site. Customers can also export logs to third party SIEM and Analytics Platforms.</li>
</ol>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="https://www.cloudflare.com/application-services/products/bot-management/">Cloudflare Bot Management Product Page</a></li>
<li><a href="https://blog.cloudflare.com/tag/bot-management/">Cloudflare Blog - Bot Management</a></li>
<li><a href="/bots/">Bots documentation</a></li>
<li><a href="https://youtu.be/6EnekTohO7I?si=tk8FUB0xtk1PxsJV">Video: Cloudflare Bot Management and Turnstile with Demo</a></li>
</ul>
