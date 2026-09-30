---
cp9:
  canonical: https://developers.cloudflare.com/realtime/turn/replacing-existing/
  description: Migrate from self-hosted or third-party TURN servers to Cloudflare Realtime TURN.
  full_title: Replacing existing TURN servers · Cloudflare Realtime docs
  head_html: <title>Replacing existing TURN servers · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Migrate from self-hosted or third-party TURN servers to Cloudflare Realtime TURN."><link rel="canonical" href="https://developers.cloudflare.com/realtime/turn/replacing-existing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/turn/replacing-existing/index.md"><meta property="og:title" content="Replacing existing TURN servers · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Migrate from self-hosted or third-party TURN servers to Cloudflare Realtime TURN."><meta property="og:url" content="https://developers.cloudflare.com/realtime/turn/replacing-existing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/turn/replacing-existing/#page","headline":"Replacing existing TURN servers \u00b7 Cloudflare Realtime docs","description":"Migrate from self-hosted or third-party TURN servers to Cloudflare Realtime TURN.","url":"https://developers.cloudflare.com/realtime/turn/replacing-existing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/turn/replacing-existing/
  schema: 1
---
<p>If you are an existing TURN provider but would like to switch to providing Cloudflare Realtime TURN for your customers, there are a few considerations.</p>
<h2 id="benefits">Benefits</h2>
<p>Cloudflare Realtime TURN service can reduce tangible and untangible costs associated with TURN servers:</p>
<ul>
<li>Server costs (AWS EC2 etc)</li>
<li>Bandwidth costs (Egress, load balancing etc)</li>
<li>Time and effort to set up a TURN process and maintenance of server</li>
<li>Scaling the servers up and down</li>
<li>Maintain the TURN server with security and feature updates</li>
<li>Maintain high availability</li>
</ul>
<h2 id="recommendations">Recommendations</h2>
<h3 id="separate-environments-with-turn-keys">Separate environments with TURN keys</h3>
<p>When using Cloudflare Realtime TURN service at scale, consider separating environments such as &quot;testing&quot;, &quot;staging&quot; or &quot;production&quot; with TURN keys. You can create up to 1,000 TURN keys in your account, which can be used to generate end user credentials.</p>
<p>There is no limit to how many end-user credentials you can create with a particular TURN key.</p>
<h3 id="tag-users-with-custom-identifiers">Tag users with custom identifiers</h3>
<p>Cloudflare Realtime TURN service lets you tag each credential with a custom identifier as you generate a credential like below:</p>
<pre tabindex="0"><code class="language-bash">curl https://rtc.live.cloudflare.com/v1/turn/keys/$TURN_KEY_ID/credentials/generate \&#10;&#45;-header &quot;Authorization: Bearer $TURN_KEY_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;ttl&quot;: 864000, &quot;customIdentifier&quot;: &quot;user4523958&quot;}&#x27;&#10;</code></pre>
<p>Use this field to aggregate usage for a specific user or group of users and collect analytics.</p>
<h3 id="monitor-usage">Monitor usage</h3>
<p>You can monitor account wide usage with the <a href="/realtime/turn/analytics/">GraphQL analytics API</a>. This is useful for keeping track of overall usage for billing purposes, watching for unexpected changes. You can get timeseries data from TURN analytics with various filters in place.</p>
<h3 id="monitor-for-credential-abuse">Monitor for credential abuse</h3>
<p>If you share TURN credentials with end users, credential abuse is possible. You can monitor for abuse by tagging each credential with custom identifiers and monitoring for top custom identifiers in your application via the <a href="/realtime/turn/analytics/">GraphQL analytics API</a>.</p>
<h2 id="how-to-bill-end-users-for-their-turn-usage">How to bill end users for their TURN usage</h2>
<p>When billing for TURN usage in your application, it's crucial to understand and account for adaptive sampling in TURN analytics. This system employs adaptive sampling to efficiently handle large datasets while maintaining accuracy.</p>
<p>The sampling process in TURN analytics works on two levels:</p>
<ul>
<li>At data collection: Usage data points may be sampled if they are generated too quickly.</li>
<li>At query time: Additional sampling may occur if the query is too complex or covers a large time range.</li>
</ul>
<p>To ensure accurate billing, write a single query that sums TURN usage per customer per time period, returning a single value. Avoid using queries that list usage for multiple customers simultaneously.</p>
<p>By following these guidelines and understanding how TURN analytics handles sampling, you can ensure more accurate billing for your end users based on their TURN usage.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11565.md")
</aside>
<h3 id="example-queries">Example queries</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="incorrect-approach-example">Incorrect approach example</h3>
@markup("md", "content/.markup/bodies/11564.md")
</aside>
<pre tabindex="0"><code>query{&#10;  viewer {&#10;    usage: accounts(filter: { accountTag: &quot;8846293bd06d1af8c106d89ec1454fe6&quot; }) {&#10;        callsTurnUsageAdaptiveGroups(&#10;          filter: {&#10;          datetimeMinute_gt: &quot;2024-07-15T02:07:07Z&quot;&#10;          datetimeMinute_lt: &quot;2024-08-10T02:07:05Z&quot;&#10;        }&#10;          limit: 100&#10;          orderBy: [customIdentifier_ASC]&#10;        ) {&#10;          dimensions {&#10;            customIdentifier&#10;          }&#10;          sum {&#10;            egressBytes&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#10;</code></pre>
<p>Below is a query that queries usage only for a single customer.</p>
<pre tabindex="0"><code>query{&#10;  viewer {&#10;    usage: accounts(filter: { accountTag: &quot;8846293bd06d1af8c106d89ec1454fe6&quot; }) {&#10;        callsTurnUsageAdaptiveGroups(&#10;          filter: {&#10;          datetimeMinute_gt: &quot;2024-07-15T02:07:07Z&quot;&#10;          datetimeMinute_lt: &quot;2024-08-10T02:07:05Z&quot;&#10;          customIdentifier: &quot;myCustomer1111&quot;&#10;        }&#10;          limit: 1&#10;          orderBy: [customIdentifier_ASC]&#10;        ) {&#10;          dimensions {&#10;            customIdentifier&#10;          }&#10;          sum {&#10;            egressBytes&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#10;</code></pre>
