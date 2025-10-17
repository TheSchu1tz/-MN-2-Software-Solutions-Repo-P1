#include <algorithm>
#include <iostream>
#include <fstream>
#include <random>
#include <vector>
#include <limits>
#include <cmath>

using namespace std;

//class for Node objects
class Node {
private:
    double x;
    double y;
public:
    Node(double newX, double newY) : x(newX), y(newY){};
    void setX(double newX){
        x = newX;
    }
    void setY(double newY){
        y = newY;
    }
    double getX(){
        return x;
    }
    double getY(){
        return y;
    }
};

//calculates distance between two Nodes
double distance(Node a, Node b) {
    return sqrt(pow((b.getX() - a.getX()),2)+pow((b.getY() - a.getY()),2));
}

//calculates total path distance of current Node organization
double totalDistance(vector<Node> currPath) {
    double result = 0;
    Node pad = currPath[0];
    for (int i = 0; i < currPath.size() - 1; ++i){
        result += distance(currPath[i], currPath[i+1]);
    }
    result += distance(currPath.back(), currPath.front());
    return result;
}

//randomly shuffles order, replacing shortestDistance if new shortest is generated (outputs final shortest in place of eventual .txt output with all information)
float searchUntilEnter(){
    
}

int main() {
    //variable declarations
    string fileName;
    ifstream inputFile;
    vector<Node> Path;
    float shortestDistance = INFINITY;

    //get file name, open file, check if bad, take in all coords, count
    cout << "Enter the name of file: ";
    cin >> fileName;
    inputFile.open(fileName);
    if (!inputFile.is_open()){
        cout << "Error" << endl;
    }
    float A, B;
    while (inputFile >> A >> B){
        Path.push_back(Node(A, B));
    }
    inputFile.close();

    //begin outputting shortest paths
    cout << "There are " << Path.size() << " nodes, computing shortest route.." << endl;
    cout << "   Shortest Route Discovered So Far " << endl;

    //Replace with function running until 'Enter' pressed
    random_device rd;
    default_random_engine rng(rd());
    for (int i = 0; i < 100; ++i){
        shuffle(Path.begin() + 1, Path.end() - 1, rng);
        float currDistance = totalDistance(Path);
        if (currDistance < shortestDistance){
            shortestDistance = currDistance;
            cout << "       " << shortestDistance << endl;
        }
    }
    
    return 0;
}