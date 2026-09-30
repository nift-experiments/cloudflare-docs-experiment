<p>The following example defines a single cache rule for a zone using Terraform. The rule configures several cache settings and sets a custom cache key for incoming requests addressed at <code>example.net</code>.</p>
<details class="nb-details"><summary>Terraform �CODE3� resource</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3876.md")
</div></details>
<p>The following example configures <a href="/cache/concepts/vary/">Vary</a>. It normalizes <code>Accept</code> and <code>Accept-Language</code>, and bypasses cache for any other header in the origin <code>Vary</code> response.</p>
<details class="nb-details"><summary>Terraform example: Cache expected Vary responses</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3877.md")
</div></details>
<p>For additional guidance on using Terraform with Cloudflare, refer to <a href="/terraform/">Terraform</a>.</p>
