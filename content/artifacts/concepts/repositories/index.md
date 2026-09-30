---
cp9:
  canonical: https://developers.cloudflare.com/artifacts/concepts/repositories/
  description: Understand repository identity, APIs, and scope.
  full_title: Repositories · Cloudflare Artifacts docs
  head_html: <title>Repositories · Cloudflare Artifacts docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand repository identity, APIs, and scope."><link rel="canonical" href="https://developers.cloudflare.com/artifacts/concepts/repositories/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/artifacts/concepts/repositories/index.md"><meta property="og:title" content="Repositories · Cloudflare Artifacts docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand repository identity, APIs, and scope."><meta property="og:url" content="https://developers.cloudflare.com/artifacts/concepts/repositories/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Artifacts"><meta name="algolia_product_filter" content="Artifacts"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Artifacts"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/artifacts/concepts/repositories/#page","headline":"Repositories \u00b7 Cloudflare Artifacts docs","description":"Understand repository identity, APIs, and scope.","url":"https://developers.cloudflare.com/artifacts/concepts/repositories/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /artifacts/concepts/repositories/
  schema: 1
---
<p>Artifacts stores work in repositories. A repository is one isolated Git service with its own history, refs, remote URL, tokens, and durable state.</p>
<p>Every repo lives inside one namespace. If the namespace does not exist yet, Artifacts creates it when you create the first repo in it.</p>
<p>The namespace groups related repositories, and the repository name identifies one repository inside that group.</p>
<h2 id="understand-repository-identity">Understand repository identity</h2>
<p>A repository has three identifiers:</p>
<ul>
<li>a namespace name</li>
<li>a repository name</li>
<li>a repository ID returned by the APIs</li>
</ul>
<p>The namespace and repository name form the stable address that you use in the Workers binding, the REST API, and the Git remote. The repository ID is useful when you need an opaque identifier in API responses or logs.</p>
<p>Each repository is isolated from other repositories. Tokens, lifecycle, refs, and mutations apply to that repository only.</p>
<h2 id="understand-the-repository-apis">Understand the repository APIs</h2>
<p>Artifacts exposes the same repository through three interfaces:</p>
<table>
<thead>
<tr>
<th>Interface</th>
<th>What you use it for</th>
<th>What it returns</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers binding</td>
<td>Create, list, import, inspect, fork, delete, and mint tokens from a Worker</td>
<td>Repository metadata, repository handles, and repo-scoped token results</td>
</tr>
<tr>
<td>REST API</td>
<td>Create, list, import, inspect, fork, delete, and mint tokens from external systems</td>
<td>Cloudflare API responses with repository metadata and token results</td>
</tr>
<tr>
<td>Git protocol</td>
<td>Clone, fetch, pull, and push repository contents</td>
<td>Standard Git behavior over HTTPS</td>
</tr>
</tbody>
</table>
<p>These interfaces point to the same repository.</p>
<p>For example, you can create a repository from the <a href="/artifacts/api/workers-binding/">Workers binding</a> or the <a href="/artifacts/api/rest-api/">REST API</a>, then hand the returned <code>remote</code> URL to a standard Git client. You do not create different repositories for each interface.</p>
<h2 id="understand-how-the-interfaces-relate">Understand how the interfaces relate</h2>
<p>The Workers binding and the REST API are control-plane interfaces. Use them to manage repositories and tokens.</p>
<p>The Git protocol is the data-plane interface. Use it to read and write commits, trees, and refs through a normal Git workflow.</p>
<p>That split leads to a common pattern:</p>
<ol>
<li>Use the Workers binding or REST API to create a repository.</li>
<li>Read back the repository <code>remote</code> URL.</li>
<li>Mint a repo-scoped token.</li>
<li>Use the <code>remote</code> and token with <code>git clone</code>, <code>git fetch</code>, <code>git pull</code>, or <code>git push</code>.</li>
</ol>
<h2 id="understand-repository-scope">Understand repository scope</h2>
<p>Repository scope matters in two places: naming and access.</p>
<h3 id="name-inside-a-namespace">Name inside a namespace</h3>
<p>Repository names are unique within a namespace, not across your whole account. You can reuse a short repository name in different namespaces when that helps your environment or tenant layout.</p>
<p>For example, a repository named <code>app</code> can exist in both the <code>prod</code> namespace and the <code>staging</code> namespace.</p>
<h3 id="token-inside-a-repository">Token inside a repository</h3>
<p>Artifacts tokens are repo-scoped. A token minted for one repository does not grant access to another repository, even when both repositories live in the same namespace.</p>
<p>Use <code>read</code> tokens for clone, fetch, and pull. Use <code>write</code> tokens only when a client must push changes.</p>
<h2 id="use-repositories-as-units-of-work">Use repositories as units of work</h2>
<p>Artifacts works best when you treat each repository as one unit of work.</p>
<p>Use one repository per agent, session, user task, baseline, or fork target when those units need separate history, cleanup, and access control. Use namespaces to group those repositories by environment, tenant, or shard.</p>
<p>For more information, refer to <a href="/artifacts/concepts/namespaces/">Namespaces</a>, <a href="/artifacts/concepts/how-artifacts-works/">How Artifacts works</a>, and <a href="/artifacts/concepts/best-practices/">Best practices for Artifacts</a>.</p>
