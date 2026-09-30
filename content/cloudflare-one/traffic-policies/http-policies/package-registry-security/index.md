<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6493.md")
</aside>
<p>Gateway can detect software package downloads across seven major package ecosystems and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write HTTP policies using <code>pkg.*</code> selectors to allow or block package downloads at whatever granularity you need, from blocking an entire ecosystem to restricting a single package version.</p>
<h2 id="how-it-works">How it works</h2>
<p>Package detection operates entirely on the HTTP request URL structure. Gateway recognizes the API contract of each supported registry protocol, not the hostname serving the traffic. This means detection works the same way whether traffic goes to the official public registry, a self-hosted mirror, a corporate proxy registry such as Artifactory or Nexus, or any other compatible endpoint. If the URL path matches the shape of a known registry download, Gateway classifies it.</p>
<p>Detection is fail-open. If the URL cannot be classified as a package download, the request proceeds as normal non-package traffic. A classification failure will never block or break a package install.</p>
<h3 id="supported-ecosystems">Supported ecosystems</h3>
<p>Gateway detects package downloads for the following ecosystems:</p>
<table>
<thead>
<tr>
<th>Ecosystem</th>
<th>Example artifact pattern</th>
<th>Namespace</th>
</tr>
</thead>
<tbody>
<tr>
<td>npm</td>
<td><code>/{package}/-/{package}-{version}.tgz</code></td>
<td>Scope (for example, <code>@babel</code>)</td>
</tr>
<tr>
<td>PyPI</td>
<td><code>/packages/{hash}/{hash}/{hash}/{package}-{version}.whl</code></td>
<td>—</td>
</tr>
<tr>
<td>RubyGems</td>
<td><code>/gems/{package}-{version}.gem</code></td>
<td>—</td>
</tr>
<tr>
<td>Cargo</td>
<td><code>/crates/{package}/{package}-{version}.crate</code></td>
<td>—</td>
</tr>
<tr>
<td>Go</td>
<td><code>/{module}/@v/{version}.zip</code></td>
<td>Module path</td>
</tr>
<tr>
<td>Maven</td>
<td><code>/maven2/{group}/{artifact}/{version}/{artifact}-{version}.jar</code></td>
<td>Group ID</td>
</tr>
<tr>
<td>NuGet</td>
<td><code>/{package}/{version}/{package}.{version}.nupkg</code></td>
<td>—</td>
</tr>
</tbody>
</table>
<h3 id="detected-operation">Detected operation</h3>
<p>The initial release detects <strong>download</strong> operations only. Download is the one operation where the package name, version, and ecosystem are all derivable from the URL path across every supported registry. Other operations such as resolve (metadata lookups) and publish use different endpoints, hosts, or HTTP methods that require additional signal beyond the URL path.</p>
<h2 id="selectors">Selectors</h2>
<p>The following selectors are available for <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> with the Allow and Block actions:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>UI name</th>
<th>API example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pkg.ecosystem</code></td>
<td>Package Ecosystem</td>
<td><code>pkg.ecosystem == &quot;npm&quot;</code></td>
<td>The package ecosystem detected from the request URL.</td>
</tr>
<tr>
<td><code>pkg.name</code></td>
<td>Package Name</td>
<td><code>pkg.name == &quot;lodash&quot;</code></td>
<td>The package name extracted from the download URL.</td>
</tr>
<tr>
<td><code>pkg.version</code></td>
<td>Package Version</td>
<td><code>pkg.version == &quot;4.17.21&quot;</code></td>
<td>The package version extracted from the download URL. Supports exact match and ecosystem-aware comparison operators.</td>
</tr>
<tr>
<td><code>pkg.namespace</code></td>
<td>Package Namespace</td>
<td><code>pkg.namespace == &quot;@babel&quot;</code></td>
<td>The package namespace, when the ecosystem supports one. For npm this is the scope, for Maven this is the group ID, and for Go this is the module path.</td>
</tr>
<tr>
<td><code>pkg.purl</code></td>
<td>Package URL</td>
<td><code>pkg.purl == &quot;pkg:npm/lodash@4.17.21&quot;</code></td>
<td>The <a href="https://github.com/package-url/purl-spec">Package URL (PURL)</a> derived from the detected coordinates. Available in the API only.</td>
</tr>
</tbody>
</table>
<h3 id="build-expressions-in-the-dashboard">Build expressions in the dashboard</h3>
<p>In the dashboard, <strong>Package Ecosystem</strong> is the primary selector. Selecting it reveals nested fields for specifying package name, version, and namespace. The following rules apply:</p>
<ul>
<li>You must select an ecosystem before any other package fields become available.</li>
<li>You must select exactly one ecosystem to enable the nested fields. If you use the <code>in</code> or <code>not in</code> operator to match multiple ecosystems, the nested package name, version, and namespace fields are disabled.</li>
<li>You must add a package name before you can add a version constraint.</li>
<li>The namespace field is only available for ecosystems that support one. The label changes based on the selected ecosystem: <strong>Scope</strong> for npm, <strong>Group ID</strong> for Maven, and <strong>Module namespace</strong> for Go.</li>
<li>The <code>pkg.purl</code> (Package URL) selector is not available in the dashboard. Use the API to write expressions that match on PURL.</li>
</ul>
<p>When using the API directly, these selectors can be combined freely in wirefilter expressions without these constraints.</p>
<h3 id="version-comparison-operators">Version comparison operators</h3>
<p>The <code>pkg.version</code> selector supports ecosystem-aware comparison operators in addition to exact string matching. Each ecosystem uses its own native versioning semantics:</p>
<table>
<thead>
<tr>
<th>Ecosystem</th>
<th>Versioning standard</th>
</tr>
</thead>
<tbody>
<tr>
<td>npm</td>
<td>SemVer</td>
</tr>
<tr>
<td>Cargo</td>
<td>SemVer</td>
</tr>
<tr>
<td>PyPI</td>
<td>PEP 440</td>
</tr>
<tr>
<td>RubyGems</td>
<td>Gem::Version</td>
</tr>
<tr>
<td>Go</td>
<td>Go module versions</td>
</tr>
<tr>
<td>Maven</td>
<td>Maven version ordering</td>
</tr>
<tr>
<td>NuGet</td>
<td>NuGet normalization and ordering</td>
</tr>
</tbody>
</table>
<p>The following comparison operators are supported:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>API syntax</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>equals</td>
<td><code>==</code></td>
<td>Normalized equality using ecosystem-specific identity rules.</td>
</tr>
<tr>
<td>not equals</td>
<td><code>!=</code></td>
<td>Negation of normalized equality.</td>
</tr>
<tr>
<td>greater than</td>
<td><code>&gt;</code></td>
<td>Version is greater than the specified value using native ordering.</td>
</tr>
<tr>
<td>greater than or equal</td>
<td><code>&gt;=</code></td>
<td>Version is greater than or equal to the specified value.</td>
</tr>
<tr>
<td>less than</td>
<td><code>&lt;</code></td>
<td>Version is less than the specified value.</td>
</tr>
<tr>
<td>less than or equal</td>
<td><code>&lt;=</code></td>
<td>Version is less than or equal to the specified value.</td>
</tr>
</tbody>
</table>
<p>When a version string cannot be parsed by the ecosystem's versioning rules, or when the detected ecosystem does not match the comparison context, the comparison returns no match. This includes <code>!=</code>, meaning an unparseable version does not match anything.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6492.md")
</aside>
<h2 id="example-policies">Example policies</h2>
<h3 id="block-all-downloads-from-a-specific-ecosystem">Block all downloads from a specific ecosystem</h3>
<p>To block all PyPI package downloads across your organization:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>pypi</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;pypi&quot;&#10;</code></pre>
<h3 id="block-a-specific-package">Block a specific package</h3>
<p>To block a known malicious or unwanted npm package regardless of version:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>npm</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Package Name</td>
<td>is</td>
<td><code>event-stream</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;npm&quot; and pkg.name == &quot;event-stream&quot;&#10;</code></pre>
<h3 id="block-vulnerable-versions-of-a-package">Block vulnerable versions of a package</h3>
<p>To block all versions of <code>lodash</code> below <code>4.17.21</code>, which is the version that patched CVE-2021-23337:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>npm</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Package Name</td>
<td>is</td>
<td><code>lodash</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Package Version</td>
<td>less than</td>
<td><code>4.17.21</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;npm&quot; and pkg.name == &quot;lodash&quot; and pkg.version &lt; &quot;4.17.21&quot;&#10;</code></pre>
<h3 id="restrict-packages-to-a-sanctioned-registry-mirror">Restrict packages to a sanctioned registry mirror</h3>
<p>To allow npm package downloads only through your corporate Artifactory instance and block all other npm downloads, create two policies:</p>
<p><strong>Policy 1 - Allow sanctioned mirror (higher priority):</strong></p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>npm</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Host</td>
<td>is</td>
<td><code>npm.internal.example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;npm&quot; and http.request.host == &quot;npm.internal.example.com&quot;&#10;</code></pre>
<p><strong>Policy 2 - Block all other npm downloads (lower priority):</strong></p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>npm</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;npm&quot;&#10;</code></pre>
<p>Because detection is based on the registry protocol rather than the hostname, both the public <code>registry.npmjs.org</code> and your internal mirror at <code>npm.internal.example.com</code> are detected as npm traffic. Policy 1 (at higher priority) allows the sanctioned mirror, and Policy 2 blocks everything else.</p>
<h3 id="block-a-specific-package-unless-from-a-sanctioned-host">Block a specific package unless from a sanctioned host</h3>
<p>To allow downloads of a sensitive internal package only through your corporate registry, blocking it from all other sources:</p>
<p><strong>Policy 1 - Allow from sanctioned host (higher priority):</strong></p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>npm</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Package Namespace</td>
<td>is</td>
<td><code>@acme</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Package Name</td>
<td>is</td>
<td><code>internal-sdk</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Host</td>
<td>is</td>
<td><code>npm.internal.example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;npm&quot; and pkg.namespace == &quot;@acme&quot; and pkg.name == &quot;internal-sdk&quot; and http.request.host == &quot;npm.internal.example.com&quot;&#10;</code></pre>
<p><strong>Policy 2 - Block from all other hosts (lower priority):</strong></p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>is</td>
<td><code>npm</code></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Package Namespace</td>
<td>is</td>
<td><code>@acme</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Package Name</td>
<td>is</td>
<td><code>internal-sdk</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>Wirefilter expression:</p>
<pre><code class="language-txt">pkg.ecosystem == &quot;npm&quot; and pkg.namespace == &quot;@acme&quot; and pkg.name == &quot;internal-sdk&quot;&#10;</code></pre>
<h2 id="detection-and-mirrors">Detection and mirrors</h2>
<p>Package detection classifies traffic based on the URL path structure of each registry's download API. It does not rely on matching against a list of known registry hostnames. This design means that any server serving packages using a compatible URL layout is detected the same way, whether it is:</p>
<ul>
<li>The official public registry (for example, <code>registry.npmjs.org</code> or <code>pypi.org</code>)</li>
<li>A corporate proxy registry such as JFrog Artifactory, Sonatype Nexus, or AWS CodeArtifact</li>
<li>A self-hosted mirror</li>
<li>A CDN-fronted registry endpoint</li>
</ul>
<p>The <code>http.request.host</code> selector remains available for policies that need to distinguish between specific registry hosts. By combining <code>pkg.*</code> selectors with <code>http.request.host</code>, you can write rules that apply different actions depending on where the package is being fetched from.</p>
<h2 id="logging">Logging</h2>
<p>When Gateway detects a package download, the package metadata is included in the Gateway HTTP log. This data is available in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a> and through <a href="/logs/logpush/logpush-job/datasets/account/gateway_http/">Logpush</a>.</p>
<h3 id="activity-log-fields">Activity Log fields</h3>
<p>The following package fields are available in the Gateway Activity Log:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Package Ecosystem</td>
<td>The detected registry type (for example, <code>npm</code>, <code>pypi</code>, <code>cargo</code>).</td>
</tr>
<tr>
<td>Package URL (PURL)</td>
<td>The Package URL string derived from the detected coordinates (for example, <code>pkg:npm/lodash@4.17.21</code>).</td>
</tr>
</tbody>
</table>
<h3 id="logpush-fields">Logpush fields</h3>
<p>Package metadata is available in the <code>PackageInfo</code> object in the <code>gateway_http</code> Logpush dataset:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>PackageInfo.Ecosystem</code></td>
<td><code>string</code></td>
<td>The detected package ecosystem.</td>
</tr>
<tr>
<td><code>PackageInfo.Namespace</code></td>
<td><code>string</code></td>
<td>The package namespace, if applicable.</td>
</tr>
<tr>
<td><code>PackageInfo.Name</code></td>
<td><code>string</code></td>
<td>The package name.</td>
</tr>
<tr>
<td><code>PackageInfo.Version</code></td>
<td><code>string</code></td>
<td>The package version string.</td>
</tr>
<tr>
<td><code>PackageInfo.Purl</code></td>
<td><code>string</code></td>
<td>The Package URL string.</td>
</tr>
</tbody>
</table>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Package detection requires <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> to be turned on. Packages downloaded over connections that bypass TLS inspection (due to Do Not Inspect policies or applications on the <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#inspection-limitations">inspection limitations list</a>) are not detected.</li>
<li>Some language runtimes and HTTP clients maintain their own certificate trust stores separate from the operating system. If the certificate used for inspection (such as the Cloudflare managed certificate) is only installed in the OS trust store, package downloads from these clients may fail with certificate verification errors. Refer to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">Install certificate manually</a> for instructions on adding the certificate to application-specific trust stores, including Python, Node.js, Ruby, Rust, Java, and Go.</li>
<li>Only <strong>download</strong> operations are detected. Metadata lookups (resolve), package publishing, and other registry operations are not classified.</li>
<li>Version comparison uses each ecosystem's native ordering rules. Cross-ecosystem version comparisons are not supported.</li>
<li>Ecosystem-specific range syntax (such as npm <code>^1.2.3</code>, PyPI <code>~=1.4</code>, or Maven interval notation) is not supported. Use the individual comparison operators (<code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>) instead.</li>
</ul>
