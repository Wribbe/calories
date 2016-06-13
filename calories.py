#!/usr/bin/env python2
#coding=UTF-8

import sys

ingredients = [line.strip() for line in open(sys.argv[1]).readlines() if line.strip()]
delimiter = ';'

container = 0
if ingredients[0].startswith('skål'):
    container = int(ingredients.pop(0).split(delimiter)[1])


total_calories = 0
total_weight = 0

for ingredient in ingredients:
    weight, calories = [float(number) for number in ingredient.split(delimiter)[1:]]
    total_weight += weight
    total_calories += calories * ((weight-container)/100.0)

print("Total calories: {}cal".format(total_calories))
print("Total weight: {}g".format(total_weight))
print("Total cal/g: {:.3} cal/g".format(total_calories/total_weight))
