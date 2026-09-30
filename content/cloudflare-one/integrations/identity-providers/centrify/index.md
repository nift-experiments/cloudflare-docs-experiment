---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/
  description: Centrify in Zero Trust integrations.
  full_title: Centrify · Cloudflare One docs
  head_html: <title>Centrify · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Centrify in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/index.md"><meta property="og:title" content="Centrify · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Centrify in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="OIDC,SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/#page","headline":"Centrify \u00b7 Cloudflare One docs","description":"Centrify in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/centrify/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["OIDC","SSO"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/centrify/
  schema: 1
---
<p>Centrify secures access to infrastructure, DevOps, cloud, and other modern enterprise so you can prevent the number one cause of breaches: privileged access abuse.</p>
<h2 id="set-up-centrify-as-an-oidc-provider">Set up Centrify as an OIDC provider</h2>
<h3 id="1-create-an-application-in-centrify"><ol>
<li>Create an application in Centrify</li>
</ol></h3>
<ol>
<li>
<p>Log in to the Centrify administrator panel.</p>
</li>
<li>
<p>Select <strong>Apps</strong>.</p>
</li>
<li>
<p>Select <strong>Add Web Apps</strong>.</p>
</li>
<li>
<p>Select the <strong>Custom</strong> tab, then select <strong>Add OpenID Connect</strong>.</p>
</li>
<li>
<p>On the <strong>Add Web App</strong> screen, select <strong>Yes</strong> to create an OpenID Connect application.</p>
</li>
<li>
<p>Enter an <strong>Application ID</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/centrify/centrify-4.png" alt="Centrify Settings with Application ID added" /></p>
<ol start="7">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Trust</strong> in the <strong>Settings</strong> menu.</p>
</li>
<li>
<p>Enter a strong application secret on the <strong>Trust</strong> section.</p>
</li>
<li>
<p>Under <strong>Service Provider Configuration</strong> enter your application's authentication domain as the resource application URL.</p>
</li>
<li>
<p>Under <strong>Authorized Redirect URIs</strong>, select <strong>Add</strong>.</p>
</li>
<li>
<p>Under <strong>Authorized Redirect URIs</strong>, enter the following URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre tabindex="0"><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-one/identity/centrify/centrify-6.png" alt="Centrify Trust Identity Provider Configuration with team domain and callback" /></p>
<ol start="13">
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>Copy the following values:</p>
</li>
</ol>
<ul>
<li><strong>Client ID</strong></li>
<li><strong>Client Secret</strong></li>
<li><strong>OpenID Connect Issuer URL</strong></li>
<li><strong>Application ID</strong> from the <strong>Settings</strong> tab</li>
</ul>
<ol start="15">
<li>
<p>Go to the <strong>User Access</strong> tab.</p>
</li>
<li>
<p>Select the roles to grant access to your application.</p>
</li>
</ol>
<h3 id="2-add-centrify-to-cloudflare-one"><ol start="2">
<li>Add Centrify to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Paste in the <strong>Client ID</strong>, <strong>Client Secret</strong>, <strong>Centrify account URL</strong> and <strong>Application ID</strong>.</p>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, enter <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> that you wish to add to your users' identity.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to the identity provider you want to test.</p>
<h2 id="example-api-config">Example API Config</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;centrify_account&quot;: &quot;https://abc123.my.centrify.com/&quot;,&#10;		&quot;centrify_app_id&quot;: &quot;exampleapp&quot;&#10;	},&#10;	&quot;type&quot;: &quot;centrify&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
