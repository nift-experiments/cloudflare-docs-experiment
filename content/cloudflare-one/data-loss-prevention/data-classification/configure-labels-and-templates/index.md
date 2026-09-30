<p>Labels and templates define the classification metadata you can apply to sensitive content in Cloudflare DLP.</p>
<p>Use the <strong>Labels</strong> tab to create and manage sensitivity schemas, sensitivity levels, data tag groups, and data tags. Use the <strong>Templates</strong> tab to review Cloudflare-managed starting points for sensitivity schemas and data tag groups.</p>
<h2 id="labels">Labels</h2>
<p>Labels help you describe matched content in a consistent way.</p>
<p>Data Classification supports two label types:</p>
<ul>
<li><strong>Sensitivity schemas and levels</strong> define an ordered classification hierarchy.</li>
<li><strong>Data tag groups and tags</strong> define additional descriptors you can apply to content.</li>
</ul>
<p>You can use labels directly in custom DLP profiles and assign them through data classes.</p>
<h3 id="sensitivity-schemas-and-levels">Sensitivity schemas and levels</h3>
<p>A sensitivity schema is a named hierarchy of sensitivity levels, such as <code>Public</code>, <code>Internal</code>, <code>Confidential</code>, or <code>Restricted</code>.</p>
<p>Each schema contains one or more ordered levels. In custom DLP profiles, selecting a sensitivity level lets you match content at that level or higher within the selected schema.</p>
<h3 id="create-a-sensitivity-schema">Create a sensitivity schema</h3>
<p>When creating a sensitivity schema, you can either create a custom schema from scratch or start from a template.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Labels</strong>.</li>
<li>Select <strong>Create labels</strong>.</li>
<li>In <strong>Sensitivity schema</strong>, choose one of the following:
<ul>
<li><strong>Create a custom schema</strong> to define the schema from scratch</li>
<li><strong>Choose a template</strong> to start from a Cloudflare-managed template</li>
</ul>
</li>
<li>Enter or review the name and description.</li>
<li>Add or update the sensitivity levels you want to include, in order.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can edit the resulting sensitivity schema after creation.</p>
<h3 id="data-tag-groups-and-tags">Data tag groups and tags</h3>
<p>A data tag group contains related tags you can use to describe content beyond its sensitivity level. For example, a data tag group could contain tags for business function, data owner, or content category.</p>
<h3 id="create-a-data-tag-group">Create a data tag group</h3>
<p>When creating a data tag group, you can either create a custom group from scratch or start from a template.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Labels</strong>.</li>
<li>Select <strong>Create labels</strong>.</li>
<li>In <strong>Data tag group</strong>, choose one of the following:
<ul>
<li><strong>Create a custom group</strong> to define the group from scratch</li>
<li><strong>Choose a template</strong> to start from a Cloudflare-managed template</li>
</ul>
</li>
<li>Enter or review the name and description.</li>
<li>Add or update the data tags you want to include.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can edit the resulting data tag group after creation.</p>
<h2 id="templates">Templates</h2>
<p>Templates provide Cloudflare-managed starting points for sensitivity schemas and data tag groups.</p>
<p>Templates are not linked objects. When you build from a template, Cloudflare creates a new sensitivity schema or data tag group in your account. After that, you can edit it like any other label object you create.</p>
<p>You can start from a template in either of the following ways:</p>
<ul>
<li>from the <strong>Templates</strong> tab, by reviewing a template and selecting <strong>Build with template</strong></li>
<li>from the <strong>Labels</strong> tab, by selecting <strong>Create labels</strong> and then <strong>Choose a template</strong> inline during creation</li>
</ul>
<h3 id="build-from-a-template-from-the-templates-tab">Build from a template from the Templates tab</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Data classification</strong> &gt; <strong>Templates</strong>.</li>
<li>Select a template to review its details.</li>
<li>Select <strong>Build with template</strong>.</li>
<li>Review and customize the resulting sensitivity schema or data tag group.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>After you build from a template, the resulting object appears in the <strong>Labels</strong> tab and can be used in data classes and DLP profiles.</p>
<h2 id="use-labels-in-dlp">Use labels in DLP</h2>
<p>After you create labels, you can use them in either of the following ways:</p>
<ul>
<li>assign them to content through <a href="/cloudflare-one/data-loss-prevention/data-classification/build-a-data-class/">Build a data class</a></li>
<li>apply them directly in <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">custom DLP profiles</a></li>
</ul>
<p>In custom DLP profiles, sensitivity levels and data tags can be used directly as profile criteria, even when they are not assigned through a data class.</p>
