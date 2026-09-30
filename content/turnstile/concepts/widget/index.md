<p>A Turnstile widget defines how Turnstile behaves on your webpage. Each widget has a mode, a label, a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15031.md")
</div>, and a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/15032.md")
</div>. You can create multiple widgets with different configurations.
<p>Turnstile is hosted under <code>challenges.cloudflare.com</code>. Your application will connect to this origin. If your site uses a <a href="/turnstile/reference/content-security-policy/">Content Security Policy</a>, you must allow connections to this domain.</p>
<h2 id="widget-components">Widget components</h2>
<p>Each widget gets its own unique sitekey and secret key pair, and options for configurations.</p>
<table>
<thead>
<tr>
<th>Component</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sitekey</td>
<td>Public key used to invoke the Turnstile widget on your site.</td>
</tr>
<tr>
<td>Secret key</td>
<td>Private key used for server-side token validation.</td>
</tr>
<tr>
<td>Configurations</td>
<td>Mode, hostnames, appearance settings, and other options.</td>
</tr>
</tbody>
</table>
<h2 id="widget-modes">Widget modes</h2>
<p>The available modes for Turnstile widgets are <strong>Managed</strong>, <strong>Non-Interactive</strong>, and <strong>Invisible</strong>.</p>
<table>
<thead>
<tr>
<th>Widget mode</th>
<th>Description</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Managed</strong> (recommended)</td>
<td>Automatically chooses between non-interactive or checkbox challenge based on visitor risk level. No images or text to decipher.</td>
<td>Simple setup with adaptive security. Balances protection and user experience.</td>
</tr>
<tr>
<td><strong>Non-Interactive</strong></td>
<td>Displays visible widget with loading spinner. Runs challenges without requiring visitor interaction.</td>
<td>Minimize friction while showing verification is occurring.</td>
</tr>
<tr>
<td><strong>Invisible</strong></td>
<td>Runs challenges completely in the background with no visible widget or loading indicators.</td>
<td>Maximize visual experience with zero visible verification elements.</td>
</tr>
</tbody>
</table>
<h3 id="managed-mode-recommended">Managed mode (recommended)</h3>
<p>Managed mode is fully managed by Cloudflare. It automatically chooses the appropriate action based on client-side signals and risk levels. Cloudflare uses the information from the visitor to decide if an interactive challenge should be used.</p>
<p>Turnstile will only require interaction if a further check is necessary to verify that the visitor is human. When an interaction is required, the visitor will be prompted to select a box. There will be no images or text to decipher.</p>
<p>Managed mode is ideal for users who want a simple configuration without needing to fine-tune the widget's behavior.</p>
<h3 id="non-interactive-mode">Non-Interactive mode</h3>
<p>Visitors will see a widget with a loading spinner while the challenges run in their browsers. Unlike managed mode, visitors will never be required or prompted to interact with the widget.</p>
<p>Non-Interactive mode is ideal for users who want to prioritize visitor experience and do not want to add any friction on their website with a Turnstile interaction.</p>
<h3 id="invisible-mode">Invisible mode</h3>
<p>Invisible mode is similar to Non-Interactive mode where visitors will never interact with the Turnstile widget. Visitors will also not see a widget or any indication that an invisible browser challenge is in progress.</p>
<p>Invisible mode is ideal for users who want to prioritize visitor and visual experience on their website.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="link-to-cloudflare-s-turnstile-privacy-policy">Link to Cloudflare's Turnstile Privacy Policy</h3>
@markup("md", "content/.markup/bodies/15030.md")
</aside>
<hr />
<h2 id="widget-customization">Widget customization</h2>
<h3 id="sizes">Sizes</h3>
<p>Widgets can be implemented in normal, flexible, or compact sizes.</p>
<p>Refer to <a href="/turnstile/get-started/client-side-rendering/widget-configurations/">Widget configurations</a> for detailed configuration options and code examples.</p>
<h3 id="appearance-and-themes">Appearance and themes</h3>
<p>Turnstile widgets support multiple appearance modes and themes to match your website's design.</p>
<p>Refer to <a href="/turnstile/get-started/client-side-rendering/widget-configurations/">Widget configurations</a> for implementation details.</p>
<hr />
<h2 id="widget-states">Widget states</h2>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Normal widget operation states&#10;accDescr: This diagram details a Turnstile widget&#x27;s normal operation states.&#10;    A[&lt;b&gt;Loading&lt;/b&gt;&lt;br /&gt;&lt;small&gt;Widget is processing the challenge.&lt;/small&gt; ] --&gt; B[&lt;b&gt;Interaction*&lt;/b&gt;&lt;br /&gt;&lt;small&gt;Visitor needs to check the box. &lt;br /&gt;*Managed mode only.&lt;/small&gt;]&#10;    B --&gt; C[&lt;b&gt;Success&lt;/b&gt;&lt;br /&gt;&lt;small&gt;The Challenge was completed successfully.&lt;/small&gt;]&#10;</code></pre>
<h3 id="error-states">Error states</h3>
<table>
<thead>
<tr>
<th><span style="width:200px">Type</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Unknown error</td>
<td>When an unknown error occurs during the challenge, visitors will encounter this widget state. Visitors can follow the troubleshooting guidelines from the widget or refresh the page to retry the challenge.</td>
</tr>
<tr>
<td>Interaction timed out</td>
<td>When the visitor is presented with a checkbox but does not interact with it for an extended period of time. The challenge must be reissued by reloading the page or the widget.</td>
</tr>
<tr>
<td>Challenge timed out</td>
<td>When the verification was completed but no further action has been taken, the challenge outcome will no longer be valid. For example, if a Turnstile widget is on a login page and the Turnstile successfully ran, but the visitor did not log in for an extended period of time, the challenge must be reissued by reloading the page or the widget.</td>
</tr>
<tr>
<td>Outdated or unsupported browser</td>
<td>Visitors with outdated browsers or unsupported browsers will encounter this widget state. Refer to <a href="/cloudflare-challenges/reference/supported-browsers/">Supported browsers</a> for more information regarding supported browsers.</td>
</tr>
</tbody>
</table>
