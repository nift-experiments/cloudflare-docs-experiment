---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/
  description: Understand namespaces, repos, and durability.
  full_title: How Artifacts works · Cloudflare Artifacts docs
  head_html: <title>How Artifacts works · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand namespaces, repos, and durability."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/index.md"><meta property="og:title" content="How Artifacts works · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand namespaces, repos, and durability."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/#page","headline":"How Artifacts works \u00b7 Cloudflare Artifacts docs","description":"Understand namespaces, repos, and durability.","url":"https://developers.cloudflare.com/artifacts/concepts/how-artifacts-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/concepts/how-artifacts-works/
  schema: 1
---
<p>Artifacts creates Git repos on demand. Each repo is an isolated Git service with its own remote URL, tokens, and durable state.</p>
<h2 id="core-model">Core model</h2>
<p>Namespaces are the top-level container for repos. A repo lives inside one namespace, and its name is unique within that namespace.</p>
<p>Artifacts does not provision namespaces separately. When you create the first repo with a new namespace name, Artifacts creates that namespace implicitly.</p>
<p>A namespace provides the naming and routing boundary for repos. Together, the namespace and repo name form the repo's stable address, and API responses also return a repo ID.</p>
<p>Like <a href="/durable-objects/concepts/what-are-durable-objects/">Durable Objects</a>, a repo is a single logical instance that Cloudflare can route to from any region.</p>
<p>Because each repo is isolated, it has its own:</p>
<ul>
<li>Git history and refs</li>
<li>access tokens and remote URL</li>
<li>lifecycle and durable state</li>
</ul>
<p>Repos can be created as needed. This lets Artifacts model many small units of work across separate repos.</p>
<p>Forking follows the same model. A fork creates a new repo that starts from an existing repo's history, then diverges independently with its own tokens, routing, and lifecycle.</p>
<p>Access is also repo-scoped. Each repo has its own tokens, and each token can be limited to a specific level of access:</p>
<ul>
<li><code>read</code> for clone, fetch, pull, indexing, and review</li>
<li><code>write</code> for push and other mutations</li>
</ul>
<p>Your Worker or API layer decides when to mint those tokens. That keeps authentication and authorization outside the repo while still making the repo usable from Workers, the REST API, or any standard Git client.</p>
<h2 id="durability">Durability</h2>
<p>Artifacts is durable by default. A repo does not depend on one process staying alive or on one data center staying available.</p>
<p>Behind the scenes, Cloudflare replicates repo data synchronously across multiple data centers and copies it asynchronously to object storage and snapshots. You do not need to build your own replication, failover, or snapshot pipeline to keep repository state available.</p>
<p>Artifacts handles the Git server lifecycle and storage infrastructure underneath these Git workflows.</p>
<h2 id="learn-more">Learn more</h2>
<p>For repo patterns, refer to <a href="/artifacts/concepts/best-practices/">Best practices for Artifacts</a>. For token behavior, refer to <a href="/artifacts/api/git-protocol/">Git protocol</a>. For product updates, refer to the <a href="/artifacts/platform/changelog/">Artifacts changelog</a>.</p>
