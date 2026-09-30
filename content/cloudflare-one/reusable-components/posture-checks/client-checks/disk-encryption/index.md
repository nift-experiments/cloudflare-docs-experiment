<p>The Disk Encryption device posture attribute ensures that disks are encrypted on a device.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/">Cloudflare One Client Checks</a>.</p>
<h2 id="enable-the-disk-encryption-check">Enable the disk encryption check</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</li>
<li>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</li>
<li>Select <strong>Disk Encryption</strong>.</li>
<li>Enter a descriptive name for the check.</li>
<li>Select your operating system.</li>
<li>Either enable disk encryption for all volumes, or input the specific volume(s) you want to check for encryption (for example, <code>C</code>).</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>Next, go to <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the disk encryption check is returning the expected results.</p>
<h2 id="validate-disk-encryption-status">Validate disk encryption status</h2>
<p>The following commands will return the disk encryption status on various operating systems. The results can help you validate if the posture check is working as expected.</p>
<h3 id="macos">macOS</h3>
<ol>
<li>
<p>Open a terminal window.</p>
</li>
<li>
<p>Run the <code>/usr/sbin/system_profiler SPStorageDataType</code> command to return a list of drivers on the system and note the value of <strong>Mount Point</strong>.</p>
</li>
</ol>
<pre><code class="language-sh">/usr/sbin/system_profiler SPStorageDataType&#10;</code></pre>
<pre><code class="language-sh">Storage:&#10;&#10;   Data:&#10;&#10;     Free: 428.52 GB (428,519,702,528 bytes)&#10;     Capacity: 494.38 GB (494,384,795,648 bytes)&#10;     Mount Point: /System/Volumes/Data&#10;</code></pre>
<ol start="3">
<li>Run the <code>diskutil info</code> command for a specific <strong>Mount Point</strong> and look for the value returned for <strong>FileVault</strong>. It must show <strong>Yes</strong> for the disk to be considered encrypted.</li>
</ol>
<pre><code class="language-sh">diskutil info /System/Volumes/Data | grep FileVault&#10;</code></pre>
<pre><code class="language-sh"> FileVault:                 Yes&#10;</code></pre>
<h3 id="windows">Windows</h3>
<ol>
<li>Open a PowerShell window.</li>
<li>Run the <code>Get-BitLockerVolume</code> command to list all volumes detected on the system.</li>
<li><strong>Protection Status</strong> must be set to <strong>On</strong> for the disk to be considered encrypted.</li>
</ol>
<h3 id="linux">Linux</h3>
<p>List all hard drives on the system:</p>
<pre><code class="language-sh">lsblk&#10;</code></pre>
<pre><code class="language-sh">NAME                        MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT&#10;nvme0n1                     259:0    0 476.9G  0 disk&#10;├─nvme0n1p1                 259:1    0   512M  0 part  /boot/efi&#10;├─nvme0n1p2                 259:2    0   488M  0 part  /boot&#10;└─nvme0n1p3                 259:3    0   476G  0 part&#10;  └─nvme0n1p3_crypt         253:0    0 475.9G  0 crypt&#10;    ├─my--vg-root   253:1            0 474.9G  0 lvm   /&#10;    └─my--vg-swap_1 253:2            0   976M  0 lvm   [SWAP]&#10;</code></pre>
<p>On Linux, encryption is reported per mounted partition, not physical drive. In the example above, the root and swap partitions are considered encrypted because they are located within a <code>crypt</code> container. The <code>/boot</code> and <code>/boot/efi</code> partitions remain unencrypted.</p>
<h3 id="ios-android-and-chromeos">iOS, Android and ChromeOS</h3>
<p>These platforms are always encrypted and so no disk encryption check is supported.</p>
