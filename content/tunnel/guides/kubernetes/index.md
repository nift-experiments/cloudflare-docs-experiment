<p><a href="https://kubernetes.io/">Kubernetes</a> is a container orchestration tool that is used to deploy applications onto physical or virtual machines, scale the deployment to meet traffic demands, and push updates without downtime. The Kubernetes cluster, or environment, where the application instances are running is connected internally through a private network. You can install the <code>cloudflared</code> daemon inside of the Kubernetes cluster in order to connect applications inside of the cluster to Cloudflare.</p>
<p>This guide will cover how to expose a Kubernetes service to the public Internet using a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14931.md")
</div> Cloudflare Tunnel. For the purposes of this example, we will deploy a basic web application alongside `cloudflared` in Google Kubernetes Engine (GKE). The same principles apply to any other Kubernetes environment (such as `minikube`, `kubeadm`, or a cloud-based Kubernetes service) where `cloudflared` can connect to Cloudflare's network.
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="locally-managed-tunnels">Locally-managed tunnels</h3>
@markup("md", "content/.markup/bodies/14930.md")
</aside>
<h2 id="architecture">Architecture</h2>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/kubernetes-tunnel.png" alt="Diagram showing how a user connects to Kubernetes services through Cloudflare Tunnel" /></p>
<p>As shown in the diagram, we recommend setting up <code>cloudflared</code> as an adjacent <a href="https://kubernetes.io/docs/concepts/workloads/controllers/deployment/">deployment</a> to the application deployments. Having a separate Kubernetes deployment for <code>cloudflared</code> allows you to scale <code>cloudflared</code> independently of the application. In the <code>cloudflared</code> deployment, you can spin up <a href="/tunnel/configuration/#replicas-and-high-availability">multiple replicas</a> running the same Cloudflare Tunnel — there is no need to build a dedicated tunnel for each <code>cloudflared</code> pod. Each <code>cloudflared</code> replica / pod can reach all Kubernetes services in the cluster.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14928.md")
</aside>
<p>Once the cluster is connected to Cloudflare, you can configure Cloudflare Tunnel routes to control how <code>cloudflared</code> will proxy traffic to services within the cluster. For example, you may wish to publish certain Kubernetes applications to the Internet and restrict other applications to internal Cloudflare One Client users.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To complete the following procedure, you will need:</p>
<ul>
<li><a href="https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project">A Google Cloud Project</a></li>
<li><a href="/fundamentals/manage-domains/add-site/">A zone on Cloudflare</a></li>
</ul>
<h2 id="1-create-a-gke-cluster"><ol>
<li>Create a GKE cluster</li>
</ol></h2>
<p>To create a new Kubernetes cluster in Google Cloud:</p>
<ol>
<li>Open <a href="https://console.cloud.google.com/">Google Cloud</a> and go to <strong>Kubernetes Engine</strong>.</li>
<li>In <strong>Clusters</strong>, select <strong>Create</strong>.</li>
<li>Name the cluster. In this example, we will name it <code>cloudflare-tunnel</code>.</li>
<li>(Optional) Choose your desired region and other cluster specifications. For this example, we will use the default specifications.</li>
<li>Select <strong>Create</strong>.</li>
<li>To connect to the cluster:
<ol>
<li>Select the three-dot menu.</li>
<li>Select <strong>Connect</strong>.</li>
<li>Select <strong>Run in Cloud Shell</strong> to open a terminal in the browser.</li>
<li>Select <strong>Authorize</strong>.</li>
<li>Press <code>Enter</code> to run the pre-populated <code>gcloud</code> command.</li>
<li>(Recommended) In the Cloud Shell menu, select <strong>Open Editor</strong> to launch the built-in IDE.</li>
</ol>
</li>
<li>In the Cloud Shell terminal, run the following command to check the cluster status:</li>
</ol>
<pre><code class="language-sh">kubectl get all&#10;</code></pre>
<pre><code class="language-sh">NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE&#10;service/kubernetes   ClusterIP   34.118.224.1   &lt;none&gt;        443/TCP   15m&#10;</code></pre>
<h2 id="2-create-pods-for-the-web-app"><ol start="2">
<li>Create pods for the web app</li>
</ol></h2>
<p>A pod represents an instance of a running process in the cluster. In this example, we will deploy the <a href="https://httpbin.org/">httpbin</a> application with two pods and make the pods accessible inside the cluster at <code>httpbin-service:80</code>.</p>
<ol>
<li>Create a folder for your Kubernetes manifest files:</li>
</ol>
<pre><code class="language-sh">mkdir tunnel-example&#10;</code></pre>
<ol start="2">
<li>Change into the directory:</li>
</ol>
<pre><code class="language-sh">cd tunnel-example&#10;</code></pre>
<ol start="3">
<li>In the <code>tunnel-example</code> directory, create a new file called <code>httpbin.yaml</code>. This file defines the Kubernetes deployment for the httpbin app.</li>
</ol>
<pre><code class="language-yaml">apiVersion: apps/v1&#10;kind: Deployment&#10;metadata:&#10;  name: httpbin-deployment&#10;  namespace: default&#10;spec:&#10;  replicas: 2&#10;  selector:&#10;    matchLabels:&#10;      app: httpbin&#10;  template:&#10;    metadata:&#10;      labels:&#10;        app: httpbin&#10;    spec:&#10;      containers:&#10;        &#45; name: httpbin&#10;          image: kennethreitz/httpbin:latest&#10;          imagePullPolicy: IfNotPresent&#10;          ports:&#10;            &#45; containerPort: 80&#10;</code></pre>
<ol start="4">
<li>Create a new <code>httpbinsvc.yaml</code> file. This file defines a Kubernetes service that allows other apps in the cluster (such as <code>cloudflared</code>) to access the set of httpbin pods.</li>
</ol>
<pre><code class="language-yaml">apiVersion: v1&#10;kind: Service&#10;metadata:&#10;  name: httpbin-service&#10;  namespace: default&#10;spec:&#10;  type: LoadBalancer&#10;  selector:&#10;    app: httpbin&#10;  ports:&#10;    &#45; port: 80&#10;      targetPort: 80&#10;</code></pre>
<ol start="5">
<li>Use the following command to run the application inside the cluster:</li>
</ol>
<pre><code class="language-sh">kubectl create -f httpbin.yaml -f httpbinsvc.yaml&#10;</code></pre>
<ol start="6">
<li>Check the status of your deployment:</li>
</ol>
<pre><code class="language-sh">kubectl get all&#10;</code></pre>
<pre><code class="language-sh">NAME                                     READY   STATUS    RESTARTS   AGE&#10;pod/httpbin-deployment-bc6689c5d-b5ftk   1/1     Running   0          79s&#10;pod/httpbin-deployment-bc6689c5d-cbd9m   1/1     Running   0          79s&#10;&#10;NAME                      TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)        AGE&#10;service/httpbin-service   LoadBalancer   34.118.225.147   34.75.201.60   80:31967/TCP   79s&#10;service/kubernetes        ClusterIP      34.118.224.1     &lt;none&gt;         443/TCP        24h&#10;&#10;NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE&#10;deployment.apps/httpbin-deployment   2/2     2            2           79s&#10;&#10;NAME                                           DESIRED   CURRENT   READY   AGE&#10;replicaset.apps/httpbin-deployment-bc6689c5d   2         2         2       79s&#10;</code></pre>
<h2 id="3-create-a-tunnel"><ol start="3">
<li>Create a tunnel</li>
</ol></h2>
<p>To create a Cloudflare Tunnel:</p>
<ol>
<pre><code>&lt;li&gt;&#10;	In the &lt;a href=&quot;https://dash.cloudflare.com/&quot;&gt;Cloudflare dashboard&lt;/a&gt;,&#10;	go to &lt;strong&gt;Networking&lt;/strong&gt; &amp;gt; &lt;strong&gt;Tunnels&lt;/strong&gt;.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Select &lt;strong&gt;Create a tunnel&lt;/strong&gt;.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Enter a name for your tunnel (for example, &lt;code&gt;gke-tunnel&lt;/code&gt;).&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Select &lt;strong&gt;Create Tunnel&lt;/strong&gt;.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	&lt;p&gt;&#10;		Choose your operating system and select{&quot; &quot;}&#10;		&lt;strong&gt;Docker&lt;/strong&gt;.&#10;	&lt;/p&gt;&#10;	&lt;p&gt;&#10;		Applications must be packaged into a containerized image before you can&#10;		run it in Kubernetes. Therefore, we will use the &lt;code&gt;cloudflared&lt;/code&gt;{&quot; &quot;}&#10;		Docker container image to deploy the tunnel in Kubernetes.&#10;	&lt;/p&gt;&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Instead of running the installation command, copy just the token value&#10;	rather than the whole command. The token value is of the form{&quot; &quot;}&#10;	&lt;code&gt;eyJhIjoiNWFiNGU5Z...&lt;/code&gt; You will need the token for the Kubernetes&#10;	manifest file.&#10;&lt;/li&gt;&#10;</code></pre>
</ol>
<p>Leave the Cloudflare Tunnel browser tab open while we focus on the Kubernetes deployment.</p>
<h2 id="4-store-the-tunnel-token"><ol start="4">
<li>Store the tunnel token</li>
</ol></h2>
<p><code>cloudflared</code> uses a tunnel token to run a remotely-managed Cloudflare Tunnel. You can store the tunnel token in a <a href="https://kubernetes.io/docs/concepts/configuration/secret/">Kubernetes secret</a>.</p>
<ol>
<li>In GKE Cloud Shell, create a <code>tunnel-token.yaml</code> file with the following content. Make sure to replace <code>&lt;YOUR_TUNNEL_TOKEN&gt;</code> with your tunnel token (<code>eyJhIjoiNWFiNGU5Z...</code>).</li>
</ol>
<pre><code class="language-yaml">apiVersion: v1&#10;kind: Secret&#10;metadata:&#10;  name: tunnel-token&#10;stringData:&#10;  token: &lt;YOUR_TUNNEL_TOKEN&gt;&#10;</code></pre>
<ol start="2">
<li>Create the secret:</li>
</ol>
<pre><code class="language-sh">kubectl create -f tunnel-token.yaml&#10;</code></pre>
<ol start="3">
<li>Check the newly created secret:</li>
</ol>
<pre><code class="language-sh">kubectl get secrets&#10;</code></pre>
<pre><code class="language-sh">NAME        TYPE     DATA   AGE&#10;tunnel-token   Opaque   1      100s&#10;</code></pre>
<h2 id="5-create-pods-for-cloudflared"><ol start="5">
<li>Create pods for cloudflared</li>
</ol></h2>
<p>To run the Cloudflare Tunnel in Kubernetes:</p>
<ol>
<li>Create a Kubernetes deployment for a remotely-managed Cloudflare Tunnel:</li>
</ol>
<pre><code class="language-yaml">apiVersion: apps/v1&#10;kind: Deployment&#10;metadata:&#10;  name: cloudflared-deployment&#10;  namespace: default&#10;spec:&#10;  replicas: 2&#10;  selector:&#10;    matchLabels:&#10;      pod: cloudflared&#10;  template:&#10;    metadata:&#10;      labels:&#10;        pod: cloudflared&#10;    spec:&#10;      securityContext:&#10;        sysctls:&#10;          &#35; Allows ICMP traffic (ping, traceroute) to resources behind cloudflared.&#10;          &#45; name: net.ipv4.ping_group_range&#10;            value: &quot;65532 65532&quot;&#10;      containers:&#10;        &#45; image: cloudflare/cloudflared:latest&#10;          name: cloudflared&#10;          env:&#10;            &#35; Defines an environment variable for the tunnel token.&#10;            &#45; name: TUNNEL_TOKEN&#10;              valueFrom:&#10;                secretKeyRef:&#10;                  name: tunnel-token&#10;                  key: token&#10;          command:&#10;            &#35; Configures tunnel run parameters&#10;            &#45; cloudflared&#10;            &#45; tunnel&#10;            &#45; --no-autoupdate&#10;            &#45; --loglevel&#10;            &#45; info&#10;            &#45; --metrics&#10;            &#45; 0.0.0.0:2000&#10;            &#45; run&#10;          livenessProbe:&#10;            httpGet:&#10;              &#35; Cloudflared has a /ready endpoint which returns 200 if and only if&#10;              &#35; it has an active connection to Cloudflare&#x27;s network.&#10;              path: /ready&#10;              port: 2000&#10;            failureThreshold: 1&#10;            initialDelaySeconds: 10&#10;            periodSeconds: 10&#10;</code></pre>
<ol start="2">
<li>Deploy <code>cloudflared</code> to the cluster:</li>
</ol>
<pre><code class="language-sh">kubectl create -f tunnel.yaml&#10;</code></pre>
<p>Kubernetes will install the <code>cloudflared</code> image on two pods and run the tunnel using the command <code>cloudflared tunnel --no-autoupdate --loglevel info --metrics 0.0.0.0:2000 run</code>. <code>cloudflared</code> will consume the tunnel token from the <code>TUNNEL_TOKEN</code> environment variable.</p>
<ol start="3">
<li>Check the status of your cluster:</li>
</ol>
<pre><code class="language-sh">kubectl get all&#10;</code></pre>
<pre><code class="language-sh">NAME                                          READY   STATUS    RESTARTS   AGE&#10;pod/cloudflared-deployment-6d5f9f9666-85l5w   1/1     Running   0          21s&#10;pod/cloudflared-deployment-6d5f9f9666-wb96x   1/1     Running   0          21s&#10;pod/httpbin-deployment-bc6689c5d-b5ftk        1/1     Running   0          3m36s&#10;pod/httpbin-deployment-bc6689c5d-cbd9m        1/1     Running   0          3m36s&#10;&#10;NAME                      TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)        AGE&#10;service/httpbin-service   LoadBalancer   34.118.225.147   34.75.201.60   80:31967/TCP   3m36s&#10;service/kubernetes        ClusterIP      34.118.224.1     &lt;none&gt;         443/TCP        24h&#10;&#10;NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE&#10;deployment.apps/cloudflared-deployment   2/2     2            2           22s&#10;deployment.apps/httpbin-deployment       2/2     2            2           3m37s&#10;&#10;NAME                                                DESIRED   CURRENT   READY   AGE&#10;replicaset.apps/cloudflared-deployment-6d5f9f9666   2         2         2       22s&#10;replicaset.apps/httpbin-deployment-bc6689c5d        2         2         2       3m37s&#10;</code></pre>
<p>You should see two <code>cloudflared</code> pods and two <code>httpbin</code> pods with a <code>Running</code> status. If your <code>cloudflared</code> pods keep restarting, check the <code>command</code> syntax in <code>tunnel.yaml</code> and make sure that the <a href="/tunnel/configuration/#run-parameters">tunnel run parameters</a> are in the correct order.</p>
<h2 id="6-verify-tunnel-status"><ol start="6">
<li>Verify tunnel status</li>
</ol></h2>
<p>To print logs for a <code>cloudflared</code> instance:</p>
<pre><code class="language-sh">kubectl logs pod/cloudflared-deployment-6d5f9f9666-85l5w&#10;</code></pre>
<pre><code class="language-sh">2025-06-11T22:00:47Z INF Starting tunnel tunnelID=64c359b6-e111-40ec-a3a9-199c2a656613&#10;2025-06-11T22:00:47Z INF Version 2025.6.0 (Checksum 72f233bb55199093961bf099ad62d491db58819df34b071ab231f622deff33ce)&#10;2025-06-11T22:00:47Z INF GOOS: linux, GOVersion: go1.24.2, GoArch: amd64&#10;2025-06-11T22:00:47Z INF Settings: map[loglevel:debug metrics:0.0.0.0:2000 no-autoupdate:true token:*****]&#10;2025-06-11T22:00:47Z INF Generated Connector ID: aff7c4a0-85a3-4ac9-8475-1e0aa1af8d94&#10;2025-06-11T22:00:47Z DBG Fetched protocol: quic&#10;2025-06-11T22:00:47Z INF Initial protocol quic&#10;...&#10;</code></pre>
<h2 id="7-add-a-tunnel-route"><ol start="7">
<li>Add a tunnel route</li>
</ol></h2>
<p>Now that the tunnel is up and running, we can route the httpbin service through the tunnel.</p>
<ol>
<pre><code>&lt;li&gt;&#10;	In the &lt;a href=&quot;https://dash.cloudflare.com/&quot;&gt;Cloudflare dashboard&lt;/a&gt;, go&#10;	to &lt;strong&gt;Networking&lt;/strong&gt; &amp;gt; &lt;strong&gt;Tunnels&lt;/strong&gt; and select your&#10;	tunnel.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	On the &lt;strong&gt;Routes&lt;/strong&gt; tab, select &lt;strong&gt;Add route&lt;/strong&gt; &amp;gt;{&quot; &quot;}&#10;	&lt;strong&gt;Published application&lt;/strong&gt;.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Enter a hostname for the application (for example,{&quot; &quot;}&#10;	&lt;code&gt;httpbin.&amp;lt;your-domain&amp;gt;.com&lt;/code&gt;).&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Under &lt;strong&gt;Service&lt;/strong&gt;, enter{&quot; &quot;}&#10;	&lt;code&gt;{&quot;http://httpbin-service&quot;}&lt;/code&gt;. &lt;code&gt;httpbin-service&lt;/code&gt; is the&#10;	name of the Kubernetes service defined in &lt;code&gt;httpbinsvc.yaml&lt;/code&gt;.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Select &lt;strong&gt;Add route&lt;/strong&gt;.&#10;&lt;/li&gt;&#10;</code></pre>
</ol>
<h2 id="8-test-the-connection"><ol start="8">
<li>Test the connection</li>
</ol></h2>
<p>To test, open a new browser tab and go to <code>httpbin.&lt;your-domain&gt;.com</code>. You should see the httpbin homepage.</p>
<p>You can optionally add <a href="/tunnel/integrations/#cloudflare-access">Cloudflare Access</a> to control who can access the service.</p>
