<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/3514.md")
</div> provide more detail about *why* Cloudflare assigned a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/3515.md")
</div> to a request.
<p>Use these tags to learn more about your bot traffic and better inform security settings.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3513.md")
</aside>
<h2 id="potential-values">Potential values</h2>
<p>Once you <a href="#enable-bot-tags">enable bot tags</a>, you can see more information about bot requests, such as whether a request came from a verified bot (like Bing) or a category of verified bot (like SearchEngine).</p>
<p>The following values are <strong>examples</strong> of what may be present in the <code>BotTags</code> log field, but not an exhaustive list:</p>
<ul>
<li>api</li>
<li>google</li>
<li>bing</li>
<li>googleAds</li>
<li>googleMedia</li>
<li>googleImageProxy</li>
<li>pinterest</li>
<li>newRelic</li>
<li>baidu</li>
<li>apple</li>
<li>yandex</li>
</ul>
<p>When matching the Ruleset Engine field, use uppercase tag values such as <code>API</code>, <code>GOOGLE</code>, or <code>BING</code>.</p>
<h2 id="use-bot-tags">Use bot tags</h2>
<p>To include bot tags in logs, add the <code>BotTags</code> field when using <a href="/logs/logpush/">Logpush</a>.</p>
<p>To match bot tags in Ruleset Engine expressions, use the <a href="/ruleset-engine/rules-language/fields/reference/cf.bot_management.tags/"><code>cf.bot_management.tags</code></a> field. For example:</p>
<pre><code class="language-txt">any(cf.bot_management.tags[*] eq &quot;API&quot;)&#10;</code></pre>
