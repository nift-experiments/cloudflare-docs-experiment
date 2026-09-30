---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/
  description: New updates and improvements at Cloudflare.
  full_title: Access git commit sha and branch name as environment variables in Workers Builds · Changelog
  head_html: <title>Access git commit sha and branch name as environment variables in Workers Builds · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Access git commit sha and branch name as environment variables in Workers Builds · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/#page","headline":"Access git commit sha and branch name as environment variables in Workers Builds \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-06-10-default-env-vars/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-06-10-default-env-vars/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2025</time><h2 id="post-title">Access git commit sha and branch name as environment variables in Workers Builds</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/ci-cd/builds/">Workers Builds</a> connects your Worker to a <a href="/workers/ci-cd/builds/git-integration/">Git repository</a>, and automates building and deploying your code on each pushed change.</p>
<p>To make CI/CD pipelines even more flexible, Workers Builds now automatically injects <a href="/workers/ci-cd/builds/configuration/#environment-variables">default environment variables</a> into your build process (much like the defaults in <a href="/pages/configuration/build-configuration/#environment-variables">Cloudflare Pages projects</a>). You can use these variables to customize your build process based on the deployment context, such as the branch or commit.</p>
<p>The following environment variables are injected by default:</p>
<table>
<thead>
<tr>
<th>Environment Variable</th>
<th>Injected value</th>
<th>Example use-case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CI</code></td>
<td><code>true</code></td>
<td>Changing build behavior when run on CI versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI</code></td>
<td><code>1</code></td>
<td>Changing build behavior when run on Workers Builds versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI_BUILD_UUID</code></td>
<td><code>&lt;build-uuid-of-current-build&gt;</code></td>
<td>Passing the Build UUID along to custom workflows</td>
</tr>
<tr>
<td><code>WORKERS_CI_COMMIT_SHA</code></td>
<td><code>&lt;sha1-hash-of-current-commit&gt;</code></td>
<td>Passing current commit ID to error reporting, for example, Sentry</td>
</tr>
<tr>
<td><code>WORKERS_CI_BRANCH</code></td>
<td><code>&lt;branch-name-from-push-event</code></td>
<td>Customizing build based on branch, for example, disabling debug logging on <code>production</code></td>
</tr>
</tbody>
</table>
<p>You can override these default values and add your own custom environment variables by navigating to <strong>your Worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment variables</strong>.</p>
<p>Learn more in the <a href="/workers/ci-cd/builds/configuration/#environment-variables">Build configuration documentation</a>.</p>
</div></article></div>
