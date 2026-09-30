---
cp9:
  canonical: https://developers.cloudflare.com/client-side-security/rules/violations/
  description: Cloudflare reports any violations to your content security rules.
  full_title: Content security rule violations · Client-side security docs
  head_html: <title>Content security rule violations · Client-side security docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare reports any violations to your content security rules."><link rel="canonical" href="https://developers.cloudflare.com/client-side-security/rules/violations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/client-side-security/rules/violations/index.md"><meta property="og:title" content="Content security rule violations · Client-side security docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare reports any violations to your content security rules."><meta property="og:url" content="https://developers.cloudflare.com/client-side-security/rules/violations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Client-side security"><meta name="algolia_product_filter" content="Client-side security"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Client-side security"><meta name="pcx_tags" content="GraphQL,CSP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/client-side-security/rules/violations/#page","headline":"Content security rule violations \u00b7 Client-side security docs","description":"Cloudflare reports any violations to your content security rules.","url":"https://developers.cloudflare.com/client-side-security/rules/violations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL","CSP"]}</script>
  markdown: true
  noindex: false
  route: /client-side-security/rules/violations/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3961.md")
</aside>
<p>A rule violation occurs when a browser loads a resource that is not covered by one of your <a href="/client-side-security/rules/">content security rules</a>. For log rules, the resource loads normally but is reported. For allow rules, the browser blocks the resource.</p>
<p>Shortly after you configure content security rules, the Cloudflare dashboard will start displaying any violations of those rules. This information is available for rules with any <a href="/client-side-security/rules/#rule-actions">action</a> (<em>Allow</em> and <em>Log</em>).</p>
<p>Information about rule violations is also available via <a href="#get-rule-violations-via-graphql-api">GraphQL API</a> and <a href="#get-rule-violations-via-logpush">Logpush</a>.</p>
<h2 id="review-rule-violations-in-the-dashboard">Review rule violations in the dashboard</h2>
<p>To view rule violation information:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>(Optional) Filter by <strong>Content security rules</strong>.</li>
</ol>
<p>The displayed information includes the following:</p>
<ul>
<li>A sparkline next to the rule name, showing violations in the past seven days.</li>
<li>For content security rules with associated violations, an expandable details section for each rule, with the top resources present in violation events and a sparkline per top resource.</li>
</ul>
<h2 id="get-rule-violations-via-graphql-api">Get rule violations via GraphQL API</h2>
<p>Use the <a href="/analytics/graphql-api/">Cloudflare GraphQL API</a> to obtain rule violation information through the following dataset:</p>
<ul>
<li><code>pageShieldReportsAdaptiveGroups</code></li>
</ul>
<p>You can query the dataset for rule violations that occurred in the past 30 days.</p>
<p>Use <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a> to explore the available fields the GraphQL schema. For more information, refer to <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">Explore the GraphQL schema</a>.</p>
<p>For an introduction to GraphQL querying, refer to <a href="/analytics/graphql-api/getting-started/querying-basics/">Querying basics</a>.</p>
<h3 id="example">Example</h3>
<pre tabindex="0"><code class="language-graphql">query PageShieldReports(&#10;	$zoneTag: string&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			pageShieldReportsAdaptiveGroups(&#10;				limit: 100&#10;				orderBy: [datetime_ASC]&#10;				filter: { datetime_geq: $datetimeStart, datetime_leq: $datetimeEnd }&#10;			) {&#10;				avg {&#10;					sampleInterval&#10;				}&#10;				count&#10;				dimensions {&#10;					policyID&#10;					datetime&#10;					datetimeMinute&#10;					datetimeFiveMinutes&#10;					datetimeFifteenMinutes&#10;					datetimeHalfOfHour&#10;					datetimeHour&#10;					url&#10;					urlHost&#10;					host&#10;					resourceType&#10;					pageURL&#10;					action&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Example curl request</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3962.md")
</div></details>
<h2 id="get-rule-violations-via-logpush">Get rule violations via Logpush</h2>
<p><a href="/logs/logpush/">Cloudflare Logpush</a> supports pushing logs to storage services, <span class="nb-glossary-tooltip" title="SIEM">SIEM systems</span>, and log management providers.</p>
<p>Information about rule violations is available in the <a href="/logs/logpush/logpush-job/datasets/zone/page_shield_events/"><code>page_shield_events</code> dataset</a>.</p>
<p>For more information on configuring Logpush jobs, refer to <a href="/logs/logpush/">Logpush</a> documentation.</p>
