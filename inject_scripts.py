"""Post-process built HTML to inject scripts that can't be added via myst.yml."""
import pathlib

SCRIPT = """<script>
(function () {
  function expandNav() {
    document.querySelectorAll('[aria-label="Open Folder"]').forEach(function (btn) {
      if (btn.getAttribute('aria-expanded') === 'false') btn.click();
    });
  }
  var attempts = 0;
  var interval = setInterval(function () {
    if (document.querySelectorAll('[aria-label="Open Folder"]').length > 0) {
      expandNav();
      clearInterval(interval);
    } else if (++attempts > 50) {
      clearInterval(interval);
    }
  }, 50);
})();
</script>"""

html_dir = pathlib.Path("_build/html")
for html_file in html_dir.rglob("*.html"):
    content = html_file.read_text(encoding="utf-8")
    if SCRIPT not in content and "</body>" in content:
        html_file.write_text(content.replace("</body>", SCRIPT + "</body>"), encoding="utf-8")
        print(f"Injected: {html_file}")
