---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/
  description: PingOne in Zero Trust integrations.
  full_title: PingOne · Cloudflare One docs
  head_html: <title>PingOne · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="PingOne in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/index.md"><meta property="og:title" content="PingOne · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="PingOne in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="OIDC,SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/#page","headline":"PingOne \u00b7 Cloudflare One docs","description":"PingOne in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/pingone-oidc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["OIDC","SSO"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/pingone-oidc/
  schema: 1
---
<p>The PingOne cloud platform from PingIdentity provides SSO identity management. Cloudflare Access supports PingOne as an OIDC identity provider.</p>
<h2 id="set-up-pingone-as-an-oidc-provider">Set up PingOne as an OIDC provider</h2>
<h3 id="1-create-an-application-in-pingone"><ol>
<li>Create an application in PingOne</li>
</ol></h3>
<ol>
<li>In your PingIdentity environment, go to <strong>Connections</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Add Application</strong>.</li>
<li>Enter an <strong>Application Name</strong>.</li>
<li>Select <strong>OIDC Web App</strong> and then <strong>Save</strong>.</li>
<li>Select <strong>Resource Access</strong> and add the <strong>email</strong> and <strong>profile</strong> scopes.</li>
<li>In the <strong>Configuration</strong> tab, select <strong>General</strong>.</li>
<li>Copy the <strong>Client ID</strong>, <strong>Client Secret</strong>, and <strong>Environment ID</strong> to a safe place. These IDs will be used in a later step to add PingOne to Cloudflare One.</li>
<li>In the <strong>Configuration</strong> tab, select the pencil icon.</li>
<li>In the <strong>Redirect URIs</strong> field, enter the following URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="10">
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="2-add-pingone-to-cloudflare-one"><ol start="2">
<li>Add PingOne to Cloudflare One</li>
</ol></h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</li>
<li>Select <strong>PingOne</strong>.</li>
<li>Input the <strong>Client ID</strong>, <strong>Client Secret</strong>, and <strong>Environment ID</strong> generated previously.</li>
<li>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a>. PKCE will be performed on all login attempts.</li>
<li>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups">Synchronize users and groups</a>.</li>
<li>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to your users' identity.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can now <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test your connection</a> and create <a href="/cloudflare-one/access-controls/policies/">Access policies</a> based on the configured login method.</p>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;ping_env_id&quot;: &quot;&lt;your ping environment id&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;ping&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
