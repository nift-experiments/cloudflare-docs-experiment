---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing self-managed OAuth clients · Changelog
  head_html: <title>Introducing self-managed OAuth clients · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing self-managed OAuth clients · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/#page","headline":"Introducing self-managed OAuth clients \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-03-public-oauth-clients/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-03-public-oauth-clients/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 3, 2026</time><h2 id="post-title">Introducing self-managed OAuth clients</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.</p>
<p>OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.</p>
<h4 id="what-is-new">What is new</h4>
<p>Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.</p>
<h4 id="create-an-application">Create an application</h4>
<p>To create an application, go to <strong>Manage account</strong> &gt; <strong>OAuth clients</strong> in your account on the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<h4 id="select-limited-scopes">Select limited scopes</h4>
<p>If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.</p>
<p>Users can review the requested scopes before they consent.</p>
<h4 id="apps-for-both-private-and-public-use">Apps for both private and public use</h4>
<p>Applications start with <code>private</code> visibility. Private applications can only be used by members of the account where the application was created.</p>
<p>To make an application available to any Cloudflare user, complete the prerequisites for <code>public</code> visibility.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients">client visibility</a>.</p>
<h4 id="client-domain-verification">Client domain verification</h4>
<p>Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.</p>
<p>After verification, users see a verified badge on the consent page.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification">domain verification</a>.</p>
<h4 id="learn-more">Learn more</h4>
<p>For more information, refer to <a href="/fundamentals/oauth/">OAuth clients</a>.</p>
</div></article></div>
