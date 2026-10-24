"""Imposter"""
import json

alive = {}
die = {}

while True:
    text = input()
    if text == "Start":
        break
    name = json.loads(text)
    alive.update(name)

while True:
    KICK = input()
    if KICK == "End":
        break
    if KICK in alive:
        role = alive.pop(KICK)
        die[KICK] = role

impostor = list(alive.values()).count("Impostor")
print(f"{impostor} Impostor Remains")

print("***Alive***")
for name in sorted(alive.keys()):
    print(f"{name} : {alive[name]}")

print("***Dead***")
for name in sorted(die.keys()):
    print(f"{name} : {die[name]}")
