<p>gRPC is a Remote Procedure Call (RPC) framework that allows client applications to call methods on a remote server as if they were running on the same local machine. You can connect gRPC servers and clients to Cloudflare's global network, making it easier to build applications that use services across different data centers and environments.</p>
<p>Cloudflare Tunnel supports gRPC traffic via <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private subnet routing</a>. Public hostname deployments are not currently supported.
<br /> <br />
In this example, we will connect a gRPC server to Cloudflare using the
<code>cloudflared</code> <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/5263.md")
</div>, secure
the server with Gateway policies, and open a gRPC channel to the server using
the Cloudflare One Client.
<h2 id="1-set-up-a-grpc-server"><ol>
<li>Set up a gRPC server</li>
</ol></h2>
<ol>
<li>
<p>To set up a gRPC Python application, follow this <a href="https://grpc.io/docs/languages/python/quickstart/">quick start guide</a>.</p>
</li>
<li>
<p>Start the server:</p>
</li>
</ol>
<pre><code class="language-sh">~/grpc/examples/python/helloworld $ python3 greeter_server.py&#10;WARNING: All log messages before absl::InitializeLog() is called are written to STDERR&#10;I0000 00:00:1721770418.373806    3677 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache&#10;Server started, listening on 50051&#10;</code></pre>
<h2 id="2-connect-the-server-to-cloudflare"><ol start="2">
<li>Connect the server to Cloudflare</li>
</ol></h2>
<p>To establish a secure, outbound-only connection to Cloudflare:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Create a new tunnel</a> or edit an existing <code>cloudflared</code> tunnel.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the private IP or CIDR address of your server, and select <strong>Create route</strong>.</li>
</ol>
<h2 id="3-route-private-network-ips-through-the-cloudflare-one-client"><ol start="3">
<li>Route private network IPs through the Cloudflare One Client</li>
</ol></h2>
<p>By default, WARP excludes traffic bound for <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 space</a>, which are IP addresses typically used in private networks and not reachable from the Internet. In order for the Cloudflare One Client to send traffic to your <p>private network</p>
, you must configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> so that the IP/CIDR of your <p>private network</p>
routes through the Cloudflare One Client.</p>
<ol>
<li>First, check whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude</strong> or <strong>Include</strong> mode.</li>
<li>Edit your Split Tunnel routes depending on the mode:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5267.md")
</div></div>
<h2 id="4-recommended-create-a-gateway-policy"><ol start="4">
<li>(Recommended) Create a Gateway policy</li>
</ol></h2>
<p>You can configure <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a> to either block or allow access to the gRPC server. The following example consists of two policies: the first allows gRPC connections from devices that pass <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>, and the second blocks all other traffic. Make sure that the Allow policy has higher <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">priority</a>.</p>
<h3 id="1-allow-secured-devices"><ol>
<li>Allow secured devices</li>
</ol></h3>
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
<td>Destination Port</td>
<td>is</td>
<td><code>50051</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Destination IP</td>
<td>is</td>
<td><code>172.31.0.133</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>is</td>
<td><code>macOS firewall (Firewall)</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Passed Device Posture Checks</td>
<td>is</td>
<td><code>macOS disk encryption (Disk encryption)</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="2-block-everything-else"><ol start="2">
<li>Block everything else</li>
</ol></h3>
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
<td>Destination IP</td>
<td>in</td>
<td><code>172.31.0.0/16</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>For more details on setting up the Gateway proxy, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#4-recommended-filter-network-traffic-with-gateway">Filter network traffic with Gateway</a>.</p>
<h2 id="5-set-up-the-client"><ol start="5">
<li>Set up the client</li>
</ol></h2>
<p>gRPC clients can connect to the server by installing the Cloudflare One Client on the device and enrolling in your Zero Trust organization. When the client makes a request to a private IP exposed through Cloudflare Tunnel, WARP routes the connection through Cloudflare's network to the corresponding tunnel.</p>
<p>To set up the gRPC client:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on your device in Traffic and DNS mode.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Create device enrollment rules</a> to determine which devices can enroll to your Zero Trust organization.</li>
<li>Install gRPC on the device by following this <a href="https://grpc.io/docs/languages/python/quickstart/">quick start guide</a>.</li>
<li>Modify <code>greeter.py</code> to point to the private IP of your gRPC server. This is the same private IP configured in your <a href="#2-connect-the-server-to-cloudflare">Cloudflare Tunnel routes</a>. For example,</li>
</ol>
<pre><code class="language-python">def run():&#10;    &#35; NOTE(gRPC Python Team): .close() is possible on a channel and should be&#10;    &#35; used in circumstances in which the with statement does not fit the needs&#10;    &#35; of the code.&#10;    print(&quot;Will try to greet world ...&quot;)&#10;    with grpc.insecure_channel(&quot;172.31.0.133:50051&quot;) as channel:&#10;        stub = helloworld_pb2_grpc.GreeterStub(channel)&#10;        response = stub.SayHello(helloworld_pb2.HelloRequest(name=&quot;you&quot;))&#10;    print(&quot;Greeter client received: &quot; + response.message)&#10;</code></pre>
<h2 id="6-test-the-connection"><ol start="6">
<li>Test the connection</li>
</ol></h2>
<ol>
<li>On the client device, ensure that the Cloudflare One Client is <code>Connected</code>.</li>
<li>Run the gRPC client application:</li>
</ol>
<pre><code class="language-sh">~/grpc/examples/python/helloworld $ python3 greeter_client.py&#10;Will try to greet world ...&#10;WARNING: All log messages before absl::InitializeLog() is called are written to STDERR&#10;I0000 00:00:1721771484.489711 4414247 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache&#10;Greeter client received: Hello, you!&#10;</code></pre>
<p>You can view <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-your-local-machine">Tunnel logs</a> to validate that requests are coming into the tunnel and reaching the gRPC server as intended.</p>
