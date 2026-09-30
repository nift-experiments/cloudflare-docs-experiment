---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/
  description: New updates and improvements at Cloudflare.
  full_title: One-click Access protection for Workers now creates reusable Cloudflare Access policies · Changelog
  head_html: <title>One-click Access protection for Workers now creates reusable Cloudflare Access policies · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="One-click Access protection for Workers now creates reusable Cloudflare Access policies · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/#page","headline":"One-click Access protection for Workers now creates reusable Cloudflare Access policies \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-03-reusable-access-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-03-reusable-access-policies/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 4, 2025</time><h2 id="post-title">One-click Access protection for Workers now creates reusable Cloudflare Access policies</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers applications now use reusable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policies</a> to reduce duplication and simplify access management across multiple Workers.</p>
<p>Previously, enabling Cloudflare Access on a Worker created per-application policies, unique to each application. Now, we create reusable policies that can be shared across applications:</p>
<ul>
<li>
<p><strong>Preview URLs</strong>: All Workers preview URLs share a single &quot;Cloudflare Workers Preview URLs&quot; policy across your account. This policy is automatically created the first time you enable Access on any preview URL. By sharing a single policy across all preview URLs, you can configure access rules once and have them apply company-wide to all Workers which protect preview URLs. This makes it much easier to manage who can access preview environments without having to update individual policies for each Worker.</p>
</li>
<li>
<p><strong>Production workers.dev URLs</strong>: When enabled, each Worker gets its own reusable policy (named <code>&lt;worker-name&gt; - Production</code>) by default. We recognize production services often have different access requirements and having individual policies here makes it easier to configure service-to-service authentication or protect internal dashboards or applications with specific user groups. Keeping these policies separate gives you the flexibility to configure exactly the right access rules for each production service. When you disable Access on a production Worker, the associated policy is automatically cleaned up if it's not being used by other applications.</p>
</li>
</ul>
<p>This change reduces policy duplication, simplifies cross-company access management for preview environments, and provides the flexibility needed for production services. You can still customize access rules by editing the reusable policies in the Zero Trust dashboard.</p>
<p>To enable Cloudflare Access on your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Workers &amp; Pages</strong>.</li>
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, click <strong>Manage Cloudflare Access</strong> to customize the policy.</li>
</ol>
<p>For more information on configuring Cloudflare Access for Workers, refer to the <a href="/workers/configuration/routing/workers-dev/#manage-access-to-workersdev">Workers Access documentation</a>.</p>
</div></article></div>
