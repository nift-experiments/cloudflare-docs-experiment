<p>Images in the <a href="/cache/how-to/purge-cache/">cache must be purged</a> or expired before seeing any changes in Polish settings.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9357.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the domain where you want to activate Polish.</li>
<li>Select <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Image Optimization</strong>.</li>
<li>Under <strong>Polish</strong>, select <em>Lossy</em> or <em>Lossless</em> from the drop-down menu. <a href="/images/polish/compression/#lossy"><em>Lossy</em></a> gives greater file size savings.</li>
<li>(Optional) Select <strong>WebP</strong>. Enable this option if you want to further optimize PNG and JPEG images stored in the origin server, and serve them as WebP files to browsers that support this format.</li>
</ol>
<p>To ensure WebP is not served from cache to a browser without WebP support, disable any WebP conversion utilities at your origin web server when using Polish.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9356.md")
</aside>
