<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 21, 2025</time><h2 id="post-title">Subaddressing support in Email Routing</h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>Subaddressing, as defined in <a href="https://www.rfc-editor.org/rfc/rfc5233">RFC 5233</a>, also known as plus addressing, is now supported in Email Routing. This enables using the &quot;+&quot; separator to augment your custom addresses with arbitrary detail information.</p>
<p>Now you can send an email to <code>user+detail@example.com</code> and it will be captured by the <code>user@example.com</code> custom address. The <code>+detail</code> part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> or an <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">Agent application</a>.</p>
<p>Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.</p>
<p><img src="/assets/upstream/images/changelog/email-service/subaddressing.png" alt="Subaddressing" /></p>
<p>Check our <a href="/email-service/configuration/email-routing-addresses/#subaddressing">Developer Docs</a> to learn how to enable subaddressing in Email Routing.</p>
</div></article></div>
