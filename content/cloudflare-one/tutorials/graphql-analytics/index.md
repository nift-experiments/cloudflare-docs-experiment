---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/
  description: Use the GraphQL Analytics API to review data for Cloudflare Network Firewall network traffic related to rules matching your traffic.
  full_title: GraphQL Analytics · Cloudflare One docs
  head_html: <title>GraphQL Analytics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the GraphQL Analytics API to review data for Cloudflare Network Firewall network traffic related to rules matching your traffic."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/index.md"><meta property="og:title" content="GraphQL Analytics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the GraphQL Analytics API to review data for Cloudflare Network Firewall network traffic related to rules matching your traffic."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="GraphQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/#page","headline":"GraphQL Analytics \u00b7 Cloudflare One docs","description":"Use the GraphQL Analytics API to review data for Cloudflare Network Firewall network traffic related to rules matching your traffic.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/graphql-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GraphQL"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/graphql-analytics/
  schema: 1
---
<p>Use the GraphQL Analytics API to review data for Cloudflare Network Firewall network traffic related to rules matching your traffic. This contains both rules you configured in the Cloudflare Network Firewall dashboard, and the rules managed by Cloudflare as a part of <a href="/cloudflare-network-firewall/how-to/enable-managed-rulesets/">Cloudflare Network Firewall Managed rules</a> and <a href="/cloudflare-network-firewall/about/ids/">Cloudflare Network Firewall IDS</a> features.</p>
<p>Before you begin, you must have an <a href="/analytics/graphql-api/getting-started/authentication/">API token</a>. For additional help getting started with GraphQL Analytics, refer to <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<h2 id="obtain-cloudflare-account-id">Obtain Cloudflare Account ID</h2>
<p>To construct a Network Firewall GraphQL query for an object, you will need a Cloudflare Account ID</p>
<h3 id="obtain-your-cloudflare-account-id">Obtain your Cloudflare Account ID</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account.</li>
<li>The URL in your browser's address bar should show <code>https://dash.cloudflare.com/</code> followed by a hex string. The hex string is your Cloudflare Account ID.</li>
</ol>
<h3 id="obtain-the-rule-id-for-a-firewall-rule">Obtain the rule ID for a firewall rule</h3>
<p>To construct queries to gather analytics for a particular rule, you need the rule ID for each firewall rule.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cloudflare Network Firewall</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>Custom rules</strong> tab, locate the rule you need the rule ID for from the list and select the three dots &gt; <strong>Edit</strong>.</li>
<li>Locate the <strong>Rule ID</strong> and select the copy button.</li>
<li>Select <strong>Cancel</strong> to return to the <strong>Cloudflare Network Firewall</strong> page.</li>
</ol>
<h2 id="explore-graphql-schema-with-cloudflare-network-firewall-query-example">Explore GraphQL schema with Cloudflare Network Firewall query example</h2>
<p>In this section, you will run a test query to retrieve a five minute count of all configured Cloudflare Network Firewall rules within five minute intervals. You can copy and paste the code below into GraphiQL.</p>
<p>For additional information about the Analytics schema, refer to <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">Explore the Analytics schema with GraphiQL</a>.</p>
<pre tabindex="0"><code class="language-graphql">query MagicFirewallExample($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			magicFirewallSamplesAdaptiveGroups(&#10;				filter: { datetime_geq: $start, datetime_leq: $end }&#10;				limit: 2&#10;				orderBy: [datetimeFiveMinute_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					datetimeFiveMinute&#10;					ruleId&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="example-queries-for-cloudflare-network-firewall">Example queries for Cloudflare Network Firewall</h2>
<h3 id="obtain-analytics-for-a-specific-rule">Obtain analytics for a specific rule</h3>
<p>Use the example below to display the total number of packets and bits for the top ten suspected malicious traffic streams within the last hour. After receiving the results, you can sort by packet rates with a five minute average.</p>
<p>For each stream, display the:</p>
<ul>
<li>Source and destination IP addresses</li>
<li>Ingress Cloudflare data centers that received it</li>
<li>Total traffic volume in bits and packets received within the hour</li>
<li>Actions taken by the firewall rule</li>
</ul>
<pre tabindex="0"><code class="language-graphql">query MagicFirewallObtainRules(&#10;	$accountId: string!&#10;	$ruleId: string&#10;	$start: Time&#10;	$end: Time&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountId }) {&#10;			magicFirewallNetworkAnalyticsAdaptiveGroups(&#10;				filter: { ruleId: $ruleId, datetime_geq: $start, datetime_leq: $end }&#10;				limit: 10&#10;				orderBy: [avg_packetRateFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					coloCity&#10;					ipDestinationAddress&#10;					ipSourceAddress&#10;					outcome&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="obtain-ids-analytics">Obtain IDS analytics</h3>
<p>Use the example below to display the total number of packets and bits for the top 10 traffic streams that Cloudflare Network Firewall IDS has detected in the last hour.</p>
<p>By setting <code>verdict</code> to <code>drop</code> and <code>outcome</code> as <code>pass</code>, we are filtering for traffic that was marked as a detection (i.e. verdict was drop) but was not dropped (for example, outcome was <code>pass</code>). This is because currently, Cloudflare Network Firewall IDS only detects malicious traffic but does not drop the traffic.</p>
<p>For each stream, display the:</p>
<ul>
<li>Source and destination IP addresses.</li>
<li>Ingress Cloudflare data centers that received it.</li>
<li>Total traffic volume in bits and packets received within the hour.</li>
</ul>
<pre tabindex="0"><code class="language-graphql">query MagicFirewallObtainIDS($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			magicIDPSNetworkAnalyticsAdaptiveGroups(&#10;				filter: {&#10;					datetime_geq: $start&#10;					datetime_leq: $end&#10;					verdict: drop&#10;					outcome: pass&#10;				}&#10;				limit: 10&#10;				orderBy: [avg_packetRateFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					coloCity&#10;					ipDestinationAddress&#10;					ipSourceAddress&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Alternatively, to inspect all traffic that was analyzed, but grouped into malicious traffic and other traffic, the example below can be used. The response will contain two entries for each five minute timestamp. <code>verdict</code> will be set to <code>drop</code> for malicious traffic, and <code>verdict</code> will be set to <code>pass</code> for traffic that did not match any of the IDS rules.</p>
<pre tabindex="0"><code class="language-graphql">query MagicFirewallTraffic($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			magicIDPSNetworkAnalyticsAdaptiveGroups(&#10;				filter: { datetime_geq: $start, datetime_leq: $end }&#10;				limit: 10&#10;				orderBy: [avg_packetRateFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					coloCity&#10;					ipDestinationAddress&#10;					ipSourceAddress&#10;					verdict&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
