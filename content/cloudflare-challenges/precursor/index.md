<p>Precursor is a client-side, session-based verification system that continuously evaluates a visitor's behavior over time. Instead of relying on a single challenge event, Precursor runs ongoing verification in the browser to detect automation that appears legitimate in individual requests but exhibits non-human patterns across a session.</p>
<h2 id="how-it-works">How it works</h2>
<p>Precursor operates as a continuous client-side verification loop:</p>
<ul>
<li>A client-side script is injected into the page</li>
<li>The script continuously collects signals and performs verification</li>
<li>Each execution produces signals that are evaluated by Cloudflare</li>
<li>Results are used to update session state stored in the <code>cf_clearance</code> cookie</li>
<li>The process repeats throughout the session</li>
</ul>
<p>This enables Cloudflare to continuously evaluate session behavior over time.</p>
<h2 id="get-started">Get started</h2>
<p>Enable Precursor for your zone:</p>
<ol>
<li>In the Cloudflare dashboard, select your zone.</li>
<li>Go to <strong>Security</strong> &gt; <strong>Settings</strong>.</li>
<li>Locate <strong>Precursor</strong>.</li>
<li>Turn on Precursor.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-challenges/precursor-settings.png" alt="Security Settings page in the Cloudflare dashboard, showing the Precursor card with the on/off toggle" /></p>
<ol start="5">
<li>
<p><strong>Choose a mode:</strong> To fully verify a user session, visitors may need to complete a lightweight Challenge to establish a valid session. Precursor provides two modes depending on whether you want to prioritize user experience or strict verification:</p>
<ul>
<li>
<p><strong>Minimize Friction (default)</strong>
Does not show an interstitial Challenge to the visitor. Instead, Precursor attempts to establish session state in the background.
This provides a smoother user experience, but cannot guarantee that every session is fully verified.</p>
</li>
<li>
<p><strong>Maximize Security (recommended)</strong>
Shows a lightweight interstitial Challenge to establish a valid session if one does not already exist.
This ensures every session is verified before a user can proceed, but may introduce additional friction.</p>
</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-challenges/precursor-rules.png" alt="Precursor mode selector showing Minimize Friction and Maximize Security options" /></p>
<p>For most customers, selecting a mode is the only configuration required.</p>
<h3 id="precursor-rules-optional">Precursor Rules (optional)</h3>
<p>Precursor runs across your zone by default. Precursor Rules do not enable or disable Precursor — they determine which mode applies to each request.</p>
<p>For example:</p>
<ul>
<li>Run <strong>Minimize Friction</strong> across your site, but run <strong>Maximize Security</strong> to enforce a valid session on <code>/checkout</code>.</li>
<li>Run <strong>Maximize Security</strong> on all pages, except your homepage.</li>
</ul>
<h3 id="use-precursor-with-apis">Use Precursor with APIs</h3>
<p>If your zone serves both browser pages and API endpoints, use Precursor Rules to scope where strict enforcement applies.</p>
<p>When Precursor is set to <strong>Maximize Security</strong>, requests must present a valid <code>cf_clearance</code> cookie. This can affect:</p>
<ul>
<li>API endpoints called by non-browser clients (for example, <code>curl</code>, mobile backends, server-to-server jobs)</li>
<li>Browser API calls that do not send cookies</li>
</ul>
<p>For mixed HTML/API traffic, use one of these patterns:</p>
<ul>
<li>Start with <strong>Minimize Friction</strong> globally, then apply <strong>Maximize Security</strong> only to sensitive pages or paths with Precursor Rules.</li>
<li>Start with <strong>Maximize Security</strong> globally, then add <strong>Minimize Friction</strong> Precursor Rules for API hostnames or API paths.</li>
</ul>
<p>For browser XHR/fetch requests that must access endpoints under <strong>Maximize Security</strong>, ensure cookies are included:</p>
<pre><code class="language-js">fetch(&quot;/api/search&quot;, {&#10;  credentials: &quot;include&quot;,&#10;});&#10;</code></pre>
<pre><code class="language-js">axios.get(&quot;/api/search&quot;, {&#10;  withCredentials: true,&#10;});&#10;</code></pre>
<p>Use <strong>Minimize Friction</strong> on endpoints that should not require challenge-style session enforcement. Precursor still evaluates session behavior and can continue contributing detection signals and bot score context.</p>
<h2 id="relationship-to-javascript-detections">Relationship to JavaScript Detections</h2>
<p>Precursor supersedes JavaScript Detections (JSD). JSD and Precursor both collect client-side signals, but Precursor evaluates them continuously across a session instead of as a one-time check.</p>
<ul>
<li>Precursor moves from one-time execution to continuous verification</li>
<li>Precursor introduces session-based state</li>
<li>Precursor enables dynamic runtime control</li>
</ul>
<p>When either JSD or Precursor contributes to bot score, Cloudflare exposes the source as <strong>JavaScript Fingerprinting</strong>.</p>
<h4 id="if-you-already-use-jsd">If you already use JSD</h4>
<p>Cloudflare will disable JSD when you enable Precursor to avoid running both features on the same traffic. Precursor includes all detections previously covered by JSD, and any JSD-driven Security Rules will still apply.</p>
<h4 id="if-you-do-not-use-jsd">If you do not use JSD</h4>
<p>If you enable Precursor without previously using JSD, you may see more traffic with bot score below 30.</p>
<h2 id="relationship-to-challenge-pages">Relationship to Challenge Pages</h2>
<p>Precursor and Challenges serve different roles:</p>
<ul>
<li>Challenges provide point-in-time verification</li>
<li>Precursor provides continuous, session-level verification</li>
</ul>
<p>Precursor does not replace Challenges. Instead, it strengthens them by:</p>
<ul>
<li>determining when additional Challenges should be required</li>
<li>re-evaluating visitors after they have already passed a Challenge</li>
<li>identifying automation that emerges over time</li>
</ul>
<h2 id="relationship-to-cf-clearance-cookie">Relationship to <code>cf_clearance</code> cookie</h2>
<p>Precursor is tightly integrated with <a href="/cloudflare-challenges/concepts/clearance/#cf_clearance-cookies"><code>cf_clearance</code></a>. When running Precursor:</p>
<ul>
<li>effective clearance may be reduced or invalidated</li>
<li>additional Challenges may be triggered</li>
<li>the visitor may be re-verified during the same session</li>
</ul>
<h2 id="visibility-in-security-analytics">Visibility in Security Analytics</h2>
<p>Once Precursor runs on a zone, its detections appear in the zone's Analytics view. To open it, select your zone in the Cloudflare dashboard, then go to <strong>Security</strong> &gt; <strong>Analytics</strong> &gt; <strong>Traffic</strong> &gt; <strong>Bot analysis</strong>. The bot score distribution and WAF rule-match counts now include Precursor's detections.</p>
<p>For more information, refer to <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
