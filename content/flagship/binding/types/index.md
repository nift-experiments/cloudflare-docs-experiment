---
cp9:
  canonical: https://developers.cloudflare.com/flagship/binding/types/
  description: TypeScript type definitions for the Flagship binding, including Flagship, FlagshipEvaluationContext, and FlagshipEvaluationDetails.
  full_title: Types · Cloudflare Flagship docs
  head_html: <title>Types · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="TypeScript type definitions for the Flagship binding, including Flagship, FlagshipEvaluationContext, and FlagshipEvaluationDetails."><link rel="canonical" href="https://developers.cloudflare.com/flagship/binding/types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/binding/types/index.md"><meta property="og:title" content="Types · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="TypeScript type definitions for the Flagship binding, including Flagship, FlagshipEvaluationContext, and FlagshipEvaluationDetails."><meta property="og:url" content="https://developers.cloudflare.com/flagship/binding/types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/binding/types/#page","headline":"Types \u00b7 Cloudflare Flagship docs","description":"TypeScript type definitions for the Flagship binding, including Flagship, FlagshipEvaluationContext, and FlagshipEvaluationDetails.","url":"https://developers.cloudflare.com/flagship/binding/types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/binding/types/
  schema: 1
---
<p>The Flagship binding uses the following TypeScript types. These are available from the <code>@cloudflare/workers-types</code> package after running <code>npx wrangler types</code>.</p>
<h2 id="flagship"><code>Flagship</code></h2>
<p>The binding type. Each Flagship binding in your Wrangler configuration is typed as <code>Flagship</code> on the <code>Env</code> interface.</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;	FLAGS: Flagship;&#10;}&#10;</code></pre>
<p>Refer to the <a href="/flagship/binding/methods/">methods reference</a> for the full list of evaluation methods available on the binding.</p>
<h2 id="flagshipevaluationcontext"><code>FlagshipEvaluationContext</code></h2>
<p>A record of attribute names to values passed for <a href="/flagship/targeting/">targeting rules</a>. Use this to provide user attributes such as user ID, country, or plan type.</p>
<pre tabindex="0"><code class="language-ts">type FlagshipEvaluationContext = Record&lt;string, string | number | boolean&gt;;&#10;</code></pre>
<h2 id="flagshipevaluationdetails"><code>FlagshipEvaluationDetails</code></h2>
<p>Returned by the <code>*Details</code> methods. Contains the evaluated value and metadata about how Flagship resolved the flag.</p>
<pre tabindex="0"><code class="language-ts">interface FlagshipEvaluationDetails&lt;T&gt; {&#10;	flagKey: string;&#10;	value: T;&#10;	variant?: string;&#10;	reason?: string;&#10;	errorCode?: string;&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>flagKey</code></td>
<td><code>string</code></td>
<td>The key of the evaluated flag.</td>
</tr>
<tr>
<td><code>value</code></td>
<td><code>T</code></td>
<td>The resolved flag value.</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>string</code></td>
<td>The name of the matched variant, if any.</td>
</tr>
<tr>
<td><code>reason</code></td>
<td><code>string</code></td>
<td>Why the flag resolved to this value (for example, <code>&quot;TARGETING_MATCH&quot;</code> or <code>&quot;DEFAULT&quot;</code>).</td>
</tr>
<tr>
<td><code>errorCode</code></td>
<td><code>string</code></td>
<td>An error code if evaluation failed (for example, <code>&quot;TYPE_MISMATCH&quot;</code> or <code>&quot;GENERAL&quot;</code>).</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/flagship/reference/evaluation-reasons/">evaluation reasons and error codes</a> for the full list of possible values.</p>
