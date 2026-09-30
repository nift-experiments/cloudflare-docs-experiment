<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Browser Run adds Live View, Human in the Loop, and Session Recordings</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>When browser automation fails or behaves unexpectedly, it can be hard to understand what happened. We are shipping three new features in <a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) to help:</p>
<ul>
<li><strong><a href="/browser-run/features/live-view/">Live View</a></strong> for real-time visibility</li>
<li><strong><a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a></strong> for human intervention</li>
<li><strong><a href="/browser-run/features/session-recording/">Session Recordings</a></strong> for replaying sessions after they end</li>
</ul>
<h4 id="live-view">Live View</h4>
<p><a href="/browser-run/features/live-view/">Live View</a> lets you see what your agent is doing in real time. The page, DOM, console, and network requests are all visible for any active browser session. Access Live View from the Cloudflare dashboard, via the hosted UI at <code>live.browser.run</code>, or using native Chrome DevTools.</p>
<h4 id="human-in-the-loop">Human in the Loop</h4>
<p>When your agent hits a snag like a login page or unexpected edge case, it can hand off to a human instead of failing. With <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, a human steps into the live browser session through Live View, resolves the issue, and hands control back to the script.</p>
<p>Today, you can step in by opening the Live View URL for any active session. Next, we are adding a handoff flow where the agent can signal that it needs help, notify a human to step in, then hand control back to the agent once the issue is resolved.</p>
<p><img src="/images/browser-run/liveview.gif" alt="Browser Run Human in the Loop demo where an AI agent searches Amazon, selects a product, and requests human help when authentication is needed to buy" /></p>
<h4 id="session-recordings">Session Recordings</h4>
<p><a href="/browser-run/features/session-recording/">Session Recordings</a> records DOM state so you can replay any session after it ends. Enable recordings by passing <code>recording: true</code> when launching a browser. After the session closes, view the recording in the Cloudflare dashboard under <strong>Browser Run</strong> &gt; <strong>Runs</strong>, or retrieve via API using the session ID. Next, we are adding the ability to inspect DOM state and console output at any point during the recording.</p>
<p><img src="/images/browser-run/sessionrecording.gif" alt="Browser Run session recording showing an automated browser navigating the Sentry Shop and adding a bomber jacket to the cart" /></p>
<p>To get started, refer to the documentation for <a href="/browser-run/features/live-view/">Live View</a>, <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a>, and <a href="/browser-run/features/session-recording/">Session Recording</a>.</p>
</div></article></div>
