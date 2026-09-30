<h2 id="geo-key-manager-v2">Geo Key Manager v2 <span class="nb-badge">Beta</span></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14062.md")
</aside>
<p>Geo Key Manager v2 gives customers flexibility when choosing the geographical boundaries of where their keys are stored.</p>
<p>Using the <code>policy</code> field, customers can define policies containing allow and block lists of countries or regions where the private key should be stored.</p>
<p>To use Geo Key Manager v2 with the API, generally, follow the steps to <a href="/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate">upload a custom certificate</a>.</p>
<p>When sending the <a href="/api/resources/custom_certificates/methods/create/"><code>POST</code></a> request, include the <code>policy</code> parameter to define policies containing allow and block lists of countries or regions where the private key should be stored.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14061.md")
</aside>
<h3 id="examples">Examples</h3>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/14063.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/14064.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14060.md")
</aside>
<h2 id="geo-key-manager-v1">Geo Key Manager v1</h2>
<p>The first version of Geo Key Manager supports 3 regions: U.S., E.U., and a set of High Security Data Centers. If you would like to restrict your private key to another country or region, <a href="https://www.cloudflare.com/lp/geo-key-manager/">apply for the closed beta</a> of the new version.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14067.md")
</div></div>
