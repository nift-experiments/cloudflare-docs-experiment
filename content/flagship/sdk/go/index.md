---
cp9:
  canonical: https://developers.cloudflare.com/flagship/sdk/go/
  description: Set up the Flagship OpenFeature provider to evaluate Flagship feature flags from Go server applications.
  full_title: Go SDK · Cloudflare Flagship docs
  head_html: <title>Go SDK · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up the Flagship OpenFeature provider to evaluate Flagship feature flags from Go server applications."><link rel="canonical" href="https://developers.cloudflare.com/flagship/sdk/go/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/sdk/go/index.md"><meta property="og:title" content="Go SDK · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up the Flagship OpenFeature provider to evaluate Flagship feature flags from Go server applications."><meta property="og:url" content="https://developers.cloudflare.com/flagship/sdk/go/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/sdk/go/#page","headline":"Go SDK \u00b7 Cloudflare Flagship docs","description":"Set up the Flagship OpenFeature provider to evaluate Flagship feature flags from Go server applications.","url":"https://developers.cloudflare.com/flagship/sdk/go/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/sdk/go/
  schema: 1
---
<p>The Go SDK provides an OpenFeature-compatible server provider for Go applications. It evaluates flags over HTTP and does not support the Cloudflare Workers binding.</p>
<h2 id="installation">Installation</h2>
<p>Install with <code>go get</code>:</p>
<pre tabindex="0"><code class="language-sh">go get github.com/cloudflare/flagship/sdks/go&#10;</code></pre>
<h2 id="setup">Setup</h2>
<p>Configure the provider with your Flagship app ID, Cloudflare account ID, and an <a href="/flagship/api-tokens/">API token</a> with Flagship Evaluate or Flagship App Evaluate permission.</p>
<pre tabindex="0"><code class="language-go">package main&#10;&#10;import (&#10;	&quot;context&quot;&#10;	&quot;log&quot;&#10;&#10;	flagship &quot;github.com/cloudflare/flagship/sdks/go&quot;&#10;	&quot;github.com/open-feature/go-sdk/openfeature&quot;&#10;)&#10;&#10;func main() {&#10;	ctx := context.Background()&#10;&#10;	provider, err := flagship.NewProvider(flagship.Options{&#10;		AppID:     &quot;&lt;APP_ID&gt;&quot;,&#10;		AccountID: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;		AuthToken: &quot;&lt;API_TOKEN&gt;&quot;,&#10;	})&#10;	if err != nil {&#10;		log.Fatal(err)&#10;	}&#10;&#10;	if err := openfeature.SetProviderAndWait(provider); err != nil {&#10;		log.Fatal(err)&#10;	}&#10;	defer openfeature.Shutdown()&#10;&#10;	client := openfeature.NewDefaultClient()&#10;	evalCtx := openfeature.NewEvaluationContext(&quot;user-42&quot;, map[string]any{&#10;		&quot;plan&quot;: &quot;enterprise&quot;,&#10;	})&#10;&#10;	enabled, err := client.BooleanValue(ctx, &quot;new-checkout&quot;, false, evalCtx)&#10;	if err != nil {&#10;		log.Fatal(err)&#10;	}&#10;&#10;	log.Println(&quot;new-checkout:&quot;, enabled)&#10;}&#10;</code></pre>
<h2 id="flag-types">Flag types</h2>
<p>The Go SDK supports all OpenFeature server-side flag types.</p>
<pre tabindex="0"><code class="language-go">enabled, _ := client.BooleanValue(ctx, &quot;new-checkout&quot;, false, evalCtx)&#10;variant, _ := client.StringValue(ctx, &quot;homepage-hero&quot;, &quot;control&quot;, evalCtx)&#10;rate, _ := client.FloatValue(ctx, &quot;sample-rate&quot;, 0.1, evalCtx)&#10;limit, _ := client.IntValue(ctx, &quot;upload-limit&quot;, 10, evalCtx)&#10;config, _ := client.ObjectValue(ctx, &quot;ui-config&quot;, map[string]any{&quot;theme&quot;: &quot;light&quot;}, evalCtx)&#10;</code></pre>
<p>Use the <code>*ValueDetails</code> methods when you need reason, variant, metadata, or error codes.</p>
<h2 id="response-caching">Response caching</h2>
<p>The provider can cache evaluations to avoid a network round-trip for repeated flag/context pairs. Caching is off by default and enabled by setting <code>CacheTTL</code>:</p>
<pre tabindex="0"><code class="language-go">provider, err := flagship.NewProvider(flagship.Options{&#10;	AppID:        &quot;&lt;APP_ID&gt;&quot;,&#10;	AccountID:    &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	AuthToken:    &quot;&lt;API_TOKEN&gt;&quot;,&#10;	CacheTTL:     30 * time.Second, // values may be up to this stale&#10;	CacheMaxSize: 1000,             // LRU-evicted beyond this many entries&#10;})&#10;</code></pre>
<p>Each cache entry is keyed by flag key, flag type, and the full evaluation context, so distinct contexts never share a cached value. Cache hits resolve with <code>reason == openfeature.CachedReason</code>.</p>
<p>Disabled flags, errors, and type mismatches are never cached. Because freshness is TTL-based, a flag change in Flagship takes effect after the entry expires.</p>
<p>The cache is per-provider instance, guarded by a mutex for concurrent use, and cleared on <code>Shutdown</code>.</p>
<h2 id="configuration-options">Configuration options</h2>
<table>
<thead>
<tr>
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AppID</code></td>
<td>Flagship app ID.</td>
</tr>
<tr>
<td><code>AccountID</code></td>
<td>Required with <code>AppID</code>.</td>
</tr>
<tr>
<td><code>BaseURL</code></td>
<td>Base URL override. Defaults to <code>https://api.cloudflare.com</code>.</td>
</tr>
<tr>
<td><code>AuthToken</code></td>
<td>Adds <code>Authorization: Bearer &lt;token&gt;</code> to each request.</td>
</tr>
<tr>
<td><code>Headers</code></td>
<td>Static headers. Explicit <code>Authorization</code> overrides <code>AuthToken</code>.</td>
</tr>
<tr>
<td><code>HeadersFactory</code></td>
<td>Dynamic per-request headers. Values override <code>Headers</code> and <code>AuthToken</code>.</td>
</tr>
<tr>
<td><code>HTTPClient</code></td>
<td>Custom HTTP client.</td>
</tr>
<tr>
<td><code>Timeout</code></td>
<td>Per-attempt timeout. Defaults to 5 seconds.</td>
</tr>
<tr>
<td><code>Retries</code></td>
<td>Retry attempts on transient errors. Defaults to 1 and is capped at 10.</td>
</tr>
<tr>
<td><code>DisableRetries</code></td>
<td>Disables retries when set to <code>true</code>.</td>
</tr>
<tr>
<td><code>RetryDelay</code></td>
<td>Delay between retries. Defaults to 1 second and is capped at 30 seconds.</td>
</tr>
<tr>
<td><code>CacheTTL</code></td>
<td>Enables in-memory response caching when greater than 0. Cached values may be up to this duration stale.</td>
</tr>
<tr>
<td><code>CacheMaxSize</code></td>
<td>Maximum number of cached entries. LRU-evicted beyond this limit. Defaults to 1000 when <code>CacheTTL</code> is set.</td>
</tr>
<tr>
<td><code>Logging</code></td>
<td>Enables debug and error logging. Off by default.</td>
</tr>
<tr>
<td><code>Logger</code></td>
<td>Optional <code>slog</code>-compatible logger. Uses the default <code>slog</code> logger when unset.</td>
</tr>
<tr>
<td><code>Hooks</code></td>
<td>Provider-level OpenFeature hooks.</td>
</tr>
</tbody>
</table>
<h2 id="evaluation-context">Evaluation context</h2>
<p>Context attributes are sent as URL query parameters. Supported values are strings, numeric types, booleans, and <code>time.Time</code>. <code>nil</code> values are skipped. Maps, slices, structs, and other complex values return <code>INVALID_CONTEXT</code> through OpenFeature and do not trigger an HTTP request.</p>
