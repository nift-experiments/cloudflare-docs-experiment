<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 17, 2026</time><h2 id="post-title">Preview sent emails in the Activity log</h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new <strong>Preview</strong> section to inspect the message as it was sent, across tabs for the rendered <strong>HTML</strong> body, the <strong>Text</strong> body, the <strong>Headers</strong>, the <strong>Attachments</strong>, and the full <strong>Raw</strong> <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> source.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-message-preview.png" alt="The rendered HTML preview of a sent email in the Email Service Activity log" /></p>
<p>Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.</p>
<p>To make messages previewable, turn on <strong>Email preview</strong> in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have <strong>Email preview</strong> turned on automatically.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-preview-setting.png" alt="The Email preview setting in a sending domain's settings" /></p>
<p>Refer to <a href="/email-service/observability/logs/#message-preview">Email logs</a> for more information.</p>
</div></article></div>
