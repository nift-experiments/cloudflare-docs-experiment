---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/
  description: Extract structured JSON data from webpages using AI with the Browser Run /json endpoint.
  full_title: /json - Capture structured data using AI · Cloudflare Browser Run docs
  head_html: <title>/json - Capture structured data using AI · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Extract structured JSON data from webpages using AI with the Browser Run /json endpoint."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/index.md"><meta property="og:title" content="/json - Capture structured data using AI · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Extract structured JSON data from webpages using AI with the Browser Run /json endpoint."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><meta name="pcx_tags" content="JSON"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/#page","headline":"/json - Capture structured data using AI \u00b7 Cloudflare Browser Run docs","description":"Extract structured JSON data from webpages using AI with the Browser Run /json endpoint.","url":"https://developers.cloudflare.com/browser-run/quick-actions/json-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON"]}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/json-endpoint/
  schema: 1
---
<p>The <code>/json</code> endpoint extracts structured data from a webpage. You can specify the expected output using either a <code>prompt</code> or a <code>response_format</code> parameter which accepts a JSON schema. The endpoint returns the extracted data in JSON format.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3630.md")
</aside>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/json&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<p>And at least one of:</p>
<ul>
<li><code>prompt</code> (string), or</li>
<li><code>response_format</code> (object with a JSON Schema)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Extract product info (title, price, availability) or listings (jobs, rentals)</li>
<li>Normalize article metadata (title, author, publish date, canonical URL)</li>
<li>Convert unstructured pages into typed JSON for downstream pipelines</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="with-a-prompt-and-json-schema">With a Prompt and JSON schema</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3634.md")
</div></div>
<h3 id="with-only-a-prompt">With only a prompt</h3>
<p>In this example, only a prompt is provided. The endpoint will use the prompt to extract the data, but the response will not be structured according to a JSON schema.
This is useful for simple extractions where you do not need a specific format.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/json&#x27; \&#10;  &#45;H &#x27;authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;content-type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://developers.cloudflare.com/&quot;,&#10;    &quot;prompt&quot;: &quot;get me the list of AI products&quot;&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;AI Products&quot;: [&#10;			&quot;Build a RAG app&quot;,&#10;			&quot;Workers AI&quot;,&#10;			&quot;Vectorize&quot;,&#10;			&quot;AI Gateway&quot;,&#10;			&quot;AI Playground&quot;&#10;		]&#10;	}&#10;}&#10;</code></pre>
<h3 id="with-only-a-json-schema-no-prompt">With only a JSON schema (no prompt)</h3>
<p>In this case, you supply a JSON schema via the <code>response_format</code> parameter. The schema defines the structure of the extracted data.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/json&#x27; \&#10;  &#45;H &#x27;authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;content-type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;	&quot;url&quot;: &quot;https://developers.cloudflare.com/&quot;,&#10;	&quot;response_format&quot;: {&#10;		&quot;type&quot;: &quot;json_schema&quot;,&#10;		&quot;json_schema&quot;: {&#10;			&quot;type&quot;: &quot;object&quot;,&#10;			&quot;properties&quot;: {&#10;			&quot;products&quot;: {&#10;				&quot;type&quot;: &quot;array&quot;,&#10;				&quot;items&quot;: {&#10;				&quot;type&quot;: &quot;object&quot;,&#10;				&quot;properties&quot;: {&#10;					&quot;name&quot;: {&#10;					&quot;type&quot;: &quot;string&quot;&#10;					},&#10;					&quot;link&quot;: {&#10;					&quot;type&quot;: &quot;string&quot;&#10;					}&#10;				},&#10;				&quot;required&quot;: [&#10;					&quot;name&quot;&#10;				]&#10;				}&#10;			}&#10;			}&#10;		}&#10;    }&#10;  }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;products&quot;: [&#10;			{&#10;				&quot;name&quot;: &quot;Workers&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/workers/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Pages&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/pages/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;R2&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/r2/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Images&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/images/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Stream&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/stream/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Build a RAG app&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/workers-ai/tutorials/build-a-retrieval-augmented-generation-ai/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Workers AI&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/workers-ai/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Vectorize&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/vectorize/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;AI Gateway&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/ai-gateway/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;AI Playground&quot;,&#10;				&quot;link&quot;: &quot;https://playground.ai.cloudflare.com/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Access&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/cloudflare-one/access-controls/policies/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Tunnel&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Gateway&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/cloudflare-one/traffic-policies/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Browser Isolation&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/&quot;&#10;			},&#10;			{&#10;				&quot;name&quot;: &quot;Replace your VPN&quot;,&#10;				&quot;link&quot;: &quot;https://developers.cloudflare.com/learning-paths/replace-vpn/concepts/&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3629.md")
</aside>
<h3 id="using-a-custom-model-byo-api-key">Using a custom model (BYO API Key)</h3>
<p>Browser Run can use a custom model for which you supply credentials. List the model(s) in the <code>custom_ai</code> array:</p>
<ul>
<li><code>model</code> should be formed as <code>&lt;provider&gt;/&lt;model_name&gt;</code> and the provider must be one of these <a href="/ai-gateway/usage/chat-completion/#supported-providers">supported providers</a>.</li>
<li><code>authorization</code> is the bearer token or API key that allows Browser Run to call the provider on your behalf.</li>
</ul>
<p>This example uses the <code>custom_ai</code> parameter to instruct Browser Run to use a Anthropic's Claude Sonnet 4 model. The prompt asks the model to extract the main <code>&lt;h1&gt;</code> and <code>&lt;h2&gt;</code> headings from the target URL and return them in a structured JSON object.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/json&#x27; \&#10;  &#45;H &#x27;authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;content-type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;  &quot;url&quot;: &quot;http://demoto.xyz/headings&quot;,&#10;  &quot;prompt&quot;: &quot;Get the heading from the page in the form of an object like h1, h2. If there are many headings of the same kind then grab the first one.&quot;,&#10;  &quot;response_format&quot;: {&#10;    &quot;type&quot;: &quot;json_schema&quot;,&#10;    &quot;json_schema&quot;: {&#10;      &quot;type&quot;: &quot;object&quot;,&#10;      &quot;properties&quot;: {&#10;        &quot;h1&quot;: {&#10;          &quot;type&quot;: &quot;string&quot;&#10;        },&#10;        &quot;h2&quot;: {&#10;          &quot;type&quot;: &quot;string&quot;&#10;        }&#10;      },&#10;      &quot;required&quot;: [&#10;        &quot;h1&quot;&#10;      ]&#10;    }&#10;  },&#10;  &quot;custom_ai&quot;: [&#10;    {&#10;      &quot;model&quot;: &quot;anthropic/claude-sonnet-4-20250514&quot;,&#10;      &quot;authorization&quot;: &quot;Bearer &lt;ANTHROPIC_API_KEY&gt;&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;h1&quot;: &quot;Heading 1&quot;,&#10;		&quot;h2&quot;: &quot;Heading 2&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="using-a-custom-model-with-fallbacks">Using a custom model with fallbacks</h3>
<p>You may specify multiple models to provide automatic failover. Browser Run will attempt the models in order until one succeeds. To add failover, list additional models in the <code>custom_ai</code> array.</p>
<p>In this example, Browser Run first calls Anthropic's Claude Sonnet 4 model. If that request returns an error, it automatically retries with Meta Llama 3.3 70B from <a href="/workers-ai/">Workers AI</a>, then OpenAI's GPT-4o.</p>
<pre tabindex="0"><code>&quot;custom_ai&quot;: [&#10;  {&#10;    &quot;model&quot;: &quot;anthropic/claude-sonnet-4-20250514&quot;,&#10;    &quot;authorization&quot;: &quot;Bearer &lt;ANTHROPIC_API_KEY&gt;&quot;&#10;  },&#10;  {&#10;    &quot;model&quot;: &quot;workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;    &quot;authorization&quot;: &quot;Bearer &lt;CLOUDFLARE_AUTH_TOKEN&gt;&quot;&#10;  },&#10;{&#10;    &quot;model&quot;: &quot;openai/gpt-4o&quot;,&#10;    &quot;authorization&quot;: &quot;Bearer &lt;OPENAI_API_KEY&gt;&quot;&#10;  }&#10;]&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="json-extraction-returns-null-or-empty-results">JSON extraction returns null or empty results</h3>
<p>If the <code>/json</code> endpoint returns null or empty results:</p>
<ul>
<li><strong>Provide a clear prompt</strong> — Be specific about what data to extract and where it appears on the page (for example, &quot;Extract the product name, price, and description from the main product section&quot;).</li>
<li><strong>Define a response schema</strong> — Use <code>response_format</code> with a JSON schema to enforce the expected output structure.</li>
<li><strong>Use a custom model</strong> — If the default <a href="/workers-ai/">Workers AI</a> model does not produce the desired results, use the <code>custom_ai</code> parameter to specify a different model. Refer to <a href="/browser-run/quick-actions/json-endpoint/#using-a-custom-model-byo-api-key">Using a custom model (BYO API Key)</a> for details.</li>
</ul>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3628.md")
</aside>
<h2 id="troubleshooting-1">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
