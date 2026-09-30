<p>Import from S3 lets you define one or more sources of images to bulk import from Amazon S3. You can reuse a source to import only new images into your Cloudflare Images account.</p>
<p>Imports skip unsupported objects and files in the source. You can also target paths, define image prefixes, and view error logs.</p>
<p><span id="when-to-use-sourcing-kit"></span></p>
<h2 id="check-storage-class-support">Check storage class support</h2>
<p>Use Import from S3 for buckets that contain images in non-archival storage classes. Import from S3 skips images in <a href="https://aws.amazon.com/s3/storage-classes/#Archive">archival storage classes</a>, which require a separate import.</p>
<p>Import from S3 skips images stored using S3 Glacier tiers (not including Glacier Instant Retrieval) and logs them in the migration log. It also skips and logs images stored using S3 Intelligent Tiering in the Deep Archive tier.</p>
