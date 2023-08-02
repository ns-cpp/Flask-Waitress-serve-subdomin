# server.py
from waitress import serve
from main.app import app as main_app
from second.app import app as second_app 
# from main.app kısmı ise main uygulamnın bulunduğu klasör adı .app ise klasörün içersindeki ana scriptin adı örn main/app.py
# import app kısmına uygulama içersindeki app = Flask(__name__) kısmına flask ı hangi ad ile tanımladıysanız o adı girin

from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response

class HostDispatcher(object):
    def __init__(self, default_app, subdomain_apps):
        self.default_app = default_app
        self.subdomain_apps = subdomain_apps

    def get_application(self, host):
        if host in self.subdomain_apps:
            return self.subdomain_apps[host]
        return self.default_app

    def __call__(self, environ, start_response):
        request = Request(environ)
        app = self.get_application(request.host)
        return app(environ, start_response)

if __name__ == '__main__':
    default_app = main_app # Ana uygulamanızı burada tanımlayın. örn: site.com a gidildiğinde açılacak olan uygulama

    subdomain_apps = {
        'yourSubDomain.yourDomain.com': second_app,
        # Add more subdomains and their corresponding Flask apps as needed
        # Diğer subdomainleri buraya ekleyin
    }

    dispatcher = HostDispatcher(default_app, subdomain_apps)
    serve(dispatcher, host='0.0.0.0', port=80)
