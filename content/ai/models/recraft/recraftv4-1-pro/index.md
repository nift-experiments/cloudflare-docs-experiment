---
cp9:
  canonical: https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/
  description: recraft/recraftv4-1-pro
  full_title: Recraft V4.1 Pro · Cloudflare AI docs
  head_html: <title>Recraft V4.1 Pro · Cloudflare AI docs</title><meta name="generator" content="Nift"><meta name="description" content="recraft/recraftv4-1-pro"><link rel="canonical" href="https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Recraft V4.1 Pro · Cloudflare AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="recraft/recraftv4-1-pro"><meta property="og:url" content="https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI"><meta name="algolia_product_filter" content="AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/#page","headline":"Recraft V4.1 Pro \u00b7 Cloudflare AI docs","description":"recraft/recraftv4-1-pro","url":"https://developers.cloudflare.com/ai/models/recraft/recraftv4-1-pro/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /ai/models/recraft/recraftv4-1-pro/
  schema: 1
---
<img src="/assets/upstream/images/workers-ai/recraft.svg" alt="Recraft logo" width="48" height="48">

<h1 id="recraft-v4-1-pro">Recraft V4.1 Pro</h1>

<p><code>recraft/recraftv4-1-pro</code></p>

Recraft V4.1 Pro generates high-resolution, art-directed images at 2048px+ tuned for high aesthetics, with strong composition, text rendering, and refined design taste. Built for print and production work.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text-to-Image</td></tr>
<tr><th>Terms</th><td><a href="https://www.recraft.ai/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Per image: 0.25</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

High-resolution illustration for print

<section class="model-example"><strong>Print-Ready Illustration</strong>
<p>High-resolution illustration for print</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed vintage botanical illustration of a rose with leaves and thorns, scientific illustration style&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/print-ready-illustration.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/print-ready-illustration.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-pro&#x27;,
  {
    prompt:
      &#x27;A detailed vintage botanical illustration of a rose with leaves and thorns, scientific illustration style&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A detailed vintage botanical illustration of a rose with leaves and thorns, scientific illustration style&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/print-ready-illustration.png" alt="Print-Ready Illustration">
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>Large Format Art</strong>
<p>Large canvas digital art</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sweeping fantasy landscape with floating islands, waterfalls cascading into clouds, and ancient stone bridges connecting the islands&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/large-format-art.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/large-format-art.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-pro&#x27;,
  {
    prompt:
      &#x27;A sweeping fantasy landscape with floating islands, waterfalls cascading into clouds, and ancient stone bridges connecting the islands&#x27;,
    size: &#x27;2048x2048&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A sweeping fantasy landscape with floating islands, waterfalls cascading into clouds, and ancient stone bridges connecting the islands&quot;,
    &quot;size&quot;: &quot;2048x2048&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/large-format-art.png" alt="Large Format Art">
</section>

<section class="model-example"><strong>Brand Asset</strong>
<p>Professional brand asset with controlled colors</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A modern, clean illustration of a shield with a checkmark inside, representing security and trust&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          15,
          23,
          42
        ]
      },
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            46,
            117,
            182
          ]
        },
        {
          &quot;rgb&quot;: [
            255,
            255,
            255
          ]
        }
      ]
    },
    &quot;size&quot;: &quot;2048x2048&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/brand-asset.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/brand-asset.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-pro&#x27;,
  {
    prompt:
      &#x27;A modern, clean illustration of a shield with a checkmark inside, representing security and trust&#x27;,
    controls: {
      background_color: { rgb: [15, 23, 42] },
      colors: [{ rgb: [46, 117, 182] }, { rgb: [255, 255, 255] }],
    },
    size: &#x27;2048x2048&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A modern, clean illustration of a shield with a checkmark inside, representing security and trust&quot;,
    &quot;controls&quot;: {
      &quot;background_color&quot;: {
        &quot;rgb&quot;: [
          15,
          23,
          42
        ]
      },
      &quot;colors&quot;: [
        {
          &quot;rgb&quot;: [
            46,
            117,
            182
          ]
        },
        {
          &quot;rgb&quot;: [
            255,
            255,
            255
          ]
        }
      ]
    },
    &quot;size&quot;: &quot;2048x2048&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/brand-asset.png" alt="Brand Asset">
</section>

<section class="model-example"><strong>Editorial Illustration</strong>
<p>Magazine-quality editorial illustration</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A conceptual illustration of artificial intelligence as a tree with circuit-board branches and glowing data leaves&quot;
  },
  &quot;output&quot;: {
    &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/editorial-illustration.png&quot;
  },
  &quot;raw_response&quot;: {
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;Unified&quot;
    },
    &quot;result&quot;: {
      &quot;image&quot;: &quot;https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/editorial-illustration.png&quot;
    },
    &quot;state&quot;: &quot;Completed&quot;
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;recraft/recraftv4-1-pro&#x27;,
  {
    prompt:
      &#x27;A conceptual illustration of artificial intelligence as a tree with circuit-board branches and glowing data leaves&#x27;,
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;recraft/recraftv4-1-pro&quot;,
  &quot;input&quot;: {
    &quot;prompt&quot;: &quot;A conceptual illustration of artificial intelligence as a tree with circuit-board branches and glowing data leaves&quot;
  }
}&#x27;</code></pre>
<img src="https://pub-04a6d208d361438ea01b797e6973bd19.r2.dev/catalog/recraft__recraftv4-1-pro/editorial-illustration.png" alt="Editorial Illustration">
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>string</td><td>Required.</td></tr><tr><td><code>size</code></td><td>string</td><td></td></tr><tr><td><code>style</code></td><td>string</td><td></td></tr><tr><td><code>substyle</code></td><td>string</td><td></td></tr><tr><td><code>controls</code></td><td>object</td><td></td></tr><tr><td><code>controls.colors</code></td><td>array</td><td></td></tr><tr><td><code>controls.colors[].rgb</code></td><td>array</td><td>Required.</td></tr><tr><td><code>controls.background_color</code></td><td>object</td><td></td></tr><tr><td><code>controls.background_color.rgb</code></td><td>array</td><td>Required.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>image</code></td><td>string</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/recraft/recraftv4-1-pro/schema-input.json)
- [Output schema](/ai/models/recraft/recraftv4-1-pro/schema-output.json)

