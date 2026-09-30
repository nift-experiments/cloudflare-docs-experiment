---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/manage-members/manage/
  description: Add, edit, and remove Cloudflare account members and their permission policies.
  full_title: Manage account members · Cloudflare Fundamentals docs
  head_html: <title>Manage account members · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Add, edit, and remove Cloudflare account members and their permission policies."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/manage-members/manage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/manage-members/manage/index.md"><meta property="og:title" content="Manage account members · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add, edit, and remove Cloudflare account members and their permission policies."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/manage-members/manage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/manage-members/manage/#page","headline":"Manage account members \u00b7 Cloudflare Fundamentals docs","description":"Add, edit, and remove Cloudflare account members and their permission policies.","url":"https://developers.cloudflare.com/fundamentals/manage-members/manage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/manage-members/manage/
  schema: 1
---
<p>Granting access to others on your account is done with several sets of data principles:</p>
<ol>
<li>Accounts have Account Members.</li>
<li>Account Members have policies.</li>
<li>Policies are constructed out of actors, roles, and scopes.</li>
</ol>
<p>When assigning a new user, you can assign a policy to them directly. If multiple policies are needed, they can be added or revoked at a later time.</p>
<p>Learn how to add new account members, edit or revoke their access, and resend verification emails.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8866.md")
</aside>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/492e46e01d4db17c302f8d10278ab3d8/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F57def76d-110a-419e-a7e4-9278829d6800%2Fpublic" title="Manage account members" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="view-account-members">View account members</h2>
<p>To manage account members, you must have a role of <strong>Super Administrator</strong> and have a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8869.md")
</div></div>
<h2 id="add-account-members">Add account members</h2>
<p>To manage account members, you must have a role of <strong>Super Administrator</strong> and have a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8872.md")
</div></div>
<h2 id="edit-member-permissions">Edit member permissions</h2>
<p>To manage account members, you must have a role of <strong>Super Administrator</strong> and have a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8875.md")
</div></div>
<h2 id="resend-an-invitation">Resend an invitation</h2>
<p>If you invited a member to your account but they cannot find the invitation or the invitation expires, you can resend the invitation through the Cloudflare dashboard:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select your account<sup><a href="#footnote-fundamentals-resend-member-invitation-mdx-1">1</a></sup>.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Members</strong>.</li>
<li>Select a member record where their <strong>Status</strong> is <strong>Invite Pending</strong>.</li>
<li>Select <strong>Resend invite</strong>.</li>
</ol>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-fundamentals-resend-member-invitation-mdx-1">To manage account members, you must have a role of **Super Administrator** and have a [verified email address](/fundamentals/user-profiles/verify-email-address/).</li></ol></section>
<h2 id="remove-account-members">Remove account members</h2>
<p>To manage account members, you must have a role of <strong>Super Administrator</strong> and have a <a href="/fundamentals/user-profiles/verify-email-address/">verified email address</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8878.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8864.md")
</aside>
<h2 id="super-administrator-access">Super Administrator access</h2>
<p>If you are a Super Administrator for an account that has existing domains and you decide to leave the account, you can invite a new Super Administrator who will have access to the same account privileges.</p>
<p>You can delete your user as a Super Administrator, but you cannot delete your account. Other Super Administrators will continue to have access to the appropriate privileges to manage the account, including billing information.</p>
