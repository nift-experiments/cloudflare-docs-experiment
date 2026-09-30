---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/
  description: Google in Zero Trust integrations.
  full_title: Google · Cloudflare One docs
  head_html: <title>Google · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Google in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/index.md"><meta property="og:title" content="Google · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Google in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Google"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/#page","headline":"Google \u00b7 Cloudflare One docs","description":"Google in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/google/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Google"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/google/
  schema: 1
---
<p>You can integrate Google authentication with Cloudflare Access without a Google Workspace account. The integration allows any user with a Google account to log in (if the <a href="/cloudflare-one/access-controls/policies/">Access policy</a> allows them to reach the resource). Unlike the instructions for <a href="/cloudflare-one/integrations/identity-providers/google-workspace/">Google Workspace</a>, the steps below will not allow you to pull group membership information from a Google Workspace account.</p>
<p>You do not need to be a Google Cloud Platform user to integrate Google as an identity provider with Cloudflare One. You will only need to open the Google Cloud Platform to configure IdP integration settings.</p>
<h2 id="set-up-google-as-an-identity-provider">Set up Google as an identity provider</h2>
<ol>
<li>
<p>Log in to the Google Cloud Platform <a href="https://console.cloud.google.com/">console</a>. Create a new project, name the project, and select <strong>Create</strong>.</p>
</li>
<li>
<p>On the project home page, go to <strong>APIs &amp; Services</strong> and on the sidebar select <strong>Credentials</strong>.</p>
</li>
<li>
<p>Select <strong>Configure Consent Screen</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/google/configure-consent-screen.png" alt="Location to configure a Consent Screen in the Google Cloud Platform console." /></p>
<ol start="4">
<li>
<p>To configure the consent screen:</p>
<ol>
<li>Select <strong>Get started</strong>.</li>
<li>Enter an <strong>App name</strong> and a <strong>User support email</strong>.</li>
<li>Choose <strong>External</strong> as the Audience Type. Since this application is not being created in a Google Workspace account, any user with a Gmail address can log in.</li>
<li>Enter your <strong>Contact Information</strong>. Google Cloud Platform requires an email in your account.</li>
<li>Agree to Google's user data policy and select <strong>Continue</strong>.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
</li>
<li>
<p>The OAuth overview page will load. On the OAuth overview screen, select <strong>Create OAuth client</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/google/create-oauth-client.png" alt="Location to create an OAuth client in the Google Cloud Platform console." /></p>
<ol start="6">
<li>
<p>Choose <em>Web application</em> as the <strong>Application type</strong> and give your OAuth Client ID a name.</p>
</li>
<li>
<p>Under <strong>Authorized JavaScript origins</strong>, in the <strong>URIs</strong> field, enter your team domain:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="8">
<li>Under <strong>Authorized redirect URIs</strong>, in the <strong>URIs</strong> field, enter the following URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="9">
<li>
<p>After creating the OAuth client, select the OAuth client that you just created. Google will present the <strong>OAuth Client ID</strong> value and <strong>Client secret</strong> value. The client secret field functions like a password and should not be shared. Copy both the <strong>OAuth Client ID</strong> value and <strong>Client secret</strong> value.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>. Choose <strong>Google</strong> on the next page.</p>
</li>
<li>
<p>Input the Client ID (<strong>App ID</strong> in the Cloudflare dashboard) and Client Secret fields generated previously.</p>
</li>
<li>
<p>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a>. PKCE will be performed on all login attempts.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="test-your-connection">Test your connection</h2>
<p>To test that your connection is working, go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and select <strong>Test</strong> next to Google.</p>
<h2 id="example-api-config">Example API Config</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;&#10;	},&#10;	&quot;type&quot;: &quot;google&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="error-401-deleted-client"><code>Error 401: deleted_client</code></h3>
<p>If you deleted the OAuth client (or the OAuth client expired) in Google, you will receive a <code>Error 401: deleted_client</code> authorization error.</p>
<p>To fix this issue, complete steps 6 through 12 in the <a href="/cloudflare-one/integrations/identity-providers/google/#set-up-google-as-an-identity-provider">Google</a> guide and steps 9 through 15 in the <a href="/cloudflare-one/integrations/identity-providers/google/#set-up-google-as-an-identity-provider">Google Workspace</a> guide.</p>
