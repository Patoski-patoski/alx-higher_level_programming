#!/bin/bash

for i in {0..10}; 
do 
	touch "${i}-main.py";
	chmod +x "${i}-main.py";
done

