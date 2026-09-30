---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/
  description: Identity providers in Zero Trust integrations.
  full_title: Identity providers · Cloudflare One docs
  head_html: <title>Identity providers · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Identity providers in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/index.md"><meta property="og:title" content="Identity providers · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Identity providers in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SSO"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/#page","headline":"Identity providers \u00b7 Cloudflare One docs","description":"Identity providers in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SSO"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/
  schema: 1
---
<p>Cloudflare One integrates with your organization's identity provider to apply Cloudflare One and Secure Web Gateway policies. If you work with partners, contractors, or other organizations, you can integrate multiple identity providers simultaneously.</p>
<p>When you create a new Zero Trust organization, Cloudflare automatically configures the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method. Your users can authenticate with their existing Cloudflare account credentials without any additional setup, and you can add more identity providers at any time.</p>
<p>You can also send a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a> to approved email addresses. No configuration needed — simply add a user's email address to an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> and to the group that allows your team to reach the application. You can configure OTP and an identity provider at the same time to let users choose their own authentication method.</p>
<p>Adding an identity provider as a login method requires configuration both in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong> and with the identity provider itself. Consult our IdP-specific documentation to learn more about what you need to set up.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5044.md")
</aside>
<h2 id="set-up-idps-in-cloudflare-one">Set up IdPs in Cloudflare One</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5047.md")
</div></div>
<p>Your IdP will now be listed in the <strong>Login methods</strong> card.</p>
<h2 id="test-idps-in-cloudflare-one">Test IdPs in Cloudflare One</h2>
<p>To test if an IdP is correctly configured:</p>
<ol>
<li>Go to <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Select <strong>Test</strong> next to the IdP you would like to test. This will attempt to connect to the IdP to verify if a valid connection is established.</li>
</ol>
<h3 id="your-provider-is-connected">Your provider is connected</h3>
<p>If your provider is connected, another window will open in your browser, with this message:</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/connected-idp.png" alt="&quot;Your connection works!&quot; message displayed for a successful IdP test" /></p>
<h3 id="your-provider-is-not-connected">Your provider is not connected</h3>
<p>If your provider is not connected, another window will open in your browser. Along with an error message, you will receive a detailed explanation of why the test has failed.</p>
<h2 id="use-the-api">Use The API</h2>
<p>We recommend that you use our dashboard to configure your identity providers. However, if you would like to use the <a href="https://api.cloudflare.com/">Cloudflare API</a>, each of the identity provider topics covered here include an example API configuration snippet as well.</p>
