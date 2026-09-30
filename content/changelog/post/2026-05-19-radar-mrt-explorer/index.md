<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 19, 2026</time><h2 id="post-title">MRT Explorer on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes an <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer</a> tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.</p>
<h4 id="loading-a-file">Loading a file</h4>
<p>Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-form.png" alt="Screenshot of the MRT Explorer file input form" /></p>
<h4 id="inspecting-events">Inspecting events</h4>
<p>Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-list.png" alt="Screenshot of the MRT Explorer event list" /></p>
<h4 id="event-details">Event details</h4>
<p>Clicking on the &quot;View details&quot; action opens a modal with additional properties and the full event JSON.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-details.png" alt="Screenshot of the MRT Explorer event details modal" /></p>
<h4 id="shareable-urls">Shareable URLs</h4>
<p>When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.</p>
<p>Try the <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer on Cloudflare Radar</a>.</p>
</div></article></div>
