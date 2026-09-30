<p>By default, Version Management is not enabled on a zone.</p>
<p>To enable <a href="https://dash.cloudflare.com/?to=/:account/:zone/versioning">Version Management</a>:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Enable versioning</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15315.md")
</aside>
<p>Once you <a href="/version-management/how-to/enable/">enable</a> Version Management, Cloudflare will automatically create:</p>
<ul>
<li><strong>Version Zero</strong>, think about this as the configuration of your current zone. Once default environments are created, Version Zero is automatically deployed to them, guaranteeing no disruption in your live traffic. This Version is also permanently editable. In case you decide to disable Zone Versioning, Version Zero will become your zone again.</li>
<li><strong>Global Configuration</strong>, you can find all the configurations here that are not supported by Version Management.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15314.md")
</aside>
<p>On the Environments page, you can create default environments for <strong>Production</strong>, <strong>Staging</strong>, and <strong>Development</strong>.</p>
<h2 id="disable-version-management">Disable Version Management</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15313.md")
</aside>
<p>To disable Zone Versioning:</p>
<ol>
<li>
<p>Confirm that <strong>Version Zero</strong> has the correct configurations for your zone:</p>
<ol>
<li>
<p>Use the <a href="/version-management/how-to/compare-versions/">comparison feature</a> to view the differences between your current <strong>Production</strong> version and <strong>Version Zero</strong>.</p>
</li>
<li>
<p>If there are differences, make changes to <strong>Version Zero</strong> so it matches your current <strong>Production</strong> version.</p>
</li>
<li>
<p><a href="/version-management/how-to/environments/#promote-a-version">Promote</a> <strong>Version Zero</strong> to your <strong>Production</strong> environment.</p>
</li>
<li>
<p>Confirm that your new <strong>Production</strong> environment functions as expected.</p>
</li>
</ol>
</li>
<li>
<p>Send a <code>GET</code> request to the <code>/zones/{zone_id}/environments</code> endpoint.</p>
</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/environments&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>In the response, save the following values:</p>
<ul>
<li>The environment <code>ref</code> of every rule</li>
</ul>
<ol start="3">
<li>Using the <code>ref</code> of those environments, send a <code>DELETE</code> request to the <code>/zones/{zone_id}/environments/{ref}</code> endpoint for each environment.</li>
</ol>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/environments/{ref}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<ol start="4">
<li>Then, send a <code>GET</code> request to find all HTTP applications (or versions of your zone).</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/http_applications&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>Save the <code>id</code> of each HTTP application.</p>
<ol start="5">
<li>Using the <code>id</code> of those HTTP applications, send <code>DELETE</code> requests for every application.</li>
</ol>
<pre><code class="language-bash">curl --request DELETE \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/http_applications/{http_application_id}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>Once all these steps are completed, Zone Versioning will go back to its original landing page.</p>
