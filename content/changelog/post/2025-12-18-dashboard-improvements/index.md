<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 18, 2025</time><h2 id="post-title">Workers for Platforms - Dashboard Improvements</h2>
<div class="changelog-badges"><span>workers-for-platforms</span></div><div class="changelog-body"><p><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> lets you build multi-tenant platforms on <a href="/workers/">Cloudflare Workers</a>, allowing your end users to deploy and run their own code on your platform. It's designed for anyone building an AI vibe coding platform, e-commerce platform, website builder, or any product that needs to securely execute user-generated code at scale.</p>
<p>Previously, setting up Workers for Platforms required using the API. Now, the Workers for Platforms UI supports namespace creation, dispatch worker templates, and tag management, making it easier for Workers for Platforms customers to build and manage multi-tenant platforms directly from the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/dashboard-improvements.png" alt="Workers for Platforms Dashboard Improvements" /></p>
<h4 id="key-improvements">Key improvements</h4>
<ul>
<li><strong>Namespace Management:</strong> You can now create and configure <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">dispatch namespaces</a> directly within the dashboard to start a new platform setup.</li>
<li><strong>Dispatch Worker Templates:</strong> New Dispatch Worker templates allow you to quickly define how traffic is routed to individual Workers within your namespace. Refer to the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic Dispatch documentation</a> for more examples.</li>
<li><strong>Tag Management:</strong> You can now set and update <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/tags/">tags</a> on User Workers, making it easier to group and manage your Workers.</li>
<li><strong>Binding Visibility:</strong> <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">Bindings</a> attached to User Workers are now visible directly within the User Worker view.</li>
<li><strong>Deploy Vibe Coding Platform in one-click:</strong> Deploy a <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">reference implementation</a> of an AI vibe coding platform directly from the dashboard. Powered by the Cloudflare's <a href="https://github.com/cloudflare/vibesdk">VibeSDK</a>, this starter kit integrates with Workers for Platforms to handle the deployment of AI-generated projects at scale.</li>
</ul>
<p>To get started, go to <strong>Workers for Platforms</strong> under <strong>Compute &amp; AI</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
</div></article></div>
