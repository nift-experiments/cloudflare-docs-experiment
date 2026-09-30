---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/
  description: Route Amazon Bedrock requests through AI Gateway for observability and control.
  full_title: Amazon Bedrock · Cloudflare AI Gateway docs
  head_html: <title>Amazon Bedrock · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Route Amazon Bedrock requests through AI Gateway for observability and control."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/index.md"><meta property="og:title" content="Amazon Bedrock · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route Amazon Bedrock requests through AI Gateway for observability and control."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/#page","headline":"Amazon Bedrock \u00b7 Cloudflare AI Gateway docs","description":"Route Amazon Bedrock requests through AI Gateway for observability and control.","url":"https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/usage/providers/bedrock/
  schema: 1
---
<p><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock</a> allows you to build and scale generative AI applications with foundation models.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/aws-bedrock&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>When making requests to Amazon Bedrock, you will need:</p>
<ul>
<li>AI Gateway account ID</li>
<li>AI Gateway gateway name</li>
<li>AWS credentials (<code>accessKeyId</code>, <code>secretAccessKey</code>, and <code>region</code>) with permissions for Amazon Bedrock</li>
<li>The name of the Amazon Bedrock model you want to use</li>
</ul>
<h2 id="url-structure">URL structure</h2>
<p>When making requests to Amazon Bedrock, replace <code>https://bedrock-runtime.us-east-1.amazonaws.com/</code> in the URL you are currently using with <code>https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/aws-bedrock/bedrock-runtime/us-east-1/</code>, then append the model you want to use.</p>
<p>For example, to invoke the Anthropic Claude model in <code>us-east-1</code>:</p>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/aws-bedrock/bedrock-runtime/us-east-1/model/us.anthropic.claude-haiku-4-5-20251001-v1:0/invoke&#10;</code></pre>
<h2 id="authenticating-with-amazon-bedrock">Authenticating with Amazon Bedrock</h2>
<p>Amazon Bedrock uses <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html">AWS Signature Version 4 (SigV4)</a> to authenticate API requests. Unlike providers such as OpenAI or Anthropic that use a simple API key, AWS requires each request to be cryptographically signed with your credentials.</p>
<p>AI Gateway handles this complexity for you. When you store your AWS credentials using BYOK, the gateway automatically signs each request before forwarding it to AWS.</p>
<h3 id="authentication-methods-comparison">Authentication methods comparison</h3>
<table>
<thead>
<tr>
<th>Method</th>
<th><code>cf-aig-authorization</code> header</th>
<th><code>Authorization</code> header</th>
<th>Signing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BYOK (Recommended)</strong></td>
<td><code>Bearer {CF_AIG_TOKEN}</code></td>
<td>Not needed</td>
<td>Gateway signs automatically</td>
</tr>
<tr>
<td><strong>Client-side signing</strong></td>
<td><code>Bearer {CF_AIG_TOKEN}</code></td>
<td>Pre-signed AWS headers</td>
<td>You sign with <code>aws4fetch</code> or AWS SDK</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-confuse-the-headers">Do not confuse the headers</h3>
@markup("md", "content/.markup/bodies/2981.md")
</aside>
<h3 id="option-1-byok-recommended">Option 1: BYOK (Recommended)</h3>
<p>The recommended approach is to store your AWS credentials using AI Gateway's <a href="/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Keys (BYOK)</a> feature. This keeps your credentials secure and eliminates the need for client-side request signing.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>AI</strong> &gt; <strong>AI Gateway</strong> &gt; your gateway &gt; <strong>Provider Keys</strong>.</li>
<li>Select <strong>Add API Key</strong> and choose <strong>Amazon Bedrock</strong> as the provider.</li>
<li>Enter your AWS credentials as a JSON object with the following structure:</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;accessKeyId&quot;: &quot;AKIAIOSFODNN7EXAMPLE&quot;,&#10;	&quot;secretAccessKey&quot;: &quot;wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY&quot;,&#10;	&quot;region&quot;: &quot;us-east-1&quot;&#10;}&#10;</code></pre>
<ol start="4">
<li>Select <strong>Save</strong>.</li>
</ol>
<p>If you are using temporary credentials from AWS STS (for example, from assuming an IAM role), include the <code>sessionToken</code> field:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;accessKeyId&quot;: &quot;ASIAIOSFODNN7EXAMPLE&quot;,&#10;	&quot;secretAccessKey&quot;: &quot;wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY&quot;,&#10;	&quot;region&quot;: &quot;us-east-1&quot;,&#10;	&quot;sessionToken&quot;: &quot;FwoGZXIvYXdzEBY...&quot;&#10;}&#10;</code></pre>
<p>With BYOK configured, you only need to include the <code>cf-aig-authorization</code> header in your requests. AI Gateway handles the AWS SigV4 signing automatically.</p>
<h3 id="option-2-client-side-signing">Option 2: Client-side signing</h3>
<p>If you prefer to sign requests yourself, you can use the <a href="https://github.com/mhart/aws4fetch"><code>aws4fetch</code></a> library or any AWS SDK to sign the request before sending it through AI Gateway. Refer to the <a href="#client-side-signing-with-aws4fetch">client-side signing example</a> below.</p>
<h2 id="examples">Examples</h2>
<h3 id="curl-with-byok">cURL with BYOK</h3>
<p>With your AWS credentials <a href="/ai-gateway/configuration/bring-your-own-keys/">stored as a provider key</a>, requests are simple — no AWS signing required:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/aws-bedrock/bedrock-runtime/us-east-1/model/us.anthropic.claude-haiku-4-5-20251001-v1:0/invoke&quot; \&#10;  &#45;H &quot;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ],&#10;    &quot;max_tokens&quot;: 256,&#10;    &quot;anthropic_version&quot;: &quot;bedrock-2023-05-31&quot;&#10;  }&#x27;&#10;</code></pre>
<h3 id="client-side-signing-with-aws4fetch">Client-side signing with aws4fetch</h3>
<p>If you are not using BYOK, you must sign the request before sending it through AI Gateway. The following example uses the <code>aws4fetch</code> library in a Cloudflare Worker:</p>
<pre tabindex="0"><code class="language-typescript">import { AwsClient } from &quot;aws4fetch&quot;;&#10;&#10;interface Env {&#10;	accessKey: string;&#10;	secretAccessKey: string;&#10;}&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		const cfAccountId = &quot;{account_id}&quot;;&#10;		const gatewayName = &quot;{gateway_id}&quot;;&#10;		const region = &quot;us-east-1&quot;;&#10;&#10;		const awsClient = new AwsClient({&#10;			accessKeyId: env.accessKey,&#10;			secretAccessKey: env.secretAccessKey,&#10;			region: region,&#10;			service: &quot;bedrock&quot;,&#10;		});&#10;&#10;		const body = JSON.stringify({&#10;			messages: [{ role: &quot;user&quot;, content: &quot;What does ethereal mean?&quot; }],&#10;			max_tokens: 256,&#10;			anthropic_version: &quot;bedrock-2023-05-31&quot;,&#10;		});&#10;&#10;		// Sign against the original AWS URL&#10;		const awsUrl = `https://bedrock-runtime.${region}.amazonaws.com/model/us.anthropic.claude-haiku-4-5-20251001-v1:0/invoke`;&#10;&#10;		const presignedRequest = await awsClient.sign(awsUrl, {&#10;			method: &quot;POST&quot;,&#10;			headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;			body: body,&#10;		});&#10;&#10;		// Send through AI Gateway&#10;		const gatewayUrl = `https://gateway.ai.cloudflare.com/v1/${cfAccountId}/${gatewayName}/aws-bedrock/bedrock-runtime/${region}/model/us.anthropic.claude-haiku-4-5-20251001-v1:0/invoke`;&#10;&#10;		const response = await fetch(gatewayUrl, {&#10;			method: &quot;POST&quot;,&#10;			headers: presignedRequest.headers,&#10;			body: body,&#10;		});&#10;&#10;		if (&#10;			response.ok &amp;&amp;&#10;			response.headers.get(&quot;content-type&quot;)?.includes(&quot;application/json&quot;)&#10;		) {&#10;			const data = await response.json();&#10;			return new Response(JSON.stringify(data));&#10;		}&#10;&#10;		return new Response(&quot;Invalid response&quot;, { status: 500 });&#10;	},&#10;};&#10;</code></pre>
<h2 id="use-the-anthropic-messages-api">Use the Anthropic Messages API</h2>
<p>Amazon Bedrock provides an Anthropic-native Messages API through the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/inference-messages-api.html"><code>bedrock-mantle</code> endpoint</a>. AI Gateway passes native Anthropic requests, responses, and server-sent events through without translation.</p>
<p>Configure native Anthropic clients with this base URL:</p>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/&lt;GATEWAY_ID&gt;/aws-bedrock/bedrock-mantle/&lt;AWS_REGION&gt;/anthropic&#10;</code></pre>
<p>The client appends <code>/v1/messages</code> to the base URL. Choose an AWS Region that <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html">supports the <code>bedrock-mantle</code> endpoint</a>, and use a model ID with the <code>anthropic.</code> prefix, such as <code>anthropic.claude-opus-5</code>.</p>
<p>If you use stored AWS credentials, the associated AWS Identity and Access Management (IAM) policy must allow the <code>bedrock-mantle:CreateInference</code> action. AI Gateway signs each request for the <code>bedrock-mantle</code> service.</p>
<p>The following examples call the Messages API with stored AWS credentials or an Amazon Bedrock API key:</p>
<p>Set <code>$ACCOUNT_ID</code>, <code>$GATEWAY_ID</code>, <code>$AWS_REGION</code>, and <code>$CF_AIG_TOKEN</code> before running an example. For the API key example, also set <code>$BEDROCK_API_KEY</code> to an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html">Amazon Bedrock API key</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/2984.md")
</div></div>
<h2 id="using-the-unified-api-openai-compatible">Using the Unified API (OpenAI compatible)</h2>
<p>AI Gateway provides a <a href="/ai-gateway/usage/chat-completion/">Unified API</a> that lets you use the OpenAI chat completions format with Bedrock models. This is currently supported for <strong>Anthropic Claude</strong> and <strong>Amazon Nova</strong> model families. You can use the OpenAI SDK to access these models running on Bedrock without changing your request format.</p>
<p>When you authenticate to Amazon Bedrock with an API key, the Unified API sends requests to <code>us-east-1</code>. When you authenticate with AWS Signature Version 4 (SigV4), it uses the region selected in your stored AWS credentials instead.</p>
<h3 id="endpoint-1">Endpoint</h3>
<pre tabindex="0"><code class="language-txt">https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions&#10;</code></pre>
<h3 id="curl">cURL</h3>
<p>With your AWS credentials <a href="/ai-gateway/configuration/bring-your-own-keys/">stored as a provider key</a>, specify the model using the <code>aws-bedrock/{model}</code> format:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions&quot; \&#10;  &#45;H &quot;cf-aig-authorization: Bearer {CF_AIG_TOKEN}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;aws-bedrock/us.anthropic.claude-haiku-4-5-20251001-v1:0&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h3 id="openai-sdk">OpenAI SDK</h3>
<pre tabindex="0"><code class="language-javascript">import OpenAI from &quot;openai&quot;;&#10;&#10;const client = new OpenAI({&#10;	apiKey: &quot;{CF_AIG_TOKEN}&quot;,&#10;	baseURL:&#10;		&quot;https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat&quot;,&#10;});&#10;&#10;const response = await client.chat.completions.create({&#10;	model: &quot;aws-bedrock/us.anthropic.claude-haiku-4-5-20251001-v1:0&quot;,&#10;	messages: [&#10;		{&#10;			role: &quot;user&quot;,&#10;			content: &quot;What is Cloudflare?&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;console.log(response.choices[0].message.content);&#10;</code></pre>
