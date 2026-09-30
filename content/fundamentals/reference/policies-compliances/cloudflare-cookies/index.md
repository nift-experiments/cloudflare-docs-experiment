---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/
  description: Review the cookies Cloudflare sets for load balancing, bot management, challenges, and other product features.
  full_title: Cloudflare Cookies · Cloudflare Fundamentals docs
  head_html: <title>Cloudflare Cookies · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Review the cookies Cloudflare sets for load balancing, bot management, challenges, and other product features."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/index.md"><meta property="og:title" content="Cloudflare Cookies · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review the cookies Cloudflare sets for load balancing, bot management, challenges, and other product features."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/#page","headline":"Cloudflare Cookies \u00b7 Cloudflare Fundamentals docs","description":"Review the cookies Cloudflare sets for load balancing, bot management, challenges, and other product features.","url":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/policies-compliances/cloudflare-cookies/
  schema: 1
---
<p>Cloudflare uses various cookies to maximize network resources, manage traffic, and protect our customers’ sites from malicious traffic.</p>
<h2 id="understanding-the-cloudflare-cookies">Understanding the Cloudflare Cookies</h2>
<p>As defined in our <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a>, all the cookies listed below are strictly necessary to provide the services requested by our customers, unless otherwise stated.</p>
<p>As mentioned in our Privacy Policy, Cloudflare encourages our customers to disclose the use of these cookies to their end users. In some jurisdictions, customers may be required by law to disclose these cookies to their end users.</p>
<p>By default, cookie data may be processed in Cloudflare's data center in the United States and is subject to the cross-border data transfer section 7 of the Cloudflare <a href="https://www.cloudflare.com/privacypolicy/">Privacy Policy</a>. Customers who use the <a href="/data-localization/">Data Localization Suite</a> can control where cookie data is processed (with <a href="/data-localization/regional-services/">Regional Services</a>) and logged (using the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a>).</p>
<h3 id="cflb-cookie-for-cloudflare-load-balancer-session-affinity">__cflb cookie for Cloudflare Load Balancer session affinity</h3>
<p>When enabling session affinity with <a href="/load-balancing/understand-basics/session-affinity/">Cloudflare Load Balancer</a>, Cloudflare sets a <code>__cflb</code> cookie with a unique value on the first response to the requesting client. Cloudflare routes future requests to the same origin, optimizing network resource usage. In the event of a failover, Cloudflare sets a new <code>__cflb</code> cookie to direct future requests to the failover pool.</p>
<p>The <code>__cflb</code> cookie allows Cloudflare to return an end user to the same customer origin for a specific period of time configured by the customer. This allows the end user to have a seamless experience (for example, this cookie is used for keeping an end user’s items in a shopping cart while they continue to navigate around the website). This cookie is a session cookie that lasts from several seconds up to 24 hours.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9012.md")
</aside>
<h3 id="cf-bm-cookie-for-cloudflare-bot-products">__cf_bm cookie for Cloudflare bot products</h3>
<p>Cloudflare's <a href="/bots/">bot products</a> identify and mitigate automated traffic to protect your site from bad bots. Cloudflare places the <code>__cf_bm</code> cookie on end-user devices that access customer sites protected by Bot Management or Bot Fight Mode. The <code>__cf_bm</code> cookie is necessary for these bot solutions to function properly.</p>
<p>This cookie expires after 30 minutes of continuous inactivity by the end user. The cookie contains information related to the calculation of Cloudflare's proprietary bot score and, when Anomaly Detection is enabled on Bot Management, a session identifier. The information in the cookie (other than time-related information) is encrypted and can only be decrypted by Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9011.md")
</aside>
<p>A separate <code>__cf_bm</code> cookie is generated for each site that an end user visits, as Cloudflare does not track users from site to site or from session to session. The <code>__cf_bm</code> cookie is generated independently by Cloudflare, and does not correspond to any user ID or other identifiers in a customer's web application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9010.md")
</aside>
<p>You can disable the <code>__cf_bm</code> cookie using the <code>bm_cookie_enabled</code> field <a href="/api/resources/bot_management/methods/update/">via the API</a>.</p>
<h3 id="cfseq-cookie-for-cloudflare-bot-products">__cfseq cookie for Cloudflare bot products</h3>
<p><a href="/bots/additional-configurations/sequence-rules/">Sequence rules</a> uses cookies to track the order of requests a user has made and the time between requests and makes them available via <a href="/rules/">Cloudflare Rules</a>. This allows you to write rules that match valid or invalid sequences. The specific cookies used to validate sequences are called sequence cookies.</p>
<h3 id="cf-clearance-cookie-for-cloudflare-bot-products">cf_clearance cookie for Cloudflare bot products</h3>
<p>The <code>cf_clearance</code> cookie is required for <a href="/bots/additional-configurations/javascript-detections/">JavaScript detections</a>. JavaScript detections are stored in the <code>cf_clearance</code> cookie.</p>
<p>The <code>cf_clearance</code> cookie is set with <code>SameSite=None; Secure; Partitioned</code> so that challenge state is preserved across cross-site requests while complying with <a href="https://developers.google.com/privacy-sandbox/cookies/chips">CHIPS ↗</a>. When the cookie is issued inside a third-party context, it is stored in a partition keyed to the top-level site and is not shared across embedding sites. For details, refer to <a href="/waf/troubleshooting/samesite-cookie-interaction/#partitioned-cookies-chips-and-cf_clearance">Partitioned cookies (CHIPS) and <code>cf_clearance</code></a>.</p>
<h3 id="cf-ob-info-and-cf-use-ob-cookie-for-cloudflare-always-online">cf_ob_info and cf_use_ob cookie for Cloudflare Always Online</h3>
<p>The <code>cf_ob_info</code> cookie provides information on:</p>
<ul>
<li>The HTTP Status Code returned by the origin web server</li>
<li>The Ray ID of the original failed request</li>
<li>The data center serving the traffic</li>
</ul>
<p>The <code>cf_use_ob</code> cookie informs Cloudflare to fetch the requested resource from the Always Online cache on the designated port. Applicable values are: 0, 80, and 443. The <code>cf_ob_info</code> and <code>cf_use_ob</code> cookies are persistent cookies that expire after 30 seconds.</p>
<h3 id="cfwaitingroom-for-cloudflare-waiting-room">__cfwaitingroom for Cloudflare Waiting Room</h3>
<p><a href="/waiting-room/">Cloudflare's Waiting Room</a> product enables a waiting room for a particular host and path combination within a zone. Visitors are put in the waiting room and provided an estimate of when they will be allowed to access the application, if not immediately available.</p>
<p>The <code>__cfwaitingroom</code> cookie is only used to track visitors that access a waiting room enabled host and path combination for a zone. Visitors using a browser that does not accept cookies cannot visit the host and path combination while the waiting room is active. For more details, refer to <a href="/waiting-room/reference/waiting-room-cookie/">Waiting Room cookies</a>.</p>
<h3 id="cfruid-to-support-cloudflare-rate-limiting-previous-version">__cfruid to support Cloudflare Rate Limiting (previous version)</h3>
<p>The <code>__cfruid</code> cookie is strictly necessary to support Cloudflare Rate Limiting products. As part of our Rate Limiting solution, this cookie is required to manage incoming traffic and to have better visibility on the origin of a particular request.</p>
<h3 id="cfuvid-for-rate-limiting-rules">_cfuvid for Rate Limiting Rules</h3>
<p>The Rate Limiting Rules product uses a number of techniques for applying rate limits to traffic where multiple unique visitors share the same IP address, such as traffic from behind a NAT. These techniques can be enabled by using the <code>cf.unique_visitor_id</code> field in the rate limiting configuration.</p>
<p>The <code>_cfuvid</code> cookie is only set when a site uses this option in a Rate Limiting Rule, and is only used to allow the Cloudflare WAF to distinguish individual users who share the same IP address. Visitors who do not provide the cookie are likely to be grouped together and may not be able to access the site if there are many other visitors from the same IP address.</p>
<h3 id="additional-cookies-used-by-the-challenge-platform">Additional cookies used by the Challenge Platform</h3>
<p>The table below shows additional cookies used by the Challenge Platform.</p>
<table>
<thead>
<tr>
<th>Cookie Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf_clearance</code></td>
<td>Clearance Cookie stores the proof of challenge passed. It is used to no longer issue a challenge if present. It is required to reach an origin server.</td>
</tr>
<tr>
<td><code>cf_chl_rc_i</code>; <code>cf_chl_rc_ni</code>; <code>cf_chl_rc_m</code></td>
<td>These cookies are for internal use which allows Cloudflare to identify production issues on clients.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9009.md")
</aside>
<h3 id="cloudflare-access-cookies">Cloudflare Access cookies</h3>
<p>To review Cloudflare Access cookies and their behavior, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#access-cookies">Access cookies</a>.</p>
