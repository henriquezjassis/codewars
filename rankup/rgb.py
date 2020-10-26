#!/bin/python3

def rgb(r, g, b):
	round = lambda x: min(255, max(x, 0))
	return f"{round(r):02x}{round(g):02x}{round(b):02x}"