<p>Follow this tutorial to start testing and deploying zone configuration changes with Version Management.</p>
<h2 id="enable-versioning">Enable versioning</h2>
<p>By default, Version Management is not enabled on a zone.</p>
<p>To enable <a href="https://dash.cloudflare.com/?to=/:account/:zone/versioning">Version Management</a>:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Enable versioning</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/199.md")
</aside>
<h2 id="optional-create-additional-environments">(Optional) Create additional environments</h2>
<p>Once you <a href="/version-management/how-to/enable/">enable</a> Version Management, Cloudflare will automatically create:</p>
<ul>
<li><strong>Version Zero</strong>, think about this as the configuration of your current zone. Once default environments are created, Version Zero is automatically deployed to them, guaranteeing no disruption in your live traffic. This Version is also permanently editable. In case you decide to disable Zone Versioning, Version Zero will become your zone again.</li>
<li><strong>Global Configuration</strong>, you can find all the configurations here that are not supported by Version Management.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/198.md")
</aside>
<p>On the Environments page, you can create default environments for <strong>Production</strong>, <strong>Staging</strong>, and <strong>Development</strong>.</p>
<p>These environments each serve a specific purpose and are accessed differently:</p>
<ul>
<li><strong>Development</strong>: Meant to validate that changes work correctly. The default <a href="/version-management/reference/traffic-filters/">traffic filters</a> are that the <code>cf.zone.name</code> matches your zone name, the <code>Edge Server IP</code> is a specific value, and the request contains a cookie with <code>development=true</code>.</li>
<li><strong>Staging</strong>: Meant to test changes before sending them to <strong>Production</strong>. The default <a href="/version-management/reference/traffic-filters/">traffic filters</a> are that the <code>cf.zone.name</code> matches your zone name and the <code>Edge Server IP</code> is a specific value.</li>
<li><strong>Production</strong>: Meant to hold all configurations applied to your zone. You cannot edit the <a href="/version-management/reference/traffic-filters/">traffic filters</a> - which are just that the <code>cf.zone.name</code> is equal to your zone's name - and cannot delete this environment. This environment has a read-only check enabled, so versions promoted to this environment will become read-only as well.</li>
</ul>
<p>Based on your organization's needs, you may need to create additional environments to test and roll out changes.</p>
<br />
<p>For more details, refer to <a href="/version-management/how-to/environments/#create-environment">Create environment</a>.</p>
<h2 id="update-configurations">Update configurations</h2>
<p>Before making changes, make sure you are inside the correct version of your zone.</p>
<p>To change between different versions of your zone:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and a domain that has version management. The Global Configuration of your domain will load.</li>
<li>Go to the product or feature you wish to modify.
<ul>
<li><strong>If the product or feature is available for versioning</strong>: The last version you were working on will load.</li>
<li><strong>If the product or feature is NOT available for versioning</strong>: Your Global Configuration will load, and any changes you make will impact live traffic.</li>
</ul>
</li>
<li>Ensure that the configuration or version displayed in the domain summary bar is the one you would like to work on. If not, select the version in the domain summary bar to open the version switcher.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/197.md")
</aside>
<p>The Domain Summary is accessible from all pages and allows you to quickly switch between versions and domains.</p>
<p><img src="/assets/upstream/images/version-management/configurable-versions.png" alt="Switch between versions of your configuration" /></p>
<p>From within a version, you can update configurations just as you would with your normal zone configurations. Any changes are saved automatically.</p>
<h2 id="test-version">Test version</h2>
<p>Once you have made changes to a version, apply that version to your lowest-ranked environment.</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong>.</li>
<li>Go to <strong>Environments</strong>.</li>
<li>On your lowest-ranked environment, use the <strong>Version</strong> dropdown to select your desired version.</li>
</ol>
<p>To test your version, send requests to that environment that match the pattern specified in its <a href="/version-management/reference/traffic-filters/">traffic filters</a>.</p>
<p>For more details about what happens to these requests, refer to the version's <a href="/version-management/how-to/versions/#view-metrics">metrics</a>.</p>
<h2 id="promote-version">Promote version</h2>
<p>Next, <a href="/version-management/how-to/environments/#change-environment-version">promote</a> your version through your different environments.</p>
<p>To promote a version:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong>.</li>
<li>Select <strong>Environments</strong>.</li>
<li>On the environment in which you tested the version, select <strong>Promote</strong>. This option will only be available if the lower-ranked environment has a different version than the higher-ranked environment.</li>
</ol>
<p>Promoting a version to a read-only environment will make the version permanently read-only.</p>
<p>After promoting to each environment, test the new version in your new environment.</p>
<h2 id="repeat">Repeat</h2>
<p>For new changes to your zone, <a href="/version-management/how-to/versions/#create-version">create a new version</a> and repeat this process.</p>
<h2 id="delete-specific-version">Delete specific version</h2>
<p>The versions created in Version Management are immutable and cannot be deleted to ensure that changes are tracked and can be rolled back if needed.</p>
<p>You can, however, create a new version and clone the configuration from the previous version, making any necessary changes before promoting it to your desired environment. This solution allows you to effectively &quot;delete&quot; the old version by no longer using it.</p>
