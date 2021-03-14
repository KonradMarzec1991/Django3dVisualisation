## DjangoVisualizations

### Description
Mini project facilitates endpoint for figure projections (2/3d).

### Stack
Pursued with technologies: `django`, `DRF`, `matplotlib`, `pillow`.

### Installation
Please follow steps:
1) `git clone https://github.com/KonradMarzec1991/Django3dVisualisation.git`
2) `python manage.py runserver (inside main folder)` <br />

### Testing
The best way to test endpoint is to use `Postman`.
You can POST `/projection` with Content-Type `application/json` and coordinates.

Input used in below examples:
```
{
  "geometry": [{"x1": -207, "x2": -332, "y1": 9, "y2": 191, "z1": 0, "z2": 18}, {"x1": -207, "x2": -332, "y1": 209, "y2": 391, "z1": 0, "z2": 18}, {"x1": 207, "x2": 332, "y1": 9, "y2": 191, "z1": 0, "z2": 18}, {"x1": 207, "x2": 332, "y1": 209, "y2": 391, "z1": 0, "z2": 18}, {"x1": -8, "x2": 10, "y1": 9, "y2": 191, "z1": 0, "z2": 320}, {"x1": -8, "x2": 10, "y1": 209, "y2": 391, "z1": 0, "z2": 320}, {"x1": -350, "x2": -332, "y1": 9, "y2": 191, "z1": 0, "z2": 320}, {"x1": -350, "x2": -332, "y1": 209, "y2": 391, "z1": 0, "z2": 320}, {"x1": 332, "x2": 350, "y1": 9, "y2": 191, "z1": 0, "z2": 320}, {"x1": 332, "x2": 350, "y1": 209, "y2": 391, "z1": 0, "z2": 320}, {"x1": -350, "x2": 350, "y1": 391, "y2": 409, "z1": 0, "z2": 320}, {"x1": -350, "x2": 350, "y1": 191, "y2": 209, "z1": 0, "z2": 320}, {"x1": -350, "x2": 350, "y1": -9, "y2": 9, "z1": 0, "z2": 320}],
  "plane": "XYZ"
}
```
