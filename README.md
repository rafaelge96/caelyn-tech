# caelyn-web

Web institucional de **Caelyn** y centro de políticas de privacidad de sus aplicaciones.

Publicada con GitHub Pages.

## Estructura

```
index.html              Landing + listado de políticas de privacidad
styles.css              Estilos (estética limpia, claro/oscuro automático)
privacidad/
  oremus.html           Política de privacidad de Oremus
```

## Añadir la política de una nueva app

1. Crea `privacidad/<nombre-app>.html` (puedes copiar `oremus.html` como plantilla).
2. En `index.html`, dentro de `.policy-list`, añade un nuevo `<li class="policy-item">`
   enlazando a esa página.
3. Haz commit y push. GitHub Pages se actualiza solo en uno o dos minutos.

## Desarrollo local

Es HTML estático. Ábrelo directamente o sirve la carpeta:

```
python3 -m http.server
```
