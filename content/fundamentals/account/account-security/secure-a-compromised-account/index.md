---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/
  description: If you observe suspicious activity within your Cloudflare account, secure your account with these steps.
  full_title: Secure compromised account · Cloudflare Fundamentals docs
  head_html: <title>Secure compromised account · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="If you observe suspicious activity within your Cloudflare account, secure your account with these steps."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/index.md"><meta property="og:title" content="Secure compromised account · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="If you observe suspicious activity within your Cloudflare account, secure your account with these steps."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/#page","headline":"Secure compromised account \u00b7 Cloudflare Fundamentals docs","description":"If you observe suspicious activity within your Cloudflare account, secure your account with these steps.","url":"https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/account/account-security/secure-a-compromised-account/
  schema: 1
---
<p>If you observe suspicious activity within your Cloudflare account, secure your account with these steps.</p>
<h2 id="step-1-change-your-password">Step 1 - Change your password</h2>
<p>For more guidance on changing your password, refer to <a href="/fundamentals/user-profiles/change-password-or-email/">Change email address or password</a>.</p>
<h2 id="step-2-revoke-active-account-sessions">Step 2 - Revoke active account sessions</h2>
<p>When there is more than one active session associated with your email account, you can revoke any session that is not the current session.</p>
<p>To revoke a session:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>My Profile</strong> &gt; <strong>Sessions</strong>.</li>
<li>On a specific section, click <strong>Revoke</strong>.</li>
<li>You will be prompted to enter your password before revoking the session.</li>
</ol>
<h2 id="step-3-enable-two-factor-authentication-2fa">Step 3 - Enable Two-Factor Authentication (2FA)</h2>
<p>To prevent future compromises, make sure that you have <a href="/fundamentals/user-profiles/2fa/">Two-Factor Authentication (2FA)</a> enabled on your account.</p>
<h2 id="step-4-change-api-keys-and-tokens">Step 4 - Change API keys and tokens</h2>
<h3 id="api-keys">API keys</h3>
<p>If your API key might be compromised, change your API key:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>In the <strong>API Keys</strong> section, find your key.</li>
<li>Select <strong>Change</strong>.</li>
</ol>
<h3 id="api-tokens">API tokens</h3>
<p>If your token is lost or compromised, you can either create a new token or roll your token to generate a new secret. Rolling your API token into a new one will invalidate the previous token, but the access and permissions will be the same as the previous API token. The new token uses the <a href="/fundamentals/api/get-started/token-formats/">scannable format</a>, which allows credential scanning tools to detect leaked tokens.</p>
<p>To roll your API token:</p>
<ol>
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next to the API token you want to roll, select the <strong>three dot icon</strong> &gt; <strong>Roll</strong>.</li>
<li>Select <strong>Confirm</strong> to generate a new API token.</li>
</ol>
<h2 id="step-5-review-the-audit-log">Step 5 - Review the audit log</h2>
<p>To access audit logs in the Cloudflare dashboard:</p>
<p>In the Cloudflare dashboard, go to the <strong>Audit Logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>You can search these audit logs by user email or domain and filter by date range. To download audit logs, click <strong>Download CSV</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8940.md")
</aside>
<p>If you notice any settings were changed, you should undo those changes.</p>
