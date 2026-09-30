<p>Offlabel is an Enterprise-only feature that removes Cloudflare branding and logo from Turnstile widgets. When enabled, widgets display without any visual references to Cloudflare.</p>
<p>When Offlabel is enabled:</p>
<ul>
<li>The Cloudflare logo and color schemes are removed from all widget states.</li>
<li>The widget maintains the same functionality, behavior, and WCAG 2.2 AA accessibility compliance.</li>
<li>All security features remain unchanged.</li>
</ul>
<p>The widget will display with a clean, unbranded appearance that integrates seamlessly with your website's design.</p>
<hr />
<h2 id="implementation">Implementation</h2>
<h3 id="enable-offlabel">Enable Offlabel</h3>
<p>After your account team enables the Offlabel entitlement, you can activate it for specific widgets using the Cloudflare API.</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;&#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;&#45;H &quot;Content-Type: application/json&quot; \&#10;&#45;d &#x27;{&#10;    &quot;offlabel&quot;: true&#10;}&#x27;&#10;</code></pre>
<h3 id="create-new-widgets-with-offlabel">Create new widgets with Offlabel</h3>
<p>You can enable Offlabel when creating new widgets.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets&quot; \&#10;&#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;&#45;H &quot;Content-Type: application/json&quot; \&#10;&#45;d &#x27;{&#10;    &quot;name&quot;: &quot;Branded Widget&quot;,&#10;    &quot;domains&quot;: [&quot;example.com&quot;],&#10;    &quot;mode&quot;: &quot;managed&quot;,&#10;    &quot;offlabel&quot;: true&#10;}&#x27;&#10;</code></pre>
<h3 id="verification">Verification</h3>
<p>Confirm Offlabel is enabled by checking your widget configuration.</p>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;&#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>The response will include <code>&quot;offlabel&quot;: true</code> when the feature is active.</p>
<h3 id="link-to-cloudflare-s-turnstile-privacy-policy">Link to Cloudflare's Turnstile Privacy Policy</h3>
<p>As a condition of enabling offlabel, you must reference Cloudflare's <a href="https://www.cloudflare.com/turnstile-privacy-policy/">Turnstile Privacy Addendum</a> in one of two ways:</p>
<ol>
<li>Link to it in your own privacy policy.</li>
<li>Configure the widget to display a link to Cloudflare's privacy policy using the <a href="/turnstile/get-started/client-side-rendering/widget-configurations/#complete-configuration-reference">JavaScript Render Parameters</a>.</li>
</ol>
<hr />
<h2 id="availability">Availability</h2>
<p>Offlabel is available exclusively to Enterprise customers with the Enterprise Turnstile add-on or Standalone Enterprise Turnstile customers.</p>
<p>Contact your account team for access to the Offlabel feature.</p>
