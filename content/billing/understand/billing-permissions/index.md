---
cp9:
  canonical: https://developers.cloudflare.com/billing/understand/billing-permissions/
  description: Who can view and manage billing on your Cloudflare account.
  full_title: Billing permissions · Cloudflare Billing docs
  head_html: <title>Billing permissions · Cloudflare Billing docs</title><meta name="generator" content="Nift"><meta name="description" content="Who can view and manage billing on your Cloudflare account."><link rel="canonical" href="https://developers.cloudflare.com/billing/understand/billing-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/billing/understand/billing-permissions/index.md"><meta property="og:title" content="Billing permissions · Cloudflare Billing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Who can view and manage billing on your Cloudflare account."><meta property="og:url" content="https://developers.cloudflare.com/billing/understand/billing-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Billing"><meta name="algolia_product_filter" content="Billing"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/billing/understand/billing-permissions/#page","headline":"Billing permissions \u00b7 Cloudflare Billing docs","description":"Who can view and manage billing on your Cloudflare account.","url":"https://developers.cloudflare.com/billing/understand/billing-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /billing/understand/billing-permissions/
  schema: 1
---
<p>Access to billing features in the Cloudflare dashboard depends on the role assigned to each account member. This page maps each billing action to the required role.</p>
<h2 id="roles-and-billing-capabilities">Roles and billing capabilities</h2>
<table>
<thead>
<tr>
<th>Action</th>
<th>Super Administrator</th>
<th>Administrator</th>
<th>Billing</th>
</tr>
</thead>
<tbody>
<tr>
<td>View invoices and billing history</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Download invoice PDFs</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>View billable usage dashboard</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Pay an outstanding balance</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Add or update payment methods</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Change billing address</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Change billing email</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Set up budget alerts</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Change or cancel subscriptions</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Upgrade or downgrade a domain plan</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Manage account members and roles</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3382.md")
</aside>
<h2 id="assign-the-billing-role">Assign the Billing role</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Select your account.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Members</strong>.</li>
<li>Select <strong>Invite</strong> to add a new member, or select an existing member to edit their role.</li>
<li>Assign the <strong>Billing</strong> role.</li>
</ol>
<p>For more detail on account roles, refer to <a href="/fundamentals/manage-members/manage/">Manage account members</a>.</p>
<h2 id="api-access-for-billing">API access for billing</h2>
<p>API tokens used for billing endpoints require the <code>Billing Read</code> or <code>Billing Edit</code> permission. To create an API token with billing access:</p>
<ol>
<li>Go to <strong>My Profile</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select <strong>Create Token</strong>.</li>
<li>Use the <strong>Custom token</strong> template.</li>
<li>Under <strong>Permissions</strong>, select <strong>Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Read</strong> (or <strong>Edit</strong>).</li>
</ol>
<p>For full API documentation, refer to the <a href="https://developers.cloudflare.com/api/">Cloudflare API reference</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/manage-members/manage/">Manage account members</a> — Add, remove, and change roles for account members</li>
<li><a href="/fundamentals/api/get-started/create-token/">API tokens</a> — Create tokens with specific permissions</li>
<li><a href="/billing/understand/how-billing-works/">How Cloudflare billing works</a> — Billing lifecycle and charge types</li>
</ul>
