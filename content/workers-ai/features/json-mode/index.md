---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/features/json-mode/
  description: Force Workers AI text generation models to return valid JSON output using response_format or JSON schemas.
  full_title: JSON Mode · Cloudflare Workers AI docs
  head_html: <title>JSON Mode · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="Force Workers AI text generation models to return valid JSON output using response_format or JSON schemas."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/features/json-mode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/features/json-mode/index.md"><meta property="og:title" content="JSON Mode · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Force Workers AI text generation models to return valid JSON output using response_format or JSON schemas."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/features/json-mode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers AI"><meta name="pcx_tags" content="JSON"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers-ai/features/json-mode/#page","headline":"JSON Mode \u00b7 Cloudflare Workers AI docs","description":"Force Workers AI text generation models to return valid JSON output using responseformat or JSON schemas.","url":"https://developers.cloudflare.com/workers-ai/features/json-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON"]}</script>
  markdown: true
  noindex: false
  route: /workers-ai/features/json-mode/
  schema: 1
---
<p>response_format: {
title: &quot;JSON Mode&quot;,
type: &quot;object&quot;,
properties: {
type: {
type: &quot;string&quot;,
enum: [&quot;json_object&quot;, &quot;json_schema&quot;],
},
json_schema: {},
}
}
}`;</p>
<p>&quot;messages&quot;: [
{
&quot;role&quot;: &quot;system&quot;,
&quot;content&quot;: &quot;Extract data about a country.&quot;
},
{
&quot;role&quot;: &quot;user&quot;,
&quot;content&quot;: &quot;Tell me about India.&quot;
}
],
&quot;response_format&quot;: {
&quot;type&quot;: &quot;json_schema&quot;,
&quot;json_schema&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;name&quot;: {
&quot;type&quot;: &quot;string&quot;
},
&quot;capital&quot;: {
&quot;type&quot;: &quot;string&quot;
},
&quot;languages&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;string&quot;
}
}
},
&quot;required&quot;: [
&quot;name&quot;,
&quot;capital&quot;,
&quot;languages&quot;
]
}
}
}`;</p>
<p>&quot;response&quot;: {
&quot;name&quot;: &quot;India&quot;,
&quot;capital&quot;: &quot;New Delhi&quot;,
&quot;languages&quot;: [
&quot;Hindi&quot;,
&quot;English&quot;,
&quot;Bengali&quot;,
&quot;Telugu&quot;,
&quot;Marathi&quot;,
&quot;Tamil&quot;,
&quot;Gujarati&quot;,
&quot;Urdu&quot;,
&quot;Kannada&quot;,
&quot;Odia&quot;,
&quot;Malayalam&quot;,
&quot;Punjabi&quot;,
&quot;Sanskrit&quot;
]
}
}`;</p>
<p>When we want text-generation AI models to interact with databases, services, and external systems programmatically, typically when using tool calling or building AI agents, we must have structured response formats rather than natural language.</p>
<p>Workers AI supports JSON Mode, enabling applications to request a structured output response when interacting with AI models.</p>
<h2 id="schema">Schema</h2>
<p>JSON Mode is compatible with OpenAI’s implementation; to enable add the <code>response_format</code> property to the request object using the following convention:</p>
<pre tabindex="0"><code class="language-json">{&#10;  response_format: {&#10;    title: &quot;JSON Mode&quot;,&#10;    type: &quot;object&quot;,&#10;    properties: {&#10;      type: {&#10;        type: &quot;string&quot;,&#10;        enum: [&quot;json_object&quot;, &quot;json_schema&quot;],&#10;      },&#10;      json_schema: {},&#10;    }&#10;  }&#10;}</code></pre>
<p>Where <code>json_schema</code> must be a valid <a href="https://json-schema.org/">JSON Schema</a> declaration.</p>
<h2 id="json-mode-example">JSON Mode example</h2>
<p>When using JSON Format, pass the schema as in the example below as part of the request you send to the LLM.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;messages&quot;: [&#10;    {&#10;      &quot;role&quot;: &quot;system&quot;,&#10;      &quot;content&quot;: &quot;Extract data about a country.&quot;&#10;    },&#10;    {&#10;      &quot;role&quot;: &quot;user&quot;,&#10;      &quot;content&quot;: &quot;Tell me about India.&quot;&#10;    }&#10;  ],&#10;  &quot;response_format&quot;: {&#10;    &quot;type&quot;: &quot;json_schema&quot;,&#10;    &quot;json_schema&quot;: {&#10;      &quot;type&quot;: &quot;object&quot;,&#10;      &quot;properties&quot;: {&#10;        &quot;name&quot;: {&#10;          &quot;type&quot;: &quot;string&quot;&#10;        },&#10;        &quot;capital&quot;: {&#10;          &quot;type&quot;: &quot;string&quot;&#10;        },&#10;        &quot;languages&quot;: {&#10;          &quot;type&quot;: &quot;array&quot;,&#10;          &quot;items&quot;: {&#10;            &quot;type&quot;: &quot;string&quot;&#10;          }&#10;        }&#10;      },&#10;      &quot;required&quot;: [&#10;        &quot;name&quot;,&#10;        &quot;capital&quot;,&#10;        &quot;languages&quot;&#10;      ]&#10;    }&#10;  }&#10;}</code></pre>
<p>The LLM will follow the schema, and return a response such as below:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;response&quot;: {&#10;    &quot;name&quot;: &quot;India&quot;,&#10;    &quot;capital&quot;: &quot;New Delhi&quot;,&#10;    &quot;languages&quot;: [&#10;      &quot;Hindi&quot;,&#10;      &quot;English&quot;,&#10;      &quot;Bengali&quot;,&#10;      &quot;Telugu&quot;,&#10;      &quot;Marathi&quot;,&#10;      &quot;Tamil&quot;,&#10;      &quot;Gujarati&quot;,&#10;      &quot;Urdu&quot;,&#10;      &quot;Kannada&quot;,&#10;      &quot;Odia&quot;,&#10;      &quot;Malayalam&quot;,&#10;      &quot;Punjabi&quot;,&#10;      &quot;Sanskrit&quot;&#10;    ]&#10;  }&#10;}</code></pre>
<p>As you can see, the model is complying with the JSON schema definition in the request and responding with a validated JSON object.</p>
<h2 id="supported-models">Supported Models</h2>
<p>This is the list of models that now support JSON Mode:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/">@cf/meta/llama-3.3-70b-instruct-fp8-fast</a></li>
<li><a href="/workers-ai/models/llama-3-8b-instruct/">@cf/meta/llama-3-8b-instruct</a></li>
<li><a href="/workers-ai/models/llama-3.1-8b-instruct/">@cf/meta/llama-3.1-8b-instruct</a></li>
<li><a href="/workers-ai/models/hermes-2-pro-mistral-7b/">@hf/nousresearch/hermes-2-pro-mistral-7b</a></li>
<li><a href="/workers-ai/models/deepseek-coder-6.7b-instruct-awq/">@hf/thebloke/deepseek-coder-6.7b-instruct-awq</a></li>
<li><a href="/workers-ai/models/deepseek-r1-distill-qwen-32b/">@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</a></li>
</ul>
<p>We will continue extending this list to keep up with new, and requested models.</p>
<p>Note that Workers AI can't guarantee that the model responds according to the requested JSON Schema. Depending on the complexity of the task and adequacy of the JSON Schema, the model may not be able to satisfy the request in extreme situations. If that's the case, then an error <code>JSON Mode couldn't be met</code> is returned and must be handled.</p>
<p>JSON Mode currently doesn't support streaming.</p>
