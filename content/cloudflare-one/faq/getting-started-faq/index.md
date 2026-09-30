---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/
  description: Review FAQs about getting started with Cloudflare Zero Trust.
  full_title: Getting started with Cloudflare Zero Trust FAQ · Cloudflare One docs
  head_html: <title>Getting started with Cloudflare Zero Trust FAQ · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review FAQs about getting started with Cloudflare Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/index.md"><meta property="og:title" content="Getting started with Cloudflare Zero Trust FAQ · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review FAQs about getting started with Cloudflare Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/#page","headline":"Getting started with Cloudflare Zero Trust FAQ \u00b7 Cloudflare One docs","description":"Review FAQs about getting started with Cloudflare Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/faq/getting-started-faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/faq/getting-started-faq/
  schema: 1
---
<p><a href="/cloudflare-one/faq/">❮ Back to FAQ</a></p>
<h2 id="how-do-i-sign-up-for-cloudflare-zero-trust">How do I sign up for Cloudflare Zero Trust?</h2>
<p>You can sign up today on the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>. Go to <strong>Zero Trust</strong>, choose a team name and a payment plan, and start protecting your network in just a few minutes.</p>
<h2 id="what-is-a-team-domain-team-name">What is a team domain/team name?</h2>
<p>Your team domain is a unique subdomain assigned to your Cloudflare account, for example, <code>&lt;your-team-name&gt;.cloudflareaccess.com</code>. <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Setting up a team domain</a> is an essential step in your Zero Trust configuration. This is where your users will find the apps you have secured behind Cloudflare Zero Trust — displayed in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> — and will be able to make login requests to them. The customizable portion of your team domain is called <strong>team name</strong>. You can view your team name and team domain in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Settings</strong>.</p>
<table>
<thead>
<tr>
<th>team name</th>
<th>team domain</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>your-team-name</code></td>
<td><code>&lt;your-team-name&gt;.cloudflareaccess.com</code></td>
</tr>
</tbody>
</table>
<p>You can change your team name at any time, unless you have the Cloudflare dashboard SSO feature enabled on your account. If Cloudflare dashboard SSO is enabled, you must <a href="/fundamentals/manage-members/dashboard-sso/#change-your-zero-trust-team-name">turn off SSO</a> before changing your team name.</p>
<p>When you change your team name, the old name becomes available for other accounts to claim. However, if you delete your entire Zero Trust organization, any team name it used is permanently reserved and cannot be reused by any account — including your own.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4501.md")
</aside>
<h3 id="how-do-i-transfer-a-team-name-to-another-account">How do I transfer a team name to another account?</h3>
<p>If you want to move a team name from one Cloudflare account to another (for example, migrating from a personal account to a company account), you can do so as long as the source Zero Trust organization still exists:</p>
<ol>
<li>In the source account, go to <strong>Settings</strong> and change the team name to a temporary value (for example, <code>mycompany-old</code>).</li>
<li>In the destination account, go to <strong>Settings</strong> and set the team name to the desired value.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4500.md")
</aside>
<h3 id="why-is-my-old-team-name-is-still-showing-up-on-the-login-page-and-app-launcher">Why is my old team name is still showing up on the Login page and App Launcher?</h3>
<p>After changing your team name, you will need to check your Block page, Login page, and App Launcher settings to make sure the new team name is reflected.</p>
<p>To verify that your team name change is successfully rendering on the Block page, Login page and App Launcher:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Custom pages</strong> &gt; <strong>Team name and domain</strong>.</li>
<li>Find the <strong>Account Gateway block page</strong> and <strong>Access login page</strong> sections, then select <strong>Manage</strong> next to the page you would like to review first.</li>
<li>Review that the value in <strong>Your Organization's name</strong> matches your new team name.</li>
<li>If the desired name is not already displayed, change the value to your desired team name and select <strong>Save</strong>.</li>
<li>Check both pages (<strong>Account Gateway block page</strong> and <strong>Access login page</strong> to set <strong>Your Organization's name</strong> as your desired team name.</li>
</ol>
<p>The App Launcher will display the same team name set on the Access login page, so you do not need to update the <strong>Your Organization's name</strong> field in the App Launcher page.</p>
<h2 id="how-do-i-change-my-subscription-plan">How do I change my subscription plan?</h2>
<p>To make changes to your subscription, visit the Billing section under <strong>Zero Trust</strong> &gt; <strong>Settings</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>. You can change or cancel your subscription at any time. Just remember - if you downgrade your plan during a billing cycle, your downgraded pricing will apply in the next billing cycle. If you upgrade during a billing cycle, you will be billed for the upgraded plan at the moment you select it.</p>
<h2 id="how-are-active-seats-measured">How are active seats measured?</h2>
<p>Cloudflare Zero Trust subscriptions consist of seats that users in your account consume. When users authenticate to an application or enroll their agent into the Cloudflare One Client, they count against one of your active seats. Seats can be added, removed, or revoked at <strong>Settings</strong> &gt; <strong>Cloudflare One plan</strong>. If all seats are currently consumed, you must first remove users before decreasing your purchased seat count.</p>
<h3 id="removing-users">Removing users</h3>
<p>User seats can be removed for Access and Gateway at <strong>Team &amp; Resources</strong> &gt; <strong>Users</strong> &gt; <strong>Your users</strong>. Removing a user will have consequences both on Access and on Gateway:</p>
<ul>
<li>
<p><strong>Access</strong>: All active sessions for that user will be invalidated. A user will be able to log back into an application unless you create an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> to block future logins from that user.</p>
</li>
<li>
<p><strong>Gateway</strong>: All active devices for that user will be logged out of your Zero Trust organization, which stops all filtering and routing via the Cloudflare One Client. A user will be able to re-enroll their device unless you create a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">device enrollment policy</a> to block them.</p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4499.md")
</aside>
<h3 id="revoking-users">Revoking users</h3>
<p>The Revoke action will terminate active sessions and log out active devices, but will not remove the user's consumption of an active seat.</p>
<h2 id="how-do-i-know-if-my-network-is-protected-behind-cloudflare-zero-trust">How do I know if my network is protected behind Cloudflare Zero Trust?</h2>
<p>You can visit the <a href="https://help.one.cloudflare.com/">Zero Trust help page</a>. This page will give you an overview of your network details, as well as an overview of the categories that are being blocked and/or allowed.</p>
