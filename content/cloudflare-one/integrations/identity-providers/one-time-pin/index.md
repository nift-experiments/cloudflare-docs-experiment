---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/
  description: One-time PIN login in Zero Trust integrations.
  full_title: One-time PIN login · Cloudflare One docs
  head_html: <title>One-time PIN login · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="One-time PIN login in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/index.md"><meta property="og:title" content="One-time PIN login · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="One-time PIN login in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/#page","headline":"One-time PIN login \u00b7 Cloudflare One docs","description":"One-time PIN login in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/one-time-pin/
  schema: 1
---
<p>Cloudflare Access can send a one-time PIN (OTP) to approved email addresses as an alternative to integrating an identity provider. You can simultaneously configure OTP login and the identity provider of your choice to allow users to select their own authentication method.</p>
<p>New Zero Trust organizations use the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as their default login method. OTP is no longer added automatically, but you can set it up at any time using the following steps.</p>
<p>For example, if your team uses Okta but you are collaborating with someone outside your organization, you can use OTP to grant access to guests.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5031.md")
</aside>
<h2 id="set-up-otp">Set up OTP</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5035.md")
</div></div>
<p>To grant a user access to an application, simply add their email address to an <a href="/cloudflare-one/access-controls/policies/policy-management/#create-a-policy">Access policy</a>.</p>
<h2 id="allow-otp-emails-through-your-email-gateway">Allow OTP emails through your email gateway</h2>
<p>If your email gateway blocks, rate limits, or scans OTP emails, allowlist the sender domain <code>notify.cloudflare.com</code>, the sender address <code>noreply@notify.cloudflare.com</code>, and these IP addresses:</p>
<ul>
<li><code>104.30.16.2</code></li>
<li><code>104.30.16.3</code></li>
<li><code>104.30.16.4</code></li>
<li><code>104.30.16.5</code></li>
<li><code>104.30.16.6</code></li>
<li><code>104.30.16.7</code></li>
</ul>
<h2 id="log-in-with-otp">Log in with OTP</h2>
<p>To log in to Access using the one-time PIN:</p>
<ol>
<li>Go to the application protected by Access.</li>
<li>On the Access login page, enter your email address and select <strong>Send login code</strong>.
<img src="/assets/upstream/images/cloudflare-one/identity/otp/otp1.png" alt="Enter email to sign in with OTP." /></li>
<li>If the email is allowed by an Access policy, you will receive a PIN in your inbox. This secure PIN expires 10 minutes after the initial request.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5030.md")
</aside>
<ol start="4">
<li>Paste the PIN into the Access login page and select <strong>Sign in</strong>.
<img src="/assets/upstream/images/cloudflare-one/identity/otp/otp2.png" alt="Enter PIN to sign in." />
<ul>
<li>If the code was valid, you will be redirected to the application.</li>
<li>If the code was invalid, you will see <strong>That account does not have access.</strong></li>
<li>If you see <strong>This One-Time PIN has already been used</strong>, the code was already consumed. This typically occurs when an email security tool on your network automatically scans the email and follows the link before you enter the code. Select <strong>Request new code</strong> and try again.</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5029.md")
</aside>
<h2 id="otp-behavior-and-limits">OTP behavior and limits</h2>
<p>Keep the following behavior in mind when troubleshooting OTP logins:</p>
<ul>
<li>Each PIN is single-use.</li>
<li>Requesting a new PIN invalidates the previous PIN.</li>
<li>Cloudflare only sends the email if the user is allowed by an Access policy.</li>
<li>Third-party mail security tools may consume the link before the user does, which makes the code appear already used.</li>
</ul>
<p>If users repeatedly fail to sign in, request a fresh code and verify that your mail filtering or link-scanning product is allowlisting <code>noreply@notify.cloudflare.com</code>.</p>
