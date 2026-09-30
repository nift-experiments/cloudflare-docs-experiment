---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/fine-tunes/public-loras/
  description: Cloudflare offers a few public LoRA adapters that are immediately ready for use.
  full_title: Public LoRA adapters · Cloudflare Workers AI docs
  head_html: <title>Public LoRA adapters · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare offers a few public LoRA adapters that are immediately ready for use."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/fine-tunes/public-loras/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/fine-tunes/public-loras/index.md"><meta property="og:title" content="Public LoRA adapters · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare offers a few public LoRA adapters that are immediately ready for use."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/fine-tunes/public-loras/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workers AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/features/fine-tunes/public-loras/#page","headline":"Public LoRA adapters \u00b7 Cloudflare Workers AI docs","description":"Cloudflare offers a few public LoRA adapters that are immediately ready for use.","url":"https://developers.cloudflare.com/workers-ai/features/fine-tunes/public-loras/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/fine-tunes/public-loras/
  schema: 1
---
<p>Cloudflare offers a few public LoRA adapters that can immediately be used for fine-tuned inference. You can try them out immediately via our <a href="https://playground.ai.cloudflare.com">playground</a>.</p>
<p>Public LoRAs will have the name <code>cf-public-x</code>, and the prefix will be reserved for Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15822.md")
</aside>
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Compatible with</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://huggingface.co/predibase/magicoder">cf-public-magicoder</a></td>
<td>Coding tasks in multiple languages</td>
<td><code>@cf/mistral/mistral-7b-instruct-v0.1</code> <br/> <code>@hf/mistral/mistral-7b-instruct-v0.2</code></td>
</tr>
<tr>
<td><a href="https://huggingface.co/predibase/jigsaw">cf-public-jigsaw-classification</a></td>
<td>Toxic comment classification</td>
<td><code>@cf/mistral/mistral-7b-instruct-v0.1</code> <br/> <code>@hf/mistral/mistral-7b-instruct-v0.2</code></td>
</tr>
<tr>
<td><a href="https://huggingface.co/predibase/cnn">cf-public-cnn-summarization</a></td>
<td>Article summarization</td>
<td><code>@cf/mistral/mistral-7b-instruct-v0.1</code> <br/> <code>@hf/mistral/mistral-7b-instruct-v0.2</code></td>
</tr>
</tbody>
</table>
<p>You can also list these public LoRAs with an API call:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/finetunes/public \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="running-inference-with-public-loras">Running inference with public LoRAs</h2>
<p>To run inference with public LoRAs, you just need to define the LoRA name in the request.</p>
<p>We recommend that you use the prompt template that the LoRA was trained on. You can find this in the HuggingFace repos linked above for each adapter.</p>
<h3 id="curl">cURL</h3>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1 \&#10;  &#45;-header &#x27;Authorization: Bearer {cf_token}&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;Write a python program to check if a number is even or odd.&quot;&#10;      }&#10;    ],&#10;    &quot;lora&quot;: &quot;cf-public-magicoder&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="javascript">JavaScript</h3>
<pre tabindex="0"><code class="language-js">const answer = await env.AI.run(&quot;@cf/mistral/mistral-7b-instruct-v0.1&quot;, {&#10;	stream: true,&#10;	raw: true,&#10;	messages: [&#10;		{&#10;			role: &quot;user&quot;,&#10;			content:&#10;				&quot;Summarize the following: Some newspapers, TV channels and well-known companies publish false news stories to fool people on 1 April. One of the earliest examples of this was in 1957 when a programme on the BBC, the UKs national TV channel, broadcast a report on how spaghetti grew on trees. The film showed a family in Switzerland collecting spaghetti from trees and many people were fooled into believing it, as in the 1950s British people didn&#x27;t eat much pasta and many didn&#x27;t know how it was made! Most British people wouldnt fall for the spaghetti trick today, but in 2008 the BBC managed to fool their audience again with their Miracles of Evolution trailer, which appeared to show some special penguins that had regained the ability to fly. Two major UK newspapers, The Daily Telegraph and the Daily Mirror, published the important story on their front pages.&quot;,&#10;		},&#10;	],&#10;	lora: &quot;cf-public-cnn-summarization&quot;,&#10;});&#10;</code></pre>
