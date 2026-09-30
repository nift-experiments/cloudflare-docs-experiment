<p class="article-summary">Create a redirect rule to redirect visitors using mobile devices to a different hostname.</p>
<p>The following examples will redirect visitors using mobile devices — based on the request user agent string — to a different hostname.</p>
<h2 id="redirect-mobile-users-dropping-the-original-uri-path">Redirect mobile users dropping the original URI path</h2>
<p>This example static redirect will redirect requests for the current zone (<code>example.com</code>) from mobile users to <code>m.example.com</code> without preserving the URI path in the original HTTP request.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13206.md")
</div>
<p>Notes about this example:</p>
<ul>
<li>The <code>not http.host in {&quot;m.example.com&quot;}</code> condition prevents redirect loops.</li>
<li>The user agent condition follows <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox#device-specific_user_agent_strings">Mozilla's recommendation</a> for identifying mobile devices.</li>
<li>The <strong>Then</strong> &gt; <strong>URL</strong> value should be the same as the one you entered in the <code>http.host</code> condition of the rule's filter expression.</li>
<li>You can redirect users to other zones on Cloudflare or to other hostnames not on Cloudflare.</li>
</ul>
<h2 id="redirect-mobile-users-keeping-the-original-path">Redirect mobile users keeping the original path</h2>
<p>This example single redirect will redirect requests for the current zone (<code>example.com</code>) from mobile users to <code>m.example.com</code>, keeping the URI path of the original HTTP request.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/13207.md")
</div>
<p>Notes about this example:</p>
<ul>
<li>The <code>not http.host in {&quot;m.example.com&quot;}</code> condition prevents redirect loops.</li>
<li>The user agent condition follows <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent/Firefox#device-specific_user_agent_strings">Mozilla's recommendation</a> for identifying mobile devices.</li>
<li>The hostname in <strong>Then</strong> &gt; <strong>Expression</strong> should be the same as the one you entered in the <code>http.host</code> condition of the rule's filter expression.</li>
<li>Depending on your use case, you may want to enable <strong>Then</strong> &gt; <strong>Preserve query string</strong> to also keep the query string of the original request.</li>
<li>You can redirect users to other zones on Cloudflare or to other hostnames not on Cloudflare.</li>
</ul>
