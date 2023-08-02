# Flask Waitress serve subdomin
Running multiple applications with subdomains on the same machine with flask

Waitres serve ile aynı makinede birden fazla Flask uygulamasını subdominler ile çalıştırma


# Warning

```
# Do not use this section in the main application
if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5001)
```
kısmını yalnızca alt uygulamarda kullanın ve alt uygulamaların her birini farklı bir port üzerinde çalıştırın

use the above code only in sub-applications. and run each of the sub-applications with a different port
