# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'


# Part 1: Greet Template, Define a function greet in main.py that takes these arguments, in this order:

def greet(name: str, greeting_template = 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    return greeting

print(greet("Zafar"))
print(greet("Zafar", "What's up <name> !"))

# Part 2: Force, force = mass × gravity

dict_planets = {
                'sun': 274, 
                'jupiter': 24.9, 
                'neptune': 11.2, 
                'saturn': 10.4, 
                'earth': 9.8,
                'uranus': 8.9, 
                'venus': 8.9, 
                'mars': 3.7, 
                'mercury': 3.7, 
                'moon': 1.6, 
                'pluto': 0.6
                }


def force(mass, body='earth'):
    a = dict_planets[body] 
    force = mass * a
    return force

# Part 3: Gravity, pull = G × ((m1 × m2)/d2)

def pull(m1, m2, d):
    g = 6.674 * (10**-11)
    pull = g * ((m1 * m2) / (d**2))
    return pull