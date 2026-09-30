<p>When your <a href="/fundamentals/concepts/how-cloudflare-works/">website traffic is routed through the Cloudflare network</a>, we act as a reverse proxy. This allows Cloudflare to speed up page load time by routing packets more efficiently and caching static resources (images, JavaScript, CSS, etc.). As a result, when responding to requests and logging them, your origin server returns a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a>.</p>
<p>For example, if you install applications that depend on the incoming IP address of the original visitor, a Cloudflare IP address is logged by default. The original visitor IP address appears in an appended HTTP header called <a href="/fundamentals/reference/http-headers/#cf-connecting-ip"><code>CF-Connecting-IP</code></a>. By following our <a href="#web-server-instructions">web server instructions</a>, you can log the original visitor IP address at your origin server. If this HTTP header is not available when requests reach your origin server, check your <a href="/rules/transform/">Transform Rules</a> and <a href="/rules/transform/managed-transforms/">Managed Transforms</a> configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14697.md")
</aside>
<p>The diagram below illustrates the different ways that IP addresses are handled with and without Cloudflare.</p>
<p><img src="/assets/upstream/images/support/Restoring_IPs__1_.png" alt="The diagram illustrates the different ways that IP addresses are handled with and without Cloudflare." /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14696.md")
</aside>
<hr />
<h2 id="mod-remoteip">mod_remoteip</h2>
<p>Cloudflare no longer updates and supports <em>mod_cloudflare.</em> However, if you are using an Apache web server with an operating system such as <strong>Ubuntu Server 18.04</strong> and <strong>Debian 9 Stretch</strong>, you can use <em>mod_remoteip</em> to log your visitor’s original IP address.</p>
<p><strong>As this module was created by an outside party, we can't provide technical support for issues related to the plugin.</strong></p>
<p>To install <em>mod_remoteip</em> on your Apache web server:</p>
<ol>
<li>Enable <em>mod_remoteip</em> by issuing the following command:</li>
</ol>
<pre><code class="language-sh">sudo a2enmod remoteip&#10;</code></pre>
<ol start="2">
<li>Update the site configuration to include <em>RemoteIPHeader CF-Connecting-IP</em>, e.g. <code>/etc/apache2/sites-available/000-default.conf</code></li>
</ol>
<pre><code>ServerAdmin webmaster@localhost&#10;DocumentRoot /var/www/html&#10;ServerName remoteip.andy.support&#10;RemoteIPHeader CF-Connecting-IP&#10;ErrorLog ${APACHE_LOG_DIR}/error.log&#10;CustomLog ${APACHE_LOG_DIR}/access.log combined&#10;</code></pre>
<ol start="3">
<li>Update combined <em>LogFormat</em> entry in <code>apache.conf</code>, replacing <em>%h</em> with <em>%a in</em> <code>/etc/apache2/apache2.conf.</code> For example, if your current <em>LogFormat</em> appeared as follows</li>
</ol>
<pre><code>LogFormat &quot;%h %l %u %t \&quot;%r\&quot; %&gt;s %O \&quot;%{Referer}i\&quot; \&quot;%{User-Agent}i\&quot;&quot; combined&#10;</code></pre>
<p>you would update <em>LogFormat</em> to the following:</p>
<pre><code>LogFormat &quot;%a %l %u %t \&quot;%r\&quot; %&gt;s %O \&quot;%{Referer}i\&quot; \&quot;%{User-Agent}i\&quot;&quot; combined&#10;</code></pre>
<ol start="4">
<li>Define trusted proxy addresses by creating <code>/etc/apache2/conf-available/remoteip.conf</code> by entering the following code and <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a>:</li>
</ol>
<pre><code>RemoteIPHeader CF-Connecting-IP&#10;RemoteIPTrustedProxy 192.0.2.1 (example IP address)&#10;RemoteIPTrustedProxy 192.0.2.2 (example IP address)&#10;(repeat for all Cloudflare IPs listed at https://www.cloudflare.com/ips/)&#10;</code></pre>
<ol start="5">
<li>Enable Apache configuration:</li>
</ol>
<pre><code class="language-sh">sudo a2enconf remoteip&#10;</code></pre>
<pre><code class="language-sh">Enabling conf remoteip.&#10;To activate the new configuration, you need to run:&#10;service apache2 reload&#10;</code></pre>
<ol start="6">
<li>Test Apache configuration:</li>
</ol>
<pre><code class="language-sh">sudo apache2ctl configtest&#10;</code></pre>
<pre><code class="language-sh">Syntax OK&#10;</code></pre>
<ol start="7">
<li>Restart Apache:</li>
</ol>
<pre><code class="language-sh">sudo systemctl restart apache2&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14695.md")
</aside>
<hr />
<h2 id="mod-cloudflare">mod_cloudflare</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14694.md")
</aside>
<h3 id="installing">Installing</h3>
<p>There are two methods for installing mod_cloudflare: by downloading the Apache extension from GitHub or by adding code to your origin web server.</p>
<h4 id="downloading-packets-or-scripts-from-github">Downloading packets or scripts from GitHub</h4>
<p>If you are using an Apache web server, you can download mod_cloudflare from <a href="https://github.com/cloudflare/mod_cloudflare">GitHub</a>.</p>
<h4 id="adding-code-to-your-origin-web-server">Adding code to your origin web server</h4>
<p>If you can't install mod_cloudflare, or if there is no Cloudflare plugin available for your content management system platform to restore original visitor IP, add this code to your origin web server in or before the <code>&lt;body&gt;</code> tag on any page that needs the original visitor IPs:</p>
<pre><code class="language-php">&lt;?php if (isset($_SERVER[&#x27;HTTP_CF_CONNECTING_IP&#x27;])) $_SERVER[&#x27;REMOTE_ADDR&#x27;] = $_SERVER[&#x27;HTTP_CF_CONNECTING_IP&#x27;];?&gt;&#10;</code></pre>
<p>This command will only make the IP address available to scripts that need it. It doesn’t store the IP in your actual server logs.</p>
<h3 id="removing">Removing</h3>
<h4 id="apache">Apache</h4>
<p>To remove <em>mod_cloudflare</em>, you should comment out the Apache config line that loads <em>mod_cloudflare</em>.</p>
<p>This varies based on your Linux distribution, but for most people, if you look <code>in /etc/apache2</code>, you should be able to search to find the line:</p>
<p><code>LoadModule cloudflare_module</code></p>
<p>Comment or remove this line, then restart apache, and <em>mod_cloudflare</em> should be gone.</p>
<p>If you are running Ubuntu or Debian, you should see.</p>
<p><code>file/etc/apache2/mods-enabled/cloudflare.load</code></p>
<p>delete this file to remove <em>mod_cloudflare</em>, then restart Apache.</p>
<h4 id="nginx">Nginx</h4>
<p><em>mod_cloudflare</em> is not needed for Nginx. Use the <a href="http://nginx.org/en/docs/http/ngx_http_realip_module.html"><code>ngx_http_realip_module</code> NGINX module</a> and the configuration parameters described in the <a href="https://developers.cloudflare.com/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/#web-server-instructions">Web server instructions</a> instead.</p>
<hr />
<h2 id="web-server-instructions">Web server instructions</h2>
<p>Refer below for instructions on how to configure your web server to log original visitor IPs based on your web server type:</p>
<h3 id="apache-2-4">Apache 2.4</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14693.md")
</aside>
<ol>
<li>Make sure the following is installed:
<ul>
<li>Red Hat/Fedora<code>sudo yum install httpd-devel libtool git</code></li>
<li>Debian/Ubuntu<code>sudo apt-get install apache2-dev libtool git</code></li>
</ul>
</li>
<li>Clone the following for the most recent build of <em>mod_cloudflare</em>:
<ul>
<li>Red Hat/Fedora/Debian/Ubuntu:<code>git clone https://github.com/cloudflare/mod_cloudflare.git; cd mod_cloudflare</code></li>
</ul>
</li>
<li>Use the Apache extension tool to convert the .c file into a module:
<ul>
<li>Red Hat/Fedora/Debian/Ubuntu:<code>apxs -a -i -c mod_cloudflare.c</code></li>
</ul>
</li>
<li>Restart and verify the module is active:
<ul>
<li>Red Hat/Fedora<code>service httpd restart; httpd -M|grep cloudflare</code></li>
<li>Debian/Ubuntu:<code>sudo apachectl restart; apache2ctl -M|grep cloudflare</code></li>
</ul>
</li>
<li>If your web server is behind a load balancer, add the following line to your Apache configuration (httpd.conf usually) and replace 123.123.123.123 with your load balancer's IP address:</li>
</ol>
<pre><code>IfModule cloudflare_module&#10;CloudFlareRemoteIPHeader X-Forwarded-For&#10;CloudFlareRemoteIPTrustedProxy [insert your load balancer’s IP address]&#10;DenyAllButCloudFlare&#10;/IfModule&#10;</code></pre>
<h3 id="nginx-1">Nginx</h3>
<p>Use the <a href="http://nginx.org/en/docs/http/ngx_http_realip_module.html"><code>ngx_http_realip_module</code> Nginx module</a> and the following configuration parameters:</p>
<pre><code>&#35;example IP address&#10;set_real_ip_from 192.0.2.1; &#10;&#10;&#35;use any of the following two&#10;&#10;real_ip_header CF-Connecting-IP;&#10;&#35;real_ip_header X-Forwarded-For;&#10;</code></pre>
<p>That list of prefixes needs to be updated regularly, and we publish the full list in <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14692.md")
</aside>
<p>Also refer to: <a href="https://danielmiessler.com/blog/getting-real-ip-addresses-using-cloudflare-nginx-and-varnish/">Cloudflare and NGINX</a>.</p>
<h3 id="easyapache-and-cpanel">EasyApache and cPanel</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14691.md")
</aside>
<ol>
<li>Run the following script to install mod_cloudflare as part of EasyApache: <code>bash &lt;(curl -s https://raw.githubusercontent.com/cloudflare/mod_cloudflare/master/EasyApache/installer.sh)</code></li>
<li>Upon installing, you will need to recompile your Apache with the new mod_cloudflare plugin.</li>
<li>To fix this, open up your Apache configuration. This can typically be found in <code>/etc/apache2/apache2.conf</code>, <code>/etc/httpd/httpd.conf</code>, <code>/usr/local/apache/conf/httpd.conf</code> or another location depending on configuration. If you're unsure, ask your hosting provider.</li>
<li>At the very end add:<code>CloudflareRemoteIPTrustedProxy {LOOPBACK_ADDRESS}</code> So, if your server is located at 127.0.0.1, it will look like:<code>CloudflareRemoteIPTrustedProxy 127.0.0.1</code></li>
<li>If you have more than one server to add to the trusted proxy list, you can add them at the end: CloudflareRemoteIPTrustedProxy 127.0.0.1 127.0.0.2</li>
</ol>
<h3 id="lighttpd">Lighttpd</h3>
<p>To have Lighttpd automatically rewrite the server IP for the access logs and for your application, you can follow one of the two solutions below.</p>
<ol>
<li>Open your <strong>lighttpd.conf</strong> file and add <em>mod_extforward</em> to the <em>server.modules</em> list. It must come <strong>after</strong> <em>mod_accesslog</em> to show the real IP in the access logs</li>
<li>Add the following code block anywhere in the <strong>lighttpd.conf</strong> file after the server modules list and then restart Lighttpd</li>
</ol>
<pre><code>$HTTP[&quot;remoteip&quot;] == &quot;192.2.0.1 (example IP address)&quot;&#10;{&#10;extforward.forwarder = ( &quot;all&quot; =&gt; &quot;trust&quot; )&#10;extforward.headers = (&quot;CF-Connecting-IP&quot;)&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14690.md")
</aside>
<h3 id="litespeed-server">LiteSpeed server</h3>
<ol>
<li>Go to your LiteSpeed Web Admin Console.</li>
<li>Enable the option Use Client IP in Header in Configuration.</li>
<li>Once enabled, your access logs will now show the correct IP addresses, and even PHP's <code>$_SERVER['REMOTE_ADDR']</code> variable will contain the client real IP address, instead of a Cloudflare IP address, which in itself will resolve most problems you could hit when enabling Cloudflare on PHP-enabled web sites (like WordPress or vBulletin installs).</li>
</ol>
<h3 id="microsoft-iis">Microsoft IIS</h3>
<h4 id="for-iis-7-8">For IIS 7 - 8:</h4>
<p>Follow the directions in the <a href="https://techcommunity.microsoft.com/t5/iis-support-blog/how-to-use-x-forwarded-for-header-to-log-actual-client-ip/ba-p/873115">Microsoft Community</a>.</p>
<h4 id="for-iis-8-5-10">For IIS 8.5 - 10:</h4>
<p>From IIS 8.5 onwards, custom logging is a built-in option. Refer to <a href="http://www.iis.net/learn/get-started/whats-new-in-iis-85/enhanced-logging-for-iis85">IIS Enhanced Logging</a>.</p>
<ol>
<li>
<p>In IIS Manager, double click on <strong>Logging</strong> in the <em>Actions</em> menu of the site you are working on.</p>
</li>
<li>
<p>After this launches, select <strong>W3C</strong> as the format and then click <strong>Select Fields</strong> next to the format drop-down in the <em>Log File</em> sub-section.</p>
</li>
<li>
<p>Click on <strong>Add Field</strong> and add in <em>CF-Connecting-IP</em> header.</p>
</li>
<li>
<p>Click <strong>Ok</strong>. You should see your new entry reflected under <strong>Custom Fields</strong>. Click on <strong>Apply</strong> when you are back in the <em>Logging</em> window.</p>
</li>
<li>
<p>If this is successful, the log file should now have an underscore:You should also see the change in the fields:</p>
</li>
<li>
<p>Restart the site, then W3SVC, then the entire instance if the change doesn’t reflect immediately.When using enhanced logging in IIS 8.5+, it <strong>does not restore</strong> original visitor IP at the application level.</p>
</li>
</ol>
<h3 id="tomcat-7">Tomcat 7</h3>
<p>To have Tomcat7 automatically restore the original visitor IP to your access logs and application you will need to add <code>%{CF-Connecting-IP}i</code> into your log schema.</p>
<p>As an example, you could add the below block to your <code>server.xml</code> file.</p>
<pre><code class="language-xml">&lt;Valve className=&quot;org.apache.catalina.valves.AccessLogValve&quot; directory=&quot;logs&quot; prefix=&quot;localhost_access_log.&quot; suffix=&quot;.txt&quot; pattern=&quot;%{CF-Connecting-IP}i - %h %u %t - &amp;quot;%r&amp;quot; - %s - %b - %{CF-RAY}i&quot;/&gt;&#10;</code></pre>
<p>Which would result in your logs looking like this:</p>
<p><code>Visitor IP - Cloudflare IP - [04/Dec/2014:23:18:15 -0500] - &quot;GET / HTTP/1.1&quot; - 200 - 1895 - 193d704b85200296-SJC</code></p>
<h3 id="magento">Magento</h3>
<p>Refer to this third-party tutorial on restoring original visitor IP with <a href="https://tall-paul.co.uk/2012/03/02/magento-show-remote-ip-when-using-cloudflare/">Magento and Cloudflare</a>.</p>
<p>Similarly, Cloudflare did not write this <a href="https://marketplace.magento.com/">Magento extension</a>, but some of our customers have found it helpful.</p>
<p>As this plugin was created by an outside party, we can't provide technical support for issues related to the plugin.</p>
<h3 id="ipb-invision-power-board">IPB (Invision Power Board)</h3>
<p>To enable correct IP matching when running an Invision Power Board 3 installation through Cloudflare, follow these directions:</p>
<p>Log into your IPB installation's ACP.</p>
<ol>
<li>Click <strong>System</strong>.</li>
<li>Under Overview, click <strong>Security</strong>.</li>
<li>Under Security Center, click <strong>Security Settings</strong>.Check that <em>Trust IP addresses provided by proxies?</em> is green.</li>
</ol>
<h4 id="ipb4-description-of-trust-ip-addresses-provided-by-proxies">IPB4 description of <em>Trust IP addresses provided by proxies?</em></h4>
<p>If your network environment means requests are handled through a proxy (such as in an intranet situation in an office or university, or on a load-balanced server cluster), you may need to enable this setting so that the correct IP address is used. However, when enabled, a malicious user can abuse the system to provide a fake IP address. In most environments, this setting should be left off.</p>
<h3 id="phpbb">PHPBB</h3>
<p>If you are using an Apache server, then we would recommend installing <a href="https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html">mod_remoteip</a> to restore the visitor IP back to your logs.</p>
<p>If you do not have access to your server to install a mod, then you may be able to <a href="https://www.phpbb.com/community/viewtopic.php?p=13936406#p13936406">modify the core</a>.</p>
<h3 id="mybb-forums">MyBB forums</h3>
<p>More recent versions of MyBB include a Scrutinize User's IP address option.</p>
<p><code>Admin CP &gt; Configuration &gt; Server and Optimization Options &gt; Scrutinize User's IP address? &gt; Yes</code></p>
<p>Alternatively, you may install the <a href="https://mods.mybb.com/view/antoligy-mybb-cloudflare-management-plugin">Cloudflare management plugin</a> available for MyBB 1.6.</p>
<h4 id="mybb-1-6-0-1-6-1-1-6-2-or-1-6-3">MyBB 1.6.0, 1.6.1, 1.6.2, or 1.6.3</h4>
<ol>
<li>Navigate to <code>./inc/functions.php</code>.</li>
<li>Go to line 2790.</li>
<li>Replace:<code>if(isset($_SERVER['REMOTE_ADDR']))</code>With:<code>if(isset($_SERVER['HTTP_CF_CONNECTING_IP']))</code></li>
<li>Then, replace:<code>$ip = $_SERVER['REMOTE_ADDR'];</code>With:<code>$ip = $_SERVER['HTTP_CF_CONNECTING_IP'];</code></li>
</ol>
<h3 id="vanilla-forums">Vanilla forums</h3>
<p>A member of the Vanilla team has written a <a href="https://open.vanillaforums.com/addon/cloudflaresupport-plugin">Cloudflare plugin for Vanilla</a> to restore original visitor IP to the log files for self-hosted sites.</p>
<p>As this plugin was created by an outside party, we can't provide technical support for issues related to the plugin.MediaWiki</p>
<ol>
<li>Open <code>includes/GlobalFunctions.php</code>. At approximately line 370, change the following:<code>$forward = &quot;\t(proxied via {$_SERVER['REMOTE_ADDR']}{$forward})&quot;;</code>to<code>$forward = &quot;\t(proxied via {$_SERVER['HTTP_CF_CONNECTING_IP']}{$forward})&quot;;</code></li>
<li>Open <code>includes/ProxyTools.php</code>. At approximately line 79, find:<code>if ( isset( $_SERVER['REMOTE_ADDR'] ) ){</code>and replace with:<code>if ( isset( $_SERVER['HTTP_CF_CONNECTING_IP'] ) ){</code>The second step only applies to MediaWiki versions 1.18.0 and older. Newer versions of MediaWiki have completely rewritten ProxyTools.php and the following code is no longer present.</li>
<li>Find at approximately line 80:<code>$ipchain = array( IP::canonicalize($_SERVER['REMOTE_ADDR']) );</code>Save and upload to your origin web server.</li>
</ol>
<h4 id="for-versions-around-1-27-1">For versions around 1.27.1:</h4>
<ol>
<li>Go to line 1232 in <code>GlobalFunctions.php</code>, change <code>REMOTE_ADDR</code> to <code>HTTP_CF_CONNECTING_IP</code>.</li>
<li>Next, go to <code>WebRequest.php</code>, in lines 1151 to line 1159, change <code>REMOTE_ADDR</code> to <code>HTTP_CF_CONNECTING_IP</code>.</li>
</ol>
<h3 id="xenforo">XenForo</h3>
<p>A XenForo user has created a <a href="https://xenforo.com/community/resources/solidmean-cloudflare-detect.1595/">plugin for Cloudflare</a>.</p>
<p>As this plugin was created by an outside party, we can't provide technical support for issues related to the plugin.</p>
<ol>
<li>Open <code>library/config.php</code>.</li>
<li>At the end, add:<code>if (isset($_SERVER['HTTP_CF_CONNECTING_IP'])) { $_SERVER['REMOTE_ADDR'] = $_SERVER['HTTP_CF_CONNECTING_IP'];}</code></li>
<li>Upload and overwrite.</li>
</ol>
<h3 id="punbb">PunBB</h3>
<p>An outside party has created a <a href="http://punbb.informer.com/forums/post/147539/#p147539">module for Cloudflare and PunBB</a> that will restore original visitor IP.</p>
<p>As this plugin was created by an outside party, we can't provide technical support for issues related to the plugin.Cherokee server</p>
<ol>
<li>Launch <code>cherokee-admin</code> on your server.</li>
<li>Navigate to the <strong>Cherokee Administration interface</strong> in your web browser.</li>
<li>Select the <strong>Virtual Server</strong> for the domain that is being serviced by Cloudflare.</li>
<li>On the <em>Logging</em> tab for your selected <strong>Virtual Server</strong>, enable Accept Forwarded IPs.</li>
<li>In the <em>Accept from Hosts</em> box, enter <a href="https://www.cloudflare.com/ips/">Cloudflare's IP addresses</a>.</li>
</ol>
<h3 id="livezilla">Livezilla</h3>
<p>You can fix the IP address by changing the <code>PHP IP Server Param</code> field on the Livezilla server configuration to <code>HTTP_CF_CONNECTING_IP</code>.</p>
<h3 id="datalife-engine">Datalife Engine</h3>
<p>To restore visitor IP to DataLife Engine:</p>
<ol>
<li>Open:/engine/inc/include/functions.inc.phpFind:<code>$db_ip_split = explode( &quot;.&quot;, $_SERVER['REMOTE_ADDR'] );</code>Change to:<code>$db_ip_split = explode(&quot;.&quot;, $_SERVER['HTTP_CF_CONNECTING_IP'] );</code></li>
<li>Find:<code>$ip_split = explode( &quot;.&quot;, $_SERVER['REMOTE_ADDR'] );</code>Change to:<code>$ip_split = explode(&quot;.&quot;, $_SERVER['HTTP_CF_CONNECTING_IP'] );</code></li>
<li>Open:/engine/modules/addcomments.phpFind:<code>$_SERVER['REMOTE_ADDR'],</code>Change to:<code>$_SERVER['HTTP_CF_CONNECTING_IP'],</code></li>
<li>Find:<code>$db_ip_split = explode( &quot;.&quot;, $_SERVER['REMOTE_ADDR'] );</code>Change to:<code>$db_ip_split = explode( &quot;.&quot;, $_SERVER['HTTP_CF_CONNECTING_IP'] );</code></li>
</ol>
<h3 id="typo3">TYPO3</h3>
<p>An outside developer has created a <a href="https://extensions.typo3.org/extension/cloudflare/">Cloudflare extension for TYPO3</a> that will restore original visitor IP to your logs. The extension will also give the ability to clear your Cloudflare cache.</p>
<p>As this plugin was created by an outside party, we can't provide technical support for issues related to the plugin.</p>
<h3 id="vestacp">VestaCP</h3>
<p>If you use the hosting control panel VestaCP, you have both Nginx and Apache running on your server. Requests are proxied through Nginx before going to Apache.</p>
<p>Because of this Nginx proxy, you actually need to follow the instructions to configure Nginx to return the real visitor IP address. <a href="https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html">mod_remoteip</a> for Apache is not needed unless you disable the Nginx server for some requests. Adding <a href="https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html">mod_remoteip</a> to Apache will not conflict with the Nginx server configuration.</p>
<h3 id="node-js">node.js</h3>
<p>An outside developer has created a module to restore visitor IP called <a href="https://github.com/keverw/node_CloudFlare">node_cloudflare.</a></p>
<h3 id="haproxy">HAProxy</h3>
<p>In order to extract the original client IP in the X_FORWARDED_FOR header, you need to use the following configuration in HAProxy:</p>
<ol>
<li>Create a text file <code>CF_ips.lst</code> containing all IP ranges from <a href="https://www.cloudflare.com/en-gb/ips/">https://www.cloudflare.com/en-gb/ips/</a></li>
<li>Ensure to disable <code>option forwardfor</code> in HAProxy</li>
</ol>
<p>HAProxy config:</p>
<pre><code>acl from_cf src -f /path/to/CF_ips.lst&#10;acl cf_ip_hdr req.hdr(CF-Connecting-IP) -m found&#10;http-request set-header X-Forwarded-For %[req.hdr(CF-Connecting-IP)] if from_cf cf_ip_hdr&#10;</code></pre>
<h3 id="envoy-gateway">Envoy Gateway</h3>
<p>To extract the original client IP for your Envoy Gateway, set a <a href="https://gateway.envoyproxy.io/latest/tasks/traffic/client-traffic-policy/#configure-client-ip-detection">Client Traffic Policy</a> to look for the custom <a href="/fundamentals/reference/http-headers/#cf-connecting-ip"><code>CF-Connecting-IP</code> header</a>.</p>
<pre><code class="language-txt">clientIPDetection:&#10;    customHeader:&#10;        name: CF-Connecting-IP&#10;        failClosed: true&#10;</code></pre>
<p>For more details, refer to <a href="https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/http/original_ip_detection/custom_header/v3/custom_header.proto">Custom header original IP detection extension</a>.</p>
<h3 id="caddy">Caddy</h3>
<p>If you are running an application behind <a href="https://caddyserver.com/">Caddy</a> that relies on the <code>X-Forwarded-For</code> header, you can configure Caddy to override the header with Cloudflare's <a href="/fundamentals/reference/http-headers/#cf-connecting-ip">CF-Connecting-IP header</a>.</p>
<p>It is advised that you also only accept traffic from <a href="https://www.cloudflare.com/ips/">Cloudflare's IP addresses</a>; otherwise, the header could be spoofed. That's why, in the second example, we handle this as part of the Caddy configuration. Alternatively, you can handle this at the firewall level, which is usually easier to automate. If you already have a firewall or other measure in place to ensure this, your Caddyfile could look like this:</p>
<pre><code class="language-txt">https://example.com {&#10;    reverse_proxy localhost:8080 {&#10;				&#35; Sets X-Forwarded-For as the value Cloudflare gives us for CF-Connecting-IP.&#10;				header_up X-Forwarded-For {http.request.header.CF-Connecting-IP}&#10;		}&#10;}&#10;</code></pre>
<p>If you want Caddy to handle only accepting traffic from <a href="https://www.cloudflare.com/ips/">Cloudflare's IP addresses</a>, you can use a configuration like this one:</p>
<pre><code class="language-txt">https://example.com {&#10;    &#35; Restrict access to Cloudflare IPs (https://www.cloudflare.com/ips/)&#10;    @cloudflare {&#10;        remote_ip 173.245.48.0/20 103.21.244.0/22 103.22.200.0/22 103.31.4.0/22 141.101.64.0/18 108.162.192.0/18 190.93.240.0/20 188.114.96.0/20 197.234.240.0/22 198.41.128.0/17 162.158.0.0/15 104.16.0.0/13 104.24.0.0/14 172.64.0.0/13 131.0.72.0/22 2400:cb00::/32 2606:4700::/32 2803:f800::/32 2405:b500::/32 2405:8100::/32 2a06:98c0::/29 2c0f:f248::/32&#10;    }&#10;&#10;    &#35; Process requests from Cloudflare IPs&#10;    handle @cloudflare {&#10;        reverse_proxy localhost:8080 {&#10;            &#35; Sets X-Forwarded-For as the value Cloudflare gives us for CF-Connecting-IP.&#10;            header_up X-Forwarded-For {http.request.header.CF-Connecting-IP}&#10;        }&#10;    }&#10;&#10;    &#35; Deny requests from non-Cloudflare IPs&#10;    handle {&#10;        respond &quot;Access Denied&quot; 403&#10;    }&#10;}&#10;</code></pre>
<hr />
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/fundamentals/reference/http-headers/">Cloudflare HTTP headers</a></li>
<li><a href="/rules/transform/">Transform Rules</a></li>
</ul>
