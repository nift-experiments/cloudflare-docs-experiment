<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5974.md")
</aside>
<p>If your device does not support <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">certificate installation via the Cloudflare One Client</a>, you can manually install a Cloudflare certificate. You must add the certificate to both the <a href="#add-the-certificate-to-operating-systems">system keychain</a> and to <a href="#add-the-certificate-to-applications">individual application stores</a>. These steps must be performed on each new device that is to be subject to HTTP filtering.</p>
<p>Zero Trust will only inspect traffic using installed certificates set to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#activate-a-root-certificate"><strong>Available</strong> and <strong>In-Use</strong></a>.</p>
<p>To install a certificate manually, you must:</p>
<ol>
<li>Download a Cloudflare certificate and verify it.</li>
<li>Install the certificate in your operating system's certificate store.</li>
<li>If a target application does not accept certificates from the operating system, you must install the certificate in the application's certificate store.</li>
</ol>
<h2 id="1-download-a-cloudflare-root-certificate"><ol>
<li>Download a Cloudflare root certificate</li>
</ol></h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="download-limitation">Download limitation</h3>
@markup("md", "content/.markup/bodies/5973.md")
</aside>
<p>First, <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">generate</a> and download a Cloudflare certificate. The certificate is available in both <code>.pem</code> and <code>.crt</code> file format. Certain applications require the certificate to be in a specific file type, so ensure you download the most appropriate file for your use case.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Select <strong>Certificates</strong>.</li>
<li>Select the certificate you want to download.</li>
<li>Select <strong>More actions</strong>.</li>
<li>Depending on which format you want, choose <strong>Download .pem</strong> and/or <strong>Download .crt</strong>.</li>
</ol>
<p>Alternatively, you can download and install a certificate <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/#install-a-certificate-using-the-cloudflare-one-client">using the Cloudflare One Client</a>. The Cloudflare One Client will add the certificates to the device's system certificate store in <code>installed_certs/&lt;certificate_id&gt;.pem</code>.</p>
<h2 id="2-verify-the-downloaded-certificate"><ol start="2">
<li>Verify the downloaded certificate</li>
</ol></h2>
<p>To verify your download, use a terminal to check that the downloaded certificate's hash matches the thumbprint listed under <strong>Certificate thumbprint</strong>. For example:</p>
<h3 id="sha1">SHA1</h3>
<pre><code class="language-sh">openssl x509 -noout -fingerprint -sha1 -inform der -in &lt;certificate.crt&gt;&#10;</code></pre>
<pre><code class="language-sh">SHA1 Fingerprint=BB:2D:B6:3D:6B:DE:DA:06:4E:CA:CB:40:F6:F2:61:40:B7:10:F0:6C&#10;</code></pre>
<pre><code class="language-sh">openssl x509 -noout -fingerprint -sha1 -inform pem -in &lt;certificate.pem&gt;&#10;</code></pre>
<pre><code class="language-sh">SHA1 Fingerprint=BB:2D:B6:3D:6B:DE:DA:06:4E:CA:CB:40:F6:F2:61:40:B7:10:F0:6C&#10;</code></pre>
<h3 id="sha256">SHA256</h3>
<pre><code class="language-sh">openssl x509 -noout -fingerprint -sha256 -inform der -in &lt;certificate.crt&gt;&#10;</code></pre>
<pre><code class="language-sh">sha256 Fingerprint=F5:E1:56:C4:89:78:77:AD:79:3A:1E:83:FA:77:83:F1:9C:B0:C6:1B:58:2C:2F:50:11:B3:37:72:7C:62:3D:EF&#10;</code></pre>
<pre><code class="language-sh">openssl x509 -noout -fingerprint -sha256 -inform pem -in &lt;certificate.pem&gt;&#10;</code></pre>
<pre><code class="language-sh">sha256 Fingerprint=F5:E1:56:C4:89:78:77:AD:79:3A:1E:83:FA:77:83:F1:9C:B0:C6:1B:58:2C:2F:50:11:B3:37:72:7C:62:3D:EF&#10;</code></pre>
<h2 id="3-optional-convert-the-certificate"><ol start="3">
<li>(Optional) Convert the certificate</li>
</ol></h2>
<p>Some applications require a certificate formatted in the <code>.cer</code> file type. You can convert your downloaded certificate using <a href="https://www.openssl.org/">OpenSSL</a>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5977.md")
</div></div>
<h2 id="4-add-the-certificate-to-operating-systems"><ol start="4">
<li>Add the certificate to operating systems</li>
</ol></h2>
<p>If you are deploying the Cloudflare certificate to desktop devices, use the <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/automated-deployment/">Install certificate using the Cloudflare One Client</a> method.</p>
<p>Mobile devices require manual installations detailed in the instructions below.</p>
<h3 id="macos">macOS</h3>
<p>In macOS, you can choose the keychain in which you want to install the certificate. Each keychain impacts which users will be affected by trusting the root certificate.</p>
<table>
<thead>
<tr>
<th>Keychain</th>
<th>Access scope</th>
</tr>
</thead>
<tbody>
<tr>
<td>login</td>
<td>The logged in user</td>
</tr>
<tr>
<td>Local Items</td>
<td>Users with access to cached iCloud passwords</td>
</tr>
<tr>
<td>System</td>
<td>All users on the system</td>
</tr>
</tbody>
</table>
<p>To install a Cloudflare certificate in macOS, you can use either the Keychain Access application or a terminal. Both methods require you to <a href="#download-a-cloudflare-root-certificate">download a certificate</a> in <code>.crt</code> format.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5980.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="change-certificate-access-scope">Change certificate access scope</h3>
@markup("md", "content/.markup/bodies/5972.md")
</aside>
<h3 id="windows">Windows</h3>
<p>Windows offers two locations to install the certificate, each impacting which users will be affected by trusting the root certificate.</p>
<table>
<thead>
<tr>
<th>Store location</th>
<th>Access scope</th>
</tr>
</thead>
<tbody>
<tr>
<td>Current User Store</td>
<td>The logged in user</td>
</tr>
<tr>
<td>Local Machine Store</td>
<td>All users on the system</td>
</tr>
</tbody>
</table>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a>.</li>
<li>Right-click the certificate file.</li>
<li>Select <strong>Open</strong>. If a security warning appears, choose <strong>Open</strong> to proceed.</li>
<li>The <strong>Certificate</strong> window will appear. Select <strong>Install Certificate</strong>.</li>
<li>Now choose a Store Location. If a security warning appears, choose <strong>Yes</strong> to proceed.</li>
<li>On the next screen, select <strong>Browse</strong>.</li>
<li>In the list, choose the <em>Trusted Root Certification Authorities</em> store.</li>
<li>Select <strong>OK</strong>, then select <strong>Finish</strong>.</li>
</ol>
<p>The root certificate is now installed and ready to be used.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5971.md")
</aside>
<h3 id="linux">Linux</h3>
<p>The location where the root certificate should be installed is different depending on your Linux distribution. Follow the specific instructions for your distribution.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5984.md")
</div></div>
<h3 id="ios">iOS</h3>
<ol>
<li>In Safari, <a href="#download-a-cloudflare-root-certificate">download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Open Files and go to <strong>Recents</strong>.</li>
<li>Find and open the downloaded certificate file. A message will appear confirming the profile was downloaded. Select <strong>Close</strong>.</li>
<li>Open Settings. Select the <strong>Profile Downloaded</strong> section beneath your Apple Account info. Alternatively, go to <strong>General</strong> &gt; <strong>VPN &amp; Device Management</strong> and select the <strong>Gateway CA - Cloudflare Managed G1</strong> profile.</li>
<li>Select <strong>Install</strong>. If the iOS device is passcode-protected, you will be prompted to enter the passcode.</li>
<li>A certificate warning will appear. Select <strong>Install</strong>. If a second prompt appears, select <strong>Install</strong> again.</li>
<li>The Profile Installed screen will appear. Select <strong>Done</strong>. The certificate is now installed. However, before it can be used, it must be trusted by the device.</li>
<li>In Settings, go to <strong>General</strong> &gt; <strong>About</strong> &gt; <strong>Certificate Trust Settings</strong>. The installed root certificates will be displayed under Enable full trust for root certificates.</li>
<li>Turn on the Cloudflare certificate.</li>
<li>A security warning message will appear. Choose <strong>Continue</strong>.</li>
</ol>
<p>The root certificate is now installed and ready to be used.</p>
<h3 id="android">Android</h3>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a>.</li>
<li>In Settings, go to <strong>Security</strong> &gt; <strong>Advanced</strong> &gt; <strong>Encryption &amp; credentials</strong> &gt; <strong>Install a certificate</strong>.</li>
<li>Select <strong>CA certificate</strong>.</li>
<li>Select <strong>Install anyway</strong>.</li>
<li>Verify your identity.</li>
<li>Choose the certificate file you want to install.</li>
</ol>
<p>The root certificate is now installed and ready to be used.</p>
<h3 id="chromeos">ChromeOS</h3>
<p>ChromeOS devices use different methods to store and deploy root certificates. Certificates may fall under the <strong>VPN and apps</strong> or <strong>CA certificate</strong> settings. Follow the procedure that corresponds with your device.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5987.md")
</div></div>
<p>After adding the Cloudflare certificate to ChromeOS, you may also have to <a href="#browsers">install the certificate in your browser</a>.</p>
<h2 id="5-add-the-certificate-to-applications"><ol start="5">
<li>Add the certificate to applications</li>
</ol></h2>
<p>Some applications do not use the system certificate store and therefore require the certificate to be added to the application directly. For certain applications like the ones below, you will need to follow the steps in this section and add the Cloudflare certificate to the application for TLS decryption to function properly.</p>
<p>If you do not update the application to trust the Cloudflare certificate, the application will refuse to connect and you will receive an untrusted certificate error.</p>
<p>All of the applications below first require downloading a Cloudflare certificate with <a href="#download-the-cloudflare-root-certificate">the instructions above</a>. On macOS, the default path to the system keychain database file is <code>/Library/Keychains/System.keychain</code>. On Windows, the default path is <code>\Cert:\CurrentUser\Root</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5970.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5969.md")
</aside>
<h3 id="browsers">Browsers</h3>
<p>Browsers may use their own certificate stores or rely on the operating system certificate store.</p>
<h4 id="chrome">Chrome</h4>
<p>Versions of Chrome before Chrome 113 use the <a href="https://support.google.com/chrome/answer/95617?visit_id=638297158670039236-3119581239&amp;p=root_store&amp;rd=1#zippy=%2Cmanage-device-certificates-on-mac-windows">operating system root store</a> on macOS and Windows. Chrome 113 and newer on macOS and Windows -- and all versions on Linux and ChromeOS -- use the <a href="https://www.chromium.org/Home/chromium-security/root-ca-policy/#introduction">Chrome internal trust store</a>.</p>
<p>To install a Cloudflare certificate to Chrome manually:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>In Chrome, go to <strong>Settings</strong> &gt; <strong>Privacy and security</strong> &gt; <strong>Security</strong>.</li>
<li>Select <strong>Manage certificates</strong>.</li>
<li>Go to <strong>Authorities</strong>. Select <strong>Import</strong>.</li>
<li>In the file open dialog, choose the <code>certificate.pem</code> file you downloaded.</li>
<li>In the dialog box, turn on <em>Trust this certificate for identifying websites</em>, <em>Trust this certificate for identifying email users</em>, and <em>Trust this certificate for identifying software makers</em>. Select <strong>OK</strong>.</li>
<li>To verify the certificate was installed and trusted, locate it in <strong>Authorities</strong>.</li>
</ol>
<p>For information on installing a Cloudflare certificate for organizations, refer to <a href="https://support.google.com/chrome/a/answer/3505249">Google's Chrome Enterprise and Education documentation</a>.</p>
<h4 id="firefox">Firefox</h4>
<p>To install a Cloudflare certificate to Firefox manually:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>In Firefox, go to <strong>Settings</strong> &gt; <strong>Privacy &amp; Security</strong>.</li>
<li>In <strong>Security</strong>, select <strong>Certificates</strong> &gt; <strong>View Certificates</strong>.</li>
<li>In <strong>Authorities</strong>, select <strong>Import</strong>.</li>
<li>In the file open dialog, choose the <code>certificate.pem</code> file you downloaded.</li>
<li>In the dialog box, turn on <em>Trust this CA to identify websites</em> and <em>Trust this CA to identify email users</em>. Select <strong>OK</strong>.</li>
<li>To verify the certificate was installed and trusted, locate it in the table under <strong>Cloudflare</strong>.</li>
</ol>
<p>For information on installing a Cloudflare certificate for organizations, refer to this <a href="https://support.mozilla.org/en-US/kb/setting-certificate-authorities-firefox">Mozilla support article</a>.</p>
<h3 id="mobile-device-management-mdm-software">Mobile device management (MDM) software</h3>
<p>Zero Trust integrates with several <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/">mobile device management (MDM) software partners</a> to deploy the Cloudflare One Client across devices.</p>
<h4 id="microsoft-intune">Microsoft Intune</h4>
<p>To upload and deploy a Cloudflare certificate in Microsoft Intune:</p>
<ol>
<li><a href="#convert-the-certificate">Download and convert a Cloudflare certificate</a> to DER format with the <code>.cer</code> file type.</li>
<li>In Microsoft Intune, <a href="https://learn.microsoft.com/mem/intune/protect/certificates-trusted-root#to-create-a-trusted-certificate-profile">create a trusted certificate profile</a> with your converted certificate.</li>
</ol>
<p>For more information, refer to the <a href="https://learn.microsoft.com/mem/intune/protect/certificates-trusted-root">Microsoft documentation</a>.</p>
<h4 id="jamf-pro">Jamf Pro</h4>
<p>To upload and deploy a Cloudflare certificate in Jamf Pro:</p>
<ol>
<li><a href="#convert-the-certificate">Download and convert a Cloudflare certificate</a> to DER format with the <code>.cer</code> file type.</li>
<li>In Jamf Pro, go to <strong>Computers</strong> &gt; <strong>Configuration Profiles</strong> to create a computer configuration profile, or go to <strong>Devices</strong> &gt; <strong>Configuration Profiles</strong> to create a mobile device configuration profile. Select <strong>New</strong>.</li>
<li>Add a name and description for the profile.</li>
<li>Choose whether you would like Jamf to install the certificate automatically or with self-service, and whether you would like to install the certificate for a single user or all users on the device.</li>
<li>Select <strong>Add</strong> &gt; <strong>Certificate</strong>. Choose the certificate file.</li>
<li>Uncheck <strong>Allow export from keychain</strong>.</li>
<li>Select <strong>Scope</strong>, then choose which devices or groups to deploy the certificate to.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>For more information, refer to the <a href="https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/PKI_Certificates.html">Jamf Pro documentation</a>.</p>
<h4 id="kandji">Kandji</h4>
<p>To upload and deploy a Cloudflare certificate in Kandji:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.crt</code> format.</li>
<li>In Kandji, <a href="https://support.kandji.io/support/solutions/articles/72000558739-certificate-profile">upload the certificate</a> as a PKCS #1-formatted certificate.</li>
</ol>
<h4 id="hexnode">Hexnode</h4>
<p>To upload and deploy a Cloudflare certificate in Hexnode:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>In Hexnode, follow the directions for adding the certificate to <a href="https://www.hexnode.com/mobile-device-management/help/how-to-add-certificates-for-mac-devices-with-hexnode-mdm/">macOS</a>, <a href="https://www.hexnode.com/mobile-device-management/help/add-certificates-for-ios-devices-with-hexnode-mdm/">iOS</a>, and/or <a href="https://www.hexnode.com/mobile-device-management/help/how-to-add-certificates-for-android-devices-using-hexnode-mdm/">Android</a> devices.</li>
</ol>
<h4 id="jumpcloud">JumpCloud</h4>
<p>To upload and deploy a Cloudflare certificate in JumpCloud:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>In JumpCloud, <a href="https://jumpcloud.com/support/manage-device-trust-certificates#distributing-global-device-certificates-">upload the certificate</a>.</li>
<li><a href="https://jumpcloud.com/support/configure-a-conditional-access-policy">Configure a conditional access policy</a> to deploy the certificate across devices.</li>
</ol>
<h3 id="programming-languages-and-runtimes">Programming languages and runtimes</h3>
<p>Programming language runtimes often maintain their own certificate stores or use language-specific certificate management tools.</p>
<h4 id="python">Python</h4>
<p>Depending on which version of Python you have installed and your configuration, you may need to use either the <code>python</code> or <code>python3</code> command. If you use <a href="https://docs.python.org/3/library/venv.html">virtual environments</a>, you will need to repeat the following steps within each virtual environment.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5990.md")
</div></div>
<h4 id="java">Java</h4>
<p>Java may have multiple certificate keystore locations depending on different installations or applications that include Java. Depending on your Java Virtual Machine (JVM) installation, you may need to install the certificate for each instance. You may also need to manually configure each Java application to use and trust the certificate.</p>
<p>To install a Cloudflare root certificate in the system JVM, follow the procedure for your operating system. These steps require you to <a href="#download-a-cloudflare-root-certificate">download a <code>.pem</code> certificate</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5993.md")
</div></div>
<h4 id="ruby">Ruby</h4>
<p>To trust a Cloudflare root certificate in RubyGems, follow the procedure for your operating system. These steps require you to <a href="#download-a-cloudflare-root-certificate">download a <code>.pem</code> certificate</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5996.md")
</div></div>
<h4 id="rust">Rust</h4>
<p>Rust's package manager Cargo uses the system certificate store by default on most platforms. However, you may need to configure it explicitly in some cases.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5999.md")
</div></div>
<h3 id="development-tools-and-package-managers">Development tools and package managers</h3>
<p>Development tools and package managers often require certificate configuration for secure package downloads and repository access.</p>
<h4 id="git">Git</h4>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6002.md")
</div></div>
<h4 id="npm">npm</h4>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Set the <code>cafile</code> configuration to use the Cloudflare certificate:</li>
</ol>
<pre><code class="language-sh">npm config set cafile [PATH_TO_CLOUDFLARE_CERT.pem]&#10;</code></pre>
<p>On some systems you may need to set the following in your path/export list:</p>
<pre><code class="language-sh">export NODE_EXTRA_CA_CERTS=&#x27;[PATH_TO_CLOUDFLARE_CERT.pem]&#x27;&#10;</code></pre>
<h4 id="php-composer">PHP Composer</h4>
<p>The command below will set the <a href="https://getcomposer.org/doc/06-config.md#cafile"><code>cafile</code></a> configuration inside of <code>composer.json</code> to use the Cloudflare root certificate. Make sure to <a href="#download-a-cloudflare-root-certificate">download a certificate</a> in the <code>.pem</code> file type.</p>
<pre><code class="language-sh">composer config cafile [PATH_TO_CLOUDFLARE_CERT.pem]&#10;</code></pre>
<p>Alternatively, you can add this manually to your <code>composer.json</code> file under the <code>config</code> key.</p>
<h4 id="docker">Docker</h4>
<p>To install a certificate for use in a Docker container:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Create a directory for certificates in your Docker project:</li>
</ol>
<pre><code class="language-sh">cd docker-project&#10;mkdir certs&#10;mv /path/to/downloaded/certificate.pem certs/&#10;</code></pre>
<ol start="3">
<li>Verify the certificate was moved to the directory correctly. Your project should have the following structure:</li>
</ol>
<pre><code class="language-sh">docker-project/&#10;├── Dockerfile&#10;└── certs/&#10;    └── certificate.pem&#10;</code></pre>
<ol start="4">
<li>Add the certificate to your Docker image:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6005.md")
</div></div>
<h3 id="command-line-tools">Command-line tools</h3>
<p>Command-line tools typically use the system certificate store but may require specific configuration.</p>
<h4 id="curl">cURL</h4>
<p>By default, cURL will use your operating system's native certificate store. To force cURL to use your default certificate, add the <code>--ca-native</code> flag to the command. For example:</p>
<pre><code class="language-curl">curl --ca-native https://example.com&#10;</code></pre>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6009.md")
</div></div>
<h4 id="gnu-wget">GNU Wget</h4>
<p>By default, GNU Wget will use your operating system's native certificate store. To force Wget to use your default certificate, add the <code>--ca-certificate</code> flag to the command.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6013.md")
</div></div>
<h3 id="ides-and-development-environments">IDEs and development environments</h3>
<p>Integrated development environments often use their own JVMs or certificate stores.</p>
<h4 id="android-studio">Android Studio</h4>
<p>Android Studio uses its own JVM and certificate store. To install a Cloudflare root certificate:</p>
<ol>
<li>
<p><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a>.</p>
</li>
<li>
<p>Find the <code>java.home</code> value for your Android Studio installation.</p>
<ol>
<li>In Android Studio, go to <strong>Help</strong> &gt; <strong>About</strong> (or <strong>Android Studio</strong> &gt; <strong>About Android Studio</strong> on macOS).</li>
<li>Copy the JRE path shown in the dialog. For example:</li>
</ol>
</li>
</ol>
<pre><code class="language-txt">/Applications/Android Studio.app/Contents/jbr/Contents/Home&#10;</code></pre>
<ol start="3">
<li>Add the Cloudflare certificate to Android Studio's JVM:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6016.md")
</div></div>
<p>For Gradle builds within Android Studio, you may also need to configure the Gradle JVM to trust the certificate by following the same steps for the Gradle JVM location.</p>
<h4 id="jetbrains">JetBrains</h4>
<p>To install a Cloudflare root certificate on JetBrains products, refer to the links below:</p>
<ul>
<li><a href="https://www.jetbrains.com/help/objc/settings-tools-server-certificates.html">AppCode</a></li>
<li><a href="https://www.jetbrains.com/help/clion/settings-tools-server-certificates.html">CLion</a></li>
<li><a href="https://www.jetbrains.com/help/datagrip/settings-tools-server-certificates.html">DataGrip</a></li>
<li><a href="https://www.jetbrains.com/help/dataspell/settings-tools-server-certificates.html">DataSpell</a></li>
<li><a href="https://www.jetbrains.com/help/go/settings-tools-server-certificates.html">GoLand</a></li>
<li><a href="https://www.jetbrains.com/help/idea/settings-tools-server-certificates.html">IntelliJ IDEA</a></li>
<li><a href="https://www.jetbrains.com/help/phpstorm/settings-tools-server-certificates.html">PhpStorm</a></li>
<li><a href="https://www.jetbrains.com/help/pycharm/settings-tools-server-certificates.html">PyCharm</a></li>
<li><a href="https://www.jetbrains.com/help/rider/Settings_Tools_Server_Certificates.html">Rider</a></li>
<li><a href="https://www.jetbrains.com/help/webstorm/settings-tools-server-certificates.html">WebStorm</a></li>
</ul>
<h4 id="eclipse">Eclipse</h4>
<p>To install a Cloudflare root certificate on Eclipse IDE for Java Developers, you must add the certificate to the Java virtual machine (JVM) used by Eclipse.</p>
<ol>
<li>
<p><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a>.</p>
</li>
<li>
<p>Find the <code>java.home</code> value for your Eclipse installation.</p>
<ol>
<li>In Eclipse, go to <strong>Eclipse</strong> &gt; <strong>About Eclipse</strong> (or <strong>Help</strong> &gt; <strong>About Eclipse IDE</strong> on Windows and Linux)</li>
<li>Select <strong>Installation Details</strong>, then go to <strong>Configuration</strong>.</li>
<li>Search for <code>java.home</code>, then locate the value. For example:</li>
</ol>
</li>
</ol>
<pre><code class="language-txt">&#42;** System properties:&#10;java.home=/Users/&lt;username&gt;/.p2/pool/plugins/org.eclipse.justj.openjdk.hotspot.jre.full.macosx.aarch64_17.0.8.v20230831-1047/jre&#10;</code></pre>
<ol start="4">
<li>
<p>Copy the full path after <code>java.home=</code>.</p>
</li>
<li>
<p>Add the Cloudflare certificate to Eclipse's JVM:</p>
</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6019.md")
</div></div>
<p>For more information on adding certificates to Eclipse with <code>keytool</code>, refer to <a href="https://www.ibm.com/docs/en/ram/7.5.4?topic=client-adding-server-public-certificate-eclipse">IBM's documentation</a>.</p>
<h3 id="cloud-and-infrastructure-tools">Cloud and infrastructure tools</h3>
<p>Cloud service providers and infrastructure tools often require certificate configuration for API access and resource management.</p>
<h4 id="google-cloud">Google Cloud</h4>
<h5 id="google-cloud-sdk">Google Cloud SDK</h5>
<p>The commands below will set the Google Cloud SDK to use a Cloudflare certificate. For more information on configuring the Google Cloud SDK, refer to the <a href="https://cloud.google.com/sdk/docs/proxy-settings">Google Cloud documentation</a>.</p>
<ol>
<li>Get curl's <code>cacert</code> bundle.</li>
</ol>
<pre><code class="language-sh">curl --remote-name https://curl.se/ca/cacert.pem&#10;</code></pre>
<ol start="2">
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Combine the certs into a single <code>.pem</code> file.</li>
</ol>
<pre><code class="language-sh">cat cacert.pem certificate.pem &gt; ~/ca.pem&#10;</code></pre>
<ol start="4">
<li>Configure Google Cloud to use the combined <code>.pem</code>.</li>
</ol>
<pre><code class="language-sh">gcloud config set core/custom_ca_certs_file ~/ca.pem&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5968.md")
</aside>
<h5 id="kaniko">Kaniko</h5>
<p>If you use Kaniko with Google Cloud SDK, you must install a Cloudflare certificate in the <a href="https://docs.gitlab.com/ee/ci/docker/using_kaniko.html#using-a-registry-with-a-custom-certificate">Kaniko CA store</a>. For more information, refer to the <a href="https://cloud.google.com/sdk/gcloud/reference/builds/submit"><code>gcloud</code> documentation</a>.</p>
<h5 id="google-apps-manager-gam">Google Apps Manager (GAM)</h5>
<p>Google Apps Manager (GAM) uses its own certificate store. To add a Cloudflare certificate to GAM, refer to the <a href="https://github.com/GAM-team/GAM/wiki/#using-gam-with-ssl--tls-mitm-inspection">GAM documentation</a>.</p>
<h4 id="aws-cli">AWS CLI</h4>
<h5 id="global-config">Global config</h5>
<p>To persistently set the location of the certificate:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Locate and open your <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-configure-files-where">AWS configuration file</a>.</li>
<li>Configure the <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-configure-files-settings"><code>ca_bundle</code> setting</a> with the location of your certificate. For example:</li>
</ol>
<pre><code class="language-diff">[default]&#10;region = us-west-1&#10;&#10;&#43;ca_bundle = /path/to/certificate.pem&#10;</code></pre>
<ol start="4">
<li>Restart your terminal.</li>
</ol>
<h5 id="environment-variable">Environment variable</h5>
<p>To set the location of the certificate for use as an environment variable:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>In a terminal, set the <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html"><code>AWS_CA_BUNDLE</code> environment variable</a> to the location of your certificate depending on your operating system.</li>
<li>Restart your terminal.</li>
</ol>
<h4 id="azure-cli">Azure CLI</h4>
<h5 id="global-config-1">Global config</h5>
<p>To persistently set the location of the certificate:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Set the <code>REQUESTS_CA_BUNDLE</code> environment variable to point to your certificate depending on your operating system.</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6022.md")
</div></div>
<ol start="3">
<li>Restart your terminal.</li>
</ol>
<h5 id="per-command">Per-command</h5>
<p>To set the location of the certificate for a single command:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Set the <code>REQUESTS_CA_BUNDLE</code> environment variable when running the command:</li>
</ol>
<pre><code class="language-sh">REQUESTS_CA_BUNDLE=/path/to/certificate.pem az &lt;command&gt;&#10;</code></pre>
<p>For more information, refer to the <a href="https://learn.microsoft.com/cli/azure/use-cli-effectively#work-behind-a-proxy">Azure CLI documentation</a>.</p>
<h4 id="boto3">Boto3</h4>
<p>Boto3, the AWS SDK for Python, can be configured to use a Cloudflare certificate in several ways.</p>
<h5 id="environment-variable-1">Environment variable</h5>
<p>To set the location of the certificate using an environment variable:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Set the <code>AWS_CA_BUNDLE</code> environment variable depending on your operating system.</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6025.md")
</div></div>
<ol start="3">
<li>Restart your terminal.</li>
</ol>
<h5 id="aws-config-file">AWS config file</h5>
<p>To persistently set the location of the certificate in your AWS configuration:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Locate and open your <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-configure-files-where">AWS configuration file</a>.</li>
<li>Configure the <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-configure-files-settings"><code>ca_bundle</code> setting</a> with the location of your certificate. For example:</li>
</ol>
<pre><code class="language-diff">[default]&#10;region = us-west-1&#10;&#10;&#43;ca_bundle = /path/to/certificate.pem&#10;</code></pre>
<h5 id="in-code">In code</h5>
<p>To specify the certificate directly in your Python code:</p>
<ol>
<li><a href="#download-a-cloudflare-root-certificate">Download a Cloudflare certificate</a> in <code>.pem</code> format.</li>
<li>Pass the certificate path when creating a Boto3 client or resource:</li>
</ol>
<pre><code class="language-python">import boto3&#10;&#10;client = boto3.client(&#10;    &#x27;s3&#x27;,&#10;    verify=&#x27;/path/to/certificate.pem&#x27;&#10;)&#10;</code></pre>
<p>For more information, refer to the <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html">Boto3 documentation</a>.</p>
<h3 id="enterprise-applications">Enterprise applications</h3>
<p>Enterprise desktop applications and specialized tools may require custom certificate configuration.</p>
<h4 id="google-drive">Google Drive</h4>
<p>To trust a Cloudflare root certificate in the Google Drive desktop application, follow the procedure for your operating system. These steps require you to <a href="#download-a-cloudflare-root-certificate">download a <code>.pem</code> certificate</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6028.md")
</div></div>
<p>For more information, refer to the <a href="https://support.google.com/a/answer/7644837">Google documentation</a> for the <code>TrustedRootCertsFile</code> setting.</p>
<h4 id="minikube">Minikube</h4>
<p>To trust a Cloudflare root certificate in Minikube, refer to <a href="https://minikube.sigs.k8s.io/docs/handbook/vpn_and_proxy/#x509-certificate-signed-by-unknown-authority">x509: certificate signed by unknown authority</a>.</p>
