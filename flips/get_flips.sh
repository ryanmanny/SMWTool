#!/usr/bin/env bash

mkdir -p ./build;
git clone https://github.com/Alcaro/Flips.git ./build;
make --directory=./build CFLAGS=-g;
mv ./build/flips .;
rm -rf ./build;
