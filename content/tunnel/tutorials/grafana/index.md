---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/tutorials/grafana/
  description: This tutorial covers how to create the metrics endpoint and set up the Prometheus server.
  full_title: Monitor Cloudflare Tunnel with Grafana · Cloudflare Docs
  head_html: <title>Monitor Cloudflare Tunnel with Grafana · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial covers how to create the metrics endpoint and set up the Prometheus server."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/tutorials/grafana/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/tutorials/grafana/index.md"><meta property="og:title" content="Monitor Cloudflare Tunnel with Grafana · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial covers how to create the metrics endpoint and set up the Prometheus server."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/tutorials/grafana/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="Grafana,Integration"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/tutorials/grafana/#page","headline":"Monitor Cloudflare Tunnel with Grafana \u00b7 Cloudflare Docs","description":"This tutorial covers how to create the metrics endpoint and set up the Prometheus server.","url":"https://developers.cloudflare.com/tunnel/tutorials/grafana/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Grafana","Integration"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/tutorials/grafana/
  schema: 1
---
<p><a href="https://grafana.com/">Grafana</a> is a dashboard tool that visualizes data stored in other databases. You can use Grafana to convert your <a href="/tunnel/observability/#metrics">tunnel metrics</a> into actionable insights.</p>
<p>It is not possible to push metrics directly from <code>cloudflared</code> to Grafana. Instead, <code>cloudflared</code> runs a <a href="https://prometheus.io">Prometheus</a> metrics endpoint, which a Prometheus server periodically scrapes. Grafana then uses Prometheus as a data source to present metrics to the administrator.</p>
<pre tabindex="0"><code class="language-mermaid">flowchart LR&#10;&#10;  subgraph 192.168.1.1&#10;  A[cloudflared]--&gt;B[Metrics endpoint]&#10;  end&#10;&#10;  B---&gt;C&#10;  subgraph 192.168.1.2&#10;  C[Prometheus server]--&gt;D[Grafana dashboard]&#10;  end&#10;</code></pre>
<p>This tutorial covers how to create the metrics endpoint, set up the Prometheus server, and view the data in Grafana.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>You will need a Cloudflare Tunnel. To create a tunnel, refer to our <a href="/tunnel/get-started/">getting started guide</a>.</li>
</ul>
<h2 id="create-the-metrics-endpoint">Create the metrics endpoint</h2>
<p>If your tunnel was created via the CLI, run the following command on the <code>cloudflared</code> server (<code>192.168.1.1</code>):</p>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel --metrics 192.168.1.1:60123 run my-tunnel&#10;</code></pre>
<p>If your tunnel was created via the dashboard, the <a href="/tunnel/reference/run-parameters/#metrics"><code>--metrics</code></a> flag must be added to your <code>cloudflared</code> system service configuration. Refer to <a href="/tunnel/reference/run-parameters/#add-run-parameters-to-tunnel-service">Add tunnel run parameters</a> for instructions on how to do this.</p>
<h2 id="set-up-prometheus">Set up Prometheus</h2>
<p>On the Prometheus and Grafana server (<code>192.168.1.2</code>):</p>
<ol>
<li>
<p><a href="https://prometheus.io/download/">Download</a> Prometheus.</p>
</li>
<li>
<p>Extract Prometheus:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">tar xvfz prometheus-*.tar.gz&#10;cd prometheus-*&#10;</code></pre>
<ol start="3">
<li>Open <code>prometheus.yml</code> in a text editor and add the <code>cloudflared</code> job to the end of the file:</li>
</ol>
<pre tabindex="0"><code class="language-yml">&#35; my global config&#10;global:&#10;  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.&#10;  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.&#10;  &#35; scrape_timeout is set to the global default (10s).&#10;&#10;&#35; Alertmanager configuration&#10;alerting:&#10;  alertmanagers:&#10;    &#45; static_configs:&#10;        &#45; targets:&#10;          &#35; - alertmanager:9093&#10;&#10;&#35; Load rules once and periodically evaluate them according to the global &#x27;evaluation_interval&#x27;.&#10;rule_files:&#10;  &#35; - &quot;first_rules.yml&quot;&#10;  &#35; - &quot;second_rules.yml&quot;&#10;&#10;&#35; A scrape configuration containing exactly one endpoint to scrape:&#10;&#35; Here it&#x27;s Prometheus itself.&#10;scrape_configs:&#10;  &#35; The job name is added as a label `job=&lt;job_name&gt;` to any timeseries scraped from this config.&#10;  &#45; job_name: &quot;prometheus&quot;&#10;&#10;    &#35; metrics_path defaults to &#x27;/metrics&#x27;&#10;    &#35; scheme defaults to &#x27;http&#x27;.&#10;&#10;    static_configs:&#10;      &#45; targets: [&quot;localhost:9090&quot;] ## Address of Prometheus dashboard&#10;&#10;  &#45; job_name: &quot;cloudflared&quot;&#10;    static_configs:&#10;      &#45; targets: [&quot;198.168.1.1:60123&quot;] ## cloudflared server IP and the --metrics port configured for the tunnel&#10;</code></pre>
<ol start="4">
<li>Start Prometheus:</li>
</ol>
<pre tabindex="0"><code class="language-sh">./prometheus --config.file=&quot;prometheus.yml&quot;&#10;</code></pre>
<p>You can optionally configure Prometheus to run as a service so that it does not need to be manually started if the machine reboots.</p>
<ol start="5">
<li>
<p>Open a browser and go to <code>http://localhost:9090/</code>. You should be able to access the Prometheus dashboard.</p>
</li>
<li>
<p>To verify that Prometheus is fetching tunnel metrics, enter <code>cloudflared_tunnel_total_requests</code> into the expression console and select <strong>Execute</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/secure-origin-connections/monitor-tunnels/Prometheus-dashboard.png" alt="Prometheus dashboard showing tunnel metrics data" /></p>
<p>Refer to <a href="/tunnel/observability/#metrics">Available metrics</a> to check what other metrics are available.</p>
<h2 id="connect-grafana-to-prometheus">Connect Grafana to Prometheus</h2>
<ol>
<li>
<p><a href="https://grafana.com/grafana/download">Download</a> and install Grafana.</p>
</li>
<li>
<p>Start Grafana as a system service:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo systemctl daemon-reload&#10;sudo systemctl start grafana-server&#10;</code></pre>
<ol start="3">
<li>Verify that Grafana is running:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo systemctl status grafana-server&#10;</code></pre>
<ol start="4">
<li>
<p>Open a browser and go to <code>http://localhost:3000/</code>. The default HTTP port that Grafana listens to is <code>3000</code> unless you have configured a different port.</p>
</li>
<li>
<p>On the sign-in page, enter your Grafana credentials.</p>
<p>To test without an account, you can enter <code>admin</code> for both the username and password and skip the password change step.</p>
</li>
<li>
<p>In Grafana, go to <strong>Connections</strong> &gt; <strong>Data sources</strong>.</p>
</li>
<li>
<p>Select <strong>Add a new data source</strong> and select <strong>Prometheus</strong>.</p>
</li>
<li>
<p>In the <strong>Prometheus server URL</strong> field, enter the IP address and port of your Prometheus dashboard (<code>http://localhost:9090</code>).</p>
</li>
<li>
<p>Select <strong>Save &amp; test</strong>.</p>
</li>
</ol>
<h2 id="build-grafana-dashboard">Build Grafana dashboard</h2>
<ol>
<li>In Grafana, go to <strong>Dashboards</strong> &gt; <strong>New</strong> &gt; <strong>New dashboard</strong>.</li>
<li>Select <strong>Add visualization</strong>.</li>
<li>Select <strong>Prometheus</strong>.</li>
<li>In the metrics field, enter <code>cloudflared_tunnel_total_requests</code> and select <strong>Run queries</strong>. You will see a graph showing the number of requests as a function of time.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/secure-origin-connections/monitor-tunnels/Grafana-dashboard.png" alt="Grafana dashboard showing a tunnel metrics graph" /></p>
<p>You can add operations to the queries to modify what is displayed. For example, you could show all tunnel requests over a recent period of time, such as a day, rather than all tunnel requests since metrics began reporting.</p>
