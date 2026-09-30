---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/
  description: Submit human feedback on AI Gateway request logs using the Cloudflare API.
  full_title: Add Human Feedback using API · Cloudflare AI Gateway docs
  head_html: <title>Add Human Feedback using API · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Submit human feedback on AI Gateway request logs using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/index.md"><meta property="og:title" content="Add Human Feedback using API · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Submit human feedback on AI Gateway request logs using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/#page","headline":"Add Human Feedback using API \u00b7 Cloudflare AI Gateway docs","description":"Submit human feedback on AI Gateway request logs using the Cloudflare API.","url":"https://developers.cloudflare.com/ai-gateway/evaluations/add-human-feedback-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/evaluations/add-human-feedback-api/
  schema: 1
---
<p>This guide will walk you through the steps of adding human feedback to an AI Gateway request using the Cloudflare API. You will learn how to retrieve the relevant request logs, and submit feedback using the API.</p>
<p>If you prefer to add human feedback via the dashboard, refer to <a href="/ai-gateway/evaluations/add-human-feedback/">Add Human Feedback</a>.</p>
<h2 id="1-create-an-api-token"><ol>
<li>Create an API Token</li>
</ol></h2>
<ol>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API token</a> with the following permissions:</li>
</ol>
<ul>
<li><code>AI Gateway - Read</code></li>
<li><code>AI Gateway - Edit</code></li>
</ul>
<ol start="2">
<li>Get your <a href="/fundamentals/account/find-account-and-zone-ids/">Account ID</a>.</li>
<li>Using that API token and Account ID, send a <a href="/api/resources/ai_gateway/methods/create/"><code>POST</code> request</a> to the Cloudflare API.</li>
</ol>
<h2 id="2-retrieve-the-cf-aig-log-id"><ol start="2">
<li>Retrieve the <code>cf-aig-log-id</code></li>
</ol></h2>
<p>The <code>cf-aig-log-id</code> is a unique identifier for the specific log entry to which you want to add feedback. Below are two methods to obtain this identifier.</p>
<h3 id="method-1-locate-the-cf-aig-log-id-in-the-request-response">Method 1: Locate the <code>cf-aig-log-id</code> in the request response</h3>
<p>This method allows you to directly find the <code>cf-aig-log-id</code> within the header of the response returned by the AI Gateway. This is the most straightforward approach if you have access to the original API response.</p>
<p>The steps below outline how to do this.</p>
<ol>
<li><strong>Make a Request to the AI Gateway</strong>: This could be a request your application sends to the AI Gateway. Once the request is made, the response will contain various pieces of metadata.</li>
<li><strong>Check the Response Headers</strong>: The response will include a header named <code>cf-aig-log-id</code>. This is the identifier you will need to submit feedback.</li>
</ol>
<p>In the example below, the <code>cf-aig-log-id</code> is <code>01JADMCQQQBWH3NXZ5GCRN98DP</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;status&quot;: &quot;success&quot;,&#10;	&quot;headers&quot;: {&#10;		&quot;cf-aig-log-id&quot;: &quot;01JADMCQQQBWH3NXZ5GCRN98DP&quot;&#10;	},&#10;	&quot;data&quot;: {&#10;		&quot;response&quot;: &quot;Sample response data&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="method-2-retrieve-the-cf-aig-log-id-via-api-get-request">Method 2: Retrieve the <code>cf-aig-log-id</code> via API (GET request)</h3>
<p>If you do not have the <code>cf-aig-log-id</code> in the response body or you need to access it after the fact, you are able to retrieve it by querying the logs using the <a href="/api/resources/ai_gateway/subresources/logs/methods/list/">Cloudflare API</a>.</p>
<p>Send a <code>GET</code> request to get a list of logs and then find a specific ID</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;01JADMCQQQBWH3NXZ5GCRN98DP&quot;,&#10;			&quot;cached&quot;: true,&#10;			&quot;created_at&quot;: &quot;2019-08-24T14:15:22Z&quot;,&#10;			&quot;custom_cost&quot;: true,&#10;			&quot;duration&quot;: 0,&#10;			&quot;id&quot;: &quot;string&quot;,&#10;			&quot;metadata&quot;: &quot;string&quot;,&#10;			&quot;model&quot;: &quot;string&quot;,&#10;			&quot;model_type&quot;: &quot;string&quot;,&#10;			&quot;path&quot;: &quot;string&quot;,&#10;			&quot;provider&quot;: &quot;string&quot;,&#10;			&quot;request_content_type&quot;: &quot;string&quot;,&#10;			&quot;request_type&quot;: &quot;string&quot;,&#10;			&quot;response_content_type&quot;: &quot;string&quot;,&#10;			&quot;status_code&quot;: 0,&#10;			&quot;step&quot;: 0,&#10;			&quot;success&quot;: true,&#10;			&quot;tokens_in&quot;: 0,&#10;			&quot;tokens_out&quot;: 0&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h3 id="method-3-retrieve-the-cf-aig-log-id-via-a-binding">Method 3: Retrieve the <code>cf-aig-log-id</code> via a binding</h3>
<p>You can also retrieve the <code>cf-aig-log-id</code> using a binding, which streamlines the process. Here's how to retrieve the log ID directly:</p>
<pre tabindex="0"><code class="language-js">const resp = await env.AI.run(&#10;	&quot;@cf/meta/llama-3-8b-instruct&quot;,&#10;	{&#10;		prompt: &quot;tell me a joke&quot;,&#10;	},&#10;	{&#10;		gateway: {&#10;			id: &quot;my_gateway_id&quot;,&#10;		},&#10;	},&#10;);&#10;&#10;const myLogId = env.AI.aiGatewayLogId;&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/2850.md")
</aside>
<h2 id="3-submit-feedback-via-patch-request"><ol start="3">
<li>Submit feedback via PATCH request</li>
</ol></h2>
<p>Once you have both the API token and the <code>cf-aig-log-id</code>, you can send a PATCH request to submit feedback.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;feedback&quot;: 1&#10;}&#x27;</code></pre>
<p>If you had negative feedback, adjust the body of the request to be <code>-1</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;feedback&quot;: -1&#10;}&#10;</code></pre>
<h2 id="4-verify-the-feedback-submission"><ol start="4">
<li>Verify the feedback submission</li>
</ol></h2>
<p>You can verify the feedback submission in two ways:</p>
<ul>
<li><strong>Through the <a href="https://dash.cloudflare.com">Cloudflare dashboard </a></strong>: check the updated feedback on the AI Gateway interface.</li>
<li><strong>Through the API</strong>: Send another GET request to retrieve the updated log entry and confirm the feedback has been recorded.</li>
</ul>
