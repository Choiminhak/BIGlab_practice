/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   BObject.h
 * Author: Jwawon
 *
 * Created on April 19, 2016, 11:01 AM
 */

#ifndef BOBJECT_H
#define BOBJECT_H
#include <iostream> //화면출력 함수
#include <string>

class BObject {
public:
    BObject(){
        
             }
    BObject(const BObject& orig){
        
                                }
    virtual ~BObject(){
        
    }
    virtual std::string toString() const {
        return this->getClassName();
    }
    virtual std::string getClassName() const {
        return "BObject";
    }
    
    friend inline std::ostream &
    operator<<(std::ostream &theStream, const BObject & theSelf) {
        return (theStream << theSelf.toString());
    }
private:

};

#endif /* BOBJECT_H */

