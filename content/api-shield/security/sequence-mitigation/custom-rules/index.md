<p>API Shield sequence custom rules use the configured API Shield <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3259.md")
</div> to track the order of requests a user has made and the time between requests, and makes them available via [Cloudflare Rules](/rules). This allows you to write rules that match valid or invalid sequences.
<p>These rules are similar to <a href="/bots/additional-configurations/sequence-rules/">cookie sequence rules</a> but have a different set of prerequisites:</p>
<ul>
<li>They require <a href="/api-shield/get-started/#session-identifiers">session identifiers</a> to be set in API Shield.</li>
<li>Because they require session identifiers, they can only be used on traffic that can be clearly attributed to individual users through session identifiers (authenticated traffic).</li>
<li>Because Cloudflare stores the user state in memory and not in a cookie, a session's sequence lifetime is limited to 10 minutes.</li>
<li>You must set up at least one <a href="/api-shield/security/sequence-mitigation/manage-sequence-rules/">API sequence rule</a> to activate the sequence system.</li>
</ul>
<p>Rules built using these custom rules are similar to the sequence rules that can be configured <a href="/api-shield/security/sequence-mitigation/">via the API or the Cloudflare dashboard</a> as they make use of the same underlying technology. However, these custom rules allow for greater flexibility by using free-form logic on top of the recorded sequence and providing access to the full response options that rulesets offers.</p>
<h2 id="availability">Availability</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3258.md")
</aside>
<p>These sequence fields are available in:</p>
<ul>
<li><a href="/waf/custom-rules/">Custom rules</a> (<code>http_request_firewall_custom</code> phase)</li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> (<code>http_request_ratelimit</code>)</li>
<li><a href="/workers/examples/bulk-redirects/">Bulk Redirects</a> (<code>http_request_redirect</code>)</li>
<li><a href="/rules/transform/response-header-modification/">Request Header Transform Rules</a> (<code>http_request_late_transform</code>)</li>
</ul>
<table>
<thead>
<tr>
<th style="width: 35%;">Field name</th>
<th>Description</th>
<th>Example value</th>
</tr>
</thead>
<tbody style='vertical-align:top'>
<tr>
<td><p><code>cf.sequence.current_op</code><br />`String`</p></td>
<td>
          <p>This field contains the ID of the operation that matches the current request. If the current request does not match any operations defined in Endpoint Management, it will be an empty string.</p>
</td>
<td><p><code>c821cc00</code></p></td>
</tr>
<tr>
<td><p><code>cf.sequence.previous_ops</code><br />`Array<String>`</p></td>
<td>
          <p>This field contains an array of the prior operation IDs in the sequence, ordered from most to least recent. It does not include the current request. <br /><br /> If an operation is repeated, it will appear multiple times in the sequence.</p>
</td>
<td><p><code>["f54dac32", "c821cc00", "a37dc89b"]</code></p></td>
</tr>
<tr>
<td><p><code>cf.sequence.msec_since_op</code><br />`Map<Number>`</p></td>
<td>
          <p>This field contains a map where the keys are operation IDs and the values are the number of milliseconds since that operation has most recently occurred. <br /><br /> This does not include the current request or operation as it only factors in previous operations in the sequence.</p>
</td>
<td><p>`{"f54dac32": 1000, "c821cc00": 2000}`</p></td>
</tr>
</tbody>
</table>
<h2 id="build-a-sequence-custom-rule">Build a sequence custom rule</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3260.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3257.md")
</aside>
<h3 id="example-rules">Example rules</h3>
<p>Each saved endpoint will have an endpoint ID visible in its details page in Endpoint Management in the form of a UUID. The references below (<code>aaaaaaaa</code>, <code>bbbbbbbb</code>, and <code>cccccccc</code>) are the first eight characters of the endpoint ID.</p>
<p>The visitor must wait more than 2 seconds after requesting endpoint <code>aaaaaaaa</code> before requesting endpoint <code>bbbbbbbb</code>:</p>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;bbbbbbbb&quot; and &#10;cf.sequence.msec_since_op[&quot;aaaaaaaa&quot;] ge 2000&#10;</code></pre>
<p>The visitor must request endpoints <code>aaaaaaaa</code>, then <code>bbbbbbbb</code>, then <code>cccccccc</code> in that exact order:</p>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;cccccccc&quot; and &#10;cf.sequence.previous_ops[0] == &quot;bbbbbbbb&quot; and &#10;cf.sequence.previous_ops[1] == &quot;aaaaaaaa&quot;&#10;</code></pre>
<p>The visitor must request endpoint <code>aaaaaaaa</code> before endpoint <code>bbbbbbbb</code>, but endpoint <code>aaaaaaaa</code> can be anywhere in the previous 10 requests:</p>
<pre><code class="language-txt">cf.sequence.current_op eq &quot;bbbbbbbb&quot; and &#10;any(cf.sequence.previous_ops[*] == &quot;aaaaaaaa&quot;)&#10;</code></pre>
<p>The visitor must request either endpoint <code>aaaaaaaa</code> before endpoint <code>bbbbbbbb</code>, or endpoint <code>cccccccc</code> before endpoint <code>bbbbbbbb</code>:</p>
<pre><code class="language-txt">(cf.sequence.current_op eq &quot;bbbbbbbb&quot; and &#10;any(cf.sequence.previous_ops[*] == &quot;aaaaaaaa&quot;)) or &#10;(cf.sequence.current_op eq &quot;bbbbbbbb&quot; and &#10;any(cf.sequence.previous_ops[*] == &quot;cccccccc&quot;))&#10;</code></pre>
