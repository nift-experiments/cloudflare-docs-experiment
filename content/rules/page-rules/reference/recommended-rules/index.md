<p>Use Cloudflare Page Rules to improve the user experience of your domain with hardened security and enhanced site performance, while increasing reliability and minimizing bandwidth usage for your origin server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13110.md")
</aside>
<p>Keep in mind that not all rules will be right for everyone, but these are some of the most popular.</p>
<ul>
<li>301/302 Forwarding URL</li>
<li>Cache Level in specific paths</li>
<li>Edge Cache TTL, Always Online, and Browser Cache TTL</li>
</ul>
<h3 id="301-302-forwarding-url">301/302 Forwarding URL</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13109.md")
</aside>
<p>Two common examples for using forwarding URLs are:</p>
<ul>
<li>Defining the root as the canonical version of your domain.</li>
<li>Directing visitors to a specific page with an easy to remember URL.</li>
</ul>
<p>This example page rule configuration defines the root as the canonical version of your domain:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13111.md")
</div>
<p>This example redirects visitors to a specific page with an easy to remember URL:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/13112.md")
</div>
<h3 id="cache-level-in-specific-paths">Cache Level in specific paths</h3>
<p>Certain sections of a website, like the login or admin section, have different security and performance requirements than your general public-facing pages.</p>
<p>The following example page rule configuration bypasses cache for requests targeting a specific path:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/13113.md")
</div>
<h3 id="edge-cache-ttl-and-browser-cache-ttl">Edge Cache TTL and Browser Cache TTL</h3>
<p>Certain resources on your domain will likely not change often. For these resources, taking advantage of aggressive caching options can significantly reduce the load on your server and bandwidth utilization.</p>
<h4 id="examples">Examples</h4>
<p>In the following example page rule configuration, the target is a folder that holds the majority of the image assets as well as some other types of multimedia.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/13114.md")
</div>
<p>The following example page rule configuration applies unique rules for critical pages that do not change very often.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@markup("md", "content/.markup/bodies/13115.md")
</div>
