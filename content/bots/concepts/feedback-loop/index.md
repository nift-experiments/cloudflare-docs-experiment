---
cp9:
  canonical: https://developers.cloudflare.com/bots/concepts/feedback-loop/
  description: Submit feedback to improve bot detection accuracy for your domain.
  full_title: Bot Feedback Loop · Cloudflare bot solutions docs
  head_html: <title>Bot Feedback Loop · Cloudflare bot solutions docs</title><meta name="generator" content="Nift"><meta name="description" content="Submit feedback to improve bot detection accuracy for your domain."><link rel="canonical" href="https://developers.cloudflare.com/bots/concepts/feedback-loop/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/bots/concepts/feedback-loop/index.md"><meta property="og:title" content="Bot Feedback Loop · Cloudflare bot solutions docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Submit feedback to improve bot detection accuracy for your domain."><meta property="og:url" content="https://developers.cloudflare.com/bots/concepts/feedback-loop/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Bots"><meta name="algolia_product_filter" content="Bots"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Bots"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/bots/concepts/feedback-loop/#page","headline":"Bot Feedback Loop \u00b7 Cloudflare bot solutions docs","description":"Submit feedback to improve bot detection accuracy for your domain.","url":"https://developers.cloudflare.com/bots/concepts/feedback-loop/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /bots/concepts/feedback-loop/
  schema: 1
