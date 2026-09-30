<p>As you try to create a new DNS record, Cloudflare displays the following error:</p>
<pre><code class="language-txt">NS records with that host already exist. (Code:81056)&#10;</code></pre>
<h2 id="causes">Causes</h2>
<p>When a child domain (<code>blog.example.com</code>) of your domain (<code>example.com</code>) has been set up as a separate <a href="/dns/zone-setups/subdomain-setup/">subdomain zone</a>, corresponding <code>NS</code> records must have been placed within the parent zone.</p>
<p>When you are managing DNS records for the parent zone (in this example, <code>example.com</code>), you cannot create IP address resolution records (<code>A</code>, <code>AAAA</code>, or <code>CNAME</code>) with a name that specifies the same subdomain that already exists as a separate subdomain zone.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7768.md")
</div>
<h2 id="solution">Solution</h2>
<p>Before creating such records, remove any <code>NS</code> records with the same name.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7767.md")
</aside>
