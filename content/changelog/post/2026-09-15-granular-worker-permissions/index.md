---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/
  description: New updates and improvements at Cloudflare.
  full_title: Grant teammates and agents access to specific Workers · Changelog
  head_html: <title>Grant teammates and agents access to specific Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Grant teammates and agents access to specific Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/#page","headline":"Grant teammates and agents access to specific Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-15-granular-worker-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-15-granular-worker-permissions/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 15, 2026</time><h2 id="post-title">Grant teammates and agents access to specific Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now grant access to specific Workers and choose from four roles to control the level of access you give teammates, agents, and CI/CD workflows.</p>
<p>Choose from four roles to control the level of access:</p>
<ul>
<li><strong>Metadata Read-Only</strong>: View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.</li>
<li><strong>Content Read-Only</strong>: Read Worker code, settings, and observability data without the ability to modify or deploy changes.</li>
<li><strong>Editor</strong>: Update and deploy a Worker without the ability to delete it.</li>
<li><strong>Admin</strong>: Everything in Editor, plus the ability to delete the Worker.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/individual-worker-permission-roles.png" alt="Permission policy form showing four roles scoped to an individual Worker" /></p>
<p>Worker-level access controls are available today for all customers. You can configure them in the Cloudflare dashboard, through the API, or with Terraform.</p>
<h4 id="roles-designed-for-how-teams-build">Roles designed for how teams build</h4>
<p>Give <strong>Metadata Read-Only</strong> to a debugging agent so it can inspect settings and observability data without seeing Worker code. Give <strong>Content Read-Only</strong> to a code review agent so it can read code without changing it. Give <strong>Editor</strong> to a CI/CD workflow so it can deploy without deleting the Worker or accessing other Workers. <strong>Admin</strong> gives a teammate or agent full control over the Worker, including the ability to delete it.</p>
<p>Apply these roles across all Developer Platform products, across all Workers, or to an individual Worker.</p>
<h4 id="durable-objects">Durable Objects</h4>
<p>You can use granular permissions to control access to Durable Objects. Durable Objects do not have their own roles or scopes. Instead, they inherit the permissions assigned to the Worker that implements them.</p>
<p>Learn more about granular permissions in the <a href="/workers/authorization/durable-objects/">Durable Objects documentation</a>.</p>
<h4 id="grant-access-to-members-and-user-groups">Grant access to members and User Groups</h4>
<p>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and select a <a href="/fundamentals/manage-members/manage/">member</a>. Create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, set the scope to <strong>Individual Workers</strong>, select the Workers they need, and choose a role to grant the right level of access.</p>
<p>If several people on the same team or project need the same access, assign the permission policy to a <a href="/fundamentals/manage-members/user-groups/">User Group</a> instead of each member individually. Everyone added to the group automatically inherits the policy.</p>
<h4 id="create-a-scoped-api-token">Create a scoped API token</h4>
<p>For an agent or CI/CD workflow, go to <strong>Manage Account</strong> &gt; <strong>Account API Tokens</strong> and create an <a href="/fundamentals/api/get-started/account-owned-tokens/">account-owned API token</a>. Set the scope to <strong>Specified Workers</strong>, select the Workers the token can access, and choose a role to grant the right level of access.</p>
<p><img src="/assets/upstream/images/changelog/workers/scoped-worker-api-token-permissions.png" alt="Account API token policy with Metadata Read-Only access scoped to a specific Worker" /></p>
<p>For more information, refer to the <a href="/workers/authorization/workers/">Workers roles and permissions documentation</a>.</p>
</div></article></div>
