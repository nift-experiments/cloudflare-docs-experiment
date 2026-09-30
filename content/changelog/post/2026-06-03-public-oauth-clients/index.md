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
