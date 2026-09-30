<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10078.md")
</aside>
<p>Learn how and when to use PAC files instead of (or complementary to) endpoint agents.</p>
<h2 id="what-are-pac-files">What are PAC files?</h2>
<p>A <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10079.md")
</div>, or proxy auto-configuration file, is like a tiny map that guides your web browser to websites. Instead of going straight to a website, a PAC file can forward your traffic through a proxy server first, protecting your device and filtering unwanted URL access. Cloudflare users use PAC files to filter Internet traffic when they do not want to install agents on devices or where agent installations are not supported.
<p>Here is a quick overview of PAC files:</p>
<ul>
<li><strong>What they do</strong>: PAC files contain JavaScript code that decides whether or not your browser should use a proxy. The code determines this for each website you visit.</li>
<li><strong>How they work</strong>: PAC files tell your browser to run a <code>FindProxyForURL()</code> function with the website address. This function analyzes the address and decides whether to send it directly to the browser or through a specified proxy server.</li>
<li><strong>Why use them</strong>: PAC files are handy for organizations or networks that want to control access to the Internet. PAC files can allow access to some websites directly while routing others through the proxy for filtering or security.</li>
<li><strong>Benefits</strong>: Managing a single PAC file saves time and effort compared to manually configuring proxy settings for each device. It also allows for flexible rules based on websites, time and date, and other factors.</li>
</ul>
<p>Think of PAC files like a GPS: you are driving to a friend's house, but there is construction on the main road. Your GPS (the PAC file) suggests a detour through a side street (the proxy server) to get there faster.</p>
<h3 id="use-cases">Use cases</h3>
<p>Some use cases for PAC files include:</p>
<ul>
<li><strong>Versions of Windows before Windows 8/Windows Server 2012</strong>: The Cloudflare One Client does not support older versions of Windows, so PAC files provide a clientless solution to route traffic through Cloudflare to add security and filtering benefits.</li>
<li><strong>Non-persistent virtual desktop infrastructure (VDI) environments</strong>: PAC files can be especially valuable in non-persistent VDI environments where installing and saving user details for the Cloudflare One Client is challenging. In these instances, PAC files ensure consistent access and security regardless of individual user sessions.</li>
<li><strong>Backup in case of agent outage</strong>: In case of an agent outage, PAC files can act as a backup that can be deployed quickly to minimize downtime and security risk.</li>
</ul>
<h2 id="where-are-pac-files-hosted">Where are PAC files hosted?</h2>
<p>PAC files are usually hosted in a centralized location where all of the devices in your organization can reach and download the file. You can configure browsers with a PAC URL to retrieve the PAC file from the address. This typically occurs when your users open the browser. Many admins push PAC files to devices via deployment methods such as Group Policy Objects (GPOs).</p>
<h2 id="create-a-pac-file">Create a PAC file</h2>
<p>For detailed instructions on creating a PAC file, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Enable Gateway proxy with PAC files</a>.</p>
<h3 id="best-practices">Best practices</h3>
<ul>
<li>Avoid complex logic and nested conditions, as they might slow down processing time.</li>
<li>Place frequently accessed URLs and conditions at the top for faster processing.</li>
<li>Test your PAC file logic on multiple devices before deployment with tools such as an <a href="https://thorsen.pm/proxyforurl">online proxy PAC file tester</a>.</li>
<li>When users download a PAC file from a central location, the download must complete within 30 seconds or most browsers will time out.</li>
<li>Requests must complete with an HTTP response code <code>200</code>.</li>
<li>Requests must have an uncompressed body smaller than 1 MB (megabyte).</li>
<li>Do not include standard HTTP caching within your PAC file. Cached contents can make PAC instructions outdated, and thus lead to bad HTTP routing.</li>
<li>PAC files cannot be fetched through a proxy.</li>
</ul>
