<h2 id="enable-the-block-page-for-dns-policies">Enable the block page for DNS policies</h2>
<p>For DNS policies, you will need to enable the block page on a per-policy basis.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <p><strong>Traffic policies</strong> &amp;gt; <strong>Firewall policies</strong> &amp;gt; <strong>DNS</strong></p>
.</li>
<li>Select <strong>Add a policy</strong> to create a new policy, or choose the policy you want to customize and select <strong>Edit</strong>. You can only edit the block page for policies with a Block action.</li>
<li>Under <strong>Configure policy settings</strong>, turn on <strong>Modify Gateway block behavior</strong>.</li>
<li>Choose your block behavior:
<ul>
<li><strong>Use account-level block setting</strong>: Use the global block page setting configured in your account settings. The global setting can be the default Gateway block page, an <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">HTTP redirect</a>, or a <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#customize-the-block-page">custom Gateway block page</a>.</li>
<li><strong>Override account setting with URL redirect</strong>: Redirect users with a <code>307</code> HTTP redirect to a URL you specify on a policy level.</li>
</ul>
</li>
<li>(Optional) If your account-level block page setting uses a custom Gateway block page, you can turn on <strong>Add an additional message to your custom block page when traffic matches this policy</strong> to add a custom message to your custom block page when traffic is blocked by this policy. This option will replace the <strong>Message</strong> field.</li>
<li>Select <strong>Save policy</strong>.</li>
</ol>
<p>Depending on your settings, Gateway will display a block page in your users' browsers or redirect them to a specified URL when they are blocked by this policy.</p>
<h2 id="customize-the-block-page">Customize the block page</h2>
<p>You can customize the Cloudflare-hosted block page by making global changes that Gateway will display every time a user reaches your block page. Customizations will apply regardless of the type of policy (DNS or HTTP) that blocks the traffic.</p>
<p>To customize your block page:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9716.md")
</div></div>
<p>Gateway will now display a custom Gateway block page when your users visit a blocked website.</p>
<h3 id="add-a-logo-image">Add a logo image</h3>
<p>You can include an external logo image to display on your custom block page. The block page resizes all images to 146x146 pixels. The URL must be valid and no longer than 2048 characters. Accepted file types include SVG, PNG, JPEG, and GIF.</p>
