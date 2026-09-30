---
cp9:
  canonical: https://developers.cloudflare.com/flagship/concepts/
  description: Understand Flagship core concepts including apps, flags, variants, targeting rules, evaluation context, and flag propagation.
  full_title: Concepts · Cloudflare Flagship docs
  head_html: <title>Concepts · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand Flagship core concepts including apps, flags, variants, targeting rules, evaluation context, and flag propagation."><link rel="canonical" href="https://developers.cloudflare.com/flagship/concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/concepts/index.md"><meta property="og:title" content="Concepts · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand Flagship core concepts including apps, flags, variants, targeting rules, evaluation context, and flag propagation."><meta property="og:url" content="https://developers.cloudflare.com/flagship/concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/concepts/#page","headline":"Concepts \u00b7 Cloudflare Flagship docs","description":"Understand Flagship core concepts including apps, flags, variants, targeting rules, evaluation context, and flag propagation.","url":"https://developers.cloudflare.com/flagship/concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/concepts/
  schema: 1
---
<p>Flagship organizes feature flags into apps. You define flags with variants and targeting rules, then evaluate them within Cloudflare's global network.</p>
<h2 id="overview">Overview</h2>
<p>Flagship feature flags go through three stages from creation to evaluation:</p>
<ol>
<li><strong>Configure</strong> — Create flags and targeting rules in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> or through the <a href="/api/resources/flagship">API</a>.</li>
<li><strong>Propagate</strong> — Flagship automatically distributes your flag configuration across Cloudflare's global network within seconds.</li>
<li><strong>Evaluate</strong> — Your Worker (or SDK) evaluates flags locally using the propagated configuration. There is no round-trip to a central server.</li>
</ol>
<p>Flag changes take effect globally within seconds of saving. You do not need to redeploy your Worker or restart your application. If the dashboard is temporarily unavailable, flag evaluation continues to work using the last propagated configuration.</p>
<h2 id="apps">Apps</h2>
<p>An app is the top-level organizational unit in Flagship. It groups related flags together.</p>
<p>An app typically maps to a single project, service, or product surface. Each Cloudflare account can have multiple apps. For example, you might create one app for your marketing site and another for your API backend.</p>
<h2 id="flags">Flags</h2>
<p>A flag is a named feature toggle. Each flag has a key, a set of <a href="#variants">variants</a>, <a href="#targeting-rules">targeting rules</a>, and an enabled/disabled state.</p>
<p>Flag keys must be unique within an app. Keys can contain letters, numbers, hyphens, and underscores.</p>
<p>When a flag is disabled, it always returns the default variant regardless of any targeting rules. Choose a default variant that is safe for your application if Flagship cannot evaluate the flag.</p>
<h2 id="variants">Variants</h2>
<p>Variants are the possible values a flag can return. Each flag must have at least one variant, and one variant is designated as the default.</p>
<p>Flagship supports four variant types:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Boolean</td>
<td><code>on: true</code>, <code>off: false</code></td>
</tr>
<tr>
<td>String</td>
<td><code>v1: &quot;old-checkout&quot;</code>, <code>v2: &quot;new-checkout&quot;</code></td>
</tr>
<tr>
<td>Number</td>
<td><code>low: 100</code>, <code>high: 1000</code></td>
</tr>
<tr>
<td>JSON</td>
<td><code>premium: { &quot;tier&quot;: &quot;premium&quot;, &quot;features&quot;: [&quot;analytics&quot;, &quot;export&quot;] }</code></td>
</tr>
</tbody>
</table>
<p>Use boolean flags for simple on/off toggles. Use string, number, or JSON flags when you need to deliver configuration values or structured data. JSON variants can contain objects or arrays.</p>
<h2 id="targeting-rules">Targeting rules</h2>
<p>Targeting rules control which variant a flag returns for a given request. Rules are evaluated in sequential order, and the first matching rule wins. If no rule matches, the default variant is returned.</p>
<p>Each rule contains:</p>
<ul>
<li><strong>Conditions</strong> that compare an attribute from the <a href="#evaluation-context">evaluation context</a> against a value using an operator.</li>
<li>An optional <strong>percentage rollout</strong> that splits traffic across variants.</li>
<li>A <strong>variant</strong> to serve when the rule matches.</li>
</ul>
<p>Conditions within a rule can be grouped with <code>AND</code>/<code>OR</code> operators.</p>
<p>Refer to <a href="/flagship/targeting/">Targeting rules</a> and <a href="/flagship/targeting/operators/">Operators</a> for the full list of operators and configuration options.</p>
<h2 id="evaluation-context">Evaluation context</h2>
<p>The evaluation context is a set of key-value attributes that describe the current user or request (for example, <code>userId</code>, <code>country</code>, <code>plan</code>).</p>
<p>You pass the context as the third argument to evaluation methods on the binding:</p>
<pre tabindex="0"><code class="language-ts">const value = await env.FLAGS.getBooleanValue(&quot;new-checkout&quot;, false, {&#10;	userId: &quot;user-42&quot;,&#10;	country: &quot;US&quot;,&#10;});&#10;</code></pre>
<p>When using the <a href="/flagship/sdk/">OpenFeature SDK</a>, you pass context through the OpenFeature evaluation context object.</p>
<p>Flagship uses context attributes to match targeting rules and to determine percentage rollout bucketing. A consistent context (for example, the same <code>userId</code>) produces the same rollout result on every evaluation.</p>
<p>Avoid sending sensitive data in evaluation context. Only include attributes needed by targeting rules or rollout bucketing.</p>
<h2 id="flag-propagation">Flag propagation</h2>
<p>After you change a flag, it can take up to 30 seconds for the updated value to reflect globally. During this propagation window, some evaluations may still return the previous flag value.</p>
