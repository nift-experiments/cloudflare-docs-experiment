<ol>
<li>In the Cloudflare dashboard, go to <strong>Cache</strong> &gt; <strong>Cache Rules</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Cache Response Rules</strong> tab.</p>
</li>
<li>
<p>Select <strong>Create rule</strong>.</p>
</li>
<li>
<p>Enter a descriptive name for the rule in <strong>Rule name</strong>.</p>
</li>
<li>
<p>Under <strong>When incoming requests match</strong>, select <strong>All incoming requests</strong> if you want the rule to apply to all traffic or <strong>Custom filter expression</strong> if you want the rule to only apply to traffic matching the custom expression.</p>
</li>
<li>
<p>If you selected <strong>Custom filter expression</strong>, define the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">rule expression</a>. Use the <strong>Field</strong> drop-down list to choose an HTTP property and select an <strong>Operator</strong>. Both request fields (such as URI path or hostname) and response fields (such as response status code or response headers) are available for matching. Refer to <a href="/cache/how-to/cache-response-rules/settings/">Available settings</a> for the full list of available fields and operators.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3923.md")
</aside>
<ol start="7">
<li>
<p>Following the selection of the field and operator, enter the corresponding value that will trigger the Cache Response Rule. For example, if the selected field is <code>Hostname</code> and the operator is <code>equals</code>, a value of <code>example.com</code> would mean the rule matches any request to that hostname.</p>
</li>
<li>
<p>Under <strong>Then</strong>, select one of the following actions:</p>
<ul>
<li>
<p><strong>Modify cache-control directives</strong>: Set or remove <code>Cache-Control</code> directives sent by your origin. For each directive, choose <strong>Set directive</strong> or <strong>Remove directive</strong>. For duration-based directives like <code>max-age</code> or <code>s-maxage</code>, enter a value in seconds. Turn on <strong>Cloudflare only</strong> to apply the directive only within Cloudflare's cache without changing what visitors receive. Refer to <a href="/cache/how-to/cache-response-rules/settings/#supported-directives">Supported directives</a> for the full list.</p>
</li>
<li>
<p><strong>Modify cache tags</strong>: Add, override, or remove cache tags on the response for targeted <a href="/cache/how-to/purge-cache/purge-by-tags/">purging</a>. Select one of the following operations:</p>
<ul>
<li><strong>Add to existing tags</strong>: Append new tags to the current set.</li>
<li><strong>Override existing tags</strong>: Replace all current tags with the specified tags.</li>
<li><strong>Remove from existing tags</strong>: Remove specific tags from the current set.</li>
</ul>
<p>For the tag source, you can either specify tags manually or select <strong>Parse from response header</strong> to extract tags from a response header value. When parsing from a header, you can split the header value using a custom separator (for example, commas instead of spaces).</p>
</li>
<li>
<p><strong>Strip headers</strong>: Remove <code>Set-Cookie</code>, <code>ETag</code>, or <code>Last-Modified</code> headers from the origin response before Cloudflare evaluates the response for caching. Select which headers to strip.</p>
</li>
</ul>
<p>For more details on each action, refer to <a href="/cache/how-to/cache-response-rules/settings/#available-actions">Available settings</a>.</p>
</li>
<li>
<p>Under <strong>Place at</strong>, from the dropdown, you can select the order of your rule. From the main page, you can also change the order of the rules you have created.</p>
</li>
<li>
<p>To save and deploy your rule, select <strong>Deploy</strong>. If you are not ready to deploy your rule, select <strong>Save as Draft</strong>.</p>
</li>
</ol>
<p>If you are matching a hostname in your rule expression, you may be prompted to create a proxied DNS record for that hostname. Refer to <a href="/rules/reference/troubleshooting/#this-rule-may-not-apply-to-your-traffic">Troubleshooting</a> for more information.</p>
