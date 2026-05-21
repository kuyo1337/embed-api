from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)

        title = query.get("title", [""])[0]
        description = query.get("description", [""])[0]
        color = query.get("color", ["5865F2"])[0]
        image = query.get("image", [""])[0]
        thumbnail = query.get("thumbnail", [""])[0]
        url = query.get("url", [""])[0]
        author_name = query.get("author_name", [""])[0]
        author_url = query.get("author_url", [""])[0]
        author_icon = query.get("author_icon", [""])[0]
        footer_text = query.get("footer_text", [""])[0]
        footer_icon = query.get("footer_icon", [""])[0]
        timestamp = query.get("timestamp", [""])[0]
        provider_name = query.get("provider_name", [""])[0]
        provider_url = query.get("provider_url", ["https://google.com"])[0]

        html = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="theme-color" content="#{color}">
<meta property="og:site_name" content="{provider_name}">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{thumbnail or image}">

<title>{title}</title>

</head>
<body>

<script>
window.location.href = "{provider_url}";
</script>

</body>
</html>
"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())