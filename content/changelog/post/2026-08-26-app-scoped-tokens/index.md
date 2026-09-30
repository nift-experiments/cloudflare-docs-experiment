<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 26, 2026</time><h2 id="post-title">Create app-scoped API tokens for Flagship</h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p>You can now create <strong>app-scoped API tokens</strong> for <a href="/flagship/">Flagship</a>. These tokens grant access only to the Flagship apps you select, instead of every app in the account.</p>
<p>When you create a custom token, open the resource dropdown (it defaults to <strong>Entire Account</strong>) and select <strong>Specified Flagship apps</strong>. Then choose the app and a <strong>Flagship App</strong> permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.</p>
<p>Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.</p>
<p>To create a token, refer to <a href="/flagship/api-tokens/">API tokens</a> or <a href="https://dash.cloudflare.com/?to=/:account/api-tokens&amp;permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&amp;scope=specified_flagship_app">open the app-scoped token form</a> in the dashboard.</p>
</div></article></div>
