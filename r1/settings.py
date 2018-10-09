from .types import (DishType, Restaurant)


BASE = 'http://www.novae-restauration.ch/menus/'
URL1 = BASE + 'menu-week/cern/{menu}'
#URL1 = BASE + '?x={x}&y={y}&z={z}'
#URL2 = BASE + '/novae/traiteur/restauration/{html}.html?frame=1'
PARAMS = {
    Restaurant.r1: {
        'x': 'd894ddae3c17b40b4fe7e16519f950f0',
        'y': 'c7b3f79848b99a8e562a1df1d6285365',
        'z': '33',
        'menu': '13',
        'html': 'restaurant-cern',
        'pages': 1,
        'page_structure': (8,),
        'dishes': (DishType.menu1, DishType.menu2, DishType.pasta,
                   DishType.pizza, DishType.speciality, DishType.grill,
                   DishType.vegetarian, DishType.hamburger),
        'currency': 'CHF'
    },
    Restaurant.r2: {
        'x': 'ad3f8f75fe1e353b972afcce8e375d6e',
        'y': '81dc9bdb52d04dc20036dbd8313ed055',
        'z': '135',
        'html': 'bon-app',
        'pages': 1,
        'page_structure': (10,),
        'dishes': (DishType.marche, DishType.saison, DishType.vegetarian,
                   DishType.grill, DishType.pasta, DishType.speciality,
                   DishType.grill2,DishType.grill3,DishType.pizza,
                   DishType.pizza2),
        'currency': 'CHF'
    },
    Restaurant.r3: {
        'x': 'fd7538322d53ecf7f708990e221d5f36',
        'y': 'fd7538322d53ecf7f708990e221d5f36',
        'z': '145',
        'menu': '33',
        'html': 'restaurant-cern-1',
        'pages': 2,
        'page_structure': (7,),
        'dishes': (DishType.vegetarian,DishType.saison, DishType.menu2, DishType.speciality,
                   DishType.grill, DishType.pizza, DishType.pizza2),
        'currency': '€'
    }
}
