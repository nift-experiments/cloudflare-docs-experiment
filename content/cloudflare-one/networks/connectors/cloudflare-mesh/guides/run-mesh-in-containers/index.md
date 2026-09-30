---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/
  description: Run a Cloudflare Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments.
  full_title: Run Cloudflare Mesh in containers · Cloudflare One docs
  head_html: <title>Run Cloudflare Mesh in containers · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Run a Cloudflare Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/index.md"><meta property="og:title" content="Run Cloudflare Mesh in containers · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run a Cloudflare Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks,Containers,Docker,Kubernetes"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/#page","headline":"Run Cloudflare Mesh in containers \u00b7 Cloudflare One docs","description":"Run a Cloudflare Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD environments.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks","Containers","Docker","Kubernetes"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-mesh/guides/run-mesh-in-containers/
  schema: 1
---
<p>The <a href="https://hub.docker.com/r/cloudflare/mesh"><code>cloudflare/mesh</code></a> Docker image packages a Cloudflare Mesh node for Linux containers. It runs the Cloudflare One Client's <code>warp-svc</code> daemon headlessly in a minimal <a href="https://wolfi.dev/">Wolfi</a>-based runtime.</p>
<p>Use the container image to add Mesh nodes to Docker Compose stacks, Kubernetes clusters, and CI/CD pipelines — without installing packages on the host.</p>
<h2 id="supported-architectures">Supported architectures</h2>
<p>The <code>latest</code> tag is a multi-platform manifest. Docker automatically selects the appropriate image for the host architecture.</p>
<table>
<thead>
<tr>
<th>Architecture</th>
<th>Tag</th>
</tr>
</thead>
<tbody>
<tr>
<td>Multi-arch</td>
<td><code>latest</code></td>
</tr>
<tr>
<td>x86-64</td>
<td><code>latest-amd64</code></td>
</tr>
<tr>
<td>ARM64</td>
<td><code>latest-arm64</code></td>
</tr>
</tbody>
</table>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before starting the container, create a Mesh node and copy its token.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5170.md")
</div></div>
<p>If this is your first Mesh node, configure the <a href="/mesh/get-started/#required-account-settings">required account settings</a>. You can use the dashboard wizard, APIs, or Terraform.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5166.md")
</aside>
<h2 id="deploy-with-docker-compose">Deploy with Docker Compose</h2>
<p>Docker Compose is the recommended way to run a Mesh node alongside your application services. Add a <code>cloudflare-mesh</code> service to your <code>compose.yaml</code>:</p>
<pre tabindex="0"><code class="language-yaml">services:&#10;  cloudflare-mesh:&#10;    image: cloudflare/mesh:latest&#10;    container_name: cloudflare-mesh&#10;    cap_add:&#10;      &#45; NET_ADMIN&#10;      &#45; NET_RAW&#10;    devices:&#10;      &#45; /dev/net/tun:/dev/net/tun&#10;    environment:&#10;      MESH_NODE_TOKEN: ${MESH_NODE_TOKEN}&#10;      SRCNAT_ENABLED: &quot;true&quot;&#10;    sysctls:&#10;      net.ipv4.ip_forward: &quot;1&quot;&#10;      net.ipv6.conf.all.forwarding: &quot;1&quot;&#10;      net.ipv6.conf.default.forwarding: &quot;1&quot;&#10;    volumes:&#10;      &#45; mesh_data:/var/lib/cloudflare-warp&#10;    restart: unless-stopped&#10;&#10;volumes:&#10;  mesh_data:&#10;</code></pre>
<p>Start the stack:</p>
<pre tabindex="0"><code class="language-sh">MESH_NODE_TOKEN=&quot;&lt;YOUR-TOKEN&gt;&quot; docker compose up -d&#10;</code></pre>
<p>Verify the node is connected:</p>
<pre tabindex="0"><code class="language-sh">docker exec cloudflare-mesh warp-cli status&#10;</code></pre>
<h2 id="deploy-with-docker-cli">Deploy with Docker CLI</h2>
<p>For a standalone container without Compose:</p>
<pre tabindex="0"><code class="language-sh">docker run -d \&#10;  &#45;-name cloudflare-mesh \&#10;  &#45;-cap-add NET_ADMIN \&#10;  &#45;-cap-add NET_RAW \&#10;  &#45;-device /dev/net/tun \&#10;  &#45;-sysctl net.ipv4.ip_forward=1 \&#10;  &#45;-sysctl net.ipv6.conf.all.forwarding=1 \&#10;  &#45;-sysctl net.ipv6.conf.default.forwarding=1 \&#10;  &#45;e MESH_NODE_TOKEN=&quot;$MESH_NODE_TOKEN&quot; \&#10;  &#45;e SRCNAT_ENABLED=true \&#10;  &#45;v mesh_data:/var/lib/cloudflare-warp \&#10;  &#45;-restart unless-stopped \&#10;  cloudflare/mesh:latest&#10;</code></pre>
<h2 id="deploy-on-kubernetes">Deploy on Kubernetes</h2>
<p>This example creates a one-replica <code>StatefulSet</code> with persistent registration state. It requires a Kubernetes cluster that permits <code>NET_ADMIN</code>, <code>NET_RAW</code>, and <code>/dev/net/tun</code> host access (for example, GKE Standard).</p>
<h3 id="1-create-the-token-secret"><ol>
<li>Create the token Secret</li>
</ol></h3>
<pre tabindex="0"><code class="language-sh">kubectl create secret generic cloudflare-mesh \&#10;  &#45;-from-literal=MESH_NODE_TOKEN=&quot;$MESH_NODE_TOKEN&quot;&#10;</code></pre>
<h3 id="2-apply-the-manifest"><ol start="2">
<li>Apply the manifest</li>
</ol></h3>
<p>Save the following as <code>cloudflare-mesh.yaml</code>:</p>
<pre tabindex="0"><code class="language-yaml">apiVersion: v1&#10;kind: Service&#10;metadata:&#10;  name: cloudflare-mesh&#10;spec:&#10;  clusterIP: None&#10;  selector:&#10;    app: cloudflare-mesh&#10;&#45;--&#10;apiVersion: apps/v1&#10;kind: StatefulSet&#10;metadata:&#10;  name: cloudflare-mesh&#10;spec:&#10;  serviceName: cloudflare-mesh&#10;  replicas: 1&#10;  selector:&#10;    matchLabels:&#10;      app: cloudflare-mesh&#10;  template:&#10;    metadata:&#10;      labels:&#10;        app: cloudflare-mesh&#10;    spec:&#10;      containers:&#10;        &#45; name: mesh&#10;          image: cloudflare/mesh:latest&#10;          env:&#10;            &#45; name: MESH_NODE_TOKEN&#10;              valueFrom:&#10;                secretKeyRef:&#10;                  name: cloudflare-mesh&#10;                  key: MESH_NODE_TOKEN&#10;            &#45; name: SRCNAT_ENABLED&#10;              value: &quot;true&quot;&#10;          securityContext:&#10;            capabilities:&#10;              add:&#10;                &#45; NET_ADMIN&#10;                &#45; NET_RAW&#10;          volumeMounts:&#10;            &#45; name: warp-data&#10;              mountPath: /var/lib/cloudflare-warp&#10;            &#45; name: dev-net-tun&#10;              mountPath: /dev/net/tun&#10;      volumes:&#10;        &#45; name: dev-net-tun&#10;          hostPath:&#10;            path: /dev/net/tun&#10;            type: CharDevice&#10;  volumeClaimTemplates:&#10;    &#45; metadata:&#10;        name: warp-data&#10;      spec:&#10;        accessModes:&#10;          &#45; ReadWriteOnce&#10;        resources:&#10;          requests:&#10;            storage: 1Gi&#10;</code></pre>
<h3 id="3-verify-the-node"><ol start="3">
<li>Verify the node</li>
</ol></h3>
<pre tabindex="0"><code class="language-sh">kubectl apply -f cloudflare-mesh.yaml&#10;kubectl rollout status statefulset/cloudflare-mesh&#10;kubectl exec cloudflare-mesh-0 -- warp-cli status&#10;</code></pre>
<p>The <code>PersistentVolumeClaim</code> preserves the Mesh registration across Pod restarts.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5165.md")
</aside>
<h2 id="kubernetes-sidecar">Kubernetes sidecar</h2>
<p>To connect an application container to Mesh, add the Mesh image as a sidecar in the same Pod. Containers in a Pod share the network namespace, so the Mesh sidecar connects the application to Cloudflare without any application changes.</p>
<h3 id="1-create-the-token-secret-1"><ol>
<li>Create the token Secret</li>
</ol></h3>
<p>Create a separate Mesh node and Kubernetes Secret for the sidecar:</p>
<pre tabindex="0"><code class="language-sh">kubectl create secret generic cloudflare-mesh-sidecar \&#10;  &#45;-from-literal=MESH_NODE_TOKEN=&quot;$MESH_NODE_TOKEN&quot;&#10;</code></pre>
<h3 id="2-apply-the-manifest-1"><ol start="2">
<li>Apply the manifest</li>
</ol></h3>
<p>Save the following as <code>cloudflare-mesh-sidecar.yaml</code>:</p>
<pre tabindex="0"><code class="language-yaml">apiVersion: v1&#10;kind: Service&#10;metadata:&#10;  name: cloudflare-mesh-sidecar-headless&#10;spec:&#10;  clusterIP: None&#10;  selector:&#10;    app: cloudflare-mesh-sidecar&#10;&#45;--&#10;apiVersion: apps/v1&#10;kind: StatefulSet&#10;metadata:&#10;  name: cloudflare-mesh-sidecar&#10;spec:&#10;  serviceName: cloudflare-mesh-sidecar-headless&#10;  replicas: 1&#10;  selector:&#10;    matchLabels:&#10;      app: cloudflare-mesh-sidecar&#10;  template:&#10;    metadata:&#10;      labels:&#10;        app: cloudflare-mesh-sidecar&#10;    spec:&#10;      containers:&#10;        &#45; name: application&#10;          image: busybox:1.37.0&#10;          command:&#10;            &#45; sh&#10;            &#45; -c&#10;            &#45; |&#10;              echo &quot;Hello from the Kubernetes sidecar example&quot; &gt; /tmp/index.html&#10;              httpd -f -p 8080 -h /tmp&#10;          ports:&#10;            &#45; name: http&#10;              containerPort: 8080&#10;        &#45; name: mesh&#10;          image: cloudflare/mesh:latest&#10;          env:&#10;            &#45; name: MESH_NODE_TOKEN&#10;              valueFrom:&#10;                secretKeyRef:&#10;                  name: cloudflare-mesh-sidecar&#10;                  key: MESH_NODE_TOKEN&#10;            &#45; name: SRCNAT_ENABLED&#10;              value: &quot;true&quot;&#10;          securityContext:&#10;            capabilities:&#10;              add:&#10;                &#45; NET_ADMIN&#10;                &#45; NET_RAW&#10;          volumeMounts:&#10;            &#45; name: warp-data&#10;              mountPath: /var/lib/cloudflare-warp&#10;            &#45; name: dev-net-tun&#10;              mountPath: /dev/net/tun&#10;      volumes:&#10;        &#45; name: dev-net-tun&#10;          hostPath:&#10;            path: /dev/net/tun&#10;            type: CharDevice&#10;  volumeClaimTemplates:&#10;    &#45; metadata:&#10;        name: warp-data&#10;      spec:&#10;        accessModes:&#10;          &#45; ReadWriteOnce&#10;        resources:&#10;          requests:&#10;            storage: 1Gi&#10;&#45;--&#10;apiVersion: v1&#10;kind: Service&#10;metadata:&#10;  name: cloudflare-mesh-sidecar&#10;spec:&#10;  selector:&#10;    app: cloudflare-mesh-sidecar&#10;  ports:&#10;    &#45; name: http&#10;      port: 8080&#10;      targetPort: http&#10;</code></pre>
<h3 id="3-verify-the-sidecar"><ol start="3">
<li>Verify the sidecar</li>
</ol></h3>
<pre tabindex="0"><code class="language-sh">kubectl apply -f cloudflare-mesh-sidecar.yaml&#10;kubectl rollout status statefulset/cloudflare-mesh-sidecar&#10;kubectl exec cloudflare-mesh-sidecar-0 -c mesh -- warp-cli status&#10;</code></pre>
<h2 id="runtime-configuration">Runtime configuration</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>MESH_NODE_TOKEN</code></td>
<td><strong>Required</strong> for initial registration. Create the token under <strong>Networking</strong> &gt; <strong>Mesh</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Cloudflare dashboard</a>, or via the <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/create/">API</a>.</td>
</tr>
<tr>
<td><code>SRCNAT_ENABLED</code></td>
<td>Controls <a href="#source-nat">source NAT</a>. Defaults to <code>true</code>. Accepts <code>true</code>, <code>false</code>, <code>1</code>, or <code>0</code>.</td>
</tr>
<tr>
<td><code>/var/lib/cloudflare-warp</code></td>
<td>Stores registration state. Persist this path with a volume to maintain a stable Mesh identity across container recreation.</td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>Required capabilities and devices</summary><div class="nb-details-body">
@input("content/.markup/bodies/5171.md")
</div></details>
<h2 id="source-nat">Source NAT</h2>
<p>Source NAT (masquerading) is enabled by default (<code>SRCNAT_ENABLED=true</code>). When a Mesh node receives traffic from the Cloudflare edge and forwards it to a destination on the local network, it translates the source IP from the Mesh CGNAT address (<code>100.96.x.x</code>) to the node's own local interface IP. This ensures return traffic routes correctly without requiring static routes in your VPC or on-premise network.</p>
<p>Set <code>SRCNAT_ENABLED=false</code> only if the attached networks already have return routes to the Mesh IP range (<code>100.96.0.0/12</code>). For more details on return traffic routing, refer to <a href="/mesh/features/routes/#return-traffic-routing">Routes</a>.</p>
<h2 id="high-availability-on-kubernetes">High availability on Kubernetes</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="masque-required">MASQUE required</h3>
@markup("md", "content/.markup/bodies/5164.md")
</aside>
<p>For <a href="/mesh/features/high-availability/">high availability</a> with CIDR routes:</p>
<ol>
<li>Use the same Mesh node token across multiple replicas.</li>
<li>Give each Pod its own <code>PersistentVolumeClaim</code>.</li>
</ol>
<p>Cloudflare operates replicas in active-passive mode. If the active replica goes offline, traffic fails over to a standby automatically. A single replica provides no redundancy.</p>
<h2 id="hostname-routes">Hostname routes</h2>
<p>Containers support <a href="/mesh/features/routes/#hostname-routes">hostname routing</a>. To resolve Kubernetes Services through a hostname route, make sure the hostname matches the cluster's actual DNS suffix. The default is <code>cluster.local</code>, producing Service names like <code>service.namespace.svc.cluster.local</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="masque-required-1">MASQUE required</h3>
@markup("md", "content/.markup/bodies/5163.md")
</aside>
<h2 id="site-to-site-networking">Site-to-site networking</h2>
<p>Deploy a separate Mesh node container at each site with a separate node token for each node identity. Each node should advertise its locally reachable subnet as a <a href="/mesh/features/routes/">CIDR route</a>. Configure each site's router or workloads to send traffic for the remote subnet through the local Mesh node.</p>
<p>With <code>SRCNAT_ENABLED=true</code>, destinations see the Mesh node's local address. With source NAT disabled, the attached networks require return routes through their Mesh nodes.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="node-registers-as-a-regular-cloudflare-one-client-device">Node registers as a regular Cloudflare One Client device</h3>
<p>Confirm that the correct Mesh node token is set in <code>MESH_NODE_TOKEN</code>. Existing registration state in the persistent volume takes precedence — remove the volume only when you intentionally want to discard that registration and create a new identity.</p>
<h3 id="warp-cli-status-remains-connecting"><code>warp-cli status</code> remains Connecting</h3>
<p>Check the token, device profile, Gateway proxy, Split Tunnel configuration, outbound firewall connectivity, and container logs:</p>
<pre tabindex="0"><code class="language-sh">docker logs cloudflare-mesh&#10;</code></pre>
<h3 id="a-kubernetes-service-cannot-be-resolved">A Kubernetes Service cannot be resolved</h3>
<p>Confirm that the <a href="/mesh/features/routes/#hostname-routes">hostname route</a> matches the cluster's actual DNS suffix. The usual default is <code>cluster.local</code>, producing Service names such as <code>service.namespace.svc.cluster.local</code>.</p>
<h3 id="a-hostname-request-arrives-but-no-response-returns">A hostname request arrives but no response returns</h3>
<p>Check source NAT and return routing first. Verify <code>SRCNAT_ENABLED</code> is set to <code>true</code> or that your network has return routes to the Mesh IP range.</p>
<h3 id="check-node-status">Check node status</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="containerRuntime"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5174.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/mesh/features/routes/"><strong>Add routes</strong></a> — Make subnets behind the containerized node reachable from any device on your Mesh.</li>
<li><a href="/mesh/features/high-availability/"><strong>Enable high availability</strong></a> — Run multiple replicas for production resilience.</li>
<li><a href="/workers-vpc/examples/connect-to-cloudflare-mesh/"><strong>Connect from Workers</strong></a> — Use VPC Network bindings to reach private services from Cloudflare Workers.</li>
<li><a href="/mesh/best-practices/"><strong>Tips and best practices</strong></a> — Cloud VPC configuration, MTU tuning, and running alongside Cloudflare Tunnel.</li>
</ul>
