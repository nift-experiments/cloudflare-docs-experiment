---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/
  description: OneLogin in Zero Trust integrations.
  full_title: OneLogin · Cloudflare One docs
  head_html: <title>OneLogin · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="OneLogin in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/index.md"><meta property="og:title" content="OneLogin · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="OneLogin in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="OIDC,SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/#page","headline":"OneLogin \u00b7 Cloudflare One docs","description":"OneLogin in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/onelogin-oidc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["OIDC","SSO"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/onelogin-oidc/
  schema: 1
---
<p>OneLogin provides SSO identity management. Cloudflare Access supports OneLogin as an OIDC identity provider.</p>
<h2 id="set-up-onelogin-as-an-oidc-provider">Set up OneLogin as an OIDC provider</h2>
<h3 id="1-create-an-application-in-onelogin"><ol>
<li>Create an application in OneLogin</li>
</ol></h3>
<ol>
<li>
<p>Log in to your OneLogin admin portal.</p>
</li>
<li>
<p>Go to <strong>Applications</strong> &gt; <strong>Applications</strong> and select <strong>Add App</strong>.</p>
</li>
<li>
<p>Search for <code>OIDC</code> and select <strong>OpenId Connect (OIDC)</strong> by OneLogin, Inc.</p>
</li>
<li>
<p>In <strong>Display Name</strong>, enter any name for your application. Select <strong>Save</strong>.</p>
</li>
<li>
<p>Next, go to <strong>Configuration</strong>. In the <strong>Redirect URI</strong> field, enter the following URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="6">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Go to <strong>Access</strong> and choose the <strong>Roles</strong> that can access this application. Select <strong>Save</strong>.</p>
</li>
<li>
<p>Go to <strong>SSO</strong> and select <strong>Show client secret</strong>.</p>
</li>
<li>
<p>Copy the <strong>Client ID</strong> and <strong>Client Secret</strong>.</p>
</li>
</ol>
<h3 id="2-add-onelogin-to-cloudflare-one"><ol start="2">
<li>Add OneLogin to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>OneLogin</strong>.</p>
</li>
<li>
<p>Fill in the following information:</p>
<ul>
<li><strong>Name</strong>: Name your identity provider.</li>
<li><strong>App ID</strong>: Enter your OneLogin client ID.</li>
<li><strong>Client secret</strong>: Enter your OneLogin client secret.</li>
<li><strong>OneLogin account URL</strong>: Enter your OneLogin domain, for example <code>https://&lt;your-domain&gt;.onelogin.com</code>.</li>
</ul>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to your user's identity.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to OneLogin.</p>
<h2 id="example-api-config">Example API Config</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;onelogin_account&quot;: &quot;https://mycompany.onelogin.com&quot;&#10;	},&#10;	&quot;type&quot;: &quot;onelogin&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
