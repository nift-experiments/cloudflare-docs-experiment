<h2 id="2026-01-30">2026-01-30</h2><strong>Chat Pagination Overhaul</strong><p><strong>Affected SDKs:</strong> Web Core SDK 1.2.4+ and Web UI Kit 1.0.9+ (Angular/React/Web Components)</p>
<p>To streamline RealtimeKit SDK offerings, non-operational chat channel APIs have been removed. If you have a custom chat implementation using lower-level components instead of <code>rtk-chat</code>, please review the release notes thoroughly and test your implementation after upgrading.</p><h2 id="2025-11-21">2025-11-21</h2><strong>Support for legacy media engine has been removed</strong><p><strong>Affected SDKs:</strong> Web Core SDK  1.2.0+ (Angular/React/Web Components)</p>
<p>Legacy media engine support has been removed.</p>
<p>If your organization was created before March 1, 2025 and you are upgrading to <code>1.2.0</code> or above, you may experience recording issues.</p>
<p>Please contact support to migrate you to the new Cloudflare SFU media engine to ensure continued recording functionality.</p><h2 id="2025-11-21-1">2025-11-21</h2><strong>Update on meeting join issues in firefox 144+</strong><p><strong>Affected SDKs:</strong> Web Core SDK  &lt; 1.2.0 (Angular/React/Web Components)</p>
<p>In firefox 144+, users were not able to join the meetings, due to the browser's datachannel behavior change.</p>
<p>Error: <code>x.data.arrayBuffer is not a function</code></p>
<p>Please upgrade to atleast <code>v1.2.0</code> to fix this. It is advised to periodically upgrade the SDKs.</p>
