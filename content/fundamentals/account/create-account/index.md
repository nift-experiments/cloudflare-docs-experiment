---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/account/create-account/
  description: Learn how to create a new Cloudflare account.
  full_title: Create account · Cloudflare Fundamentals docs
  head_html: <title>Create account · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to create a new Cloudflare account."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/account/create-account/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/account/create-account/index.md"><meta property="og:title" content="Create account · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to create a new Cloudflare account."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/account/create-account/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/account/create-account/#page","headline":"Create account \u00b7 Cloudflare Fundamentals docs","description":"Learn how to create a new Cloudflare account.","url":"https://developers.cloudflare.com/fundamentals/account/create-account/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/account/create-account/
  schema: 1
---
<p>To create your first Cloudflare account:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8933.md")
</div>
<p>Once you create your account, Cloudflare will automatically send an email to your address to <a href="/fundamentals/user-profiles/verify-email-address/">verify that email address</a>.</p>
<h2 id="create-an-additional-free-account">Create an additional Free account</h2>
<p>Existing users can create additional Free accounts in the dashboard or with the API.</p>
<h3 id="eligibility">Eligibility</h3>
<p>The following requirements apply to Free account creation:</p>
<ul>
<li>Your Cloudflare user must be active and at least seven days old.</li>
<li>You must have the Super Administrator role on an existing account.</li>
<li>You can create up to five additional Free accounts.</li>
</ul>
<h3 id="create-an-account-in-the-dashboard">Create an account in the dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8934.md")
</div>
<h3 id="create-an-account-with-the-api">Create an account with the API</h3>
<p>Use a user-owned API token or OAuth access token. Account-owned API tokens cannot create accounts.</p>
<p>A user-owned API token requires the <strong>User Details Read</strong> permission. An OAuth access token requires the <code>user-details.read</code> scope.</p>
<p>Set the <code>standalone</code> field to <code>true</code> and omit <code>unit</code>. Every Free account creation request requires exactly one valid <code>Idempotency-Key</code> header. Reuse the same key when retrying the same request.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8937.md")
</div></div>
<p>For the complete request schema, refer to <a href="/api/resources/accounts/methods/create/">Create Account</a>.</p>
<h3 id="resolve-account-creation-errors">Resolve account creation errors</h3>
<p>Use the error message to resolve common account creation failures:</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Your user is less than seven days old.</td>
<td>Wait until the user is at least seven days old.</td>
</tr>
<tr>
<td>You are not a Super Administrator.</td>
<td>Confirm that you have the Super Administrator role on an existing account.</td>
</tr>
<tr>
<td>You reached an account creation limit.</td>
<td>Use an existing account or contact your account team.</td>
</tr>
<tr>
<td>Account creation is temporarily unavailable.</td>
<td>Retry the request later with the same idempotency key.</td>
</tr>
<tr>
<td>The idempotency key was used for a different request.</td>
<td>Use a new key for the new request. Reuse the original key only for an identical retry.</td>
</tr>
<tr>
<td>Your user is suspended.</td>
<td>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</td>
</tr>
</tbody>
</table>
<h2 id="account-name">Account name</h2>
<p>Your account name defaults to <code>&lt;&lt;YOUR_EMAIL_ADDRESS&gt;&gt;'s Account</code>.</p>
<p>You may want to customize the name of this account, either to help specify its purpose or to help associate it with multiple accounts.</p>
<p>To change your account name:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configurations</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For <strong>Account Name</strong>, select <strong>Change Name</strong>.</li>
<li>Enter a new account name.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="best-practices">Best practices</h2>
<p>If you are creating an account for your team or a business, we recommend choosing an email alias or distribution list for your <strong>Email</strong>, such as <code>cloudflare@example.com</code>.</p>
<p>This email address is the main point of contact for your Cloudflare billing, usage notifications, and account recovery.</p>
<p>Refer to <a href="/fundamentals/reference/best-practices/">Account and domain management best practices</a> for a detailed list of ways to protect your account and domain.</p>
<p>Once you <a href="/fundamentals/account/">set up an account</a>, you have several ways to interact with Cloudflare.</p>
<h2 id="interact-with-cloudflare">Interact with Cloudflare</h2>
<p>If you prefer working without code, you can manage your account and domain settings through the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8932.md")
</aside>
<p>For those who prefer to interact with Cloudflare programmatically, you can use several methods:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Docs</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/fundamentals/api/">Cloudflare API</a></td>
<td><a href="/api/">API docs</a></td>
<td>RESTful API based on HTTPS requests and JSON responses.</td>
</tr>
<tr>
<td><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform</a></td>
<td><a href="/terraform/">Terraform docs</a></td>
<td>Configure Cloudflare using HashiCorp's Infrastructure as Code tool, Terraform.</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/cloudflare-go">cloudflare-go</a></td>
<td><a href="https://github.com/cloudflare/cloudflare-go#readme">README</a></td>
<td>The official Go library for the Cloudflare API.</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a></td>
<td><a href="https://github.com/cloudflare/cloudflare-typescript#readme">README</a></td>
<td>The official TypeScript library for the Cloudflare API.</td>
</tr>
<tr>
<td><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a></td>
<td><a href="https://github.com/cloudflare/cloudflare-python#readme">README</a></td>
<td>The official Python library for the Cloudflare API.</td>
</tr>
</tbody>
</table>
