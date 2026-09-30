<p>If you are migrating from Page Rules, there is a behavior change between Page Rules and Cache Rules.</p>
<p>When you create a new Cache Rule and select <strong>Eligible for cache</strong>, the Cache Everything feature is enabled by default. With Page Rules, you had to specifically enable the Cache Everything option.</p>
<p>To maintain the same behavior you had with Page Rules (that is, not enabling Cache Everything), you need to create these two specific rules in this order before creating any additional rules.</p>
<p>Multiple matching cache rules can be combined and applied to the same request. After rule 1 matches, Cloudflare will keep evaluating other cache rules checking for matches. For more information, refer to <a href="/cache/how-to/cache-rules/order/">Order and priority</a>.</p>
<h2 id="rule-1">Rule 1</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3902.md")
</div></div>
<h2 id="rule-2">Rule 2</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3905.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3899.md")
</aside>
