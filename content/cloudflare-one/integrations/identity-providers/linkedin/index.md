---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/
  description: LinkedIn in Zero Trust integrations.
  full_title: LinkedIn · Cloudflare One docs
  head_html: <title>LinkedIn · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="LinkedIn in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/index.md"><meta property="og:title" content="LinkedIn · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="LinkedIn in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="OIDC,SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/#page","headline":"LinkedIn \u00b7 Cloudflare One docs","description":"LinkedIn in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/linkedin/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["OIDC","SSO"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/linkedin/
  schema: 1
---
<p>Cloudflare Access allows your users to use LinkedIn as their identity provider (IdP).</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Sign in to your LinkedIn account before continuing. Configuring LinkedIn as a Cloudflare Access IdP requires a LinkedIn account.</p>
<h2 id="set-up-linkedin-as-an-idp">Set up LinkedIn as an IdP</h2>
<p>To configure LinkedIn as an IdP:</p>
<ol>
<li>
<p>Go to the <a href="https://www.linkedin.com/developers">LinkedIn Developer Portal</a>.</p>
</li>
<li>
<p>Select <strong>Create App</strong>.</p>
</li>
<li>
<p>On the <strong>Create an app</strong> page, enter an <strong>App name</strong> for your application.</p>
</li>
<li>
<p>Select a <strong>LinkedIn Page</strong> for your application or select <strong>Create a new LinkedIn page</strong> if you do not have a LinkedIn page.</p>
</li>
<li>
<p>Select <strong>Upload a logo</strong> and upload your company logo image file.</p>
</li>
<li>
<p>Select <strong>API Terms of Use</strong> to read the terms of use, and agree to the terms.</p>
</li>
<li>
<p>Select <strong>Create app</strong>.</p>
</li>
<li>
<p>In the <strong>Products</strong> tab of your LinkedIn application, select <strong>Request Access</strong> next to the <strong>Sign In with LinkedIn using OpenID Connect</strong> option.</p>
</li>
<li>
<p>In the <strong>Auth</strong> tab of your LinkedIn application, find the <strong>Client ID</strong> and <strong>Client Secret</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/linkedin/lin5.png" alt="LinkedIn account settings where you will copy the Client ID and Client Secret" /></p>
<ol start="10">
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>LinkedIn</strong> as your IdP.</p>
</li>
<li>
<p>In the <strong>App ID</strong> field, copy and paste the <strong>Client ID</strong> from step 9. In the <strong>Client secret</strong> field, copy and paste the <strong>Client secret</strong> from step 9.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
<li>
<p>In the <strong>Auth</strong> tab of your LinkedIn application, go to <strong>OAuth 2.0 settings</strong> and select the pencil icon next to <strong>Authorized redirect URLs for your app</strong>.</p>
</li>
<li>
<p>Enter the following URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre tabindex="0"><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<p>To test that your connection is working, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> &gt; <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to your LinkedIn login method.</p>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;linkedin&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
