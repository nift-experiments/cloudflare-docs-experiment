<p>Consider the sections below to learn how to set up address maps.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3778.md")
</aside>
<h2 id="create-address-maps">Create address maps</h2>
<p>If you are using BYOIP, refer to the following steps. If you have <a href="/byoip/concepts/static-ips/">static IPs</a>, Cloudflare creates an address map during the static IP onboarding process, meaning you may only <a href="#manage-address-maps">edit</a> the Cloudflare-created map.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3781.md")
</div></div>
<h2 id="manage-address-maps">Manage address maps</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3784.md")
</div></div>
<h2 id="non-sni-support">Non-SNI support</h2>
<p>If your visitors use devices that have not been updated since 2011, they may not have <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3785.md")
</div> support. For further context, refer to [browser compatibility](/ssl/reference/browser-compatibility/#non-sni-support).
<p>Use address maps to specify a hostname as default SNI. This will be used whenever Cloudflare receives a non-SNI TLS handshake.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3773.md")
</aside>
<ol>
<li>If you have not already, create an address map. Refer to the <a href="#create-address-maps">section above</a> or to the <a href="/api/resources/addressing/subresources/address_maps/methods/create/">Create Address Map</a> API endpoint.</li>
<li>Take note of the address map <code>id</code>. If needed, you can use the <a href="/api/resources/addressing/subresources/address_maps/methods/list/">List Address Maps</a> endpoint to get it.</li>
<li>Make sure you add the desired IPs to the address map. Cloudflare will respond with the default SNI on those IPs. Use the dashboard or refer to <a href="/api/resources/addressing/subresources/address_maps/subresources/ips/methods/update/">Add An IP To An Address Map</a>.</li>
<li>Configure the <code>default_sni</code> value on the address map created in step 1. Refer to the <a href="/api/resources/addressing/subresources/address_maps/methods/edit/">Update Address Map</a> API endpoint for details. The default SNI can be any valid domain or subdomain owned by your account.</li>
</ol>
<h3 id="spectrum-https-applications">Spectrum HTTPS applications</h3>
<p>Default SNI for Spectrum can only be created via API using the <a href="/api/resources/addressing/subresources/address_maps/methods/create/">Create Address Map</a> endpoint.</p>
<p>Do not include any membership in your command. Your API command should resemble the following:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/address_maps \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;default_sni&quot;,&#10;  &quot;default_sni&quot;: &quot;sni.example.com&quot;,&#10;  &quot;enabled&quot;: false,&#10;  &quot;ips&quot;: [&#10;    &quot;192.0.0.1&quot;&#10;  ],&#10;  &quot;memberships&quot;: []&#10;}&#x27;</code></pre>
