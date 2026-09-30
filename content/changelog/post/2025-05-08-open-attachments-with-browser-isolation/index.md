<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 16, 2025</time><h2 id="post-title">Open email attachments with Browser Isolation</h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now safely open email attachments to view and investigate them.</p>
<p>What this means is that messages now have a <strong>Attachments</strong> section. Here, you can view processed attachments and their classifications (for example, <em>Malicious</em>, <em>Suspicious</em>, <em>Encrypted</em>). Next to each attachment, a <strong>Browser Isolation</strong> icon allows your team to safely open the file in a <strong>clientless, isolated browser</strong> with no risk to the analyst or your environment.</p>
<p><img src="/assets/upstream/images/changelog/email-security/Attachment-RBI.png" alt="Attachment-RBI" /></p>
<p>To use this feature, you must:</p>
<ul>
<li>Turn on <strong>Allow users to open a remote browser without the device client</strong> in your Zero Trust settings.</li>
<li>Have <strong>Browser Isolation (BISO)</strong> seats assigned.</li>
</ul>
<p>For more details, refer to our <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">setup guide</a>.</p>
<p>Some attachment types may not render in Browser Isolation. If there is a file type that you would like to be opened with Browser Isolation, reach out to your Cloudflare contact.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div></article></div>
