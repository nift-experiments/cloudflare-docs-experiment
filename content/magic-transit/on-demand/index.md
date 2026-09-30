<p>If you have access to the Magic Transit on-demand option, you can <a href="/byoip/concepts/dynamic-advertisement/best-practices/#configure-dynamic-advertisement">configure prefix advertisement</a> from the <strong>IP Prefixes</strong> page in your Cloudflare account home or through the <a href="/api/resources/addressing/subresources/prefixes/subresources/advertisement_status/methods/edit/">Cloudflare API</a>.</p>
<p>A common workflow is to enable prefix advertisement during an attack so that you can take advantage of Cloudflare protection and then disable advertisement once the incident is resolved. Dynamic advertisement (through the dashboard or API) does not support prefixes using BGP-controlled advertisements. Specify your preferred on-demand advertisement method during prefix onboarding.</p>
<p>To ensure smooth operation and simplify the advertisement process during an attack scenario, refer to <a href="/byoip/concepts/dynamic-advertisement/best-practices/">Dynamic advertisement: Best practices</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/755.md")
</aside>
