---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/user-profiles/login/
  description: Sign in to the Cloudflare dashboard using email and password, SSO, or social login with Apple, Google, or GitHub.
  full_title: Log in to Cloudflare · Cloudflare Fundamentals docs
  head_html: <title>Log in to Cloudflare · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Sign in to the Cloudflare dashboard using email and password, SSO, or social login with Apple, Google, or GitHub."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/user-profiles/login/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/user-profiles/login/index.md"><meta property="og:title" content="Log in to Cloudflare · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sign in to the Cloudflare dashboard using email and password, SSO, or social login with Apple, Google, or GitHub."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/user-profiles/login/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/user-profiles/login/#page","headline":"Log in to Cloudflare \u00b7 Cloudflare Fundamentals docs","description":"Sign in to the Cloudflare dashboard using email and password, SSO, or social login with Apple, Google, or GitHub.","url":"https://developers.cloudflare.com/fundamentals/user-profiles/login/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/user-profiles/login/
  schema: 1
---
<p>Go to the Cloudflare dashboard and choose your <a href="#sign-in-options">sign-in option</a>.</p>
<div class="nb-dash-button"></div>
<h2 id="sign-in-options">Sign-in options</h2>
<p>Cloudflare offers the following sign-in options:</p>
<h3 id="email-and-password">Email and password</h3>
<p>Enter your email address and password.</p>
<h3 id="single-sign-on-sso">Single Sign-On (SSO)</h3>
<p>If your admin has enabled <a href="/fundamentals/manage-members/dashboard-sso/">enabled SSO</a>, enter your email address.</p>
<h3 id="social-login">Social login</h3>
Social login allows you to sign in with a trusted 3rd party sign in service such as Apple, Google, or GitHub. Social login is only available for accounts with a verified email address, or accounts that signed up via social login initially. If you have additionally configured two-factor authentication on your account, that will be presented in addition to any login and two-factor authentication provided by the social login provider.
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8737.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8736.md")
</aside>
<h4 id="sign-in-with-apple">Sign in with Apple</h4>
<ul>
<li>
<p><strong>Same Cloudflare account email as Apple ID</strong>: You can sign in with either your email and password or sign in with Apple.</p>
</li>
<li>
<p><strong>Different Cloudflare account email as Apple ID</strong>: This option creates a new Cloudflare account. If you want to log in to an existing account, <a href="/fundamentals/user-profiles/change-password-or-email/">change your email address</a> to match the one used for your Apple ID.</p>
</li>
</ul>
<p>If you chose to share your email when creating a Cloudflare account with Apple ID and want to set a password and obtain an API key, go to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> login page and select <strong>Forgot your password?</strong> to trigger a password reset email.</p>
<p>If you have chosen to hide your email when creating a Cloudflare account with Apple ID, resetting your password will not work. You can use the suggested workaround below:</p>
<ol>
<li><a href="/fundamentals/manage-members/manage/#add-account-members">Add a new member to your account</a> using your secondary email address.</li>
<li><a href="/fundamentals/account/create-account/">Register a new Cloudflare account</a> with your secondary email address and set a password.</li>
<li>Access the Cloudflare dashboard with the new user and password to obtain an API key.</li>
</ol>
<p>Changing your Cloudflare account email address will unlink the login credentials with the Apple ID from your Cloudflare account. If you attempt to log in using the same Apple ID after the email is changed, you will create a new Cloudflare account.</p>
<p>If you created your Cloudflare account using Apple Relay and decide to change your Apple ID or email address, you will be unable to retrieve the Cloudflare account and all login options will be permanently lost.</p>
<h4 id="sign-in-with-google">Sign in with Google</h4>
<ul>
<li>
<p><strong>A Cloudflare account has already been created with your Google account's email</strong>: This option is unavailable at this time, but we are working on the capability to link and unlink social login providers to your Cloudflare account.</p>
</li>
<li>
<p>If you select <strong>Sign in with Google</strong> with an email that does not already have a Cloudflare account associated with it, Cloudflare will create a new account and allow you to sign in using <strong>Sign in with Google</strong> option moving forward.</p>
</li>
</ul>
<h4 id="sign-in-with-github">Sign in with GitHub</h4>
<ul>
<li>
<p>Sign in with GitHub uses the <a href="https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/changing-your-primary-email-address">Primary email address</a> which is set on your GitHub account. If you change your primary email address in GitHub, you will not be able to log into your Cloudflare account using GitHub social login.</p>
</li>
<li>
<p>If you select <strong>Sign in with GitHub</strong> with an email that does not already have a Cloudflare account associated with it, Cloudflare will create a new account and allow you to sign in using <strong>Sign in with GitHub</strong> option moving forward.</p>
</li>
</ul>
