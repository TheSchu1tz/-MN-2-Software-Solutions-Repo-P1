#include <algorithm>
#include <iostream>
#include <fstream>
#include <random>
#include <vector>
#include <limits>
#include <string>
#include <cmath>

using namespace std;

//class for Node objects
class Node {
private:
    double x;
    double y;
public:
    Node(double newX, double newY) : x(newX), y(newY){};
    double getX(){
        return x;
    }
    double getY(){
        return y;
    }
};

//calculates distance between two Nodes
double distance(Node& a, Node& b) {
    return sqrt(pow((b.getX() - a.getX()),2)+pow((b.getY() - a.getY()),2));
}

//calculates total path distance of current Node organization
double totalDistance(vector<Node>& currPath) {
    double result = 0;
    for (int i = 0; i < currPath.size() - 1; ++i){
        result += distance(currPath[i], currPath[i+1]);
    }
    result += distance(currPath.back(), currPath.front());
    return result;
}

//randomly shuffles order, replacing shortestDistance if new shortest is generated (outputs final shortest in place of eventual .txt output with all information)
double searchUntilEnter(vector<Node>& Path){
    double shortestDistance = INFINITY;
    string inputLine;
    random_device rd;
    default_random_engine rng(rd());
    while(1){
        //break loop if enter pressed *FIX*
        getline(cin, inputLine);
        if (inputLine == "\n"){
            cout << "Final shortest distance: " << shortestDistance << endl;
            break;
        }
        shuffle(Path.begin() + 1, Path.end() - 1, rng);
        double currDistance = totalDistance(Path);
        if (currDistance < shortestDistance){
            shortestDistance = currDistance;
            cout << "       " << shortestDistance << endl;
        }
    }
}

int main() {
    //variable declarations
    string fileName;
    ifstream inputFile;
    vector<Node> Path;

    //get file name, open file, check if bad, take in all coords, count
    cout << "Enter the name of file: ";
    cin >> fileName;
    inputFile.open(fileName);
    if (!inputFile.is_open()){
        cout << "Error" << endl;
    }
    double A, B;
    while (inputFile >> A >> B){
        Path.push_back(Node(A, B));
    }
    inputFile.close();

    cout << "First Path Order: ";
    for (int j = 0; j < Path.size(); ++j){
        if (j < Path.size() - 1){
            cout << "(" << Path[j].getX() << ", " << Path[j].getY() << ") to ";
        }
        else{
            cout << "(" << Path[j].getX() << ", " << Path[j].getY() << ")";
        }
    }

    //begin outputting shortest paths
    cout << endl << "There are " << Path.size() << " nodes, computing shortest route.." << endl;
    cout << "   Shortest Route Discovered So Far " << endl;

    //function runs until 'Enter' pressed, outputting 
    double resultDistance = searchUntilEnter(Path);

    cout << endl << "==========Results==========" << endl;
    cout << "Shortest Path Distance: " << resultDistance << endl;
    cout << "Shortest Path Order: ";
    for (int j = 0; j < Path.size(); ++j){
        if (j < Path.size() - 1){
            cout << "(" << Path[j].getX() << ", " << Path[j].getY() << ") to ";
        }
        else{
            cout << "(" << Path[j].getX() << ", " << Path[j].getY() << ")";
        }
    }
    cout << "Shortest Path Image: *Image here*";

    return 0;
}