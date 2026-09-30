<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 13, 2026</time><h2 id="post-title">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="new-datasets">New datasets</h4>
<ul>
<li><strong>Email Security Post-Delivery Events</strong>: A new dataset with fields including <code>AlertID</code>, <code>CompletedAt</code>, <code>Destination</code>, <code>FinalDisposition</code>, <code>Folder</code>, <code>From</code>, <code>FromName</code>, <code>MessageID</code>, <code>MessageTimestamp</code>, <code>MicrosoftTenantID</code>, <code>Operation</code>, <code>PostfixID</code>, <code>Reasons</code>, <code>Recipient</code>, <code>RequestedAt</code>, <code>RequestedBy</code>, <code>RequestedDisposition</code>, <code>Status</code>, <code>Subject</code>, <code>Success</code>, and <code>To</code>.</li>
<li><strong>Magic Network Monitoring Flow Logs</strong>: A new dataset with fields including <code>AWSVPCFlowJSON</code>, <code>Bits</code>, <code>DestinationAS</code>, <code>DestinationAddress</code>, <code>DestinationPort</code>, <code>DeviceID</code>, <code>EgressBits</code>, <code>EgressPackets</code>, <code>Ethertype</code>, <code>FlowProtocol</code>, <code>FlowTimestamp</code>, <code>NumFlows</code>, <code>PacketID</code>, <code>Packets</code>, <code>Protocol</code>, <code>RuleIDs</code>, <code>SampleRate</code>, <code>SampleRateType</code>, <code>SamplerAddress</code>, <code>SourceAS</code>, <code>SourceAddress</code>, <code>SourcePort</code>, <code>TcpFlags</code>, and <code>Timestamp</code>.</li>
</ul>
<h4 id="updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, and <code>AISecurityUnsafeTopicCategories</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, <code>AISecurityUnsafeTopicCategories</code>, and <code>Subrequests</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div></article></div>
