---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/
  description: Amazon Cognito in Zero Trust integrations.
  full_title: Amazon Cognito · Cloudflare One docs
  head_html: <title>Amazon Cognito · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Amazon Cognito in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/index.md"><meta property="og:title" content="Amazon Cognito · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Amazon Cognito in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="AWS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/#page","headline":"Amazon Cognito \u00b7 Cloudflare One docs","description":"Amazon Cognito in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/awscognito-oidc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AWS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/awscognito-oidc/
  schema: 1
---
<p>Amazon Cognito provides SSO identity management for end users of web and mobile apps. You can integrate Amazon Cognito as an OIDC identity provider for Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An Amazon Cognito <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-user-pool.html">user pool</a></li>
</ul>
<h2 id="set-up-amazon-cognito-oidc">Set up Amazon Cognito (OIDC)</h2>
<h3 id="1-obtain-amazon-cognito-settings"><ol>
<li>Obtain Amazon Cognito settings</li>
</ol></h3>
<p>The following Amazon Cognito values are required to set up the integration:</p>
<ul>
<li>App (client) ID</li>
<li>Client secret</li>
<li>Auth URL</li>
<li>Token URL</li>
<li>Certificate (key) URL</li>
</ul>
<p>To retrieve those values:</p>
<ol>
<li>
<p>Log in to your Amazon Cognito admin portal.</p>
</li>
<li>
<p>Go to <strong>User pools</strong> and select your user pool.</p>
</li>
<li>
<p>Select the <strong>App integration</strong> tab.</p>
</li>
<li>
<p>Under <strong>Domain</strong>, copy your user pool domain or <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html">configure a new domain</a>.</p>
</li>
<li>
<p>Make note of the following <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints.html">Amazon Cognito OIDC endpoints</a>:</p>
<ul>
<li><strong>Auth URL</strong>: <code>https://&lt;your user pool domain&gt;/oauth2/authorize</code></li>
<li><strong>Token URL</strong>: <code>https://&lt;your user pool domain&gt;/oauth2/token</code></li>
<li><strong>Certificate (key) URL</strong>: <code>https://cognito-idp.&lt;region&gt;.amazonaws.com/&lt;your user pool ID&gt;/.well-known/jwks.json</code> (This is the <strong>Token signing key URL</strong> shown in <strong>User pool overview</strong>.)</li>
</ul>
</li>
<li>
<p>Under <strong>App client list</strong>, select <strong>Create app client</strong>.</p>
</li>
<li>
<p>For <strong>App type</strong>, select <strong>Confidential client</strong>.</p>
</li>
<li>
<p>Enter an <strong>App client name</strong> for your application.</p>
</li>
<li>
<p>Ensure that <strong>Generate a client secret</strong> is selected.</p>
</li>
<li>
<p>Configure the following <strong>Hosted UI settings</strong>:</p>
<ol>
<li>In <strong>Allowed callback URLs</strong>, add the following URL:</li>
</ol>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre tabindex="0"><code>   You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;&#10;&#10;2. Select **Identity providers** to use with this app client. At minimum, enable **Cognito user pool** as a provider.&#10;&#10;3. For **OAuth 2.0 grant types**, select **Authorization code grant**.&#10;&#10;4. For **OpenID Connect scopes**, select **OpenID**, **Email**, and **Profile**.&#10;</code></pre>
<ol start="11">
<li>
<p>Select <strong>Create app client</strong>.</p>
</li>
<li>
<p>Next, select the app client you just created.</p>
</li>
<li>
<p>Copy its <strong>Client ID</strong> and <strong>Client secret</strong>.</p>
</li>
</ol>
<h3 id="2-add-amazon-cognito-as-an-identity-provider"><ol start="2">
<li>Add Amazon Cognito as an identity provider</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>OpenID Connect</strong>.</p>
</li>
<li>
<p>Name your identity provider and fill in the required fields with the information obtained from Amazon Cognito.</p>
</li>
<li>
<p>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a> if the protocol is supported by your IdP. PKCE will be performed on all login attempts.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to users' identity.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test</a> that your connection is working, select <strong>Test</strong>.</p>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;auth_url&quot;: &quot;https://&lt;your user pool domain&gt;/oauth2/authorize&quot;,&#10;		&quot;token_url&quot;: &quot;https://&lt;your user pool domain&gt;/oauth2/token&quot;,&#10;		&quot;certs_url&quot;: &quot;https://cognito-idp.&lt;region&gt;.amazonaws.com/&lt;your user pool ID&gt;/.well-known/jwks.json&quot;,&#10;		&quot;scopes&quot;: [&quot;openid&quot;, &quot;email&quot;, &quot;profile&quot;],&#10;		&quot;claims&quot;: [&quot;sub&quot;, &quot;cognito:username&quot;, &quot;name&quot;, &quot;cognito:groups&quot;]&#10;	},&#10;	&quot;type&quot;: &quot;oidc&quot;,&#10;	&quot;name&quot;: &quot;Amazon Cognito example&quot;&#10;}&#10;</code></pre>
