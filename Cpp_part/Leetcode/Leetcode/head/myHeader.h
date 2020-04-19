//
//  Header.h
//  Leetcode
//
//  Created by Allen on 4/4/20.
//  Copyright © 2020 Allen. All rights reserved.
//

#ifndef Header_h
#define Header_h
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

template <typename Array>
void printArray(const Array& array){
    for (auto val: array){
        std::cout << val << ", ";
    }
    std::cout << "\n";
}

#endif /* Header_h */
