/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Jwawon
 *
 * Created on April 15, 2016, 9:46 AM
 */

#include <cstdlib>
#include <iostream>
#include "BObject.h"

int main(int argc, char** argv) {
    BObject theObject;
    std::cout << theObject.getClassName();
    std::cout << theObject.toString();
    return 0;
}

