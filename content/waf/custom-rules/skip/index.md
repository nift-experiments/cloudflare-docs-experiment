<p>Use the <em>Skip</em> action in a custom rule to skip one or more security features. A rule configured with the <em>Skip</em> action is also known as a skip rule.</p>
<p>Skip rules allow specific requests to bypass security features that would otherwise block or challenge them. Use skip rules when legitimate traffic matches a security rule unintentionally. For example, to allow a trusted API client through <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, or to exempt an internal monitoring service from <a href="/waf/managed-rules/">Managed Rules</a>.</p>
<p>You can skip <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, <a href="/waf/managed-rules/">Managed Rules</a>, <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> rules, and several other security products. However, you cannot skip <a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> (available on the Free plan).</p>
<p>For more information on the available options, refer to <a href="/waf/custom-rules/skip/options/">Available skip options</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashNewNav"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15479.md")
</div></div>
