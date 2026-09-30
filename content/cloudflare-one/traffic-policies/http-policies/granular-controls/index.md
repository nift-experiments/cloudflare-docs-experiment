<p>With Application Granular Controls, you can create <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a> to control specific user actions within supported SaaS applications. This allows you to give users access to an application while restricting the actions that they can take within the application.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Application Granular Controls, you must:</p>
<ul>
<li>Install a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Cloudflare certificate</a> or a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/">custom certificate</a> on your users' devices.</li>
<li>Turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a>.</li>
<li>Turn on the <a href="/cloudflare-one/traffic-policies/proxy/#turn-on-the-gateway-proxy">Gateway proxy</a>.</li>
<li>(Optional) If an application uses HTTP/3, turn on the <a href="/cloudflare-one/traffic-policies/http-policies/http3/#enable-http3-inspection">Gateway proxy for UDP traffic</a>.</li>
<li>(Optional) To turn on <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content">AI prompt logging</a>, create a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#set-a-dlp-payload-encryption-public-key">DLP payload encryption public key</a>.</li>
</ul>
<h2 id="create-a-policy-with-application-granular-controls">Create a policy with Application Granular Controls</h2>
<p>To create a Gateway HTTP policy with Application Granular Controls:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6532.md")
</div></div>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
<h2 id="control-definitions">Control definitions</h2>
<p>Gateway defines Application Granular Controls at different levels of granularity, including Application Controls and Operations.</p>
<h3 id="application-controls">Application Controls</h3>
<p>Application Controls are pre-defined controls that represent user intent, such as uploads or downloads. Cloudflare organizes sets of related operations into Application Controls for each supported application. Use Application Controls when a pre-defined grouping matches your intent.</p>
<h3 id="operations">Operations</h3>
<p>Operations are the individual API-level actions that an application uses. Use Operations for more fine-grained control than Application Controls provide — for example, blocking only certain types of downloads or blocking comments where no Application Control exists. Because each SaaS application uses a unique set of operations with its own scope and behaviors, operation-level controls may require analysis for each use case.</p>
<p>Cloudflare provides Operations based on the <a href="#application-apis">available APIs for an application</a>. For more information on how Operations map to <a href="#application-controls">Application Controls</a>, refer to <a href="#compatible-applications">Compatible applications</a>.</p>
<h4 id="operation-groups">Operation Groups</h4>
<p>Operation Groups are groupings of operations defined by the application vendor. Operation Groups are typically based on a categorization of the different functional areas of the application, such as signature requests, or the entities that the application defines, such as files or folders. These definitions vary by application. Gateway groups operations into these operation groups to match the operations with the corresponding vendor API documentation.</p>
<h3 id="dlp-payloads">DLP payloads</h3>
<p>You can use Application Granular Controls with <a href="/cloudflare-one/data-loss-prevention/">Data Loss Prevention (DLP)</a> for operations that contain scannable content. This includes operations that contain the content of uploaded or downloaded files or AI prompts. For example, when a user performs a file upload, a sequence of API operations may result, such as setting up the file metadata, uploading the file content, and finalizing the upload. When applying DLP to your Zero Trust traffic, it can be helpful to specifically target an operation that contains file content.</p>
<h2 id="application-apis">Application APIs</h2>
<p>SaaS applications typically provide multiple APIs to interact with. For each application, Application Granular Controls may support the following API types:</p>
<ul>
<li>Web Application API: These APIs are consumed by the web application that users interact with through their browser.</li>
<li>Platform API: These APIs are exposed to users to allow for programmatic interaction with the SaaS application. These are typically used by automations, scripts, or other applications.</li>
</ul>
<p><a href="#application-controls">Application Controls</a> include Operations of both API types. If both API types are available when creating HTTP policies using <a href="#operations">Operations</a>, you should select the Operations that align to the API being used, or include both for wider coverage.</p>
<h2 id="compatible-applications">Compatible applications</h2>
<p>Application Granular Controls supports the following applications:</p>
<div class="nb-data-component" data-cf-component="GranularControlApplicationsList"></div>
