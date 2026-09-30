---
cp9:
  canonical: https://developers.cloudflare.com/flagship/best-practices/
  description: Best practices for using Flagship in applications, including evaluation paths, rollout workflows, and safe flag cleanup.
  full_title: Best practices · Cloudflare Flagship docs
  head_html: <title>Best practices · Cloudflare Flagship docs</title><meta name="generator" content="Nift"><meta name="description" content="Best practices for using Flagship in applications, including evaluation paths, rollout workflows, and safe flag cleanup."><link rel="canonical" href="https://developers.cloudflare.com/flagship/best-practices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/flagship/best-practices/index.md"><meta property="og:title" content="Best practices · Cloudflare Flagship docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Best practices for using Flagship in applications, including evaluation paths, rollout workflows, and safe flag cleanup."><meta property="og:url" content="https://developers.cloudflare.com/flagship/best-practices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Flagship"><meta name="algolia_product_filter" content="Flagship"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Flagship"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/flagship/best-practices/#page","headline":"Best practices \u00b7 Cloudflare Flagship docs","description":"Best practices for using Flagship in applications, including evaluation paths, rollout workflows, and safe flag cleanup.","url":"https://developers.cloudflare.com/flagship/best-practices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /flagship/best-practices/
  schema: 1
---
<p>Use these patterns to keep Flagship evaluations predictable, fast, and easy to maintain.</p>
<h2 id="choose-the-right-evaluation-path">Choose the right evaluation path</h2>
<p>Use the <a href="/flagship/binding/">Workers binding</a> inside Cloudflare Workers. The binding handles authentication automatically and avoids application-managed API tokens.</p>
<p>Use the <a href="/flagship/sdk/">OpenFeature SDK</a> when you run outside Workers or need a vendor-neutral OpenFeature interface. In Workers, you can still pass the binding to the OpenFeature server provider to keep binding performance while using OpenFeature APIs.</p>
<h2 id="evaluate-once-per-request">Evaluate once per request</h2>
<p>Avoid evaluating the same flag repeatedly in a loop. Evaluate the flag once, store the result in a local variable, and reuse it for the rest of the request.</p>
<pre tabindex="0"><code class="language-ts">const enabled = await env.FLAGS.getBooleanValue(&quot;show-related-items&quot;, false, {&#10;	userId,&#10;});&#10;&#10;for (const item of items) {&#10;	if (enabled) {&#10;		item.related = await loadRelatedItems(item.id);&#10;	}&#10;}&#10;</code></pre>
<h2 id="pass-context-consistently">Pass context consistently</h2>
<p>Targeting and percentage rollouts depend on the evaluation context you pass from your application. Use stable identifiers and the same attribute names everywhere.</p>
<pre tabindex="0"><code class="language-ts">const context = {&#10;	userId: session.user.id,&#10;	plan: session.user.plan,&#10;	country: request.cf?.country ?? &quot;unknown&quot;,&#10;};&#10;&#10;const enabled = await env.FLAGS.getBooleanValue(&quot;new-checkout&quot;, false, context);&#10;</code></pre>
<p>For OpenFeature SDKs, use <code>targetingKey</code> as the stable identifier. For the Workers binding, use the attribute configured for your rollout, such as <code>userId</code>.</p>
<h2 id="choose-safe-defaults">Choose safe defaults</h2>
<p>Every evaluation method requires a default value. Choose a default that keeps your application safe if the flag does not exist, cannot be evaluated, or has a type mismatch.</p>
<p>For release flags, this is usually the existing experience. For configuration flags, choose conservative limits or behavior that your application can handle without extra dependencies.</p>
<h2 id="use-details-for-debugging-and-observability">Use details for debugging and observability</h2>
<p>Use <code>*Details</code> methods when you need to understand why a value was returned. Details include the resolved value, variant, reason, and error metadata.</p>
<pre tabindex="0"><code class="language-ts">const details = await env.FLAGS.getBooleanDetails(&quot;new-checkout&quot;, false, {&#10;	userId: &quot;user-42&quot;,&#10;});&#10;&#10;console.log(details.value);&#10;console.log(details.variant);&#10;console.log(details.reason);&#10;console.log(details.errorCode);&#10;</code></pre>
<h2 id="roll-out-progressively">Roll out progressively</h2>
<p>Start with a small percentage rollout, monitor application metrics, then increase the percentage over time.</p>
<ol>
<li>Create the flag with a small rollout, such as 5%.</li>
<li>Monitor errors, latency, business metrics, and user feedback.</li>
<li>Increase to 25%, then 50%, then 100% as confidence grows.</li>
<li>After the rollout reaches 100%, make the winning variant the default and remove temporary targeting rules.</li>
<li>After the feature is fully shipped, remove the old code path and delete the flag.</li>
</ol>
<h2 id="clean-up-stale-flags">Clean up stale flags</h2>
<p>Flags that are disabled or fully rolled out still add maintenance cost. Before deleting a flag, disable it first, monitor for unexpected behavior, remove the evaluation code, deploy the code change, then delete the flag from Flagship.</p>
