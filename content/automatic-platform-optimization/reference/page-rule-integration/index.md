<p>The following Page Rules can control APO. Any changes to caching via Page Rules require purging the cache for the changes to take effect.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3342.md")
</aside>
<ul>
<li>
<p><strong>Cache Level: Bypass</strong> — APO bypasses pages with response header <code>cf-apo-via: origin,page-rules</code></p>
</li>
<li>
<p><strong>Cache Level: Ignore Query String</strong> — APO ignores all query strings when serving from Cache.</p>
</li>
<li>
<p><strong>Cache Level: Cache Everything</strong> — APO caches pages with all query strings.</p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3341.md")
</aside>
<ul>
<li>
<p><strong>Bypass Cache on Cookie (Business and Enterprise plans only)</strong> — APO applies custom bypass cookies in addition to the default list.</p>
</li>
<li>
<p><strong>Edge Cache TTL</strong> — APO applies custom Edge TTL instead of 30 days. This page rule is helpful for pages that can generate CAPTCHAs or nonces.</p>
</li>
<li>
<p><strong>Browser Cache TTL</strong> — APO applies custom Browser TTL.</p>
</li>
<li>
<p><code>CDN-Cache-Control</code> and <code>Cloudflare-CDN-Cache-Control</code> – Enables users to have detailed control over cache TTLs without using a page rule. For more information on the <code>CDN-Cache-Control</code> and <code>Cloudflare-CDN-Cache-Control</code> headers, refer to <a href="/cache/concepts/cache-control/">CDN-Cache-Control</a>.</p>
</li>
</ul>
