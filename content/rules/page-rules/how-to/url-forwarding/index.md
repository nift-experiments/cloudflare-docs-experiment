<p>Page Rules allow you to forward or redirect traffic to a different URL, though they are just one of the <a href="/fundamentals/reference/redirects/">options provided by Cloudflare</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13120.md")
</aside>
<hr />
<h2 id="redirect-with-page-rules">Redirect with Page Rules</h2>
<p>To configure URL forwarding or redirects using Page Rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13121.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13119.md")
</aside>
<hr />
<h2 id="forwarding-examples">Forwarding examples</h2>
<p>Imagine you want site visitors to reach your website for a variety of URL patterns. For instance, the page rule URL patterns <code>*www.example.com/products</code> and <code>*example.com/products</code> match:</p>
<pre><code class="language-txt">http://example.com/products&#10;&#10;http://www.example.com/products&#10;&#10;https://www.example.com/products&#10;&#10;https://blog.example.com/products&#10;&#10;https://www.blog.example.com/products&#10;</code></pre>
<p>but do not match:</p>
<pre><code class="language-txt">http://www.example.com/blog/products (extra directory)&#10;or&#10;http://www.example.comproducts (no trailing slash)&#10;</code></pre>
<p>Once you have created the pattern that matches what you want, select the <strong>Forwarding</strong> toggle. This will display a field where you can enter the address you want requests forwarded to.</p>
<pre><code class="language-txt">https://example.com/products&#10;</code></pre>
<p>If you enter the address above in the forwarding box and select <strong>Add Rule</strong>, within a few seconds any requests that match the pattern you entered will automatically be forwarded with an <code>HTTP 302</code> redirect status code to the new URL.</p>
<hr />
<h2 id="advanced-forwarding-options">Advanced forwarding options</h2>
<p>If you use a basic redirect, such as forwarding the apex domain (<code>example.com</code>) to <code>www.example.com</code>, then you lose anything else in the URL.</p>
<p>For example, you could set up the pattern:</p>
<pre><code class="language-txt">example.com&#10;</code></pre>
<p>And have it forward to:</p>
<pre><code class="language-txt">http://www.example.com&#10;</code></pre>
<p>However, if someone entered <code>example.com/some-particular-page.html</code>, they would be redirected to:</p>
<pre><code class="language-txt">www.example.com&#10;</code></pre>
<p>Instead of:</p>
<pre><code class="language-txt">www.example.com/some-particular-page.html&#10;</code></pre>
<p>The solution is to use variables. Each wildcard corresponds to a variable when can be referenced in the forwarding address. The variables are represented by a <code>$</code> (dollar sign) followed by a number. To refer to the first wildcard you would use <code>$1</code>, to refer to the second wildcard you would use <code>$2</code>, and so on.</p>
<p>To fix the forwarding from the apex to <code>www</code> in the above example, you could use the same pattern:</p>
<pre><code class="language-txt">example.com/*&#10;</code></pre>
<p>You would then set up the following URL for traffic to forward to:</p>
<pre><code class="language-txt">http://www.example.com/$1&#10;</code></pre>
<p>In this case, if someone went to:</p>
<pre><code class="language-txt">example.com/some-particular-page.html&#10;</code></pre>
<p>They would be redirected to:</p>
<pre><code class="language-txt">http://www.example.com/some-particular-page.html&#10;</code></pre>
