from flask import Flask, request, Response
import html
import os

app = Flask(__name__)

@app.route('/api/embed')
def embed():
    title = html.escape(request.args.get('title', ''))
    url = html.escape(request.args.get('url', ''))
    image = html.escape(request.args.get('img', ''))
    description = html.escape(request.args.get('desc', ''))
    color = html.escape(request.args.get('color', '#000000'))
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta property="og:title" content="{title}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta property="og:image" content="{image}" />
    <meta property="og:description" content="{description}" />
    <meta name="theme-color" content="{color}">
    <meta name="twitter:card" content="summary_large_image">
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="Refresh" content="5; url='{url}'" />
</head>
<body>
    <p>inspired by 3l.wtf embed api</p>
</body>
</html>"""

    return Response(html_content, mimetype='text/html')

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(port=port)
