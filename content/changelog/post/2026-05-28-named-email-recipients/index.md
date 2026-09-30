<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 28, 2026</time><h2 id="post-title">Send emails with named recipient addresses</h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>You can now send emails with display names on recipient addresses in addition to the existing <code>from</code> support. Pass an object with <code>email</code> and an optional <code>name</code> field for <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>replyTo</code>, or <code>from</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17723.md")</div>
<p>Plain strings remain fully supported for backward compatibility, and you can mix strings and named objects in the same array.</p>
<p>Refer to the <a href="/email-service/api/send-emails/workers-api/">Workers API</a> and <a href="/email-service/api/send-emails/rest-api/">REST API</a> documentation for full request examples.</p>
</div></article></div>
