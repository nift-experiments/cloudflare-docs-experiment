<p>A version is a collection of configurations related to your zone, such as WAF custom rules and <a href="/version-management/reference/available-configurations/">other optimization configurations</a>.</p>
<hr />
<h2 id="create-version">Create version</h2>
<p>Once you <a href="/version-management/how-to/enable/">enable</a> Version Management, Cloudflare will automatically create:</p>
<ul>
<li><strong>Version Zero</strong>, think about this as the configuration of your current zone. Once default environments are created, Version Zero is automatically deployed to them, guaranteeing no disruption in your live traffic. This Version is also permanently editable. In case you decide to disable Zone Versioning, Version Zero will become your zone again.</li>
<li><strong>Global Configuration</strong>, you can find all the configurations here that are not supported by Version Management.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15309.md")
</aside>
<p>On the Environments page, you can create default environments for <strong>Production</strong>, <strong>Staging</strong>, and <strong>Development</strong>.</p>
<p>If you need to test out different implementations of configurations at the same time or multiple types of changes, create a new version of your zone.
<strong>Zone Versioning</strong> roles are not adequate for creating a new version. A <strong>Super Administrator</strong> or <strong>Administrator</strong> role is required.</p>
<p>To create a new version:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and zone.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Version Management</strong>.</li>
<li>On an existing version, select <strong>Clone</strong>. This will copy over all configurations from that version.</li>
<li>If needed, you can also <strong>Edit Description</strong> to provide more detail about the purpose of this version.</li>
</ol>
<hr />
<h2 id="change-configurations-in-a-version">Change configurations in a version</h2>
<p>Your zone configurations are split up into two areas: <strong>Global Configuration</strong> and different versions.</p>
<ul>
<li>Global Configuration controls the configurations of a zone that is not available for versioning and, when changed, automatically apply to all versions of your zone.</li>
<li>Version configurations update configurations of a zone that is available for versioning and are:
<ul>
<li>Editable when not applied to a <a href="/version-management/reference/read-only-environments/">read-only environment</a>.</li>
<li>Applied when <a href="/version-management/how-to/environments/#change-environment-version">associated with an environment</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15308.md")
</aside>
<h3 id="editable-versions">Editable versions</h3>
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
@markup("md", "content/.markup/bodies/15307.md")
</aside>
<p>The Domain Summary is accessible from all pages and allows you to quickly switch between versions and domains.</p>
<p><img src="/assets/upstream/images/version-management/configurable-versions.png" alt="Switch between versions of your configuration" /></p>
<p>From within a version, you can update configurations just as you would with your normal zone configurations. Any changes are saved automatically.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15306.md")
</aside>
<h3 id="read-only-versions">Read-only versions</h3>
<p><strong>Production</strong> is a read-only environment by default. This means that any version associated with <strong>Production</strong> also becomes read-only. This configuration prevents another member of your account from accidentally editing the version associated with your live traffic. You can change this configuration by editing the environment.</p>
<br />
<p>In order to change configurations in a version associated with a <a href="/version-management/reference/read-only-environments/">read-only environment</a>, either:</p>
<ul>
<li><a href="/version-management/how-to/environments/#change-environment-version">Change the environment version</a> to another version and then make changes to your version.</li>
<li><a href="/version-management/how-to/environments/#edit-environment">Edit</a> the environment's configurations to remove the <strong>Read-only environment</strong> configuration. Then, promote a new version to this environment.</li>
</ul>
<hr />
<h2 id="view-metrics">View metrics</h2>
<p>Once you begin <a href="/version-management/reference/traffic-filters/">sending traffic</a> to an environment with a version applied, you can also view metrics about what happens to that traffic.</p>
<p>To view metrics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Account home</strong> page and select your account and zone.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Version Management</strong>.</li>
<li>On an existing version, select <strong>View Metrics</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15305.md")
</aside>
