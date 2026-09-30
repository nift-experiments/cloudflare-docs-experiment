---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
  description: Learn how to create a token to perform actions using the Cloudflare API.
  full_title: Create API token · Cloudflare Fundamentals docs
  head_html: <title>Create API token · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to create a token to perform actions using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/get-started/create-token/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/get-started/create-token/index.md"><meta property="og:title" content="Create API token · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to create a token to perform actions using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/get-started/create-token/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/api/get-started/create-token/#page","headline":"Create API token \u00b7 Cloudflare Fundamentals docs","description":"Learn how to create a token to perform actions using the Cloudflare API.","url":"https://developers.cloudflare.com/fundamentals/api/get-started/create-token/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/get-started/create-token/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisite">Prerequisite</h3>
@markup("md", "content/.markup/bodies/9002.md")
</aside>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/4e92423fc9126a22af2b0c37825d4195/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2Fd1f88307-30b6-40e3-c38e-7cec03e5ed00%2Fpublic" title="Create an API token" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<ol>
<li>Determine if you want a user token or an <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API token</a>. Use Account API tokens if you prefer service tokens that are not associated with users and your <a href="/fundamentals/api/get-started/account-owned-tokens/#compatibility-matrix">desired API endpoints are compatible</a>.</li>
<li>From the <a href="https://dash.cloudflare.com/profile/api-tokens/">Cloudflare dashboard</a>, go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong> for user tokens. For Account Tokens, go to <strong>Manage Account</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select <strong>Create Token</strong>.</li>
<li>Select a template from the available <a href="/fundamentals/api/reference/template/">API token templates</a> or create a custom token. The following example uses the <strong>Edit zone DNS</strong> template.</li>
<li>Add or edit the token name to describe why or how the token is used. Templates are prefilled with a token name and permissions.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/api/template-customize.png" alt="Token template overview screen" /></p>
<ol start="6">
<li>Modify the token's permissions. After selecting a permissions group (<em>Account</em>, <em>User</em>, or <em>Zone</em>), choose what level of access to grant the token. Most groups offer <code>Edit</code> or <code>Read</code> options. <code>Edit</code> is full CRUDL (create, read, update, delete, list) access, while <code>Read</code> is the read permission and list where appropriate. Refer to the <a href="/fundamentals/api/reference/permissions/">available token permissions</a> for more information.</li>
<li>Select which resources the token is authorized to access. For example, granting <code>Zone DNS Read</code> access to a zone <code>example.com</code> will allow the token to read DNS records only for that specific zone. Any other zone will return an error for DNS record reads operations. Any other operation on that zone will also return an error.</li>
<li>(Optional) Restrict how a token is used in the <strong>Client IP Address Filtering</strong> and <strong>TTL (time to live)</strong> fields.</li>
<li>Select <strong>Continue to summary</strong>.</li>
<li>Review the token summary. Select <strong>Edit token</strong> to make adjustments. You can also edit a token after creation.</li>
</ol>
<p><img src="/assets/upstream/images/fundamentals/api/token-summary.png" alt="Token summary screen displaying the resources and permissions selected" /></p>
<ol start="11">
<li>Select <strong>Create Token</strong> to generate the token's secret.</li>
<li>Copy the secret to a secure place.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/9001.md")
</aside>
<p><img src="/assets/upstream/images/fundamentals/api/token-complete.png" alt="Token creation completion screen displaying your API token and the curl command to test your token" /></p>
<p>The token secret page also includes an example command to test the token. Use the <code>/user/tokens/verify</code> endpoint to fetch the current status of the given token.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/user/tokens/verify&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>The result:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;100bf38cc8393103870917dd535e0628&quot;,&#10;		&quot;status&quot;: &quot;active&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: [&#10;		{&#10;			&quot;code&quot;: 10000,&#10;			&quot;message&quot;: &quot;This API Token is valid and active&quot;,&#10;			&quot;type&quot;: null&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>New API tokens use the <code>cfut_</code> prefixed <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<p>With this you have successfully created an API token and can start working with the Cloudflare API. After creating your first API token, you can create additional API tokens <a href="/fundamentals/api/how-to/create-via-api/">via the API</a>.</p>
