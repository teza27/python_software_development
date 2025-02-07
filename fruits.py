fruit_categories = {
    'fruit': {
        'apple': {
            'color': 'red',
            'taste': 'sweet'
        },
        'banana': {
            'color': 'yellow',
            'taste': 'sweet'
        }
    },
    'vegetable': {
        'carrot': {
            'color': 'orange',
            'taste': 'crunchy'
        },
        'spinach': {
            'color': 'green',
            'taste': 'bitter'
        }
    }
}


def vitamins(category: str, values: dict):
    for key, value in values.items():
        for fruit, features in value.items():
            if fruit == category:
                color = features.get("color")
                taste = features.get("taste")
                print(f"{fruit} is a {key}, it is {color} in colour and has {taste} taste")

vitamins("spinach", fruit_categories)

