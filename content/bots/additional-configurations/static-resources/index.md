<p>Pro, Business, and Enterprise customers can use Cloudflare's bot solutions to protect their <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3526.md")
</div> from bots.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3525.md")
</aside>
<h2 id="super-bot-fight-mode">Super Bot Fight Mode</h2>
<p>To enable this feature as a Pro or Business customer or an Enterprise customer without Bot Management:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3527.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3524.md")
</aside>
<h2 id="bot-management-for-enterprise">Bot Management for Enterprise</h2>
<p>Static resources are protected by default when you create <a href="/waf/custom-rules/">custom rules</a> using <code>cf.bot_management.score</code>.</p>
<p>To exclude static resources, you would need to include <code>not (cf.bot_management.static_resource)</code> as part of your custom rule.</p>
<h2 id="which-files-are-protected">Which files are protected?</h2>
<p>Static resources are files with the following extensions:</p>
<p><code>ico|jpg|png|jpeg|gif|css|js|tif|tiff|bmp|pict|webp|svg|svgz|class|jar|txt|csv|doc|docx|xls|xlsx|pdf|ps|pls|ppt|pptx|ttf|otf|woff|woff2|eot|eps|ejs|swf|torrent|midi|mid|m3u8|m4a|mp3|ogg|ts</code></p>
<p>Additionally, the <code>/.well-known/</code> URL path and all elements in it are considered a static resource, regardless of the file extension.</p>
