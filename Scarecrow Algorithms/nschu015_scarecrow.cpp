#include <algorithm>
#include <iostream>
#include <random>
#include <vector>
#include <limits>
#include <cmath>

using namespace std;

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

//Calculates distance between two nodes
double distance(Node a, Node b) {
    return sqrt(pow((b.getX() - a.getX()),2)+pow((b.getY() - a.getY()),2));
}

//Calculates total path distance of current Node organization
double totalDistance(vector<Node> currPath) {
    double result = 0;
    Node pad = currPath[0];
    for (int i = 0; i < currPath.size() - 1; ++i){
        result += distance(currPath[i], currPath[i+1]);
    }
    result += distance(currPath.back(), currPath.front());
    return result;
}

int main() {
    string fileName;
    int nodeCount = 2;
    vector<Node> Path;
    cout << "Enter the name of file: ";
    cin >> fileName;
    //open file, check if bad, take in all coords, count
    cout << "There are " << nodeCount << " nodes, computing shortest route.." << endl;
    //begin shortest distance search
    double shortestDistance = INFINITY;
    //Pentagon Path, should be 5 at minimum
    Node A(0, 0.85065);
    Node B(0.80902, 0.26287);
    Node C(0.5, -0.68819);
    Node D(-0.5, -0.68819);
    Node E(-0.80902, 0.26287);
    Path.push_back(A);
    Path.push_back(C);
    Path.push_back(E);
    Path.push_back(B);
    Path.push_back(D);
    cout << "   Shortest Route Discovered So Far " << endl;
    cout << "       " << totalDistance(Path) << endl;
    for (int i = 0; i < 10; ++i){
        random_device rd;
        default_random_engine rng(rd());
        shuffle(Path.begin() + 1, Path.end() - 1, rng);
        if (totalDistance(Path) < shortestDistance){
            shortestDistance = totalDistance(Path);
        }
        cout << "       " << shortestDistance << endl;
    }
    
    //
    return 0;
}