---
<p>The Bot Feedback Loop allows you to report requests that Bot Management <span class="nb-glossary-tooltip" title="bot score">scored</span> incorrectly. When you submit a false negative or false positive report, Cloudflare analyzes the data and uses it to train the next machine learning model.</p>
<h2 id="availability">Availability</h2>
<p>Bot Feedback Loop is available for Enterprise Bot Management customers. Visit <a href="/bots/plans/">Plans</a> for more information.</p>
<h2 id="false-positive">False Positive</h2>
<p>A false positive can happen if Cloudflare scores a request from a person using a browser, mobile application or desktop application in the <em>automated</em> or <em>likely automated</em> range.</p>
<h2 id="false-negative">False Negative</h2>
<p>If Cloudflare is unable to detect a portion of automated traffic on your site, submitting a False Negative report will help us catch it in the future.</p>
<h3 id="subtypes">Subtypes</h3>
<table>
<thead>
<tr>
<th>Subtype</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Account Creation Abuse</td>
<td>The automated creation of many new accounts in order to gain access to site resources.</td>
</tr>
<tr>
<td>Ad Fraud</td>
<td>Fraudulent increase in the number of times an advertisement is clicked on or displayed.</td>
</tr>
<tr>
<td>Credit Card Abuse</td>
<td>Attempts to repeatedly validate many credit card numbers or the same credit card number with different validation details.</td>
</tr>
<tr>
<td>Cashing Out</td>
<td>Abusing the target Internet application to obtain valuable goods.</td>
</tr>
<tr>
<td>Login Abuse</td>
<td>Attempts to gain access to a password protected portion of an Internet application using many different combinations of usernames and passwords.</td>
</tr>
<tr>
<td>Inventory Abuse</td>
<td>Automated abuse related to purchasing limited stock inventory or holding inventory to prevent others from making transactions.</td>
</tr>
<tr>
<td>Denial of Service</td>
<td>Automated requests with the intent of exhausting server resources to prevent the Internet application from functioning.</td>
</tr>
<tr>
<td>Expediting</td>
<td>Automating the use of an Internet application to make transactions faster than a human visitor to gain unfair advantage.</td>
</tr>
<tr>
<td>Fuzzing</td>
<td>Finding implementation bugs through the use of malformed data injection in an automated fashion.</td>
</tr>
<tr>
<td>Scraping</td>
<td>Automated retrieval of valuable or proprietary information from an Internet application.</td>
</tr>
<tr>
<td>Spamming</td>
<td>The abuse of content forms to send spam.</td>
</tr>
<tr>
<td>Token Cracking</td>
<td>Identification of valid token codes providing some form of user benefit within the application.</td>
</tr>
<tr>
<td>Vulnerability Scanning</td>
<td>Systematic enumeration and examination of identifiable, guessable and unknown content locations, paths, file names, parameters, to find weaknesses and points where a security vulnerability might exist.</td>
</tr>
</tbody>
</table>
<h2 id="submit-a-report">Submit a report</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3512.md")
</div>
<h2 id="via-the-api">Via the API</h2>
<h3 id="create-a-feedback-report">Create a feedback report</h3>
<pre tabindex="0"><code class="language-sh">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/bot_management/feedback&#x27; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;type&quot;: &quot;false_positive&quot;,&#10;  &quot;description&quot;: &quot;Legitimate customers having low score&quot;,&#10;  &quot;expression&quot;: &quot;(cf.bot_management.score le 46 and ip.src.asnum eq 132892 and http.host eq \&quot;api-discovery.theburritobot.com\&quot; and cf.bot_management.ja3_hash eq \&quot;3fed133de60c35724739b913924b6c24\&quot;)&quot;,&#10;  &quot;first_request_seen_at&quot;: &quot;2022-08-01T00:00:00Z&quot;,&#10;  &quot;last_request_seen_at&quot;: &quot;2022-08-10T00:00:00Z&quot;,&#10;  &quot;requests&quot;: 100,&#10;  &quot;requests_by_score&quot;: {&#10;    &quot;1&quot;: 50,&#10;    &quot;10&quot;: 50&#10;  },&#10;  &quot;requests_by_score_src&quot;: {&#10;    &quot;heuristics&quot;: 25,&#10;    &quot;machine_learning&quot;: 75&#10;  },&#10;  &quot;requests_by_attribute&quot;: {&#10;    &quot;topIPs&quot;: [&#10;      {&#10;        &quot;metric&quot;: &quot;10.75.34.1&quot;,&#10;        &quot;requests&quot;: 100&#10;      }&#10;    ],&#10;    &quot;topUserAgents&quot;: [&#10;      {&#10;        &quot;metric&quot;: &quot;curl/7.68.0&quot;,&#10;        &quot;requests&quot;: 100&#10;      }&#10;    ]&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="list-feedback-reports">List feedback reports</h3>
<pre tabindex="0"><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/bot_management/feedback&#x27; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">[&#10;	{&#10;		&quot;created_at&quot;: &quot;2022-08-19T00:05:24.749712Z&quot;,&#10;		&quot;type&quot;: &quot;false_positive&quot;,&#10;		&quot;description&quot;: &quot;Legitimate customers having low score&quot;,&#10;		&quot;expression&quot;: &quot;(cf.bot_management.score le 46 and ip.src.asnum eq 132892 and http.host eq \&quot;api-discovery.theburritobot.com\&quot; and cf.bot_management.ja3_hash eq \&quot;3fed133de60c35724739b913924b6c24\&quot;)&quot;,&#10;		&quot;first_request_seen_at&quot;: &quot;2022-08-01T00:00:00Z&quot;,&#10;		&quot;last_request_seen_at&quot;: &quot;2022-08-10T00:00:00Z&quot;,&#10;		&quot;requests&quot;: 100,&#10;		&quot;requests_by_score&quot;: {&#10;			&quot;1&quot;: 50,&#10;			&quot;10&quot;: 50&#10;		},&#10;		&quot;requests_by_score_src&quot;: {&#10;			&quot;heuristics&quot;: 25,&#10;			&quot;machine_learning&quot;: 75&#10;		},&#10;		&quot;requests_by_attribute&quot;: {&#10;			&quot;topIPs&quot;: [&#10;				{&#10;					&quot;metric&quot;: &quot;10.75.34.1&quot;,&#10;					&quot;requests&quot;: 100&#10;				}&#10;			],&#10;			&quot;topUserAgents&quot;: [&#10;				{&#10;					&quot;metric&quot;: &quot;curl/7.68.0&quot;,&#10;					&quot;requests&quot;: 100&#10;				}&#10;			]&#10;		}&#10;	}&#10;]&#10;</code></pre>
<h2 id="api-fields">API Fields</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
<th>Value Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>type</code></td>
<td>string</td>
<td>The feedback report type.</td>
<td><code>false_positive</code></td>
</tr>
<tr>
<td><code>description</code></td>
<td>string</td>
<td>The feedback report description with more details on the issue.</td>
<td>Legitimate customers having low scores.</td>
</tr>
<tr>
<td><code>expression</code></td>
<td>string</td>
<td>The wirefilter expression matching reported requests.</td>
<td><code>(cf.bot_management.score le 46 and ip.src.asnum eq 132892 and http.host eq &quot;app.example.com&quot; and cf.bot_management.ja3_hash eq &quot;3fed133de60c35724739b913924b6c24&quot;)</code></td>
</tr>
<tr>
<td><code>first_request_seen_at</code></td>
<td>string</td>
<td>The time range start when the first request has been seen, RFC 3339 format.</td>
<td><code>2022-08-01T00:00:00Z</code></td>
</tr>
<tr>
<td><code>last_request_seen_at</code></td>
<td>string</td>
<td>The time range end when the last request has been seen, RFC 3339 format.</td>
<td><code>2022-08-10T00:00:00Z</code></td>
</tr>
<tr>
<td><code>requests</code></td>
<td>integer</td>
<td>The total number of reported requests.</td>
<td><code>100</code></td>
</tr>
<tr>
<td><code>requests_by_score</code></td>
<td>object</td>
<td>The requests breakdown by score.</td>
<td>See example below.</td>
</tr>
<tr>
<td><code>requests_by_score_src</code></td>
<td>object</td>
<td>Requests breakdown by score source.</td>
<td>See example below.</td>
</tr>
<tr>
<td><code>requests_by_attribute</code></td>
<td>object</td>
<td>Requests breakdown by attribute (optional).</td>
<td>See example below.</td>
</tr>
</tbody>
</table>
<p><code>requests_by_score</code></p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;1&quot;: 50,&#10;	&quot;10&quot;: 50&#10;}&#10;</code></pre>
<p><code>requests_by_score_src</code></p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;machine_learning&quot;: 75,&#10;	&quot;heuristics&quot;: 25&#10;}&#10;</code></pre>
<p><code>requests_by_attribute</code></p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;topIPs&quot;: [&#10;		{&#10;			&quot;metric&quot;: &quot;10.75.34.1&quot;&#10;			&quot;requests&quot;: 100&#10;		}&#10;	],&#10;	&quot;topUserAgents&quot;: [&#10;		{&#10;			&quot;metric&quot;: &quot;curl/7.68.0&quot;,&#10;			&quot;requests&quot;: 100&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h3 id="expression-fields">Expression fields</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.bot_management.ja3_hash</code></td>
<td>string</td>
<td>This provides an SSL/TLS fingerprint to help you identify potential bot requests.</td>
</tr>
<tr>
<td><code>cf.bot_management.score</code></td>
<td>integer</td>
<td>This represents the likelihood that a request originates from a bot using a score from 1-99.</td>
</tr>
<tr>
<td><code>http.host</code></td>
<td>string</td>
<td>This represents the hostname used in the full request URI.</td>
</tr>
<tr>
<td><code>http.request.uri.path</code></td>
<td>string</td>
<td>This represents the URI path of the request.</td>
</tr>
<tr>
<td><code>http.user_agent</code></td>
<td>string</td>
<td>This represents the HTTP user agent which is a request header that contains a characteristic string to allow identification of the client operating system and web browser.</td>
</tr>
<tr>
<td><code>ip.src.asnum</code></td>
<td>integer</td>
<td>This represents the 16- or 32-bit integer representing the Autonomous System (AS) number associated with client IP address.</td>
</tr>
<tr>
<td><code>ip.src.country</code></td>
<td>string</td>
<td>This represents the 2-letter country code in ISO 3166-1 Alpha 2 format.</td>
</tr>
<tr>
<td><code>ip.src</code></td>
<td>string</td>
<td>The source address of the IP.</td>
</tr>
</tbody>
</table>
<h2 id="recommendations-when-submitting-a-report">Recommendations when submitting a report</h2>
<p>When you submit a report, use the filters available in the Bot Analytics dashboard to ensure that your report includes only the traffic that received an incorrect score. In addition to filtering by a score (required), you may want to filter by user-agent, IP, ASN or JA3 to more precisely highlight the section of traffic that was scored incorrectly.</p>
<p>If you are not certain if some traffic received an incorrect score, keep this traffic in the report.</p>
<p>We appreciate any comments you wish to leave in the description field that might help our team better understand these requests in the context of typical traffic to your domain.</p>
<h2 id="recommendations-after-submitting-a-false-positive">Recommendations after submitting a false positive</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3510.md")
</aside>
<p>After submitting a false positive, you can explicitly allow the traffic if you are confident that this traffic source cannot be used for abuse in the future. To allow traffic, you can create a WAF custom rule with a <a href="/waf/custom-rules/skip/options/#skip-the-remaining-custom-rules-current-ruleset">Skip the remaining custom rules</a> action that matches the characteristics of your false positive report. We recommend any skip rule that you create uses the most narrow possible scope, including restricting the request methods and URIs that the expected traffic has access to, to limit potential abuse.</p>
<ul>
<li>Allowing a <strong><a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3/JA4 fingerprint</a></strong>: If you want to allow access to a stable software client that does not come from a dedicated IP, you can do so by looking up the JA3 fingerprint(s) used by that client in the Bot Analytics dashboard, and creating a WAF custom rule to allow traffic based on that JA3 fingerprint. JA3 fingerprints will only match a client’s TLS library, so be cautious in looking for both overlap with other clients and with variation based on the operating system. <br/><br/>Cloudflare does not recommend relying on JA3 rules for mobile applications that may be abused. If you have questions about how to securely allow traffic from your mobile application, please contact your account team.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3509.md")
</aside>
<ul>
<li>Allowing an <strong>IP address</strong>: Only use an IP address to allow traffic if the IP is a dedicated resource that belongs only to the traffic source you wish to allow. <br/>If the traffic you want to allow shares an IP with other traffic sources, or if the IP changes frequently, consider an alternative to allowing by IP address.</li>
</ul>
<h2 id="recommendations-after-submitting-a-false-negative">Recommendations after submitting a false negative</h2>
<p>After submitting a false negative report, you can explicitly block or rate-limit the incorrectly scored traffic using a combination of characteristics such as IP address, JA3 fingerprint, ASN, and user-agent. Before blocking or rate-limiting based on JA3 fingerprint, please use Bot Analytics to confirm that fingerprint is not being used by legitimate traffic sources.</p>
